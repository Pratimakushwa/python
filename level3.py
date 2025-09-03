# num=int(input("enterr the number"))
# for i in range(1,num+1):
#     print(i)

# for i in range(10,0,-1):
#     if i%2==0:
#         print(i)


# i=10
# while i>=1:
#     print(i)
#     i=i-1

# n=int(input("enter the number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)


# n=int(input("enter the number"))
# i=1

# while i<=10:
#     print(n*i)
#     i=i+1
   
# n=int(input("enter the number"))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
#     i=i+1
  

# print(fact)


    
   
# n= int(input("enter the number"))
# a=0
# b=1
# for i  in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c


# n=int(input("enter the number"))
# for i in range(2,n):
#     if n%i==0:
#         print(" not a prime ")
#         break
# else:
#         print(" prime number")


# n=int(input("enter the number"))
# i=2
# while i<=n:
#     if n%i==0:
#         print("not a prime number")
#         break
#     i=i+1
# else:
#     print("prime number")


# n=30
# for i in range(1,n+1):
#     if i%3==0:
#         print(i)
# n=30
# for i in range(1,n+1):
#     if i%3==0:
#         if i==9:
#             continue
#     print(i)\\\


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print("*"*i+""*(n-i))
#     i=i+1

# n = int(input("enter the number"))
# i = 1


# while i <= n:
#     print(" " * (n - i) + "*" * (2*i-1))
#     i = i + 1

n=int(input("enter the number"))

count=0
while n>0:
    n//=10
    count=count+1
print(count)

 