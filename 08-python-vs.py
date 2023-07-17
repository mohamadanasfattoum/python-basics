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