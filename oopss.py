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


# class Student:
#     school='SHSS'
#     def __init__(self ,name,city):
#         self.name=name
#         self.city=city
#     @classmethod
#     def update(cls,new):
#         print(id(cls))
#         cls.school=new
#     def show(self):
#         print(self.name,self.city,Student.school)
# print(id(Student))
# obj=Student('pratima','bhopal')
# obj.update('new-shss')
# obj.show()
# obj1=Student('pratima','bhopal')
# obj1.show()






#     def add():
#         print(self.name)
#         print(self.city)
# obj=Student("pratima","bhopal")
# obj.add()
        


# class parent:
#     def home(self):
#         print("parent home")
# class child(parent):
#     pass

# obj=child()
# obj.home()


# class parent:
#     def home(self):
#         print("parent home")
# class child(parent):
#     def home(self):
#         print("child home")
#         super().home()
# obj=child()
# obj.home()


# single inheritance
# class parent:
#     def show(self):
#         print("parent class")
# class child(parent):
#     def child(self):
#         print("child class")

# obj=child()
# obj.child()
# obj.show()

# multiple inheritance

# class father:
#     def skill1(self):
#         print("driving")
# class mother:
#     def skill2(self):
#         print("cooking")
# class child(father,mother):
#     def skill3(self):
#         print("coding")
    
    
# obj=child()
# obj.skill1()
# obj.skill2()
# obj.skill3()

# multilevel inheritance

# class grandparent:
#     def property(self):
#         print("grandparent property")
# class parent(grandparent):
#     def car(self):
#         print("parent car")
# class child(parent):
#     def bike(self):
#         print("child bike")
# obj=child()
# obj.property()
# obj.car()
# obj.bike()


# class grandparent:
#     def bank(self):
#         print("HDEC")
#     def home(self):
    
#         print("from home")
# class parent (grandparent):
#     pass
# class child (parent):
#     pass

# obj=child()
# print()



# class A:
#     def home(self):
#         print("home from A")
# class B:
#     def bank(self):
#         print("bank from B")
#     def home(self):
#         print("home from B")
# class C(B,A):
#     pass
# obj=C()
# obj.bank()
# obj.home()


# class A:
#     def home(self):
#         print("home")
# class B(A):
#     def home(self):
#         print("home")
    
   
# class C(A):
#     pass
# obj1=C()
# obj1.home()
# obj2=B()

# obj2.home()

# class A:
#     def home(self):
#         print("home")
# class B:
#     def home(self):
#         print("home")
    
   
# class C(A,B):
#     pass
# class D(C):
#     pass
    
# class E(C):
#     def bank(self):
#         print("bank")

# obj1=E()
# obj1.home()
# obj1.bank()



# polymorphism

# class A:
#     def add (self ,x,y):
#         print(x+y)
#     def add (self ,x,y,z):
#         print(x+y+z)
# obj=A()
# obj.add(10,20,30)

# class A:
#     def add (self ,*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         print(sum)
        
# obj=A()
# obj.add(10,19)


# abatraction

# from abc import ABC , abstractmethod
# class Senior(ABC):
#     def add (self,x ,y):
#         print(x+y)

#     def sub (self,x ,y):
#         print(x-y)
#     @abstractmethod
#     def div(self):
#         pass
# class junior(Senior):
#     def div(self):
#         print("from junior class")
# obj=junior()
# obj.div()


# encapsulation

# public method
# class A :
#     principal= 'python'
#     def show (self):
#         print(A.principal)
# class B(A):
    
#     def new (self):
#         print(A.principal)
# obj=B()
# obj.new()
# obj.show()
# print(A.principal)




# protected not supoted in python
# class A :
#     _principal= 'python'
#     def _show (self):
#         print(A._principal)
# class B(A):
    
#     def new (self):
#         print(A._principal)
# obj=B()
# obj.new()
# obj._show()
# print(A._principal)

# private
class A :
    __principal= 'python'
    def _show (self):
        print(A.__principal)
class B(A):
    
    def new (self):
        print(A.__A__principal)
obj=B()
# obj.new()
# obj.__show()
# print(A.__principal)
print (dir(A))
print(A._A__principal)
