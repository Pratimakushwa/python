# class Student:
#     name="pratima"

# s1=Student()
# print(s1.name)
# s2=Student()
# print(s2.name)

# class Student:
#     def __init__(self,name,marks,roll):
#         self.name=name
#         self.marks=marks
#         self.roll=roll

# s1=Student('pratima',45,234)
 
# class Student:
#     def __init__(self,name,marks):
#       self.name=name
#       self.marks=marks

#     def get_avg(self):
#         sum=0
#         for value in self.marks:
#           sum=sum+value
#         print( "hi", self.name ,"you average score is:",sum/3)
# s1=Student('karan',[22,33,44])
# s1.get_avg()
       
# class amount:
#     def __init__(self,balance,account):
#         self.balance=balance
#         self.account=account
#     def debit(self,amount):
#         self. balance -=amount
#         print('rs',amount,"was debit")
#         print('total balance = ', self.get_balance())
#     def credit(self,amount):
#         self.balance +=amount
#         print('rs',amount,"was creadit")
#         print('total balance = ', self.get_balance())

#     def get_balance(self):
#         return self.balance


    
        

# s1=amount(1000,1234)
# s1.debit(200)
# s1.credit(46)
# s1.get_balance()


class Student:
    school='SHSS'
    def __init__(self ,name,city):
        self.name=name
        self.city=city
    @classmethod
    def update(cls,new):
        print(id(cls))
        cls.school=new
    def show(self):
        print(self.name,self.city,Student.school)
print(id(Student))
obj=Student('pratima','bhopal')
obj.update('new-shss')
obj.show()
obj1=Student('pratima','bhopal')
obj1.show()






#     def add():
#         print(self.name)
#         print(self.city)
# obj=Student("pratima","bhopal")
# obj.add()
        