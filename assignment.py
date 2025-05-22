1 # write a program to find maximum between two number
num1= int(input("enter the first number"))
num2= int(input("enter the second  number"))
if num1>num2:
    print("num1 is greatest number")
elif num2>num1:
    print("num2 is greatest")
else:
    print("invalid")

2 # write a program to find maximum  between three number
num1 = int(input("enter the first number"))
num2= int(input("enter the second number"))
num3 = int(input("enter the third number"))

if num1>num2 and num1>num3:
    print("num1 is a greatest")
elif num2>num1 and num2> num3:
    print("num2 is a greatest number")
elif num3>num1 and num3>num2:
    print("num3 is greatest")
else:
    print("invailed")

3 # write a progrom to check whether a number is negative,positive or zero 
num=int(input("enter the number"))
if num>0:
    print("positive")
elif num<0:
   print("negative")
else:
    print("zero")

4# write a program to check whether a number is divisiable 5 and 11 or not
num= int(  input("enter the number"))
if num%5==0 and num%11==0:
    print("divisiable")
else:
  print("not divisiable")

5# write a program to check whether the is even or odd
num= int(input("enter the enumber"))
if num%2==0:
    print("even")
else:
    print("odd")
 
6#  write a program to check a year is leap or not

year= int (input("enter the year"))
if year%4 == 0 or year%400 == 0:
    print("leap year")
else:
    print("not a leap year")

7# write a program to check whether a character is alphabet or not

any = input("enter the charcter")
if  (any>'a'and any<'z') or (any>'A' and any<'Z'):
    print("alphabet")
else:
    print("not  alphabet") 

8# write a program to input any alphabet  and check the whether it is vowel or consonant

char=input("enter the charcter")
if char=='a' or char=='e' or char =='i' or char=='o' or char=='u':
    print("vowel")
else:
    print("consonent")

9# write a program to input any charcter and check whether it  is  alphabet digit and special character

char= (input("enter the charcter"))
if ('a'<=char<='z')or('A'<=char<'Z'):
    print("alphabet")
elif '0'<=char<'9':
    print("digit")
else:
    print("special symbol")


10# write a program to check whether  a character  is uppercase or lowercase

char = input("Enter the character: ")
if 'a' <= char <= 'z':
    print("lowerCase")
elif 'A' <= char <= 'Z':
    print("upperCase")
else:
    print("invalid")

11# write a program to input week number  and print weekday

week= int(input("enter the week number 1 to 7"))
if week==1:
    print("monday")
elif week==2:
    print("tuesday")
elif week==3:
    print("wednesday")
elif week==4:
    print("thursdaay")
elif week ==5:
    print("fridaay")
elif week == 6:
    print("saturady")

else:
    print("weekday")

12#  write a program to input month number and print number of days in that month

month= int(input("enter the month number 1 to 12"))
if month==1:
    print("january 30 day")
elif month==2:
    print("feburary 28or 29 day")
elif month==3:
    print("march 31 days")
elif month==4:
    print("april 30 days")
elif month ==5:
    print("may 31 days")
elif month == 6:
    print("june 30 days")
elif month==7:
    print("31 days")
elif month==8:
    print(" 31 days")
elif month==9:
    print(" 30 days")
elif month ==10:
    print("31 days")
elif month == 11:
    print(" 30 days")
elif month == 12:
    print("31 days")

else:
    print("invalid")

13# write a program to count total  number of notes in given amount/

amount = int (input ("enter a amount"))
notes=[2000,1000,500,200,100,50,20 , 10 ,5,2,1]
for note in notes:
    if amount>=note:
        count=amount//note
        amount%=note
        print (f"{note} x {count}={note*count}")

14# write a program to input angles of a triangle and check whether triangle is valid or not

a = int (input("enter the  first number"))
b = int (input("enter the  second number"))
c = int (input("enter the  third number"))
if a>0 and b>0 and c>0 and a+b+c ==180:
    print ("triangle")
else:
    print("not a triangle")

15# write a program to inpute all sides of a triangle and check the whether triangle is valid or not

a = float (input("enter the  first side"))
b = float (input("enter the  second side"))
c = float (input("enter the  third side"))
if  a+b>c and b+c>a and a+c>b:

    print ("triangle is valid")
else:
    print("not a triangle is not valid")