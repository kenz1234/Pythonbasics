
#__________________________________________CLASS___METHODS___________________________________________




# class Person:
#     age = 25

#     def printAge(cls):
#         print("Age:", cls.age)

# Person.printAge = classmethod(Person.printAge)
# print(Person.age)





#___________________________________STATIC___METHODS___________________________________________





class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def square(x):
        return x * x
    
print(MathUtils.add(5, 3))
print(MathUtils.subtract(10, 4))
print(MathUtils.multiply(2, 6))
print(MathUtils.square(4))
