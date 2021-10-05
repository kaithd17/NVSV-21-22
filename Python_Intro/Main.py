from Student import Student

studentList = list()

def createStudent():
    finished: bool
    while True:
        firstname = input("Please enter the firstname of the student: ")
        lastname = input("Please enter the lastname of the student: ")
        classname = input("Please enter the class of the student: ")

        try:
            finished = True
            age: int = int(input("Please enter the age of the student: "))
            student: Student = Student(firstname, lastname, classname, age)
            studentList.append(student)
        except (ValueError, UnboundLocalError):
            print("Invalid age!\n")
            finished = False

        if finished:
            print("Student successfully created!\n")
            return


def showAllStudents():
    counter = int(1)
    print("Firstname - Lastname - Class - Age\n")
    for student in studentList:
        print("[{}] {}\n".format(counter, student))
        counter = counter + 1


def editStudent():
    valid: bool

    if len(studentList) == 0:
        print("You have to create a student first!\n")
        return
    else:
        while True:
            valid = True
            print("What student do you want to change?\n")
            showAllStudents()
            try:
                studentIndex = int(input("Please choose a student: "))
                student: Student = studentList[studentIndex-1]
            except (ValueError, IndexError):
                print("\nInvalid number!\n")
                valid = False

            if valid:
                print("What do you want to change?\n")
                print("[1] Firstname\n[2] Lastname\n[3] Classname\n[4] Age\n[5] Nothing")

                finished: bool = True
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
                            finished = False
                    elif number == 5:
                        return
                    else:
                        print("\nInvalid number!\n")
                        finished = False
                except ValueError:
                    print("\nPlease enter a number!\n")
                    finished = False

                if finished:
                    print("Student successfully edited!\n")
                    return


def deleteStudent():
    valid: bool
    if len(studentList) == 0:
        print("You have to create a student first!\n")
        return
    else:
        while True:
            valid = True
            print("Which student do you want to delete?\n")
            showAllStudents()

            try:
                studentIndex = int(input("Please choose a student: "))
                student: Student = studentList[studentIndex-1]
                studentList.remove(student)
            except (ValueError, IndexError):
                print("\nInvalid number!\n")
                valid = False

            if valid:
                print("Student successfully deleted!\n")
                return


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
                return
            else:
                print("\nInvalid number!\n")
        except ValueError:
            print("\nPlease enter a number!\n")

def readFile():
    file = open("students.csv", "r")
    while True:
        studentString: str = file.readline()
        if studentString == "":
           break
        student: Student = Student(studentString.split(";")[0], studentString.split(";")[1], studentString.split(";")[2], int(studentString.split(";")[3].replace("\n","")))
        studentList.append(student)
    file.close()

def writeFile():
    file = open("students.csv", "w")
    for student in studentList:
        file.write("{};{};{};{}\n".format(student.firstname, student.lastname, student.classname, student.age))
    file.close()

if __name__ == '__main__':
    readFile()
    studentMenu()
    writeFile()
