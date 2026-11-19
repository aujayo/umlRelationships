class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def get_age(self):
            return self.age
  
person1 = Person("Lina", 20)
print(f"Name: {person1.name}, Age: {person1.get_age()}")