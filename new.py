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
# print(ans)

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






# for i in range(len(s)):
#     count=1
#     for j in range(i+1,len(s)):
#         if s[i]==s[j]:
#             count+=1
#     print(s[i]," = ",count)

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

s1=" man",
s2="madam",
if len(s1) != len(s2):
    print(" not,anagram")
else:
     ans={}
     for i in s1:
      
        
          ans[i]=ans.get(i,0)+1
    

     for j in ans:
       if j in ans:
           ans[i]-=1
     freq= True
     for i in ans.value():
         if i!=0:
             freq=False
      
       
    

    
    
        

    
