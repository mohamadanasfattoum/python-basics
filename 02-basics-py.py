# Loop with listis
'''
l = [[1,2,3],[4,5,6,],[7,8,9]]
'''
'''

for x in l:
    for y in x:
        print(y)
'''

'''
for x in l[0]:
    print(x)

for x in l[2]:
    print(x)
'''

# break in loop
'''
for x in range(10):
    if x==5 :
        break
    print(x)
'''
# continue in loop
'''
for x in range(10):
    if x==5 :
        continue
    print(x)
'''
# pass
'''
for x in range(10):
   pass
'''
# Loops Best Practices : Examples
# -1
'''
print('Number\tSqaure')
print('--------------')


x = 1
while x < 11 :
    print (x,'\t',x*x)
    x += 1

print('welcome \nAnas')
'''
'''
print('Number\tSqaure')
print('--------------')
for x in range(1,11):
    print (x,'\t',x*x)
'''
# -2
'''
start = int(input('Enter Start : '))
end = int(input('Enter End : '))


print('Number\tSqaure')
print('--------------')


for x in range(start,end+1):
    print (x,'\t',x*x)
'''

# -3
'''
start = int(input('Enter Start : '))
end = int(input('Enter End : '))

for x in range(start):
    print('*'*end)
'''
'''
start = int(input('Enter Start : '))
end = int(input('Enter End : '))
for x in range(start):
    for y in range (end):
        print('*',end='')
    print('')
'''
# -4
'''
for x in range(1,9):
    print('*'*x)
'''
# Functions
'''
def mysum():
    x = 5
    y = 10
    print(x+y)

mysum()
'''
'''
def mysum(x,y):
    print(x+y)

mysum(5,10)
mysum(5,50)

'''
'''
def divdeby(x,y):
    for n in range(1,101):
        if n%x==0 and n%y==0 :
            print(n)

divdeby(5,10)
'''

def mysum1(x,y):
    return x+y
    
b = mysum1(5,10)
print(b)

    
