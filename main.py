from classes.game import Game
from classes.IllegalMove import IllegalMoveException

N = 10

game = Game(N, True, True)

game.show_curr()  # Init state

def toh(n, start, end):
    # Base case
    if n == 1:
        game.make_move(start, end)
        return
    other = 6 - (start + end)
    toh(n-1, start, other) # Move n-1 disc stack from start to other (Top level, this means move everything but the last disc to the middle stand)
    game.make_move(start, end) # Move the last disc to the end stand
    toh(n-1, other, end) # Move n-1 disc stack from other to end (Top level, this means move everything but the last disc to the end stand)

toh(N, 1, 3)

print("Total moves:", len(game.move_stack))
