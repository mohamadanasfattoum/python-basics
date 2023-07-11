numbers= [1,2,3,4,5,6]
'''
x,y,*z = numbers

print(*z,x,y)
print(x,*z,y)
print (----------)
'''
'''
x,y,*_ = numbers
print(*_,x,y)
print(x,*_,y)
print (----------)
'''
'''
for _ in range (10):
    print('Hallo Python')
'''

#for x in range (10):
    #print(f'{x}: Hallo Python')

#for x in (['anas','ali','ahmad','omar']):
    #print(f'{x}: Hallo Python')

#for x ,y in enumerate(['anas','ali','ahmad','omar']):
    #print(f'{x} {y}: Hallo Python')
'''    
for x ,y in enumerate(['anas','ali','ahmad','omar']):
    if x==2:
        print('-----')
    print(f'{x}: Hallo Python')
'''
'''
try:
    n = int(input('Enter Number : '))
    print(10/n)


except (ValueError, ZeroDivisionError):
    print ('please enter number > 0')

'''
'''
except Exception:
    print ('please enter number ')

except ValueError:
    print ('please enter number ')


except ZeroDivisionError:
    print ('please enter number > 0')
'''
'''
try:
    n = int(input('Enter Number : '))
    print(10/n)



except ValueError:
    print ('please enter number ')

    # close



else:
    print('in else')

finally:  # always
    print('in finally')
'''


'''
    PEP8
    PIP
            - help('modules')
            - dir(__builtins__)

            -in terminal
            - pip show django
            - pip show -libeary name-
            - pip install -libeary name-
            - pip uninstall -libeary name-
            - pip install django --upgrade
            - pip help
             
    ddocs & comments
    list comprehensions
    functional programming

'''

# ddocs & comments

# user and programmer : comment


class Calc:
    ''' class for making a colculator '''
    def sum(self,x,y):  # BUG #FIX #TODO
        ''' function to return sum of 2 values
        args : x int , y :
        return: int
'''
        return x+y     # return sum of x,y


c = Calc()
print(c.sum(1,8))




















