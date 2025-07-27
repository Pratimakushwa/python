
# def decor(func):
#     def inner(x,y):
#         x=x+20
#         y=y+20
#         z=func(x,y)
#         return z
#     return inner

# def outer ():
#     def inner():
#         print("from inner function")
#     return inner
# data=outer()
# print(data)
# x= data()



# def outer(x):
#     def inner():
#         y=x()
#         return y
#     return inner
# def x():
#     return "from function"
# data=outer(x)
# z=data()
# print(z)


# def outer (func):
#     def inner(x,y):
#         x=x+5
#         y=y*5
#         z=func(x,y)
#         return z
#     return inner
# def add( x,y):
#     z=x+y
#     return z
# data= outer(add)
# z=data(5,10)
# print(z)



# def outer ():
#     def inner():
#         print("from inner function")
#     return inner
# data=outer()
# print(data)
# x= data()


def decor(printer):
    def inner():
        printer()
        print("welcome")
    return inner
def printer():
    print("welcome")
    print("welcome")
printer=decor(printer)
printer()

       


