# cha=input("Enter a character : ")
# if cha.lower() in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
#     print(cha, "is a vowel")
# else:
#     print(cha, "is a consonant")





# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# else:
#     print("Failed")




# num1=int(input("Enter first number:"))
# num2=int(input("Enter second number:"))
# num3=int(input("Enter third number:"))
# if num1 >= num2 and num1 >= num3:
#     print(f"'{num1}' is the largest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"'{num2}' is the largest number.")
# else:
#   print(f"'{num3}' is the largest number.")





# year=int(input("Enter a Year:"))
# if(year % 4 ==0 and (year % 100!= 0 or year % 400==0)):
#     print(year, "is leap year ")
# else:
#     print(year,"Year is not a leap year")




# b = int(input("Enter a number: "))
# i=1
# for i in range (1,11):
#     a = i * b
#     print(a)




# i=0
# for i in range(1, 11):
#     print(i)



# i=1
# while i <= 20:
#      if i % 2 == 0:
#          print(i)
#      i += 1




# def sum_average(lst):
#     total = sum(lst)
#     average = total /len(lst)
#     return total, average

# num = [5,10]
# total,average = sum_average(num)

# print(f"sum : {total}")
# print(f"average : {average:.2f}")




# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = [num for num in n if num % 2 == 0]
# print("Even numbers:", even_numbers)





# n = [12, 35, 1, 10, 34, 1, 35]

# second_largest = sorted(set(n))[-2]
# print("Second largest number:", second_largest)






# n = [12, 35, 1, 10, 34, 1, 35]

# minimum = min(n)
# print("Minimum number:", minimum)   
# maximum = max(n)
# print("Maximum number:", maximum)




# n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# odd_numbers = tuple(num for num in n if num % 2 != 0)
# print("Odd numbers:", odd_numbers)



# my_tuple = (20,30,40,50,60)
# index = my_tuple.index(40)
# print("index :",index)



# n = ('a', 'b', 'c', 'd', 'e')

# converted_string = ''.join(n)
# print("Converted String:", converted_string)
# print("Type:", type(converted_string))




# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in n:
#     if num % 2 == 0:
#         n.remove(num)
#     print("List after removing even numbers:", n)






# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set1.update(set2)
# print("Updated Set:", set1)






my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4  
my_dict['b'] = 5 
del my_dict['c']  
print("Updated Dictionary:", my_dict)









# string = input("Enter a string: ")
# frequency = {}
# count = 0
# for char in string:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
# print("Character frequency:", frequency)







# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# my_dict = dict(zip(keys, values))
# print("Dictionary:", my_dict)







# my_dict = {'a': 3, 'b': 1, 'c': 2}
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# print("Sorted Dictionary:", sorted_dict)