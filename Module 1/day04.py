# thistuple = ("apple",)
# print(type(thistuple))


# thistuple = ("apple")
# print(type(thistuple))



# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])


# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])



# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)



# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# print(thistuple)




# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)




# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# print(thistuple)



# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#   print(x)


# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])


# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("orange", "kiwi", "melon")
# tuple3 = tuple1 + tuple2
# print(tuple3)




# fruits = ["apple", "banana", "cherry", "mango", "kiwi", "orange"]
# mytuple = fruits* 2
# print(mytuple)



# thistuple = ("apple", "banana", "cherry", "mango", "kiwi", "orange","apple", "banana", "cherry", "mango", "kiwi", "orange")
# x = thistuple.count("apple")
# print(x)


# thistuple = ("apple", "banana", "cherry", "mango", "kiwi", "orange")
# x = thistuple.index("orange")
# print(x)



# print("banana" in thistuple)
# print("banana" not in thistuple)



# SET_________________________________________________________________________



# thislist = {"apple", "banana", "cherry", "mango", "kiwi", "orange"}

# thislist.add("pineapple")
# print(thislist)


# thisset = {"pear", "peach", "plum","banana", "kiwi", "orange"}
# thisset.discard("banana")
# print(thisset)


# thisset.pop()
# print(thisset)

# thisset.pop()
# print(thisset)

# del thisset
# print(thisset)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"banana", "kiwi", "orange"} 

# set3 = set1 | set2
# print(set3)


# set3 = set1 - set2
# print(set3)


# set3 = set1 & set2
# print(set3)

# set3 = set1 ^ set2
# print(set3)






# DICT_________________________________________________






# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "year": 2020,
#     "colors": ["red", "white", "blue"]
# }
# print(thisdict["year"])

# x= thisdict.get("colors")
# print(x)

# thisdict["year"] = 1962
# print(thisdict)

# thisdict.update({"year": 2025})
# print(thisdict)


# thisdict = {
#     "Name": "Alice",
#     "Age": 30,
#     "Marks": 90,
# }

# thisdict["Age"] = 31
# print(thisdict)

# thisdict.pop("Marks")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)


thisdict = {    
    "Name": "Alice",
    "Age": 30,
    "Marks": 90,
    "Subjects": ["Math", "Science", "English"]
}

for x,y in thisdict.items():
    print(x,y)