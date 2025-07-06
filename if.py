# num=int(input("enter the  number"))
# if num>=1:
#     print("positive")
# elif num<=1:
#     print("negative")
# else:
#     print("zero")


# num=int(input("enter the enter"))
# if num%2==0:
#     print("even")
# elif num%2!=0:
#     print("odd")
# else:
#     print("invalid")

# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enterthr number"))
# if a>=b and a>=c:
#     print(" a is greatest")
# elif b>=a and b>=c:
#     print("b is a greatest")
# elif c>=a and c>=b:
#     print("c is the gretest")
# else:
#     print("invalid")

# year=int(input("enter the number"))
# if year%4 ==0 or year%400 ==0:
#     print("leap year")

# else:
#     print("not a leap year ")



# age=int(input("enterr the number"))
# if age>=18:
#     print("eligiable")

# else:
#     print("not eligiable")


# a=input("enter the charcter")
# if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' :
#     print("vowel")
# else:
#     print("consonent")

# b=10000
# correct_pin=1234
# pin=int(input("enter your correct pin"))
# if pin==correct_pin:
#     print("verifiction successful ")
#     print( "1 check your balance")
#     print("2 check your withdraw amount")
#     print("3 check your diposit amount")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         print(" your balance is",b)
#     elif choice==2:
#         amount=int(input("enter your amount"))
#         if b<amount:
#             print("balance insufficient")
#         elif b>amount:
#             print("balance susscessful withdrow")
#     elif choice==3:
#         deposite=int(input("enter your deposite amount"))
#         b+=deposite
#         print("your amount is suceessful deposite ,new balance is",b)
       
#     else:
#         print("invalid choice")

# else:
#     print("invalid password")
        

# amount=float(input("enter the amount"))
# if amount<=1000:
#     discount=(amount*0.5)
# elif amount<=5000:
#     discount=(amount*0.10)
# elif amount<=10000:
#     discount= amount*0.15
# elif amount<=30000:
#     discount=amount*0.20
# elif amount>50000:
#    discount=amount*0.30
# else:
#     print("invalid")
# final_amount=amount - discount

# print( "original amount", amount)
# print(" discount applied",discount)
# print(" amount to pay after discount", final_amount)
     


# num=int(input("enter the number"))
# temp=num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit*digit*digit
#     temp=temp//10
# if num==sum:
#     print("armstrong number ")
# else:
#     print("not a armstrong number")


# income=int(input("enter your income"))
# tax=0
# if income<=250000:
#     tax=0
# elif income<=500000:
#     tax=(250000*5/100)
# elif income<=1000000:
#     tax=(250000*5/100)+(income-500000)*20/100
# else:
#     tax=(250000*5/100)+(500000*20/100)+(income-1000000)*30/100
# print("total tax", tax)

# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()

# n=5
# i=1 
# while i<=n:
#     print(' '*(n-i) +'*' * i)
#     i=i+1

n=5
i=1
while i<=n:
    print(' '*i + '*' * (n-i))
    i=i+1