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


# def multi(a,b):
#     print(a*b)
# x=int(input("enter the first  number"))
# y=int(input("enter the secound  number"))
# multi(x,y)



# def add(n):
#     temp=n
#     sum=0
#     while temp>0:
#         digit= temp%10
#         sum=sum+digit*digit*digit
#         temp=temp//10
#     if sum == n:
#         print("armstrong")
#     else:
#         print("not a armstromg")
# num= int(input("enter the number"))
# add(num)



# def add(num):
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit*digit*digit
#     temp=temp//10
# if sum==num:
#     print("armtrong")
# else:
#     print("not a armstrong")
# num=int(input("enter the number"))
# add(num)




# def reverse(a):
#     rev=0
#     temp=num
#     while  temp>0:
#         digit =temp%10
#         rev=rev*10+digit
#         temp=temp//10
#     if num==rev:
#         print("palindrom")
#     else :
#         print("not a palindrom")
# num=int(input("enter the number"))
# reverse(num)



# def fact(num):
#     a=0
#     b=1
    
#     for i in range(2,num):
#         print(a)
#         c=a+b
#         print(c)
#         a=b
#         b=c
# num=int(input("enter a number"))
# fact(num)






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



# def view_data(**kwrag):
#     return (kwrag)
# dic={ "name": "jatin",
#       "rollno": 101,
#       "name1": "raj",
#       "rollno1": 102,
#       "name2": "rohot",
#       "rollno2": 103,
#     }
# view_data(**dic)
# view_data(roll1=101,roll2=202,roll3=303, roll4=404,roll=505)



# n=100
# for i in range(101,1,-1):
#    print(i)

# n=100
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)

# li=[4,7,12,19]
# for i in li:
#     print(i)

# li=[1,2,3,4,5,7,84,9]
# data=[]
# for i in li:
#     if i%2==0:
#         data.append(i)
# print(data)


# n=5
# for i in range(1,11):
#     print(n*i)
   

# n=int(input("enter the number"))
# for i in range(n):
#     print(i*i)

# s="hello"
# for i in s:
#     print(i)

# fruit=["apple", "banana","mango"]
# for i in range(len(fruit)):
#     print( fruit[i])
# for i in range(10,0,-1):
#     if i%2!=0:
#      print(i)

# n=int(input("enter the number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# s="helloooo"
# count=0
# for i in s:
#     if i in "aeiou":
#         count=count+1
# print(count)

# s="python"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)