from Student import Student


if __name__ == '__main__':
    student = Student("Thomas", "Kainz", "5DHIF", 18)
    student.firstname = "lol"
    print(student.firstname)