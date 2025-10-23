
# n=5
# s='A'
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(i):
#         print(s,end='')
#         s=chr(ord(s)+1)
#     print()


# # n=int(input("enter the number"))
# # fact=[]
# # for i in range(1,n+1):
# #     if n%i==0:
# #          fact.append(i)
# # print(fact)



# # start=int(input("enter the number"))
# # end=int(input("enter the end number"))
# # l=[]
# # for i in range(start,end+1):
# #     if i%2==0:
# #         l.append(i)
# # print(l)


# n=int(input("enter the number"))
# y=x=n
# sum=0
# count=0
# while n>0:
#     count=count+1
#     n=n//10
while x>0:
    digit=x%10
    sum=sum+digit**count
    x=x//10
if y==sum:
    print('armstron')
else:
    print('not armstrong')

n=int(input('enter the number'))
count=0
while n>0:
    n=n//10
    count=count+1
print(count)



n=int(input("enter the number"))
x=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
if x%sum==0:
    print("harsad number")
else:
    print("not a harsad number")

n=int(input("enter the number"))
x=n
sum=0
s=n*n
while s>0:
    digit=s%10
    sum=sum+digit
    s=s//10
if x==sum:
    print("neon number")
else:
    print("not a neon number")

n=int(input("enter the number"))
sum=0
product=1
while n>0:
    digit= n%10
    sum=sum+digit
    product=product+digit