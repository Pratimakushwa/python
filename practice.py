#lambda funcntion (anonymus function)
# lambda argument: expression
# 1- Use for small solutions/functionality we use lambda function 
# 2- To perform small task lambda function is more readable and faster then normal function
# 3- Mostly use with high order functions like map() filter() and reduce()

prime = lambda x: x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
print(prime(5))
 

greater = lambda x,y: x if x>y else y
print(greater(15,8))

# cube = lambda x: x*x*x
# print(cube(6))

# square = lambda x: x*x

# print(square(5))

# def square(x):
#     return x*x

# print(square(5))

lambda funcntion (anonymus function)
lambda argument: expression
1- Use for small solutions/functionality we use lambda function 
2- To perform small task lambda function is more readable and faster then normal function
3- Mostly use with high order functions like map() filter() and reduce()

prime = lambda x: x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
print(prime(5))
 

greater = lambda x,y: x if x>y else y
print(greater(15,8))

cube = lambda x: x*x*x
print(cube(6))

square = lambda x: x*x

print(square(5))

def square(x):
    return x*x



# num= int (input("enter the number"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# num= int(input("enter the number"))
# if num>0:
#     print("positive")
# else:
#     print("negative")
num= int (input("enter the number"))
if num%2==0:
    print("even number")
else:
    print("odd number")

num= int(input("enter the number"))
if num>0:
    print("positive")
else:
    print("negative")
