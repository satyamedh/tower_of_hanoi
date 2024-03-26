from classes.game import Game
from classes.IllegalMove import IllegalMoveException

game = Game(3, True)

game.show_curr()  # Init state

game.make_move(0, 2)
game.make_move(0, 1)
game.make_move(2, 1)
game.make_move(0, 2)
game.make_move(1, 0)
game.make_move(1, 2)
finished = game.make_move(0, 2)

print("Finished?", finished)
