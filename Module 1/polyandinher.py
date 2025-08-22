
#POLYMORPHISM EXAMPLE

#METHOD OVERLOADING
#DEFAULT METHOD

# class Calculator():
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
    
# c=Calculator()
# print(c.add(7,5))
# print(c.add(1,4,6))
# print(c.add(1))



#VARIABLE ARGUMENT METHOD

# class Calculator():
#     def add(self,*args):
#         return sum(args)
    
# c=Calculator()
# print(c.add(7,5))
# print(c.add(1,4,6))
# print(c.add(1))



#METHOD OVERRIDING


class Animal:
    def sound(self): 
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
a = Animal()
a.sound()

d = Dog()
d.sound()

animal = Dog()
animal.sound()


# INHERITANCE EXAMPLE


# class person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
        

#     def printname(self):
#         print(f"Full Name: {self.firstname} {self.lastname}")
# x=person("John", "Doe")
# x.printname()    





# class Person:  
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def primt_name(self):
#         print(f"Full Name: {self.first_name} {self.last_name}")

# class Student(Person):
#     pass
# x=Student("John", "Doe")
# x.primt_name()