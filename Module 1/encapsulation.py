# PUBLIC_____________________________________________________________________________________________________


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:",self.name)
#         print("Age:" ,self.age)

# s = Student("Alice", 20)
# s.display()







# PRIVATE____________________________________________________________________________________________________



# class BankAccount:
#     def __init__(self,account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance  

#     def __display_balance(self):
#         print("Account Number:", self.__account_number)
#         print("Balance:", self.__balance)

# b = BankAccount("123456789", 1000)
# b.__display_balance()




# PROTECTED__________________________________________________________________________________________________



class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _display(self):
        print("Name:", self._name)
        print("Age:", self._age)    

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self._roll_number = roll_number

    def display(self):
        self._display()
        print("Roll Number:", self._roll_number)


x = Student("Alice", 20, "A123")
x.display()