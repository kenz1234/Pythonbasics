# class Myclass:
#     x = 5

# object = Myclass()
# print(object.x) 





# class MyClass:
#     name = "Kenz"

# object = MyClass()
# print(object.name)






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)
# print(p1.name)  





class Student:
    def __init__(self,student_name, student_marks):
        self.student_name = student_name
        self.student_marks = student_marks

student1 = Student("Alice", 85)
student2 = Student("Bob", 90)

print("Name : ",student1.student_name,"\nMarks : ", student1.student_marks)
print("Name : ",student2.student_name,"\nMarks : ", student2.student_marks)
