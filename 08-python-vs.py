
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

names = ['ahmad','ali','hasan','mohamad']

def mylen(n):
    return len(n)

result= map(mylen,names)
print(list(result))