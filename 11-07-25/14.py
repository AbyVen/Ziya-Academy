def welcome_students(*names):
    for name in names:
        print(f"Welcome, {name}!")


user_input = input("Enter student names separated by commas: ")
name_list = [name.strip() for name in user_input.split(",")]

welcome_students(*name_list)
