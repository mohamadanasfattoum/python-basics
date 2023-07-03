'''
    - star : welcome message , games option
    - enter game number
    - option : option to exit
    - start play game
    - finish game : play again
    - yes : play again - no : exit

'''

# game : names seperated . . length ---> names < length


def filter_by_length():
    names = input('Enter Names : ')
    names_list = names.split(',')
    length = int(input('Enter Length : '))
    for n in names_list:
        if len(n)>= length:
            print(n)




def even_odd_range():
    start = int(input('Enter Start : '))
    end = int(input('Enter Start : '))

    even = []
    odd = []



    for x in range (start, end+1):
        if x%2==0:
            even.append(x)

        else:
            odd.append(x)

    print(even)
    print(odd)




even_odd_range()

#filter_by_length()    
