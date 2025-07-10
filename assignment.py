# implement a program to find all the  number is divisiable by 3 and 5 within a range

# start= int(input("enter the  start number"))
# end= int(input("enter the end number"))
# for i in range(start,end+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# 2 write a program to calculate the sum of  square first n natural number
# num= int(input("enter the  n natural number"))
# sum=0
# for i in range(1,num+1):
#     sum= sum+i*i
# print(sum)

# 3 print the multiplication of a number
# num= int(input ("enter the number"))
# for i in range(1,11):
#     print(num*i)

# 4 write a program to check if a number is a prime number
# n= int(input("enter the number"))
# if n<=1:
#     print("not prime")
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

# 5 implement of a program to print reverse of a number
# n=int(input("enter of a number"))
# rev=0
# while n>0:
#     digit= n%10
#     rev= rev*10+digit
#     n= n//10
# print(rev)

# 6 generate febonacci series  up to given term using loop

# n= int(input("enter the number"))
# a=0
# b=1
# print("fibonacci series")
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# # 7 implement a program to count the number of digit in a number
# n=int(input("enter the number"))
# count=0
# while n > 0:
#     n=n//10
#     count=count+1
# print(count)

# 8 write a program to calculate the sum of digit of a number

# n= int (input("enter the number"))
# sum = 0
# while n >  0:
#     digit=n % 10
#     sum=sum+digit
#     n=n//10
# print(sum)

# 9 print all prime number within a range
# n= int(input("enter the number"))
# print ("prime number from 1 to n")
# for num in range(2, n+1):
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)
 

        


            
# 10 write a program to find lcm of two number
# a= int(input("enter the number"))
# b= int(input("enter the number"))
# maxnum=max(a,b)
# while(True):
#    if maxnum%a==0 and maxnum%b==0:
#        break
#    maxnum=maxnum+1
# print(maxnum)

# 11 write a program to find hcf of two number
# a= int(input("enter the number"))
# b= int(input("enter the number"))
# if a<b:
#     min=a
# else:
#     min=b
# for i in range (1,min+1):
#     if a%i==0 and b%i==0:
#         hcf=i
# print(hcf)

#  12 write a program to print power of a number using loop

# a= int (input("enter the base of a number"))
# b=int(input("enter the  exponential number"))
# result=1
# for i in range(b):
#     result=result*a
# print(result)

# 13 check if a number is palindrom using loop
# num=int(input("enter the number"))
# temp=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if temp==rev:
#         print("palindrom")
# else:
#         print("not a palindron")

#  14 print the all armstrong number in the range
# start=int(input("enter the  start number"))
# end =int(input("enter the  end number"))
# for num in range(start,end+1):
#     temp=num
#     order=0
#     while temp>0:
#       order+=1
#       temp//=10
#     temp=num
#     sum=0
#     while temp>0:
       
#      digit=temp%10 
#      sum=sum+digit**order
#      temp=temp//10
#     if sum==num:
#       print(num)
 
 
# 15 inverted half pyramid
# for i in range(1,6):
#     for j in range(1,6):
#         if i>=j:
#             print("*",end="")
#         print(end="")
#     print()

# start= int (input("enter the number"))
# end=int(input("enter the number"))
# for num in range(start,end+1):
#     temp=num
#     sum=0
#     while num>0:
#         digit=num%10
#         sum=sum+digit*digit*digit
#         num=num//10
#     if temp==sum:
#         print(temp)


start=int(input("enter the number"))
end=int(input("enter the numebr"))
even_sum=0
odd_sum=0
for i in range(start,end+1):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("even_sum is a ", even_sum)
print("odd_sum is a ", odd_sum)