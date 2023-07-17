
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


def excep_defi(a,b):
    a= int(input('enter n: '))
    b= int(input('enter n: '))    
    return a//b

numbers =list(range(a,b))
result= map(excep_defi,numbers)
print(list(result))
    