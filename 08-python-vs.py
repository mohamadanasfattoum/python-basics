
'''
try:
    age = int(input('enter age: '))
    print(100/age)

except Exception:
    print('please enter number and >0a')


else: 
    print('######')                # no exception

finally:
    print('--------------')         # always1
'''

'''
    map
    filter
    reduce
'''
'''
def mul(n):
    return n*2
numbers = list(range(1,11))
result = map(mul,numbers)
print(list(result))
'''
'''
try:
    def excep_defi(b):
        return a//b
    a= int(input('Enter thr first numbers: '))
    b= int(input('Enter thr secund numbers: '))
    numbers =list(range(0,10))
    result= map(excep_defi,numbers)
    print(list(result))
    
except Exception as e:
    print("Error Code:",e)

'''
'''
names = ['ahmad','ali','hasan','mohamad']

def mylen(n):
    return len(n)

result= map(mylen,names)
print(list(result))
'''
'''
#lambda
names = ['ahmad','ali','hasan','mohamad']

def mylen(n):
    return len(n)

result= map(mylen,names)
print(list(result))

result2= map(lambda n : len(n),names)
print(list(result2))
'''

'''
names = ['ahmad','ali','hasan','mohamad']
result= map(lambda n :len(n) , names)
print(list(result))

names = ['ahmad','ali','hasan','mohamad']
result= filter (lambda n :len(n) , names)
print(list(result))





def myfilter(n):
    if n>5:
        return n
numbers = list(range(1,11))
result = filter(myfilter,numbers)
print(list(result))


def myfilter(n):
    if n>5:
        return n
numbers = list(range(1,11))
result = map(myfilter,numbers)
print(list(result))

def myfilter(n):
    if n>2:
        return n
numbers = [1,2,3,4,5]
result = map(myfilter,numbers)
print(tuple(result))        # map and filter should be printed as list or tuple
'''
'''
d = {'ahmad':18,'ali':56,'hasan':40,'mohamad':25}
def mynames(x):
    return x*2
r = map(mynames,d)
print(list(r))

r2 = map(mynames,d.values())
print(list(r2))
'''

my_list =[12,65,88,39,112,221,102,100,700]

result = list(filter(lambda x: (x % 13==0),my_list))
print(result)