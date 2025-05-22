# num= input("enter the number")
# print(num[: : -1])


# a,b= 10,20
# a,b = b,a
# print (a)
# print(b)

# li =[1,2,3,4,5]
# for i in li:
#     print(i)

# for i in range(1, 11):
    # print(i)

# for i in range(len(li)):
    # print(i)
    # print(i,"=",li[i])

# li=[1,2,3,4,56]
# mx=0
# for i in range(len( li)):
#     if mx <li[i]:
#         mx=li[i]
# print(mx)

# li=[1,2,3,4,56]
# min=56
# for i in range(len( li)):
#     if min >li[i]:
#         min=li[i]
# print(min)


# li=[1,2,3,4,56]
# min=9
# for i in range(len( li)):
#     if min >li[i]:
#         min=li[i]
# print(min)




# num= int(input("enter the enumber"))
# if num>0:
#     print("positive")
# else:
#     print("negative")


# num1= int(input("enter the first number"))
# num2= int(input("enter the second  number"))
# if num1>num2:
#     print("num1 is greatest number")
# elif num2>num1:
#     print("num2 is greatest")
# else:
#     print("invalid")

# num1 = int(input("enter the first number"))
# num2= int(input("enter the second number"))
# num3 = int(input("enter the third number"))
# if num1>num2 and num1>num3:
#     print("num1 is a greatest")
# elif num2>num1 and num2> num3:
#     print("num2 is a greatest number")
# elif num3>num1 and num3>num2:
#     print("num3 is greatest")
# else:
#     print("invailed")

# char=input("enter the charcter")
# if char=='a' or char=='e' or char =='i' or char=='o' or char=='u':
#     print("vowel")
# else:
#     print("consonent")

# any = input("enter the charcter")
# if  (any>'a'and any<'z') or (any>'A' and any<'Z'):
#     print("alphabet")
# else:
#     print("not  alphabet") 

# year= int (input("enter the year"))
# if year%4 == 0 or year%400 == 0:
#     print("leap year")
# else:
#     print("not a leap year")


# char= (input("enter the charcter"))
# if ('a'<=char<='z')or('A'<=char<'Z'):
#     print("alphabet")
# elif '0'<=char<'9':
#     print("digit")
# else:
#     print("special symbol")



# char = input("Enter the character: ")

# if 'a' <= char <= 'z':
#     print("lowerCase")
# elif 'A' <= char <= 'Z':
#     print("upperCase")
# else:
#     print("invalid")


# week= int(input("enter the week number 1 to 7"))
# if week==1:
#     print("monday")
# elif week==2:
#     print("tuesday")
# elif week==3:
#     print("wednesday")
# elif week==4:
#     print("thursdaay")
# elif week ==5:
#     print("fridaay")
# elif week == 6:
#     print("saturady")

# else:
#     print("weekday")

# month= int(input("enter the month number 1 to 12:"))
# if month==1:
#     print("january 30 day")
# elif month==2:
#     print("feburary 28or 29 day")
# elif month==3:
#     print("march 31 days")
# elif month==4:
#     print("april 30 days")
# elif month ==5:
#     print("may 31 days")
# elif month == 6:
#     print("june 30 days")
# elif month==7:
#     print("31 days")
# elif month==8:
#     print(" 31 days")
# elif month==9:
#     print(" 30 days")
# elif month ==10:
#     print("31 days")
# elif month == 11:
#     print(" 30 days")
# elif month == 12:
#     print("31 days")

# else:
#     print("invalid")


# num=int(input("enter the number"))
# first=0
# second=1
# print( first,second)
# for i in range(num-2):
#  next= first+second
#  first= second
#  second= next
#  print(next,end="")


# a= int (input("enter the number"))
# ans=0
# for i in range(1, a ):
#  if a%i==0:
#    ans+=i
# if ans==a:
#   print("perfact")
# else:
#   print("not perfact")
  



# li=[1,2,3,4,5]
# max=0
# for i  in range (len(li)):
#     if max<li[i]:
#         max=li[i]
#     second= second< max
#     print(secon
# num=int(input("enter the number"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# amount = int (input ("enter a amount"))
# notes=[2000,1000,500,200,100,50,20 , 10 ,5,2,1]
# for note in notes:
#     if amount>=note:
#         count=amount//note
#         amount%=note
#         print (f"{note} x {count}={note*count}")

# # write a program to input  angle of triangle and check whether  triangle valid or not
# a = int (input("enter the  first number"))
# b = int (input("enter the  second number"))
# c = int (input("enter the  third number"))
# if a>0 and b>0 and c>0 and a+b+c ==180:
#     print ("triangle")
# else:
#     print("not a triangle")

    # write a program to input  angle of triangle and check whether  triangle valid or not
a = float (input("enter the  first side"))
b = float (input("enter the  second side"))
c = float (input("enter the  third side"))
if  a+b>c and b+c>a and a+c>b:

    print ("triangle is valid")
else:
    print("not a triangle is not valid")