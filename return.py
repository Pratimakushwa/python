# def multi(a,b):
#     return a*b
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# ans=multi(a,b)
# print(ans)
 

# def multi():
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     return a*b
# print(multi())


# def febo(num):
#     for i in range(2,num):
#         if num%i==0:
#             return "not a prime"
#     return "prime"
# print(febo(3))


# def fact(num):

#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# num=int(input("enter the number"))
# print(fact(num))





# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact =fact*i
#         return fact
# n=int(input("enter a number"))
# print(fact(n))
    

# def natural(n):
#     for i in range(1,n+1):
#       if i%2==0:

#        yield i

      

# n=int(input("enter the number"))
# for num in natural(n):
   
#  print(num)

   
  


# def square(n):
#     return n*n

# n=int(input("enter the number"))
# print(square(n))



# def square(n):
#     print (n*n)

# square(7)


# def square(n):
#     print (n*n)


# # print(square(7))//output none because of there is using print again

# def num(n):

#     if n%2!=0:
#       return "odd"
#     else:
#       return "even"

     
    

# n=int(input("enter the number"))
# print(num(n))

# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             yield i
    


# n=int(input("enter the number"))
# for num in even(n):
#     print(num)
    

# def reverse(s):
  
#       return s[: : -1 ] 



# print(reverse("helllo"))


# def prime(n):
   
    
#   for i in range(2,n):
#     if n%i==0:
#         return "false"
#     else:
#         return "true"

    

# n= int(input("enter the number"))
# print(prime(n))



# def arm(n):
#     temp=n
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum=sum+digit*digit*digit
#         temp=temp//10
#   if sum==n:
#     return "armstrong"
#  else:
#     return "not aremstrong"

# n=int(input("enter the number"))
# print(arm(n))



# def add(a,b):
#     z=a+b
#     print(z)
# print(add(4,5))

# def add(a,b):
#     z=a+b
#     return z
# p=add(4,5)
# print(p)

# def add(a,b):
#     z=a+b
#     return z
# p=int (input("enter the first number"))
# q=int(input("enter the second number"))
# print(add(p,q, 10))

# def add(a,b):
#     z=a+b
#     return z
# p=int (input("enter the first number"))
# q=int(input("enter the second number"))
# print(add())

# def add(a,b):
#     z=a+b
#     return z
# p=int (input("enter the first number"))
# q=int(input("enter the second number"))
# print(add())


# //default argument
# def add(a=0,b=0):
#     z=a+b
#     return z
# # p=int (input("enter the first number"))
# # q=int(input("enter the second number"))
# print(add())


# def add(a,b):
#     z=a+b
#     return z
# p=int (input("enter the first number"))
# q=int(input("enter the second number"))
# print(add())


# def add(*args):
#     print(args)
#     print(type(args))
# add(2,4)
# add(2,3,4,56,3)

# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# # print(add(1,2,3,4,5,6))
# print(add())


# t=(1,2,3,4,5,6,7)


# x= eval(input("enter the value"))
# print(type(x))

# x= eval('4+5-2')
# print(x)


# x=eval(input( "enter the value x"))
# y=eval(input( "enter the value"))

# z=3*x+4*y
# print(z)

# def new(x,y,z):
#     print(x,y,z)
#     return x+y+z
# print(new(z=5,y=4,x=3))


# def mydict(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# mydict(x=10,y=20,z=30,p=40,q=30)


# mytr={'x':19,'y':20,'u':2}
# sum=0
# for i in mytr.values():
#     sum=sum+i
# print(sum)

# def mydict(**kwargs):
#    sum=0
#    for i in kwargs.values():
#    sum=sum+i
#    return sum
# print(mydict(x=10,y=20,z=30,p=40,q=30))



# def is_prime(n):
#     is_prime=True
#     for i in range(2,n):
#         if n%i==0:
#             is_prime= False
#             break
#     return is_prime

# n=int(input("enter the number"))
# is_prime(n)
# if is_prime:
#   print("prime number")
# else:
#     print("not a prime number")
    
# def year(y):
#     if (y%4 ==0 or y%400==0):
#         print("leap year")
#     else:
#         print("not a leap year")


# y=int(input("enter the number"))
# year(y)

# def even(n):
#     if n%2==0:
#         print("even")

#     else:
#         print("odd")
# n=int(input("enter the number"))
# even(n)

# def digit(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=digit+sum
#         n=n//10
#     print(sum)
# n=int(input("enter the number"))
# digit(n)

# def digit(n):
#     temp=n
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum=sum+digit*digit*digit
#         temp=temp//10
#     if n==sum:
#       print("armstrog")
#     else:
#        print("not a armstrong")
# n=int(input("enter the number"))
# digit(n)


# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#         return fact
    

# n=int(input("enter the number"))
# print(fact(n))






# def is_prime(n):
#     is_prime=True
#     for i in range(2,n):
#         if n%i==0:
#             is_prime= False
#             break
#     if is_prime:
#       print("prime number")
#     else:
#        print("not a prime number")

# n=int(input("enter the number"))
# is_prime(n)


# l1=[1,2,3,4,56,7]
# l2=[1,2,3,4,56,7]
# l3=[1,2,3,4,56,7]
# def add(x,y,z):
#     return x+y+z
# result=map(add,l1,l2,l3)
# print(result)
# print(list(result))


# l4=[1,3,5,7,3,]
# def squre(x):
#     return x**2
# result=map(squre,l4)
# print(result)
# print(list (result))

l5=[2,3,4,5,6,7,8,9]
def even(x):
    if x%2==0:
        return even
result=filter(even,l5)
print(result)
print(list(result))
