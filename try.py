a= int(input('enter n: '))
b= int(input('enter n: '))
def excep_defi(a,b):
    return a+b
numbers =list(range(a,b))
result= map(excep_defi,numbers)
print(list(result))
    
