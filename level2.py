# s="program"
# print(s[0:10:3])


# s="program"
# print(s[-5:])

# s="hello world"
# print(s.upper())

# s="hello world"
# data=" "
# for char in s:
#     if 'a'>=char>='z':
#         data+=chr(ord(char)-32)
#     else:
#         data+=char
# print(data)

# s="HELLO"
# data=" "
# for char in s:
#     if 'a'>=char>="z":
#         data+=chr(ord(char)-1)
#     else:
#         data+=char
# print(data)

# s="  python  "
# start=0
# while start <len(s) and s[start] == " ":
#     start+=1
# end= len(s)-1
# while end >=0 and s[end]== " ":
#     end -=1

# result=s[start:end+1]
# print(result)

# s="apple,banana, mango"
# result= s.split(",")
# print(result)


# s= " apple,banana,mango"
# result=[]
# # temp=""
# for i in s:
#     if i ==",":
#         result.append(i)
#         # temp=""
#     else:
#         result+=i
# result.append(i)
# print(result)

# s= " apple,banana,mango"
# result=[]
# temp=""
# for i in s:
#     if i ==",":
#         result.append(temp)
#         temp=""
#     else:
#         temp+=i
# result.append(temp)
# print(result)


# s="i love python"
# result=s.replace("python","java")
# print(result)

# s="python"
# print(s.index("o"))


# s="hello world"
# countword="l"
# count=0
# for i in range(len(s)):
#     if s[i]==countword:
#         count=count+1
# print(count)

# lst=["a","b","c"]
# result=""
# for i in range(len(lst)):
#     result+=lst[i]


#     if i<len(lst)-1:
#         result+="-"
# print(result)


# s="Data"
# result=s.replaceall("a","A")
# print(result)

# s="banana,chrry mango"
# result=s.split(";")
# print(result)

w="welcome"
print(w[1:-4:1])

w="welcome"
print(w[1:4:1])

w="welcome"
print(w[1:-4:-1])
w="welcome"
print(w[-1:-4:1])
