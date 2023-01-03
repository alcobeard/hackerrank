# Write your code here
import random

win_word_list = ['python', 'java', 'kotlin', 'javascript']
win_word = random.choice(win_word_list)
# win_word2 = win_word[0:3] + '-'*(len(win_word) - 3)

print('H A N G M A N\n')


def play():
    player_try = 8
    guess_word = '-' * len(win_word)
    last_guesses = []

    while player_try:
        print('\n')
        print(guess_word)
        player_guess = input('Input a letter: ')

        if player_guess in set(win_word) and player_guess not in last_guesses and len(
                player_guess) == 1 and player_guess.islower():
            res_id = [i for i, letter in enumerate(win_word) if letter == player_guess]
            temp = list(guess_word)
            for i in res_id:
                temp[i] = player_guess
            guess_word = ''.join(temp)

            last_guesses.append(player_guess)

        else:
            if len(player_guess) != 1:
                print('You should input a single letter')
            elif not player_guess.islower():
                print('It is not an ASCII lowercase letter')
            elif player_guess in last_guesses:
                print('You already typed this letter')
            else:
                print('No such letter in the word')
                last_guesses.append(player_guess)
                player_try -= 1

        if '-' not in guess_word:
            print('You guessed the word!')
            print('You survived!')
            break

    if player_try == 0:
        print('You are hanged!')


while True:
    user_input = input('Type "play" to play the game, "exit" to quit:')
    if user_input == 'play':
        play()
    elif user_input == 'exit':
        exit()