# num= input("enter the number")
# print(num[: : -1])


# a,b= 10,20
# a,b = b,a
# print (a)
# print(b)

# li =[1,2,3,4,5]
# for i in li:
#     print(i)

# for i in range(1, 11):
    # print(i)

# for i in range(len(li)):
    # print(i)
    # print(i,"=",li[i])

# li=[1,2,3,4,56]
# mx=0
# for i in range(len( li)):
#     if mx <li[i]:
#         mx=li[i]
# print(mx)

li=[1,2,3,4,56]
min=56
for i in range(len( li)):
    if min >li[i]:
        min=li[i]
print(min)
