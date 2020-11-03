import random
from minimax import minimax

if __name__ == '__main__':
    arr = random.sample(range(0, 99), 10)
    winner = minimax(arr, 6)

    print('Players: {}'.format(arr))
    print('Winner: {}'.format(winner))
