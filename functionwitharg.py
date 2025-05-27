# def perfect_number(num):
#     ans=0
#     for i in range(1,num):
#         if num%i==0:
#             ans+=i
#     if ans==num:
#         print("perfect")
#     else:
#         print("not perfct")

# a= int(input("enter the number"))
# perfect_number(a)


# type of argument
# 1 position argument
# 2 keyword argument
# 3 default argument
# 4 variable -length argument
# 5 keyword variable argument

# //return type with argument

# def sum(a,b):
#     return a+b
# num1= int(input("enter the number"))
# num2= int(input("enter the number"))

# sum=(num1,num2)

# def student_data(name,rollno):
#     print(f"the student name is {name} and the roll is {rollno} ")

# student_data(rollno=101,name="jatin") 


# defalut argument
# def sum (a=0,b=0):
#    return a+b
# sum()

# # variable length hargument
# def sum(*a):
#     ans=0
#     for i in a:
#      ans+=i
#     print(ans)
# sum(1,2,3,4,4)



def view_data(**kwrag):
    return (kwrag)
dic={ "name": "jatin",
      "rollno": 101,
      "name1": "raj",
      "rollno1": 102,
      "name2": "rohot",
      "rollno2": 103,
    }
view_data(**dic)
view_data(roll1=101,roll2=202,roll3=303, roll4=404,roll=505)




