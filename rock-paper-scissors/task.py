import random
from art import rock, paper, scissors

choices = ['Rock','Paper','Scissors']

def print_choice(choice):
    '''
    To print the art of each choice
    :param choice: 'Rock' or 'Paper' or 'Scissors' or 'None'
    :return: None, it prints the art in the console
    '''
    if choice == 'Rock':
        print(rock)
    elif choice == 'Paper':
        print(paper)
    elif choice == 'Scissors':
        print(scissors)
    else:
        print("None - No art found for the choice!!!")


def gameplay():
    user_choice = int(input('What do you choose? Type 0 for Rock, or 1 for Paper or 2 for Scissors: '))

    #User must select one of three choices
    if user_choice >2 or user_choice < 0:
        print('Incorrect choice! Exiting the game')
        return False
    else:
        global user_games
        global computer_games
        global draw_games
        print(choices[user_choice])
        print_choice(choices[user_choice])

        computer_choice = random.randint(0,2)
        print(choices[computer_choice])
        print_choice(choices[computer_choice])

        if computer_choice == user_choice:
            print("Draw")
            draw_games += 1
        else:
            if computer_choice == 1: #paper
                if user_choice == 0: #rock
                    print('You lose!')
                    computer_games += 1
                else:
                    print('You win!')
                    user_games += 1
            elif computer_choice == 2: #scissor
                if user_choice == 0: #rock
                    print('You win!')
                    user_games += 1
                else:
                    print('You lose!')
                    computer_games += 1
            else: #rock
                if user_choice == 1: #paper
                    print('You win!')
                    user_games += 1
                else:
                    print('You lose!')
                    computer_games += 1
    return True

user_games = 0
computer_games = 0
draw_games = 0
continue_game = gameplay()
while continue_game:
    print('\n' * 2)
    print(f'You won = {user_games} times | Lost = {computer_games} times | Draw = {draw_games} times')
    continue_game = gameplay()


