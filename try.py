'''
a= int(input('enter a-n: '))
b= int(input('enter b-n: '))
def excep_defi(a,b):
    return a*b
numbers =list(range(a,b))
result= map(excep_defi,numbers)
print(list(result))
'''  


for i in range(int(input('enter n: '))):
    try:
        a, b = map(int, input('enter n: ').split())
        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)
