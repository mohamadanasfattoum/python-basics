
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
