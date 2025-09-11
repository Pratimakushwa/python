# def test():
#     print("Hello")
# result = test()
# print(result)




# x = 5
# def change():
#     x = 10
# change()
# print(x)


# def fun():
#     print("hello world")
# fun()

# def fun():
#     a=10
#     b=30
#     print("sum of two number",a+b)
# fun()

# def fun():
#     a=30
#     b=20
#     c=10
#     if a>b and a>c:
#         print("a is greatest")
#     elif b>a and b>c:
#         print("b is greastest")
#     else:
#         print("c is gratest")
# fun()

# def fun():
#     s="python"
#     count=0
#     vowel="aeiouAEIOU"
#     for i in s:
#         if i in vowel:
#             count=count+1
#     print(count)
# fun()


# def fun():
#     n=int(input("enter the number"))
   
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# fun()


# def fun():
#     n=int(input("enter the number"))
#     for i in range(1,n+1):
#         print(i*i*i)
   
    
# fun()

# def fun():
#     n=5
#     square=n**2
#     cube=n**3
#     print(n)
#     print(square)
#     print(cube)
# fun()

# def fun(name="guest"):
#     print(name)
# # fun()
# fun("pratima")

# def fun(name,age):
#     return f" name is a ${name}, age is a${age}"
# result=fun( name="pratima",age=22)
# print(result)



# def fun(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum

# result=fun([1,2,3,4,454])
# print(result)


# def fun(*arg):
   
#     return  max(*arg)


# result=fun(2,3,4,5,6,7,89,77)
# print(result)
    

# def fun(*arg):
#     max=arg[0]
#     for i in arg:
#         if i>max:
#             max=i
#     return max
# result=fun(2,3,4,5,6,7,8,8)
# print(result)


# def fun(*arg):
#     count=0
#     for i in arg:
        
#         count=count+1
#     return count
# result=fun(2,3,4,5,6,7,98,9)
# print(result)


# def fun(*arg):
#     for ars in arg:
#         print(ars, end=" ")
# fun(2,3,4,5,6,7,8,9)



# def fun(*arg):
#     result=[]
#     for i in arg:
#         if i not in result:
#             result.append(i)
#     return result
# data=fun(2,3,4,5,67,8)
# print(data)


# def fun(*args):
#     return " " .join(args)
    



# data=fun("helo","world")
# print(data)


# def targetsum(num,target):
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             if num[i]+num[j]==target:
#                 return True
#         return False
# print(targetsum([1,2,3,4,5,6],7))


# def fun(num):
#     temp=num
#     rev=0
#     while num >0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     return rev==temp
# print(fun(121))


# def is_armstrong(num):
#     # -------- Step 1: Count digits --------
#     temp = num
#     count = 0
#     while temp > 0:
#         count += 1
#         temp = temp // 10

#     # -------- Step 2: Find sum of powers --------
#     temp = num
#     total = 0
#     while temp > 0:
#         digit = temp % 10   # last digit

#         # digit ^ count निकालना manually (बिना pow())
#         power = 1
#         i = 0
#         while i < count:
#             power *= digit
#             i += 1

#         total += power
#         temp = temp // 10   # अगला digit

#     # -------- Step 3: Check condition --------
#     if total == num:
#         return True
#     else:
#         return False




# def unique(*arg):
#     result= [ ]
#     for i in arg:
#         if i not in result:
#             result.append(i)
#     return result

# print(unique(2,3,4,5,6,6,4,3,2))
        


# def sum(*arg):
#     sum=0
#     for i in arg:
#         sum=sum+i
#     return sum
    
# print(sum(2,3,4,5,85,12,5,))

# def anagram(str1,str2):
#     if len(str1)!= len(str2):
#         return False
#     for ch in str1:
#         if str1.count(ch)!= str2.count(ch):
#             return False
#     return True

# print(anagram("listen","slient"))
# print(anagram("hello","world"))


# num=int(input("enter the number"))
# for i in range(1,num+1):
#     print(i)



# n1=int(input("enter the number"))
# n2=int(input("enter the number"))
# for i in range(n1,n2+1):
#     if i%2==0:
#         print(i,end=" ")

# num =int(input('enterr the number'))
# for i in range(1,11):
#     print(num*i)

# def count_char(s,target):
#     count=0
#     for ch in s:
#         if ch== target:
#             count +=1
#     return count
# print(count_char("hello","l"))








   

 
