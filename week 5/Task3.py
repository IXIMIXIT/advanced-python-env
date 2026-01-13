class Person:
    def __init__(self, name, age):
        self.name = name
        # Encapsulation: _age is protected (conventionally private)
        self._age = age 

    def introduce(self):
        return f"I am {self.name} and I am {self._age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        # Inheritance: calling the parent constructor
        super().__init__(name, age)
        self.student_id = student_id

    # Polymorphism: Overriding the parent method
    def introduce(self):
        return f"I am student {self.name} (ID: {self.student_id})."

# Demonstration
if __name__ == "__main__":
    person = Person("John", 45)
    student = Student("Emily", 20, "S12345")

    print(person.introduce())  # Output from Parent class
    print(student.introduce()) # Output from Child class (Override)