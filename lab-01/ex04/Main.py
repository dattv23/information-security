from StudentManager import StudentManager

# Initialize the StudentManager object
student_manager = StudentManager()

# Continuously display the menu until the user chooses to exit
while True:
    print("\nSTUDENT MANAGEMENT PROGRAM")
    print("*************************MENU**************************")
    print("** 1. Add a new student.                              **")
    print("** 2. Update student information by ID.              **")
    print("** 3. Delete a student by ID.                        **")
    print("** 4. Search for a student by name.                  **")
    print("** 5. Sort students by average score.                **")
    print("** 6. Sort students by name.                         **")
    print("** 7. Display the list of students.                  **")
    print("** 0. Exit the program.                              **")
    print("*******************************************************")

    # Prompt the user for a choice
    key = int(input("Select an option: "))

    if key == 1:
        print("\n1. Add a student.")
        student_manager.addStudent()
        print("\nStudent added successfully!")

    elif key == 2:
        if student_manager.getStudentCount() > 0:
            print("\n2. Update student information.")
            print("Enter ID: ")
            ID = int(input())
            student_manager.updateStudent(ID)
        else:
            print("\nNo students in the list!")

    elif key == 3:
        if student_manager.getStudentCount() > 0:
            print("\n3. Delete a student.")
            print("Enter ID: ")
            ID = int(input())
            if student_manager.deleteStudentByID(ID):
                print("\nStudent with ID =", ID, "has been deleted.")
            else:
                print("\nNo student found with ID =", ID)
        else:
            print("\nNo students in the list!")

    elif key == 4:
        if student_manager.getStudentCount() > 0:
            print("\n4. Search for a student by name.")
            print("Enter the name to search: ")
            name = input()
            search_result = student_manager.findStudentsByName(name)
            student_manager.displayStudents(search_result)
        else:
            print("\nNo students in the list!")

    elif key == 5:
        if student_manager.getStudentCount() > 0:
            print("\n5. Sort students by average score.")
            student_manager.sortStudentsByAverageScore()
            student_manager.displayStudents(student_manager.getAllStudents())
        else:
            print("\nNo students in the list!")

    elif key == 6:
        if student_manager.getStudentCount() > 0:
            print("\n6. Sort students by name.")
            student_manager.sortStudentsByName()
            student_manager.displayStudents(student_manager.getAllStudents())
        else:
            print("\nNo students in the list!")

    elif key == 7:
        if student_manager.getStudentCount() > 0:
            print("\n7. Display the list of students.")
            student_manager.displayStudents(student_manager.getAllStudents())
        else:
            print("\nNo students in the list!")

    elif key == 0:
        print("\nExiting the program. Goodbye!")
        break

    else:
        print("\nInvalid option selected. Please try again.")
