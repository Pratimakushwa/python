#create a list of word which have more then 4 character.
#Input:- ["aman","raj","rahul","jatin","pratima","gauri","prince"]
#output: ["rahul","jatin","pratima","gauri","prince"]


# a=["aman","pratima", "jatin"]
# li=[i for i in a if len(i)>4]
# print(li)

# a=[21, -7,5,64,-4]
# li=[i for i in a if i<0]
# print(li)

# s=" hello world"
# li=[i for i in s if i in "aeiou"]
# print(li)

# li=[{i:i*i} for i in range(1,6)]
# print(li)

# s="education"
# li= { i for i in s}
# print(li)



# li=[ i for i in range(1,101 ) if i%3==0 and i%5==0]
# print(li)

# li=[i*i for i in range(1,11) ]
# print(li)

        

   
    



  


# list,tuple,set,dictionary comprihension

#li = [ output for i in range() if ]

# li = [ i for i in range(1,11)]
# li = [ i*i for i in range(1,11) ]

# n=int(input("Enter a Number: ")) 
# li = {n*i for i in range(1,11)}
# print(li)
# li=list()
# for i in range(1,11):
#     li.append(i)







# for i in range(1, 6):
#     for j in range( 1,6):
#         if(i>=j):
#            print(j, end="")

         
#         print(end=" ")
#     print()

# for i in range(1, 6):
#     for j in range( 1,6):
#         if(i<=j):
#            print(j, end="")
#         else:
#          print(end=" ")
#     print()


# rows=5 
# for i in range(1, rows+1):
#     for j in range( 1, rows+1):
#         if(i<=6-j):
#            print(j, end="")
#         else:
#          print(end=" ")
#     print()


# for i in range(1, 6):
#     for j in range( i, 6):
        
#         print(j, end="")

#     print()

# rows=5 
# for i in range(1, rows+1):
#     for j in range( 1, rows+1):
#         if(i>=6-j):
#            print(j, end="")
#         else:
#          print(end=" ")
#     print()




# row = int(input("Enter Number of rows: "))
# a=65
# alpha=chr(a)
# for r in range(1,row+1):
#     for c in range(1,row+1):
#         if c<=r:
#             print(alpha,end=" ")
#             a=a+1
#             alpha=chr(a)
#         else:
#             print(" ",end=" ")
#     print()

# row = int(input("Enter Number of rows: "))
# a=65
# alpha=chr(a)
# for r in range(1,row+1):
#     for c in range(1,row+1):
#         if c<=r:
#             print(alpha,end=" ")
#             a=a+1
#             alpha=chr(a)
#         else:
#             print(" ",end=" ")
#     print()




# for i in range(1, 6):
#     for j in range( 1,6):
#         if(i>=j):
#            print(j, end="")

         
#         print(end=" ")
#     print()


# for i in range(1, 6):
#     for j in range( 1,6):
#         if(i<=j):
#            print(j, end="")
#         else:
#          print(end=" ")
#     print()













# li=[1,2,4,5,7,2]
# ans=li[:]
# for i in range(len(li)):
#     for j in range( i+1,len(li)):
#         if li[i]>li[j]:
#             li[i], li[j]=li[j],li[i]
           
# if li==ans:
#     print("yes")
# else:
#     print("no")      
        






# li=[1,2,3,4,5,6]
# max=li[0]
# for i in li:
#     if i>max:
#         max=i
        
# print(max)

  
        



# li=[1,2,3,4,4,5,2,5,31,3,1,3,6,6]
# freq={}
# count=0
# for i in li:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for value in freq.values():
#     if value>1:
#         # print(f"{value} -> {freq[value]} times")
#         count=count+1
# print(" total duplicate value",count)


# li=[1,2,3,4,5,6,7,1,2,3,4,5,6,7]
# freq={}
# for i in li:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for value in freq:
#     freq[value]>1
#     print(f"{value} -> {freq[value]},times")
   



# li=[1,2,3,4,5,6,7]
# for i in range(len(li)):
#     if i%2==0:
#         print(i)

# li=[]
# for i in range(1,11):
#     if i%2==0:
#         li.append(i)
# print(li)

# li=["apple","mango","lichi"]
# data={ }
# for i in li:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# print(data)

# li=[1,2,3,4,5,6,6,7,4]
# data=[]
# for i in range(len(li)):
#     if i not in data:
#         data.append(li(i))
# for i in range(len(li)):
#     for j in range(i+1, len(li)):


# li=["apple", "mano", "lichi"]
# for i in li:
#     print(i,len(i))

# li=[1,2,3,4,56,7,2,3,4]
# data={}
# count=0
# for i in li:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# for value in data:
#     data[value]>1
#     count=count+1
# print(count)

# li=[1,2,3,45,6,7]

# li.insert(2,5)
# li.pop(2)
# print(li)
# li=["apple","mango","lichi"]
# for i in li:
#     print(i,len(i))



# s="hello World"
# uppercase=0
# lowercase=0
# for i in s:
#     if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#         uppercase+=1
#     else:
#         lowercase+=1
# print("uppercase is a",uppercase)
# print("lowercase is a",lowercase)

# a="helloworld"
# data={}
# for i in a:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# for  key in data:
#     data[key]>1
#     print(f"{key}  {data[key]}")

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if i*i==n:
#         print("perfect square")
#         break
#     i=i+1
# else:
#     print("not a perfact square")
    
    

# n= int(input("enterthe number"))

# if n<=1:
#     print("not a prime number")
   
# for i in range(2,n):
#     if n%i==0:
#         print("not a prime number")
#         break
# else:
#     print("prime number")

    
# n=int(input("enter the number"))
# i=1
# while n>i:
#     if i*i==n:
#         print("perfect square")
#         break
#     i=i+1
# else:
#     print("not a perfect square")


    

        
# dic={
#     "name":"pratima",
#     "age":21
# }
# data={}
# for i in dic:
#     if i in data:
#         data[i]+=1
#     else:
#         data[i]=1
# print(data)
 

# dic={
#     "jatin":50,
#     "ram": 40,
#     "raj":80
# }
# max=0
# for i in dic:
#     if dic[i]>max:
#         max=dic[i]
#         ans=i
# print(ans)

# dic={
#     "jatin":50,
#     "ram": 40,
#     "raj":80
# }
# min=0
# for i in dic:
#     if dic[i]<min:
#         min=dic[i]
#         ans=i
# print(ans)



# key=['a','b']
# value=[1,2]
# d = {}
# for i in range(len(key)):
#     d[key[i]]==value[i]
# print(d)

# data={'items':120,'item2':130,'item3': 30}
# ans={ key:value for key,value in data.items()if value>100}
# print(ans)

# li={"data","science","python"}
# ans={  i:len(i) for i in li }
# print(ans)
# [expression for i in <expression> if <expression>]

# li=[i if i%2==0 else i for i in range(1,11) if i>5]
# print(li)

# prime number using comprehension

# ans=[i for i in range(1,101)if all(i%j!=0 for j in range (2,int(i**0.5)+1)) ]
# print(ans)
# for i in range(1,101):
#     is_prime=True
#     for j in range(2,int(i**0.5)+1):
#         if i%j==0:
#             is_prime=False
#     if is_prime:
#          print(i)

# tu=(i*i for i in range(1,11))
# tu=list(tu)
# print(tu)

# tu=(i*i for i in range(1,11))


# s="helow234"
# count=0
# for i in s:
#     if i in "123456789":
#         count=count+1
# print(count)
        

# num=1
# for i in range(1,10):
#     for j in range(i):
#         if num>11:
#             break
#         print(num ,end=' ')
#         num=num+1
#     print()

# ch=65
# for i in range(1,5):
#     for j in range(i):
#          print(chr(ch), end=' ')
#     ch=ch+1
#     print()
 
    
# list=[2,3,4,5]
# new=[]
# for i in list:
#     new.append(i)
# print(new)

# list=[2,3,4,5]

# for i in range(len(list)):
#     list[i]=list[i]*2
    
# print(list)

# list=[2,3,4,5,6,7]
# print(max(list))
# x={1,2,3,4,5}
# print(max(x))

# 
# t=(1,2,3,4,5,6)
# for i in t:
#     print(i)

# t=("hello",)
# print(type(t))

# t=(1,2,3,4,5,6,7,8)
# for i in t:
#     if i % 2==0:
#       print(i)

# s="python"
# t=tuple(s)
# print(t)
# s="python"
# tu=( i for i in s)
# tu=list(tu)
# print(tu)

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print( ' ' *(n-1)+' * '* i)

#     i=i+1
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print("*"*n)
#     i=i+1
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print('*'* i)
#     i=i+1






# n=int(input("enter the number"))
# i=1
# while i>0:
#     print('' *(n-i)+'*' *i)

#     i=i-1




# n = int(input("enter the number"))
# i = 1
# while i <= n:
    # print(" " * (n - i) + "*" * i)
    # print("*" * i +" " *(n-i))
    # print("*" *(n-i)+ " " *i)
#     print(" "*i+"*" *(n-i))
# #     print("*" *(n-i) +" "*i)
#     i = i + 1


# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print(''*(n-i)+'*' *i)
#     i=i+1
# i=i-2
# while i>=1:
#     # print(''*(n-i)+'*' *i)
#     print('*' *i + ''*(n-i))
#     # print(" " *(n-i)+ "* " *i)

#     i=i-1

# n = int(input("enter the number"))
# i = 1

# # upper half
# while i <= n:
#     print(" " * (n - i) + "*" * (2*i-1))
#     i = i + 1

# # lower half
# i = i - 2
# while i >= 1: 
#     print(" " * (n - i) + "*" * (2*i-1))
#     i = i - 1



# n = int(input("Enter the number: "))
# i = 1

# while i <= n:
#     # spaces + stars
#     print(" " * (n - i) + "*" * i )
#     i = i + 1

# //////////////////
# n=int(input("enter the number"))
# i=1
# while(i<=n):
#     print("*"*i+ ""*(n-i))
#     i=i+1

# n=int(input("enter the number"))
# i=1
# while(i<=n):
#     print(" "*(n-1)+"*"*i)
#     i=i+1


# n=int(input("enter the number"))
# i=1
# while(i<=n):
#     print("*"*(n-i)+" "*i )5

#     i=i+1



# pyramid
# n=int(input("enter the number"))
# i=n
# while(i>=1):
#     print(" "*(n-i)+'*'*(2*i-1))
#     i=i-1


# n=int(input("enter the number"))
# i=1
# while(i<=n):
#     print(" " *(n-i)+"*"*(2*i-1))
#     i=i+1


    # hourglass
# n=int(input("enter the number"))
# i=n
# while(i>=1):
#     print(" "*(n-i)+'*'*(2*i-1))
#     i=i-1
# i=2
# while(i<=n):
#     print(" " *(n-i)+"*"*(2*i-1))
#     i=i+1


# n = int(input("Enter number: "))

# # upper
# i = 1
# while i <= n:
#     print("*" * i)
#     i += 1

# # lower
# i = n-1
# while i >= 1:
#     print("*" * i)
#     i -= 1

# n = int(input("Enter rows: "))

# # Right Triangle
# i = 1
# while i <= n:
#     print(" " * (n - i) + "*" * i)
#     i += 1

# # Inverted Right Triangle
# i = n
# while i >= 1:
#     print(" " * (n - i) + "*" * i)
#     i -= 1

# n = int(input("Enter rows: "))

# # Upper triangle
# i = 1
# while i <= n:
#     print("*" *i+" "*(n-i))
#     i += 1

# # Lower inverted triangle
# i = n - 1
# while i >= 1:
#     print(" " *(n-i)+"*" *i)
#     # print("*" *i+" "*(n-i))

#     i -= 1
# n = int(input("Enter rows: "))

# # Upper triangle
# i = 1
# while i <= n:
#     print(" "*(n-i)+"*" * i)
#     i += 1

# # Lower inverted triangle
# i = n - 1
# while i >= 1:
#     # print(" " *(n-i)+"*" *i)
#     print("*" *i+" "*(n-i))

#     i -= 1

# n=int(input("enter the number"))
# i=1
# while i<=n:
#     print(" "*(n-i),end=" ")
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1


# n = int(input("enter the number"))
# i = n
# while i >= 1:
#     print(" " * (n - i), end="")     # spaces
#     j = 1
#     while j <= i:
#         print(chr(65+j), end="")             # 1 2 3 ...
#         j = j + 1
#     print()
#     i = i - 1


# n=int(input("enter the number"))
# i=n
# while i>=1:
#     j=0
#     while j<i:
#         print( chr(65+j),end="")
#         j= j + 1
#     print()
#     i=i-1

# dictionary of months and days
months = {
    "january": 31,
    "february": "28 or 29",
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

month = input("Enter month name: ")

# search using for loop
found = False
for m in months:
    if m == month:
        print(f"{m.capitalize()} has {months[m]} days")
        found = True   # ✅ alag line me
        break

if not found:
    print("❌ Invalid month name")
