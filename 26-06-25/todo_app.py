import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create a table for tasks if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
)
''')
conn.commit()

def create_task():
    description = input("Enter the task description: ").strip()
    if description:
        cursor.execute('INSERT INTO tasks (description) VALUES (?)', (description,))
        conn.commit()
        print("✅ Task added successfully.\n")
    else:
        print("❌ Task description cannot be empty.\n")

def view_tasks():
    cursor.execute('SELECT id, description FROM tasks')
    tasks = cursor.fetchall()
    
    if tasks:
        print("\n📋 Your Tasks:")
        for task in tasks:
            print(f"{task[0]}. {task[1]}")
    else:
        print("\n📭 No tasks found.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            create_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("👋 Exiting the To-Do List application.")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

    conn.close()

if __name__ == '__main__':
    main()
