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

# n=int(input("enter the number"))

# count=0
# while n>0:
#     n//=10
#     count=count+1
# print(count)

# n=int(input("enter the number"))
# rev=0
# while (n>0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)
 
# n=int(input("enter the number"))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n= n//10
# print(sum)

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
    # i=i+1
# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# for num in range(n1,n2+1):
#     if num > 1:
#         for j in range(2,num):
#             if num%j==0:
#                 break
#         else:
#             print(num)
    


# start=int(input("enter the number"))
# end=int(input("enter the number"))
# for n in range(start,end+1):
#     if n>0:
#         for j in range(2,n):
#             if n%j==0:
#                 break
#         else:
#             print(n)

# n=int(input("enter the number"))
# i=1
# while i<=10:
#     print(f"{i}x{n}={i*n}")
#     i=i+1
   
        
# i=i+1

# for i in range(1, 6):       # 1 to 5 tables
#     print(f"\nTable of {i}")
#     for j in range(1, 11):  # 1 to 10 multiplication
#         print(f"{i} x {j} = {i*j}")



# list=[1,2,3,4,5,6,7]
# for num in list:
#     print(num ,end=" ")

# li=[1,2,3,4,5,5]
# li.append(7)
# print(li)


# list=[4,5,6,7,8,93,5]
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)


# li=[2,3,4,5,6]
# li.reverse()
# print(li)




# set={2,3,4,5,6,3,6,4,5}
# set.add(37)
# print(set)

# list=[2,3,4,5,6,7]
# # print(list[2])
# print(list[2:5:])


# li=[3,4,5,6,7,8]
# li.append(9)
# print(li)


# list1=[2,3,4,5,6,7]
# list2=[4,5,6,78,9,99]
# list1.extend(list2)
# print(list1)

# list=[1,2,3,4,5,6]
# list.insert(2,44)
# print(list)

# list=[2,3,4,5,6,7]
# list.remove(4)
# print(list)

# list=[2,3,4,6,7,4]
# list.reverse()
# print(list)


tu=(2,3,4,4,65,5,5,67,5,67,7)
for i in tu:
    print(i)