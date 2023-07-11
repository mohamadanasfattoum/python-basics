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

try:
    n = int(input('Enter Number : '))
    print(10/n)



except ValueError:
    print ('please enter number ')
