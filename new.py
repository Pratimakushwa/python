# s="helloworldpython"
# ans={}

# for i in s:
#     if i in ans:
#         ans[i]=ans.get(i)+1
#     else:
#         ans[i]=1

# print(ans)
# s="hello"
# data={}
# for i in s:
#     if i in data:
#         data[i]=data.get(i)+1
#     else:
#         data[i]=1
# print(data)


# li=[ "raj", "ram", "jatin"]
# data={ }
# for i in li:
#     if i in data:
#         data[i]=data.get(i)+1
#     else:
#         data[i]=1
# print(data)

# data={
#     "jatin": 55,
#     "ram": 90,
#     "rahul": 80
# } 

# mx=0
# for i in data:
#     if data[i]>mx:
#         mx=data[i]
#         ans=i
# print(mx)

# print(max(data))

 

# data={
#     "jatin":50,
#     "raj": 60,
#     "ram": 80
# }

# lowest=80
# for i in data:
#     if data[i]<lowest:
#         lowest=data[i]
#         ans=i
# print(ans)

# li=[ "ram", "raj", "jatin"]
# data={}
# for i in li:
#     if i in data:
#         data[i]=data.get(i)+1
#     else:
#         data[i]= 1
# print(data)


# data={
#     "jatin":90,
#     "ram": 50,
#     "raj": 70,
# }
# max=0
# for i in data:
#     if data[i]>max:
#         max=data[i]
#         ans=i
# print(ans)


# data={
#     "jatin":90,
#     "ram":40,
#     "rama": 90,
#     "raj": 80,
#     "raja": 80,
# }
# names= list(data.keys())
# for i in range(len(names)):
#     for j in range(i+1,len(names)):
#         if data[names[i]]==data[names[j]]:
#          print(names[i], "and", names[j] , " marks are equal:",data[names[i]])





# text="eduaction is important"
# vowel={}
# for i in text:
#     if i in "aeiou":
#         if i in vowel:
#             vowel[i]=vowel.get(i)+1
#         else:
#             vowel[i]=1
# print(vowel)


# text=" Hello Worlddd This Is Python"
# upper=0
# lower=0
# for i in text:
#     if i>'A'and i<'Z':
#         upper=upper+1
#     elif i>'a' and i<'z':
#         lower=lower+1

# print(upper)
# print(lower)





#dictionary:- key and value ka pair
# key always unique value can be duplicate
# mutable
# data = {
#     "name":"jatin",
#     "rollno":101,
#     100:200,
# }

# print(data.get("no","value is not present"))

# data[1000]=100

# for i,j in data.items():
#     print(i,j)


s=[1,2,3,4,5,6,7,4,2]

for i in range(len(s)):
    count=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            count+=1
    print(s[i]," = ",count)

# print(s[0])
# print(len(s))
# for i in s:
#     print(i)

# text="hello12334world23435"
# digit={}
# for i in text:
#     if i>='0'and i<='9':
#         if i in digit:
#             digit[i]=digit.get[i]+1
       
#     else:
#        digit[i]=1
# print( digit)

# s1=" man",
# s2="madam",
# if len(s1) != len(s2):
#     print(" not,anagram")
# else:
#      ans={}
#      for i in s1:
      
        
    #       ans[i]=ans.get(i,0)+1
    

    #  for j in ans:
    #    if j in ans:
    #        ans[i]-=1
    #  freq= True
    #  for i in ans.value():
    #      if i!=0:
    #          freq=False
      
       
    
# num= int(input("enter the number"))
# temp = num
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit
#     temp=temp//10

# if num%sum==0:
#     print("harshat number")
# else:
#     print("print not a hrshat number")


# num=int(input("enter the number"))
# temp=num
# sum=0
# product=1
# while temp>0:
#     digit=temp%10
#     sum=sum+digit
#     product=product*digit
#     temp = temp//10
# if sum==product:
#     print("spy number")

# else:
#     print("not a spy number")
    

# n=int(input("enter three numner"))
# temp=n
# sum=0
# product=1
# while temp>0:
#     digit=n=temp%10
#     sum=sum+digit
#     product=product*digit
#     temp=temp//10
# if sum==product:
#     print("spy number")
# else:
#     print("not spy number")


# n=int(input("enter the number"))
# temp=n
# sum=0
# while temp>0:
#     digit=temp%10
#     sum=sum+digit
#     temp=temp//10

# if n%sum==0:
#     print("hrshad number")
# else:
#     print("not hrshad")






# s1="listen"
# s2="silent"
# if (len(s1)!=len(s2)):
#     print("not an anagram")
# else:
#     freq={}
#     for i in s1:
#         freq[i]=freq.get(i,0)+1
#     for j in s2:
#         freq[j]-=1
#     ans=True
#     for i in freq.values():
#         if i!=0:
#             ans=False
#     if (ans):
#         print("anagram")
#     else:
#         print("not an anagram")


# li=[1,2,3,4,5,67,8,2,3,4]
# visit=[]
# for i in range(len(li)):
#     if li[i] not in visit:
#         count=1
#         for j in range(i+1,len(li)):
#             if li[i]==li[j]:
#                 count=count+1
#         print( li[i],"=",count)
#         visit.append(li[i])


li=[1,2,6,2,8,3,4,5,6]
k=1
for i in range(k):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i] 
print(li,k-1)



