#List

# thislist = ["apple", "banana", "cherry","mango","kiwi","orange"]




# print(thislist[1:4]) 

# thislist[1] = "blackcurrant"
# print(thislist)

# thislist[1:4] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist.insert(2, "grape")
# print(thislist)

# thislist.append("pineapple")
# print(thislist)

# thislist2 = ["pear", "peach", "plum"]
# thislist.extend(thislist2)
# print(thislist)

# thislist.remove("banana")
# print(thislist)

# thislist.pop(2)
# print(thislist)

# thislist.pop()
# print(thislist)

# del thislist[0]
# print(thislist)

# thislist.clear()
# print(thislist)

# thislist.sort()
# print(thislist)

# thislist.sort(reverse=True)
# print(thislist)

# thislist1 = ["papaya","fruit"]
# this = thislist + thislist1 
# print(this)

fruits = ["apple", "banana", "cherry", "mango", "kiwi", "orange"]



# new_fruits = []
# for x in fruits:
#     if "a" in x:
#         new_fruits.append(x)
# print(new_fruits)


newlist = [x for x in fruits if "a" in x]
print(newlist)