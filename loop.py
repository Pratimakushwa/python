# num= int(input("enter the number"))
# for i in range(1, num):
#     print(i)

# num= int(input("enter the numebr"))
# for i in range( 1, num):
#     if i%2==0:
#         print(i)

# num= int(input("enter the numebr"))
# for i in range( 1, num):
#     if i%2!=0:
#         print(i)

# num= int(input("enter the numebr"))
# sum=0
# for i in range( 1, num):
#     sum=sum+i
#     print("total sum :", sum)
    
# num= int(input("enter the numeber"))
# sum=0
# while num>0:
#     digit= num % 10
#     sum+=digit
#     num=num// 10

# print("sum of digit:",sum)
    


# num= int(input("enter the numebr"))
# rev=0
# while num>0:
#     digit=num%10
#     rev= rev*10+ digit
#     num=num//10
# print(rev)

# num= int(input("enter the numebr"))
# greatest=0
# while num>0:
#     digit= num % 10
#     if digit>greatest:
#         greatest=digit

#     num=num// 10

# print(greatest)
    


# num= int(input("enter the numebr"))
# min=num%10
# num= num//10
# while num>0:
#     digit= num % 10
#     if digit<min:
#         min=digit

#     num=num// 10

# print(min)
    
# num= int(input("enter the numebr"))
# min=0

# while num>0:
    
#     if num<min:
#         min=num



# # print(min)
# num=int(input("inter the number"))
# temp=num
# rev=0
# while num>0:
#  digit= num%10
#  rev=rev*10+digit
#  num=num//10
#  if temp==rev:
#   print("palindrom")
#  else:
#   print("not a palindrom")


#non-return without argument

# def factorial():
#     a=int(input("Enter a Number: "))
#     ans=1
#     for i in range(1,a+1):
#         ans*=i
#     print(ans)


# factorial()

# WAP to print a sum of n natural number
# WAP to print fibonacci series 01123

# def fibnacci():
#     n= int (input("enter the number"))
#     first=0 
#     second=1
#     for i in range(n):
#         if i==0:
#             print(first)
#             continue
#         if i==1:
#             print(second)
#             continue
#         next= first+second
#         first= second
#         second= next
#     print(next)
# fibnacci()
# fibnacci()
    
    
# def natural():
#  n= int (input ("enter the number"))
#  for i in range(1,n):
#     print(i)
# natural()


#Prime Number
#perfect Number
#pallindrom

#return type without argument
# def isprime():
#     num = int(input("ENter a Number: "))
#     if num>1 and all(num%i!=0 for i in range(2,num)):
#         return "Prime"
#     else:
#         return "Not a Prime"
    
# ans=isprime()
# print(ans)

# def perfect():
#     num= int(input("enter the number"))
#     ans=0
#     for i in range(1,num):
#         if num%i==0:
#              ans+=i
#     if ans==num:
#           return "perfect"
#     else:
#           return "not perfect"
# # a= perfect()
# print(a)

# def fact():
#     num=int(input("enter the number"))
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# a=fact()
# print(a)

# def palindrom():
#     num=int(input("enter the number"))
#     rev=0
#     temp=num
#     while num>0:
#      digit= num%10
#      rev= rev*10+digit
#      num= num//10
#     if temp== rev:
#         return "palindrom"
#     else:
#         return " not a palindron"
    
# a = palindrom()
# print(a)


# def max():
#     num= int(input("enter the number"))
#     max=0
#     while num>0:
#         digit=num%10

#         if max<digit:
            
#             max=digit
#         num=num//10
#     return max
       
# a = max()
# print(a)

def prime():
    num=int(input("enter the number"))
    count =0
    for i in range(1,num):
        if num%i==0:
            count=+1
    if count==2:
        return("prime")
    else:
        return("not a prime")
a = prime()
print(a)



        