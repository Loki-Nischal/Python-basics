from random import shuffle
example = [1,2,3,4,5,6,7]

def shuffle_list(mylist):
    shuffle(mylist)
    print("Shuffled List is:",mylist)
    return mylist



# mylist = [' ','O',' ']
# shuffle_list(mylist)
# print(mylist)

def player_guess():
    guess = ''
    while guess not in ['0','1','2']: # to make sure user inputs valid value between 0,1,2
        guess = input("Pick a number: 0, 1 or 2: ")
    return int(guess)
player_choice = player_guess()
print(f"You chose: {player_choice}")

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct Guess!")
    else:
        print("Wrong Guess! Try Again")
        print(mylist)

#initial list
mylist = [' ','O',' ']

#Shuffle list
shuffled_list = shuffle_list(mylist)

#User Guess
# player_choice = player_guess()

#checking guess
check_guess(shuffled_list,player_choice)        