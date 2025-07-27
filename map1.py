l=[1,2,3,4,5,6]
def even(x):
    if x%2==0:
        return x
result=filter(even,l)
print(list(result))
    

