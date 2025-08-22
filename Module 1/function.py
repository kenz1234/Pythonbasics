# def my_function():
#     print("This is my function.")

# my_function()


# def my_function(a,b,c):
#     a= 5
#     b = 11
#     c = a+b
#     print(c)

# my_function(a=0, b=0, c=0)




# a= int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# def my_function(a,b):
#     c = a+b
#     print("sum =",c)

# my_function(a, b)



# def add_numbers(a=5, b=8):
#     c = a + b
#     print("Sum =", c)


# add_numbers(a=4,b=6)

# add_numbers(a=10)    

# add_numbers()





# def display_info(f_name, l_name):
#     print("First Name:", f_name)
#     print("Last Name:", l_name)

# display_info(l_name="John", f_name="Doe")



# def find_num(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     print("Total:", total)

# find_num(1, 2, 3, 4, 5)

# find_num(10, 20, 30)




# find the product of multiple numbers



# def find_product(*numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     print("Product:", product)

# find_product(1,4)
# find_product(3,2)


# write a function display info name age as keyword arguments and print them 

# name =str(input("Enter name: "))
# age = str(input("Enter age: "))
# marks = str(input("Enter marks: "))

# def display_info(name, age, marks):
    
#     print("Name:", name)
#     print("Age:", age)
#     print("Marks:",marks)

# # display_info(name = "Harry Potter", age=20, marks=95)
# # display_info(name = "Hermione Granger", age=21, marks=98)
# # display_info(name = "Ron Weasley", age=20, marks=90)

# display_info(name,age,marks)




def area_of_rectangle(length, width):
    area = length * width
    print("Area of rectangle:", area)

area_of_rectangle(5, 10)