import json

# Path to your JSON database
DB_FILE = "database.json"

# Sample data structure for classmates
sample_classmates = [
    {
  "cs_interview_participants": [
    {
      "name": "Caleb D. Cagatin",
      "age": 14,
      "favorite_color": "Orange",
      "favorite_subject": "Algebra",
      "favorite_song": "Happy Birthday"
    },
    {
      "name": "Xianne Arsenio C. Basas",
      "age": 13,
      "favorite_color": "Purple",
      "favorite_subject": "Math",
      "favorite_song": "WAP - Cardi B, Megan Thee Stallion"
    },
    {
      "name": "Antonio Miguel A. Garay",
      "age": 13,
      "favorite_color": "Red",
      "favorite_subject": "Health",
      "favorite_song": "Carol of the NEW! Ones - Satoishi Yuka Ft. Fujiwara Hagane"
    },
    {
      "name": "Zachary Ersh Nathan G. Ocampo",
      "age": 13,
      "favorite_color": "Blue",
      "favorite_subject": "CS",
      "favorite_song": "Pink and white"
    },
    {
      "name": "John Andre P. Quicho",
      "age": 13,
      "favorite_color": "Green",
      "favorite_subject": "Math 2",
      "favorite_song": "Love, Me normally - Will Wood"
    }
  ]
}

]

# -------------------- CREATE --------------------
def create_students(classmates):
    """Add all classmates info to database.json"""
    try:
        # Try to load existing data
        with open(DB_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        # If file doesn't exist, start with empty list
        data = []

    # Add new classmates
    data.extend(classmates)

    # Save to JSON
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("Data added successfully!")

# -------------------- READ --------------------
def read_students():
    """Read and print all students from database.json"""
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            for student in data:
                print(student)
    except FileNotFoundError:
        print("No database found.")

# -------------------- UPDATE --------------------
def update_students_school(campus_name):
    """Add a 'school' field to each student in database.json"""
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)

        # Update each student
        for student in data:
            student["school"] = campus_name

        # Save back to JSON
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("All students updated with school info!")
    except FileNotFoundError:
        print("No database found.")

# -------------------- DELETE --------------------
def delete_students_by_color(colors_to_delete):
    """Delete students whose favorite color is in colors_to_delete"""
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)

        # Keep only students whose favorite color is NOT in the list
        data = [student for student in data if student.get("favorite_color") not in colors_to_delete]

        # Save back to JSON
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
        print("Students with specified favorite colors deleted!")
    except FileNotFoundError:
        print("No database found.")

# -------------------- USAGE EXAMPLES --------------------
# 1. CREATE
create_students(sample_classmates)

# 2. READ
print("\n--- All Students ---")
read_students()

# 3. UPDATE
update_students_school("PSHS Main Campus")

# 4. READ again to check update
print("\n--- After Update ---")
read_students()

# 5. DELETE students with colors red, blue, yellow
delete_students_by_color(["red", "blue", "yellow"])

# 6. READ again to check deletion
print("\n--- After Deletion ---")
read_students()