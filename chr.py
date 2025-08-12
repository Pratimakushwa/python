# s="python"
# s1=''
# for i in s:
#     i=chr(ord(i)+1)
#     s1=s1+i
# print(s1)
# s="python"
# s=''
# for i in s:
#     i=chr(ord(i)+1)
#     s1=s1+i
# print(s1)
# s="python"
# s=''
# for i in s:
#     i=chr(ord(i)+1)
#     s1=s1+i
# print(s1)

# s="python"
# for i in s:
#     i=chr(ord(i)+1)
# print(i)


# def is_prime(n):
#     is_prime=True
#     for i in range(2,n+1):
#         if n%i==0:
#          is_prime=False
#          break

#     if is_prime:
#        print("prime number")
#     else:
#        print("not a prime number")
# n= int (input("enter the number"))
# is_prime(n)


# n=int(input("enter the number"))
# sum=1
# for i in range(n,n+1):
#     sum=sum+i*i
# print(sum)

# n=int(input("enter the number"))
# for i in range(1,11):
#  print(n*i)

# n= int (input ("enter the number"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# n=int(input("entre the number"))
# count = 0
# while n>0:
#     n=n//10
#     count=count+1
# print(count)

# n=int(input("enter the number"))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)



# a=int(input("enter the number"))
# b=int(input("enter the  number"))
# result=1

# for i in range(b):
#     result=result*a
# print(result)
    
n=int(input("enter the number"))
count=0
while n>0:
        n=n//10
        count=count+1
print(count)
