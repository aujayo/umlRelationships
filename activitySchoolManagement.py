class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age  #access__age is a more intuitive way to access the private attribute __age

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def teach(self):
        print(f"{self.name} is teaching.")

person1 = Person("Lina", 20)
student1 = Student("Lina", 20)
teacher1 = Teacher("Mona", 30)
print(f"Name: {person1.name}\n Age: {person1.get_age()}") 
print(f"Name: {student1.name}\n Age: {student1.get_age()}") 
student1.study()
print(f"Name: {teacher1.name}\n Age: {teacher1.get_age()}") 
teacher1.teach()
