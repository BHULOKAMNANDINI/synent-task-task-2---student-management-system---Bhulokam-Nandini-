import json

FILE_NAME = "students.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")

    students.append({
        "id": student_id,
        "name": name,
        "age": age
    })

    save_students(students)
    print("Student Added Successfully!")

def view_students():
    students = load_students()

    if not students:
        print("No Students Found")
        return

    for student in students:
        print(student)

def update_student():
    students = load_students()

    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["age"] = input("Enter New Age: ")

            save_students(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found")

def delete_student():
    students = load_students()

    student_id = input("Enter Student ID to Delete: ")

    students = [s for s in students if s["id"] != student_id]

    save_students(students)

    print("Student Deleted Successfully!")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")