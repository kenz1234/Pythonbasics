# x = lambda a: a + 10
# print(x(5))

# x = lambda a, b: a * b
# print(x(5, 6))  

# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))


# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]
# result = set(map(square, numbers))
# print(result)



# numbers = [1, 2, 3, 4, 5]
# result = set(map(lambda x: x * x, numbers))
# print(result)


# def check_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# even_numbers_iter = filter(check_even, numbers)
# even_numbers = list(even_numbers_iter)

# print(even_numbers)


#OROROROROROROOROROROROROROROROORORORORORORORORORORORORORO



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_numbers)




# from functools import reduce
# def add(x, y):
#     return x + y   

# numbers = [1, 2, 3, 4, 5]
# result = reduce(add, numbers)
# print(result)




from functools import reduce
a = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, a)
print(result)