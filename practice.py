#lambda funcntion (anonymus function)
# lambda argument: expression
# 1- Use for small solutions/functionality we use lambda function 
# 2- To perform small task lambda function is more readable and faster then normal function
# 3- Mostly use with high order functions like map() filter() and reduce()

# prime = lambda x: x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
# print(prime(5))
 

# greater = lambda x,y: x if x>y else y
# print(greater(15,8))

# cube = lambda x: x*x*x
# print(cube(6))

# square = lambda x: x*x

# print(square(5))

# def square(x):
#     return x*x

# print(square(5))

# lambda funcntion (anonymus function)
# lambda argument: expression
# 1- Use for small solutions/functionality we use lambda function 
# 2- To perform small task lambda function is more readable and faster then normal function
# 3- Mostly use with high order functions like map() filter() and reduce()

# prime = lambda x: x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
# print(prime(5))
 

# greater = lambda x,y: x if x>y else y
# print(greater(15,8))

# cube = lambda x: x*x*x
# print(cube(6))

# square = lambda x: x*x

# print(square(5))

# def square(x):
#     return x*x



# num= int (input("enter the number"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# num= int(input("enter the number"))
# if num>0:
#     print("positive")
# else:
#     print("negative")
# num= int (input("enter the number"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# num= int(input("enter the number"))
# if num>0:
#     print("positive")
# else:
#     print("negative")

# def is_prime(n):
#     is_prime=True
#     for i in range(2,n):
#       if n%i==0:
#         is_prime=False
#         break
#     if is_prime:
#      print("prime number")
#     else:
#      print("not a prime number")
# n=int(input("enter the number"))
# is_prime(n)

# s="ram"
# count=0
# for i in s:
#     count=count+1
# print(count)

# s="rama"
# count=0
# target= "a"
# for i in s:
#     if i==target:
#         count=count+1
# print(count)


# s="python"
# s1=""
# for i in range(5,-1,-1):
#     s1=s1+s[i]
# print(s1)

# def to_lower_case(s):
#     result = ''
#     for ch in s:
#         if 'A' <= ch <= 'Z':
#             result += chr(ord(ch) + 32)
#         else:
#             result += ch
#     return result


# s="apple"
# old="p"
# new="b"
# result=""
# for i in s:
#     if i == old:
#         result += new
#     else:
#         result += i
# print(result)



# s="pratima"

# result=""
# for i in s:
#     if i not in "aeiouAEIOU":
#         result += i
# print(result)
    

# s="banana"
# result=""
# for i in s:
#     if i not in result:
#         result +=i
   
# print(result)


# s="banana"
# result={}
# for i in s:
#     if i in result:
#         result[i] += 1
#     else:
#         result [i]= 1
# print(result)

# n=int(input("ente the number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# n=int(input("enter the number"))
# n1=int(input("enter the number"))
# for i in range(n,n1+1):
#     if i%3==0 and i%5==0:
#         print(i)
    

# n=int(input("enter the numbe"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i*i
# print(sum)

# n=int(input("enter the numbe"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# n=int(input("enter the number"))
# sum=0
# while(n>0):
#     digit=n%10
#     sum=sum+digit
#     n=n//10

# print(sum)

a=int(input("enter the number"))
b=int(input("enter the number"))
result=1
for i in range(b):
    result=result*a
print(result)