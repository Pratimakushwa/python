question = []
question.append("Q1:python was develop in")
question.append("Q2:c++ was develop in")
question.append("Q3:html was develop in")
question.append("Q4:when one is not valid keyword on python")
question.append("Q5:full form of css")
question.append("Q5:full form of css")
question.pop()
option=[
        ( "A:1995","B:1991","C:1999","D:2000"),
        ( "A:1993","B:1991","C:1979","D:2090"),
        ( "A:1991","B:1980","C:1999","D:2010"),
        ( "A:true","B:True","C:False","D:None"),
        ( "A:cascarding stylesheet","B:cascarding sheet","C:cascarding card","D:cascading style sheet")

 ]
answers= ["B","C","A","A","D"]
ans =[]
points=0
print(question[0])
print(option[0])
ans.append(input("Select the corrrect option:").upper())
points=points+1 if ans[0] == answers[0] else points

print(question[1])
print(option[1])
ans.append(input("Select the corrrect option:").upper())
points=points+1 if ans[1] == answers[1] else points

print(question[2])
print(option[2])
ans.append(input("Select the corrrect option:").upper())
points=points+1 if ans[2] == answers[2] else points
print(question[3])
print(option[3])
ans.append(input("Select the corrrect option:").upper())
points=points+1 if ans[3] == answers[3] else points
    

print(question[4])
print(option[4])
ans.append(input("Select the corrrect option:").upper())
points=points+1 if ans[4] == answers[4] else points

print()
print(f" Total points are :{points}")
print(f" your selected points are :{ans}")
print(f" The correct answer are:{answers}")
print(f" Total points are :{points}")