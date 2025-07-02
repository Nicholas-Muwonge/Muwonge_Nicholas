class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        return f"{super().display_info()}, Student ID: {self.student_id}, Course: {self.course}" 
class Lecturer(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def display_info(self):
        return f"{super().display_info()}, Employee ID: {self.employee_id}, Department: {self.department}"
class Staff(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        return f"{super().display_info()}, Employee ID: {self.employee_id}, Position: {self.position}"
if __name__ == "__main__": 
    name = input("Enter person's name: ")
    age = int(input("Enter person's age: "))
    person = Person(name, age)
    print(person.display_info())
    print()
    student_name = input("Enter student's name: ")
    student_age = int(input("Enter student's age: "))
    student_id = input("Enter student ID: ")
    course = input("Enter student's course: ")
    student = Student(student_name, student_age, student_id, course)
    print(student.display_info())
    lecturer_name = input("Enter lecturer's name: ")
    lecturer_age = int(input("Enter lecturer's age: "))
    employee_id = input("Enter lecturer's employee ID: ")
    department = input("Enter lecturer's department: ")
    lecturer = Lecturer(lecturer_name, lecturer_age, employee_id, department)
    print(lecturer.display_info())
    staff_name = input("Enter staff's name: ")
    staff_age = int(input("Enter staff's age: "))
    staff_employee_id = input("Enter staff's employee ID: ")
    position = input("Enter staff's position: ")
    staff = Staff(staff_name, staff_age, staff_employee_id, position)
    print(staff.display_info())
