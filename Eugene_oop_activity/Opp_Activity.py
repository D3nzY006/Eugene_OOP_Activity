
# Sigle in Inheratance

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    pass

dog = Dog()

dog.speak()

print("")
print("")


#2.)Multiple_Inheritence

class Father:
    father_name = "John"

    def show_father(self):
        print("Father's name:", self.father_name)

# Second parent class
class Mother:
    mother_name = "Mary"

    def show_mother(self):
        print("Mother's name:", self.mother_name)

# Child class inheriting from both parents
class Child(Father, Mother):
    def show_parents(self):
        # Accessing attributes from both parent classes
        print("Father's name:", self.father_name)
        print("Mother's name:", self.mother_name)

# Create object of child class
child = Child()

# Access methods and attributes from both parents
child.show_father()
child.show_mother()
child.show_parents()

print("")
print("")





#3.)Multilevel Inheritance

class Grandparent:
    def house(self):
        print("Grandparent owns a house")

# Child class (inherits from Grandparent)
class Parent(Grandparent):
    def car(self):
        print("Parent owns a car")

# Grandchild class (inherits from Parent)
class Child(Parent):
    def bike(self):
        print("Child owns a bike")

# Create object of the grandchild class
child = Child()

# Access methods from all levels
child.house()   # From Grandparent
child.car()     # From Parent
child.bike()    # From Child

print("")
print("")





#4.)Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("Vehicle is starting")

# First child class
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

# Second child class
class Bike(Vehicle):
    def ride(self):
        print("Bike is being ridden")

# Create objects
car = Car()
bike = Bike()

# Access parent method
car.start()
bike.start()

# Access child-specific methods
car.drive()
bike.ride()

print("")
print("")




#5.)Hybrid_Inheritance

class Person:
    def info(self):
        print("This is a person")

# First child class (multilevel inheritance)
class Employee(Person):
    def job(self):
        print("Employee has a job")

# Second parent class (used for multiple inheritance)
class Skills:
    def skill(self):
        print("Person has programming skills")

# Final child class (hybrid inheritance)
class Developer(Employee, Skills):
    def role(self):
        print("Developer writes code")

# Create object of the final class
dev = Developer()

# Access methods from all parent classes
dev.info()    # From Person
dev.job()     # From Employee
dev.skill()   # From Skills
dev.role()    # From Developer
