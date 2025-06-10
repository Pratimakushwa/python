# num= int (input("enter the number"))
# if num>0:
#     print ("positive")
# else:
#     print("negative")
# num=int (input("enter the number"))
# for i in  range(1, num):
#     print(i)

# num= int (input("enter the number"))
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)
num = int (input("enter the number"))
for i in range(1,num):
    if num%i==0:
        print("square")
    else:
        print("not divisiable")  



        num = int (input("enter the number"))
for i in range(1,num):
    if num%i==0:
        print("square")
    else:
        print("not divisiable")  

rows=5 
for i in range(1, rows+1):
    for j in range( 1, rows+1):
        if(i>=6-j):
           print(j, end="")
        else:
         print(end=" ")
    print()
       