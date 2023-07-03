
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

class student:
    def create_student(self,name):
        print(f'Welcome {name}')


s1 = student()
s1.create_student('anas')
        
