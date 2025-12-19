# Class: blueprint for creating objects. (Student)
# Object: instance of a class (Udith, Nimal, Kamal)

class Student:

    student_id = 1  # class variable

    # constructor. methods starting with __ are magic methods
    def __init__(self, name, age, course, course_price, is_international=False):
        self.name = name
        self.age = age
        self.course = course
        self.is_international = is_international
        self.set_course_price(course_price)

    def __str__(self):  # string representation of the object (like Java's toString())
        return f"Student(Name: {self.name}, Age: {self.age}, Course: {self.course}, International: {self.is_international}, Course Price: {self.__course_price})"

    # class method
    @classmethod
    def some_class_method(cls):
        return f"Inside class method. Student ID is {cls.student_id}"

    def student_name(self):
        return f"Student name is {self.name}"

    def student_course(self):
        return f"Enrolled course is {self.course}"
    
    def get_course_price(self):
        return self.__course_price
    
    def set_course_price(self, price): # down below there is a better way using property decorator.
        if price < 0:
            print("Course price cannot be negative. user entered:", price)
            raise ValueError("Course price cannot be negative.")
        else:
            self.__course_price = price


student1 = Student("Udith", 21, "Python Programming", 1000)
student1.is_international = True  # adding new property to the object
print(type(student1))
print(str(student1))
print(isinstance(student1, Student))

print("Student ID:", Student.student_id)
print("Student ID:", student1.student_id)
print(student1.student_name())
print("Student age:", student1.age)
print(student1.student_course())

print(Student.some_class_method())

#private property access using getter and setter methods
print("Course Price:", student1.get_course_price())
student1.set_course_price(1500)
print("Updated Course Price:", student1.get_course_price())

#####################

# using property decorator to create getter and setter. better way to handle private properties.
class StudentWithProperty:

    def __init__(self, name, age, course, course_price):
        self.name = name
        self.age = age
        self.course = course
        self.course_price = course_price  # calls the setter

    def __str__(self):
        return f"Student(Name: {self.name}, Age: {self.age}, Course: {self.course}, Course Price: {self.course_price})"

    @property
    def course_price(self):
        return self._course_price

    @course_price.setter
    def course_price(self, price):
        if price < 0:
            print("Course price cannot be negative. user entered:", price)
            raise ValueError("Course price cannot be negative.")
        else:
            self._course_price = price
    
student2 = StudentWithProperty("Nimal", 22, "Java Programming", 1200)
print(str(student2))