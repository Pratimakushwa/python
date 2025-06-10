num= int (input("enter the number"))
# sum=0
for i in range( num):
    # sum= sum+i
    print(i)
year= int (input("enter the year"))
if num%4==0 and num%400==0:
    print("leap year")
else:
    print("not a leap year")
