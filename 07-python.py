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


#class Calc:
#    ''' class for making a colculator '''
#    def sum(self,x,y):  # BUG #FIX #TODO
#       ''' function to return sum of 2 values
#       args : x int , y :
#        return: int
#'''
#        return x+y     # return sum of x,y


#c = Calc()
#print(c.sum(1,8))

#   list comprehensions


'''
names = ['anas','ali','ahmad','omar']

length = []
for x in names:
    length.append(len(x))

print(length)


result = [len(x) for x in names]
print (result)


result2 = [x for x in names if len(x) > 4]
print (result2)
'''
# Game input names and length with list comprehensions

'''
names = input('Enter names : ')
names_list = names.split(',')
length = int(input('Enter Length : '))
result2 = [x for x in names_list if len(x) >= length]
print (result2)
'''
'''
numbers = list(range(1,100))

even = [x for x in numbers if x%2==0]


print(even)

'''
# numbers with list comprehensions
'''
numbers = list(range(1,100))

even = [x for x in numbers if x%2==0]
odd = [x for x in numbers if x%2!=0]
print(odd)
print(even)
'''
# number without if
'''
numbers_even = list(range(0,100,2))
numbers_odd = list(range(0,100,1))
even = [x for x in numbers_even if x%2==0]
odd = [x for x in numbers_odd if x%2!=0]
print(odd)
print(even)
'''
'''
numbers = list(range(1,100))

result = [x if x%2==0 else '*' for x in numbers ]
print (result)

'''
'''
d = {'anas':20, 'ali':30, 'ahmad':40} 

d = {k:v*2 for(k,v) in d.items()}
print(d)
'''
























