import random


def play():
    player_1 = random.choice(['r', 'p', 's'])
    player_2 = random.choice(['r', 'p', 's'])
    if player_1 == player_2:
        print('It\'s a tie.')
    # winner helper function
    if winner(player_1, player_2):
        print('Player 1 won!')
    else:
        print('Player 2 won!')
    # recursion
    # if play_again():
    #   play()
    # else:
    #   print('Thanks for playing')


def play_again():
    again = random.choice([True, False])
    return again


# winner conditions
def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
            or (player == 'p' and opponent == 'r'):
        return True


def start():
    play()
    # play_again function
    while play_again():
        play()
    print('Thanks for playing')


start()
# play()
