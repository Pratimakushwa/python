# li=[ 1,2,3,4,5,6]
# k = int (input("enter the number"))
# for i in range(k):
#     for j in range(i+1, len(li)):
#         if li [i]< li[j]:
#             li[j],li[i]=li[i],li[j]
# print(li, k-1)

# li=[1,2,3,0,6,4,0,0]
# j=0
# for i in range(len (li)):
#     if li [i]!=0:
#         li[i],li[j]= li[j],li[i]
#         j=j+1
# print(li)
    
# li= [ 1,2,3,4,6]
# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         if li[i]+li[j]==10:
#           print ( li[i]+li[j])
    

# li=[1,4,3,5,2,6,8]
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#      if li[i]>li[j]:
#         li[i],li[j]= li[j],li[i]
# print(li[-2])

# li= [1,4,6,7,8,1,2,5,6]
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i] < li[j]:
#             li[i], li[j]=li[j],li[i]
# print(li)

# li=[1,2,3,4,5,6,6]
# count=0
# for i in li:
#     count=count+1
# print(count)

# li=[1,2,23,4,5,6,1,1,1]
# count=0
# for i in li:
#     if i== li[0]:
#         count=count+1
# print(count)

# li=[1,2,3,4,5,6]
# ans=li[0]
# for i in li:
#     if ans>i:
#         ans=i

# print(ans)



# li=[1,4,3,5,7,8]
# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         if li[i]>li[j]:
#             li[i],li[j]=li[j],li[i]
# print(li)
    
# li=[1,2,3,4,5,6,7]
# for i in  range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]+li[j]==10:
#             print( li[i]+li[j])

            
# li=[1,2,3,4,12,2,1,1,1]
# count=0
# for i in li:
#     if i==li[1]:
#         count=count+1
# print(count)


# li=[1,2,3,4,5,12,3,4,2]
# unique=[]
# for i in range(len(li)):
#     if li[i] not in unique:
#         unique.append(li[i])
# for i in range(len(unique)):
#     for j in range(i+1,len(unique)):
#         if unique[i] > unique[j]:
#             unique[i],unique[j]=unique[j],unique[i]
# print(unique)

# li=[1,2,3,4,5,6,3,2,4]
# ans=10
# count=0
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i]+li[j]==ans:
#              print(li[i],"+",li[j],"=",ans)
#              count=count+1
# print("total pair:", count)
           
# n=int(input("enter the number"))
# if n<=1:
#     print("not prime")
# for num in range(2,n+1):
#     for i in range(2,num):
#         if num%i==0:
            
#             break
#     else:
#           print(num)


n=int(input("enter the number"))
a=0
b=1
print("febonacci series")
for i in range(1,n+1):
    print(a)
    c=a+b
    a=b
    b=c

# n= int(input("enter the number"))
# temp=n
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit*digit*digit
#     n=n//10
# if sum==temp:
#     print("armstrong")
# else:
#     print("not armstrong")
# li=[1,2,3,4,5,67,44]
# # count=0
# for i in li:
#     if i%2==0:
#         # count=count+1
#       print(i)

# li=[1,2,3,4,5]
# sum=0
# for i in li:
#    sum=sum+i
# print(sum)
   
# li=[1,2,8,4,5,56,6]

# for i in range(len(li)):
#     for j in range(i+1, len(li)):
#         if li[i]>li[j]:
           
#             li[i],li[j]=li[j],li[i]
# print(li)

# li=[ 2,2,1,2,2]
# for i in range(len (li)):
#     count=0
#     for j in range(i+1,len(li)):
#        if li[i]==li[j]:
#          count=count+1
    

# li=[2,3,1,2,2,1,3,1]

# for i in range(len(li)-1):
#     if(li[i]!=-1):
#         freq=1
#         for j in range(i+1,len(li)):
#             if li[i]==li[j]:
#                 freq=freq+1
#                 li[j]=-1
#         print("The frequency of: ",li[i]," is ",freq)
        
# print(li)


# num=int(input("entr the number"))
# for i in range(1,num+1):
#     print(i)

# num=20
# for i in range(1,num+1):
#     if i%2==0:
#       print(i)


# i = 2
# while i<=20:
   
#       print(i)
#       i=i+2

# num=100
# sum=0
# for i in range(1,num+1):
    
#         sum=sum+i
# print(sum)

# num= int(input("enter the number"))
# for i in range(1,11):
#     print(num*i)

# i=10
# while i>=1:
#     print(i)
#     i=i-1
# s= input("enter the string")
# for i in s:
#     print(i)
# li=[10,20,30,40]
# for i in li:
#     print(i)

# li=[2,3,5,7,6,7,9,7,9,5,4,3]
# even_count=0
# odd_count=0
# for i in range(len(li)):
#     if li[i]%2==0:
#         even_count= even_count+1
#     else:
#         odd_count=odd_count+1
# print( "even",even_count)
# print("odd",odd_count)

# s="education is powerfull"
# vowel="aeiouAEIOU"
# count=0
# for i in range(len(s)):
#     if s[i] in vowel:
#         count =count+1
# print("vowel",count,)
        
# li=[1,2,3,4,5,6,7,2,2,1,3,1,4,5]
# data=[]
# for i in range(len(li)):
#     count=0
#     if li[i] not in data:
#         for j in range(len(li)):
#             if li[i]==li[j]:
#                 count=count+1
#                 if count > 1:
#                  print (li[i], " -> ", count,"times") 
#                  data.append(li[i])
                
                
           
        
# li=[2,4,3,6,8]
# data=[]
# for i in range(len(li)):
#     if i  not  in data:
#         data.append(li[i]*li[i])
# print(data)

# a= int (input("enter the number"))
# b= int(input("enterthe numebr"))
# maxNum= max(a,b)
# while(True):
#     if maxNum%a==0 and maxNum%b==0:
#         break
#     maxNum=maxNum+1
# print(maxNum)


    






























