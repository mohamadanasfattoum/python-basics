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
