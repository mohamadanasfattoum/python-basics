
'''
class A:
    def do(self):
        print('in A')

class B(A):
    pass
class C:
    def do(self):
        print('in C')

class D(B,C):
    pass




n = D()
n.do()


'''

'''
class A:
    def do(self):
        print('in A')

class B(A):
    pass
class C:
    def do(self):
        print('in C')

class D(C,B):
    pass




n = D()
n.do()

print(D.mro())
'''

'''
    - create student
    - add mark
    - get avg
'''


'''
class student:

    
    #def create_student(self,name):
        print(f'Welcome {name}')


#s1 = student()
#s1.create_student('anas')
      
    def __init__(self,name):
        print(f'Welcome {name}')
        self.marks=[]

    def add_mark(self,mark):
        self.marks.append(mark)
        print(self.marks)


    def get_avg(self):
        avg = sum(self.marks)/len(self.marks)
        print(avg)



s1 = student('anas')

s1.add_mark(20)
s1.add_mark(50)
s1.add_mark(40)
s1.add_mark(90)
s1.add_mark(30)
s1.get_avg()








s2 = student('ahmad')

s2.add_mark(30)
s2.add_mark(20)
s2.add_mark(80)
s2.add_mark(70)
s2.add_mark(10)
s2.get_avg()
'''

'''
bank
    - create account : name , age , gender
    - depostie
    - withdraw
    - view balance
    - show all details
    
'''
'''
class Bank:
    def __init__(self,name,age,gender):
        print(f'welcome {name}')
        self.balance = 0
        self.name = name
        self.age = age
        self.gender = gender
        
    def deposite(self,amount):
        self.balance += amount
        print(f'you current balance : {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('no enough balance')
            return
        self.balance -= amount
        print(f'you current balance : {self.balance}')

    def view_balance(self):
        print(f'you current balance : {self.balance}')

    def client_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        print(f"Balance:{self.balance}")


c1 = Bank('ahmad',30,'male')
c1.deposite(500)
c1.deposite(600)
c1.withdraw(120)
c1.withdraw(500)
c1.withdraw(500)
c1.view_balance()
c1.client_details()

'''

class User:
    def __init__(self,name,age,gender):
        print(f'welcome {name}')
        self.name = name
        self.age = age
        self.gender = gender

    def client_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")
        
            


class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
        print(f"Balance:{self.balance}")

    def deposite(self,amount):
        self.balance += amount
        print(f'you current balance : {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('no enough balance')
            return
        self.balance -= amount
        print(f'you current balance : {self.balance}')

    def view_balance(self):
        print(f'you current balance : {self.balance}')




c1 = Bank('ahmad',30,'male')
c1.deposite(500)
c1.deposite(600)
c1.withdraw(120)
c1.withdraw(500)
c1.withdraw(500)
c1.view_balance()
c1.client_details()
