correct_password = "secret123"
attempts = 5

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts left.")
else:
    print("Access denied. No attempts left.")