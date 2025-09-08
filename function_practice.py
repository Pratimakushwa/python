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



def fun(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

result=fun([1,2,3,4,454])
print(result)