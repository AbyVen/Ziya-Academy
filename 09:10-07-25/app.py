from flask import Flask, render_template, request, jsonify, redirect, url_for
import calendar
from datetime import datetime

app = Flask(__name__)


public_holidays = {
    "2025-01-01": "New Year's Day – Celebrates the beginning of the new year",
    "2025-08-15": "Independence Day – National Holiday",
    "2025-12-25": "Christmas Day – Celebrating the birth of Jesus Christ"
}

@app.route('/')
def index():
    year = request.args.get('year', default=datetime.today().year, type=int)
    month = request.args.get('month', default=datetime.today().month, type=int)

    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    month_name = calendar.month_name[month]
    month_days = calendar.monthcalendar(year, month)

    return render_template(
        'calendar.html',
        year=year,
        month=month,
        month_name=month_name,
        month_days=month_days,
        holidays=public_holidays
    )

@app.route('/check_holiday', methods=['POST'])
def check_holiday():
    data = request.get_json()
    date_str = data.get('date')

    if date_str in public_holidays:
        return jsonify({'holiday': True, 'description': public_holidays[date_str]})
    else:
        return jsonify({'holiday': False})

@app.route('/add_holiday', methods=['POST'])
def add_holiday():
    date = request.form.get('date')
    description = request.form.get('description')

    if date and description:
        public_holidays[date] = description
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
