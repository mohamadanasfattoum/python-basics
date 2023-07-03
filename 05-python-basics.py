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




filter_by_length()    
