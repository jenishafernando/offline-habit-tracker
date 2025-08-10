# Offline Habit Tracker

habits = []

def add_habit():
    habit = input("Enter the habit you want to track: ")
    habits.append({"habit": habit, "done": False})
    print(f"'{habit}' added!")

def mark_done():
    habit_name = input("Which habit did you complete? ")
    for h in habits:
        if h["habit"].lower() == habit_name.lower():
            h["done"] = True
            print(f"'{habit_name}' marked as done!")
            return
    print("Habit not found.")

def view_habits():
    print("\nYour Habits:")
    for h in habits:
        status = "✅ Done" if h["done"] else "❌ Not done"
        print(f"- {h['habit']} [{status}]")
    print()

while True:
    print("\nOptions: 1) Add Habit  2) Mark Done  3) View Habits  4) Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        mark_done()
    elif choice == "3":
        view_habits()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
