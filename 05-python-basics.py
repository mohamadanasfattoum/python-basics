'''
    - star : welcome message , games option
    - enter game number
    - option : option to exit
    - start play game
    - finish game : play again
    - yes : play again - no : exit

'''

class Game:
    def __init__(self):
        while True:
            print('''Welcome in our Game , REnter game Number
        1: Filter By Length
        2: Even Odd Range
        3: To Exit ....''')
            user_choice = int(input('Enter Game Number : '))
            if user_choice == 3 :
                return
            elif user_choice == 1 :
                self.filter_by_length()

            elif user_choice == 2 :
                self.even_odd_range()


            play_again = input('Press any key to play again , n to exit')
            if play_again == 'n':
                break

    def filter_by_length(self):
        names = input('Enter Names : ')
        names_list = names.split(',')
        length = int(input('Enter Length : '))
        for n in names_list:
            if len(n)>= length:
                print(n)

    def even_odd_range(self):
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








g1 = Game()


























 






