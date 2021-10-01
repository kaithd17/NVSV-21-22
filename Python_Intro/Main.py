from Student import Student

studentList = list()


def createStudent():
    firstname = input("Please enter the firstname of the student: ")
    lastname = input("Please enter the lastname of the student: ")
    classname = input("Please enter the class of the student: ")
    try:
        age: int = int(input("Please enter the age of the student: "))
    except ValueError:
        print("Invalid age!\n")
        return
    student: Student = Student(firstname, lastname, classname, age)
    studentList.append(student)
    print("Student successfully created!\n")


def showAllStudents():
    counter = int(1)
    print("\tFirstname - Lastname - Class - Age\n")
    for student in studentList:
        print("[{}] {}\n".format(counter, student))
        counter = counter + 1


def editStudent():
    if len(studentList) == 0:
        print("You have to create a student first!\n")
        return
    else:
        while True:
            print("What student do you want to change?\n")
            showAllStudents()
            try:
                studentIndex = int(input("Please choose a student: "))
                student: Student = studentList[studentIndex-1]
            except (ValueError, IndexError):
                print("\nInvalid number!\n")

            print("What do you want to change?\n")
            print("[1] Firstname\n[2] Lastname\n[3] Classname\n[4] Age\n[5] Nothing")

        
            try:
                number = int(input("Please choose a number: "))
                if number == 1:
                    firstname = input("Please enter the new firstname of the student: ")
                    student.firstname = firstname
                elif number == 2:
                    lastname = input("Please enter the new lastname of the student: ")
                    student.lastname = lastname
                elif number == 3:
                    classname = input("Please enter the new class of the student: ")
                    student.classname = classname    
                elif number == 4:
                    try:
                        age: int = int(input("Please enter the new age of the student: "))
                        student.age = age 
                    except ValueError:
                        print("Invalid age!\n")
                elif number == 5:
                    return
                else:
                    print("\nInvalid number!\n")
            except ValueError:
                print("\nPlease enter a number!\n")


def deleteStudent():
    print("Which student do you want to delete?\n")
    showAllStudents()

    studentIndex = int(input("Please choose a student: "))
    student: Student = studentList[studentIndex-1]
    studentList.remove(student)
    print("Student successfully deleted!\n")


def studentMenu():
    print("\nWelcome to my first Python Project!\n")
    while True:
        print("\t***Menu***")
        print("[1] Create Student\n[2] Show All Students\n[3] Edit Student\n[4] Delete Student\n[5] Exit")
        try:
            number = int(input("Please choose a number: "))
            print("\n")
            if number == 1:
                createStudent()
            elif number == 2:
                showAllStudents()
            elif number == 3:
                editStudent()
            elif number == 4:
                deleteStudent()
            elif number == 5:
                print("Thanks for using my software :)")
                break
            else:
                print("\nInvalid number!\n")
        except ValueError:
            print("\nPlease enter a number!\n")


if __name__ == '__main__':
    studentMenu()