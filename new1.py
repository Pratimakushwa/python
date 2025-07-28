from functools import reduce
l=[1,2,3,4,45,6,7,89]
def max_digit(x,y):
    if x>y:
        return x
    else:
        return y
result=reduce(max_digit,l,0)
print(result)

from first1 import decor
@decor
def add(x,y):
    z=x+y
    return z
result=add(5,5)
print (result)