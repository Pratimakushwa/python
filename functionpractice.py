# def string_length(s):
#     count=0
#     for _ in s:
#      count=count+1
#     return count
# print(string_length("hello"))  


# def sting(s,target):
#    return target.count ("a")
# print(sting("hello","banana"))


# def char_count(s,ch):
#     count=0
#     for i in s:
#      if i == ch:
#         count=count+1
#     return count
    
# print(char_count("banana","n2"))



# def reverse_string(s):
#     reversed_s = ""
#     for ch in s:
#         reversed_s = ch + reversed_s  # prepend character
#     return reversed_s

# print(reverse_string("hello"))





def reverse(n):
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
print(reverse(123))


