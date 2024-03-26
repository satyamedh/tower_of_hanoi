from classes.stand import Stand
from classes.disc import Disc
from classes.IllegalMove import IllegalMoveException
from typing import List

class Game:
    def __init__(self, size: int, debug: bool = False, use_123: bool = False) -> None:
        self.size = size
        self.use_123 = use_123

        self.stands: List[Stand] = [Stand(size, True), Stand(size), Stand(size)]

        self.debug = debug

        self.move_stack = []

    def show_curr(self) -> None:
        print("===========")
        for stand in self.stands:
            print(stand)
        print("===========")

    def make_move(self, from_: int, to_: int) -> bool:
        # return value is True if we finished the game
        # Blindly trust the user, no exception handling
        if self.use_123:
            from_ -= 1
            to_ -= 1
        if from_ not in range(3) or to_ not in range(3):
            raise IllegalMoveException("Invalid stand number")
        if from_ == to_:
            raise IllegalMoveException("Can't move to the same stand")
        last_disc = self.stands[from_].stk_pop()
        self.stands[to_].stk_append(last_disc)
        if self.debug:
            self.show_curr()
        self.move_stack.append((from_, to_))
        return self.stands[2].finished()

