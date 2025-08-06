# x=10
# print(x)
# print(dir(x))

# class Student:
#     "For Student Details...."
#     def __init__(self):
#         print("From external constructor1............")
#     def __init__(self):
#         print("From external constructor2............")
#     def __init__(self,name):
#         print(id(self))
#         print("From external constructor3............")

# print(dir(Student))
# print(Student.__doc__)
# print(id(Student))

# obj1 = Student("Neeraj")
# print(id(Student))
# print(id(obj1))
# obj1.__init__()

# obj2 = Student
# obj3 = Student
# print(id(obj1),id(obj2),id(obj3))


# class Student:
#     "For Student Details...."

# obj1 = Student
# print(id(Student))
# print(id(obj1))


# dummy object is called class
# constructor is specail type of varable 
# real word ki entity od programing se add krne ke liye hm oops ka use krte hai


class student:
    def __init__(self,name):
        self.name=name
    def studetail(self):
        print(self.name)
        print(self.age)

obj=student
print(id(student))
print(id(obj))

obj1=student('pratima')
print(id(obj1))
print(id(student))
print(obj1.name)

obj.age=20
obj1.studetail()
#         kisi object ke initial value ko initailse krne ke liye constructor 
# object dependent variable ko instance variable
# obect ke sath value bhi change ho to use instanse variable kahte hai