# n=int(input("enter the number"))
# # factor=[]
# for i in range(1,n):
#     if n%i==0:
#         # factor.append(i)
#      print(i,end=" ")


# n=int(input("enter the number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if (n==sum):
#     print ("perfect number")
# else:
#     print("not perfect number")

# start=int(input("enter the start number"))
# end =int(input("enter the end number"))
# for num in range(start,end+1):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum=sum+i
#     if num==sum:
#      print(num)
        
# start=int(input("enter the start number"))
# end =int(input("enter the end number"))
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                break
#         else:
#          print(num)
        


# li=[2,4,5,67,8,94,3,2,6]

# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)
            


# l=[2,3,4,67,88,6,5]
# m=max(l)
# print(m)
# l=[1,2,3,4,5,6,7]
# max=l[0]
# for i in range(1,l+1):
#     if max < l[i]:
#         max=l[i]
# print(max)
        

# li=[1,2,3,4,5,6]
# target=10
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]+ li[j]==target:
#             print("true")


# li=[1,0,3,3,0,0,4]
# l=[]
# for i in li:
#     if i!=0:
#         l.append(i)
# n=len(li)-len(l)
# for i in li:
#     l.append(0)
# print(l)


# n=int(input("enter the number"))
# if n>=1:
#     print("positive number")
# else:
#     print("negative")

# n=int (input("enter the number"))
# if n>=1:
#     print("positive")
# elif n<0:
#     print("negative")

# else:
#     print("zero")

# a=20
# b=30
# temp=a
# a=b
# b=temp

# print(a)
# print(b)

# a=20
# b=30
# a=a+b
# b=a-b


# hight=int(input("enter the number"))
# base=int(input("enter the number"))
# area=0.5*hight*base
# print(area)

# side=int(input("enter the number"))
# a=side*side
# print(a)


# year=int(input("enter the year"))
# if (year%4==0) or (year%400==0 and year%100 !=0 ):
#     print("leap year")

# else:
#     print("not a leap year")


# n=int(input("enter the number"))
# i=1
# while i<=n:
#    print(i,end=" ")
#    i=i+1

# n=int(input("enter the number"))

# i=1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1
    
  
# n=int(input("enter the number"))
# fact=1
# i=1
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)

# n=input("enter the number")
# i=1
# while i<=18:
#     print("pratima")
#     i=i+1


# s="python"
# consonent=0
# vowel=0
# v="aeiouAEIOU"
# i=0
# while i<len(s):
#     if s[i] in v:
#         vowel=vowel+1
#     else:
#         consonent=consonent+1
#     i=i+1
# print(" vowel is",vowel)
# print("consonent is ",consonent)


# s="python"
# consonent=0
# vowel=0
# v="aeiouAEIOU"
# for i in s:
#     if i in v:
#         vowel=vowel+1
#     else:
#         consonent=consonent+1
# print(" vowel is",vowel)
# print("consonent is ",consonent)



# l=[2,3,4,5,6,7,89]
# result=[]
# i=0
# while i<len(l):
#     l[i]=l[i]+5
#     i=i+1
# print(l)

# s="python"
# lst=[]
# i=0
# while i < len(s):
#     lst.append(s[i])
#     i=i+1
# print(lst)


# s="python"
# count=0
# for i in range (len(s)):
#     count=count+1
# print(count)

# s="python"
# rev=s[: :-1]
# print(rev)
# s="python"
# rev="".join(reversed(s))
# print(rev)


# s="python"
# rev=""
# for ch in s:
#     rev=ch+rev

# print(rev)



    # lcm

# x=int(input("enter the number"))
# y=int(input("enter the number"))
# if x>y:
#     greater=x
# else:
#     greater=y
# while(True):
#     if ((greater % x==0) and (greater % y== 0) ):
#         lcm=greater
#         break
#     greater=greater+1
# print(lcm)





# n=int(input("enter the number"))
# temp=n
# sum=0
# while temp>0:
#     digit=temp % 10
#     sum=sum+digit*digit*digit
#     temp=temp//10
# if sum==n:
#     print("armstrong")
# else:
#     print("not armstrong")

n=int(input("enter the number"))
rev=0
temp=n
while temp >0:
    digit=temp%10
    