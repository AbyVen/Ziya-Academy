// ================== CONFIG ==================
const API_KEY = "ce08a62a18c615265889b06f3ad7c09c";
const weatherResult = document.getElementById("weatherResult");
const forecastCards = document.getElementById("forecastCards");
const forecastChartCanvas = document.getElementById("forecastChart");
const historyDiv = document.getElementById("history");
const favoritesDiv = document.getElementById("favorites");
const loader = document.getElementById("loader");

let forecastChartInstance = null;

// ================== EVENT LISTENERS ==================
document.getElementById("searchBtn").addEventListener("click", () => {
    const city = document.getElementById("cityInput").value;
    if (city) fetchWeatherByCity(city);
});

document.getElementById("geoBtn").addEventListener("click", () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            pos => fetchWeatherByCoords(pos.coords.latitude, pos.coords.longitude),
            () => alert("Location access denied.")
        );
    }
});

document.getElementById("themeToggle").addEventListener("click", () => {
    document.body.classList.toggle("dark");
    document.getElementById("themeToggle").textContent =
        document.body.classList.contains("dark") ? "☀️" : "🌙";
});

// ================== WEATHER FUNCTIONS ==================
async function fetchWeatherByCity(city) {
    loader.style.display = "block";
    try {
        const res = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`
        );
        const data = await res.json();
        if (data.cod !== 200) throw new Error(data.message);
        displayWeather(data);
        fetchForecast(data.coord.lat, data.coord.lon);
        saveHistory(city);
    } catch (err) {
        weatherResult.innerHTML = `<p style="color:red;">${err.message}</p>`;
    }
    loader.style.display = "none";
}

async function fetchWeatherByCoords(lat, lon) {
    loader.style.display = "block";
    try {
        const res = await fetch(
            `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        );
        const data = await res.json();
        if (data.cod !== 200) throw new Error(data.message);
        displayWeather(data);
        fetchForecast(lat, lon);
        saveHistory(data.name);
    } catch (err) {
        weatherResult.innerHTML = `<p style="color:red;">${err.message}</p>`;
    }
    loader.style.display = "none";
}

function displayWeather(data) {
    const { main, weather, wind, sys, name } = data;
    const icon = `https://openweathermap.org/img/wn/${weather[0].icon}@2x.png`;
    const condition = weather[0].main.toLowerCase();

    weatherResult.innerHTML = `
    <h2>${name}, ${sys.country}</h2>
    <img src="${icon}" class="weather-icon" alt="${weather[0].description}">
    <p><b>${weather[0].description.toUpperCase()}</b></p>
    <p>🌡️ Temp: ${main.temp}°C (Feels like ${main.feels_like}°C)</p>
    <p>💧 Humidity: ${main.humidity}%</p>
    <p>🌬️ Wind: ${wind.speed} m/s</p>
    <p>🌅 Sunrise: ${new Date(sys.sunrise * 1000).toLocaleTimeString()}</p>
    <p>🌇 Sunset: ${new Date(sys.sunset * 1000).toLocaleTimeString()}</p>
    <div class="suggestion">${getSuggestion(condition, main.temp)}</div>
    <button onclick="saveFavorite('${name}')">⭐ Add to Favorites</button>
  `;

    changeBackground(condition, data);
}

async function fetchForecast(lat, lon) {
    try {
        const res = await fetch(
            `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        );
        const data = await res.json();
        displayForecast(data.list);
    } catch (err) {
        forecastCards.innerHTML = `<p style="color:red;">${err.message}</p>`;
    }
}

function displayForecast(list) {
    forecastCards.innerHTML = "";
    let dailyData = {};

    list.forEach(item => {
        const date = new Date(item.dt * 1000);
        const day = date.toLocaleDateString("en-US", { weekday: "short" });
        if (!dailyData[day]) dailyData[day] = [];
        dailyData[day].push(item.main.temp);
    });

    let labels = [], temps = [];
    Object.keys(dailyData).slice(0, 5).forEach(day => {
        const avg = (
            dailyData[day].reduce((a, b) => a + b, 0) / dailyData[day].length
        ).toFixed(1);
        labels.push(day);
        temps.push(avg);

        forecastCards.innerHTML += `
      <div class="forecast-day">
        <p>${day}</p>
        <p>${avg}°C</p>
      </div>
    `;
    });

    renderForecastChart(labels, temps);
}

function renderForecastChart(labels, temps) {
    if (forecastChartInstance && typeof forecastChartInstance.destroy === "function") {
        forecastChartInstance.destroy();
    }

    forecastChartInstance = new Chart(forecastChartCanvas, {
        type: "line",
        data: {
            labels,
            datasets: [
                {
                    label: "Avg Temp (°C)",
                    data: temps,
                    borderColor: "#fff",
                    backgroundColor: "rgba(255,255,255,0.3)",
                    fill: true,
                    tension: 0.4,
                    pointRadius: 5
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { labels: { color: "#fff" } }
            },
            scales: {
                x: { ticks: { color: "#fff" } },
                y: { ticks: { color: "#fff" } }
            }
        }
    });
}

// ================== HELPERS ==================
function getSuggestion(condition, temp) {
    if (condition.includes("rain")) return "☔ Carry an umbrella!";
    if (condition.includes("snow")) return "🧣 Wear warm clothes!";
    if (condition.includes("clear") && temp > 30) return "😎 Stay hydrated, it's hot!";
    if (condition.includes("clear") && temp < 10) return "🧥 It's chilly outside.";
    return "✅ Have a nice day!";
}

function changeBackground(condition, data = null) {
    let isNight = false;
    if (data) {
        const now = Date.now() / 1000;
        isNight = now < data.sys.sunrise || now > data.sys.sunset;
    }

    if (condition.includes("rain")) {
        document.body.style.background = "linear-gradient(135deg, #00c6ff, #0072ff)";
        loadParticles("rain", isNight);
    } else if (condition.includes("snow")) {
        document.body.style.background = "linear-gradient(135deg, #e6dada, #274046)";
        loadParticles("snow", isNight);
    } else if (condition.includes("cloud")) {
        document.body.style.background = "linear-gradient(135deg, #bdc3c7, #2c3e50)";
        loadParticles("cloud", isNight);
    } else {
        document.body.style.background = isNight
            ? "linear-gradient(135deg, #0f2027, #203a43, #2c5364)"
            : "linear-gradient(135deg, #56ccf2, #2f80ed)";
        loadParticles("clear", isNight);
    }
}

// ================== PARTICLES ==================
function loadParticles(type, isNight) {
    let config = {
        particles: {
            number: { value: 80 },
            size: { value: 3 },
            move: { speed: 1 }
        }
    };

    if (type === "rain") {
        config.particles.number.value = 200;
        config.particles.size.value = 2;
        config.particles.move.speed = 8;
        config.particles.shape = { type: "circle" };
    } else if (type === "snow") {
        config.particles.number.value = 150;
        config.particles.size.value = 4;
        config.particles.move.speed = 2;
    } else if (type === "cloud") {
        config.particles.number.value = 50;
        config.particles.size.value = 10;
        config.particles.opacity = { value: 0.2 };
    } else {
        config.particles.number.value = 50;
        config.particles.size.value = 2;
    }

    if (isNight) {
        config.particles.color = { value: "#fff" };
    }

    particlesJS("particles-js", config);
}

// ================== HISTORY & FAVORITES ==================
function saveHistory(city) {
    let history = JSON.parse(localStorage.getItem("history")) || [];
    if (!history.includes(city)) history.unshift(city);
    if (history.length > 5) history.pop();
    localStorage.setItem("history", JSON.stringify(history));
    renderHistory();
}

function renderHistory() {
    let history = JSON.parse(localStorage.getItem("history")) || [];
    historyDiv.innerHTML = "<h3>Recent Searches</h3>";
    history.forEach(city => {
        historyDiv.innerHTML += `<button onclick="fetchWeatherByCity('${city}')">${city}</button>`;
    });
}

function saveFavorite(city) {
    let fav = JSON.parse(localStorage.getItem("favorites")) || [];
    if (!fav.includes(city)) fav.push(city);
    localStorage.setItem("favorites", JSON.stringify(fav));
    renderFavorites();
}

function renderFavorites() {
    let fav = JSON.parse(localStorage.getItem("favorites")) || [];
    favoritesDiv.innerHTML = "<h3>Favorites</h3>";
    fav.forEach(city => {
        favoritesDiv.innerHTML += `<button onclick="fetchWeatherByCity('${city}')">${city}</button>`;
    });
}

// ================== INIT ==================
window.onload = () => {
    renderHistory();
    renderFavorites();
};
