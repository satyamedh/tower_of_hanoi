from classes.disc import Disc
from classes.IllegalMove import IllegalMoveException

class Stand:
    def __init__(self, max_size: int, gen_stack: bool = False,) -> None:
        self.max_size = max_size
        self.stack = []

        if gen_stack:
            self.load_init_stack()
    
    def load_init_stack(self) -> None:
        # generate a stack
        for i in range(self.max_size, 0, -1):
            self.stack.append(Disc(size=i))
    
    def __str__(self) -> str:
        tmp = self.stack + (['*'] * (self.max_size - len(self.stack)))
        return '\n'.join([str(x) for x in tmp][::-1]) + "\n|\n=\n"
    
    def stk_append(self, disc: Disc) -> None:
        assert isinstance(disc, Disc)
        if not self.stack: 
            self.stack.append(disc)
            return
        if not disc.size < self.stack[-1].size:
            raise IllegalMoveException("Sizes incompatible")
        self.stack.append(disc)
    
    def stk_pop(self) -> Disc:
        try:
            return self.stack.pop()
        except IndexError:
            raise IllegalMoveException("Popping from an empty stack!")

    def finished(self) -> bool:
        return len(self.stack) == self.max_size

    


        