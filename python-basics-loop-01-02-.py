#while loop
...
#loop with listis

l = [[1,2,3],[4,5,6],[7,8,9]]


for x in l:
    for y in x:
        print(y)
print('---------------')
...
# while vs for

a = 0
b = 0
while a < 4 :
    a =a+1
    b =b+1
    while b < 4 :
        b = b+1
        print(a,b)
print('---------------')        
...
# break
x = 0
while x < 10 :
    if x == 5 :
        break
    print(x)
    x +=1
print('---------------')
...

for x in range(10):
    if x == 5 :
        break
    print(x)
        
print('---------------')        
...
for x in range(10):
    if x == 5 :
        continue
    print(x)
        
print('---------------')        
...
