# Student Management System

records = [
    ["Aman", "Math", 88],
    ["Priya", "Physics", 91],
    ["Rahul", "Math", 76],
    ["Neha", "Chemistry", 85],
    ["Arjun", "Physics", 79],
    ["Sneha", "Math", 92],
    ["Rohit", "Chemistry", 73],
    ["Anita", "Physics", 87],
    ["Karan", "Math", 81],
    ["Meera", "Chemistry", 90]
]


# Add student
def add_student(name, subject, marks):
    for r in records:
        if r[0] == name and r[1] == subject:
            print("Student already exists for this subject.")
            return
    records.append([name, subject, marks])
    print("Student added.")


# Get toppers
def get_toppers(subject):
    subject_students = [r for r in records if r[1] == subject]
    toppers = sorted(subject_students, key=lambda x: x[2], reverse=True)[:3]
    print("Top 3 students:", toppers)


# Class average
def class_average(subject):
    marks = [r[2] for r in records if r[1] == subject]
    if marks:
        avg = sum(marks) / len(marks)
        print("Class average:", avg)
    else:
        print("No records found.")


# Above average students
def above_average_students():
    all_marks = [r[2] for r in records]
    avg = sum(all_marks) / len(all_marks)

    above = [r for r in records if r[2] > avg]
    print("Students above class average:", above)


# Remove student
def remove_student(name):
    global records
    records = [r for r in records if r[0] != name]
    print("Student removed.")


# Menu
while True:
    print("\n1 Add student")
    print("2 Show toppers")
    print("3 Show class average")
    print("4 Show above-average students")
    print("5 Remove student")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        subject = input("Subject: ")
        marks = int(input("Marks: "))
        add_student(name, subject, marks)

    elif choice == "2":
        subject = input("Subject: ")
        get_toppers(subject)

    elif choice == "3":
        subject = input("Subject: ")
        class_average(subject)

    elif choice == "4":
        above_average_students()

    elif choice == "5":
        name = input("Student name: ")
        remove_student(name)

    elif choice == "6":
        with open("students.txt", "w") as f:
            for r in records:
                f.write(str(r) + "\n")
        print("Records saved. Exiting.")
        break

    else:
        print("Invalid choice.")