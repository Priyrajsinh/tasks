# Task 50: Final Challenge - Student Management System
# Problem: Create a system that manages student records with grades.
# Hint: Use if-else for validation, float input for grades, while loop for menu, for loop to process student lists.
# Use functions for operations and dictionaries for student data.

def add_students(students):
    name = input("Enter student name: ")
    if name in students:
        print('Student already exists.')
        return
    grade = input('Enter grade (0-100): ')
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            students[name] = grade
            print(f'Added {name} with grade {grade}.')
        else:
            print('Grade must be between 0 and 100.')
    except ValueError:
        print('Invalid Grade input.')

def view_students(students):
    if not students:
        print('No Student record found')
        return
    print('\nStudents Records: ')
    for name, grade in students.items():
        print(f'{name}: {grade}')

def update_students(students):
    name = input('Enter student name to update: ')
    if name not in students:
        print('student not found')
        return 
    grade = input('Enter new grade(0-100): ')
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            students[name] = grade
            print(f"Updated {name}'s grade is {grade}.")
        else:
            print('Grade must be between 0 and 100')
    except ValueError:
        print("Ivalid Grade input.")

def delete_students(students):
    name = input("Enter Student name to delete: ")
    if name in students:
        del students[name]
        print(f"Deleted {name}")
    else:
        print(f"Student not found")

def show_stats(students):
    if not students:
        print("No student record found to show statistics.")
        return
    grades = list(students.values())
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")

students = {}

while(True):
    print("****Student Management System****")
    print("1. Add Studdents")
    print("2. View Students")
    print("3. Update Students")
    print("4. Delete Students")
    print("5. Show Statistics")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_students(students)
    elif choice == '2':
        view_students(students)
    elif choice == '3':
        update_students(students)
    elif choice == '4':
        delete_students(students)
    elif choice == '5':
        show_stats(students)
    elif choice == '6':
        print("Exiting student Management System.")
        break
    else:
        print("Ivalid Choice. Please try again")