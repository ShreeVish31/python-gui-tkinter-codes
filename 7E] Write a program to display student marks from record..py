
student_records = {}


def add_student_record(name, marks):
    student_records[name] = marks


def display_student_marks(name):
    if name in student_records:
        print(f"{name}'s marks: {student_records[name]}")
    else:
        print(f"{name} not found in records.")


while True:
    print("Options:")
    print("1. Add Student Record")
    print("2. Display Student Marks")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))
        add_student_record(name, marks)
    elif choice == '2':
        name = input("Enter student name: ")
        display_student_marks(name)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

print("Program terminated.")
