# 1
# start=int(input("inter the number"))
# end= int (input("inter the number"))
# for i in range( start,end+1):
#     if i%3 and i%5==0:
#         print(i)

# num= int(input("enter the number"))
# sum=0

# for i in range(1,num+1):
    
#     sum=sum+i*i
# print(sum)

# num = int(input("enterthe number"))
# for i in range(1,num+1):
#     print(num*i)


# num=int(input("enter the number"))
# if num<=1:
#     print("not a prime")
# for i in range(2,num):
#     if num%i==0:
#         print("not a prime number")
#         break
# else:
#         print("prime")
 


# num=  int(input("enter the number"))
# rev=0
# temp=num
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10

# if temp==rev:
#     print("palindrom")
# else:
#     print("not a palindrom")


# num= int(input("enter the nunmber"))
# a=0
# b=1
# for i in range(num):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# num=int(input("enter the number"))
# count=0
# while num>0:
#     num=num//10
#     count=count+1
    
# print(count)

# num=int(input("enter the number"))

# for n in range(2,num+1):
#     for i in range(2,n):
#         if n%i==0:
#            break
#     else:
#       print(n)

# a=int(input("enter the number"))
# b= int(input("enter the number"))
# maxNum=max(a,b)
# while(True):
#     if maxNum%a==0 and maxNum%b==0:
#         break
#     maxNum=maxNum+1
# print(maxNum)
       

# base= int(input("enter the number"))
# b=int(input("enter the number"))
# result=1
# for i in range(b):
#     result=result*base
# print(result)

num=int(input("enter the number"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit*digit*digit
    temp=temp//10
if sum==num:
    print("armtrong")
else:
    print("not a armstrong")







