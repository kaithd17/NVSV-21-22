class Student:
    firstname: str
    lastname: str
    classname: str
    age: int

    # Constructor
    def __init__(self, firstname: str, lastname: str, classname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.classname = classname
        self.age = age

    #tostring
    def __str__(self) -> str:
        formatString = "{} {} {} {}\n"
        return formatString.format(self.firstname, self.lastname, self.classname, self.age)
