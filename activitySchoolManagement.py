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

person1 = Person("Lina", 20)
student1 = Student("Lina", 20)
print(f"Name: {person1.name}\n Age: {person1.get_age()}") 
student1.study()
