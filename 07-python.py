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
