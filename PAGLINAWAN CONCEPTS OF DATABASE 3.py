import json

DB_FILE = "database.json"

def load_db():
    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_db(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_snack():
    data = load_db()

    snack = {
        "snack_id": int(input("Snack ID: ")),
        "name": input("Name: "),
        "category": input("Category: "),
        "price": int(input("Price: "))
    }

    data["snacks"].append(snack)
    save_db(data)
    print("Snack added!\n")

def add_student():
    data = load_db()

    student = {
        "student_id": int(input("Student ID: ")),
        "name": input("Name: "),
        "grade_level": int(input("Grade Level: "))
    }

    data["students"].append(student)
    save_db(data)
    print("Student added!\n")

def add_sale():
    data = load_db()

    sale = {
        "sale_id": int(input("Sale ID: ")),
        "student_id": int(input("Student ID: ")),
        "snack_id": int(input("Snack ID: ")),
        "quantity": int(input("Quantity: ")),
        "total_price": int(input("Total Price: ")),
        "date": input("Date (YYYY-MM-DD): "),
        "day": input("Day: ")
    }

    data["sales"].append(sale)
    save_db(data)
    print("Sale added!\n")

def view_data():
    data = load_db()

    print("\n--- SNACKS ---")
    for s in data["snacks"]:
        print(s)

    print("\n--- STUDENTS ---")
    for s in data["students"]:
        print(s)

    print("\n--- SALES ---")
    for s in data["sales"]:
        print(s)

def update_snack():
    data = load_db()
    sid = int(input("Enter Snack ID to update: "))

    for snack in data["snacks"]:
        if snack["snack_id"] == sid:
            snack["name"] = input("New Name: ")
            snack["category"] = input("New Category: ")
            snack["price"] = int(input("New Price: "))
            save_db(data)
            print("Snack updated!\n")
            return

    print("Snack not found!\n")

def delete_snack():
    data = load_db()
    sid = int(input("Enter Snack ID to delete: "))

    data["snacks"] = [s for s in data["snacks"] if s["snack_id"] != sid]
    save_db(data)
    print("Snack deleted!\n")

def total_sales():
    data = load_db()
    total = sum(s["total_price"] for s in data["sales"])
    print(f"\nTotal Sales: {total}")

def most_sold_snack():
    data = load_db()
    count = {}

    for sale in data["sales"]:
        sid = sale["snack_id"]
        count[sid] = count.get(sid, 0) + sale["quantity"]

    most = max(count, key=count.get)
    print(f"Most Sold Snack ID: {most} ({count[most]} sold)")

def sales_per_day():
    data = load_db()
    count = {}

    for sale in data["sales"]:
        day = sale["day"]
        count[day] = count.get(day, 0) + 1

    print("\nSales per Day:")
    for day, num in count.items():
        print(day, ":", num)

def menu():
    while True:
        print("""
1. Add Snack
2. Add Student
3. Add Sale
4. View Data
5. Update Snack
6. Delete Snack
7. Total Sales Report
8. Most Sold Snack
9. Sales per Day
0. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            add_snack()
        elif choice == "2":
            add_student()
        elif choice == "3":
            add_sale()
        elif choice == "4":
            view_data()
        elif choice == "5":
            update_snack()
        elif choice == "6":
            delete_snack()
        elif choice == "7":
            total_sales()
        elif choice == "8":
            most_sold_snack()
        elif choice == "9":
            sales_per_day()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


menu()