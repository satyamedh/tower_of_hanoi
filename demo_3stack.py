from classes.stand import Stand
from classes.disc import Disc

NUM_SIZE = 3

stand_1 = Stand(NUM_SIZE, True)
stand_2 = Stand(NUM_SIZE)
stand_3 = Stand(NUM_SIZE)


def show_curr():
    print(stand_1)
    print(stand_2)
    print(stand_3)
    print("===========")


show_curr()

last_disc = stand_1.stk_pop()
stand_3.stk_append(last_disc)

show_curr()

last_disc = stand_1.stk_pop()
stand_2.stk_append(last_disc)

show_curr()

last_disc = stand_3.stk_pop()
stand_2.stk_append(last_disc)

show_curr()

last_disc = stand_1.stk_pop()
stand_3.stk_append(last_disc)

show_curr()

last_disc = stand_2.stk_pop()
stand_1.stk_append(last_disc)

show_curr()

last_disc = stand_2.stk_pop()
stand_3.stk_append(last_disc)

show_curr()

last_disc = stand_1.stk_pop()
stand_3.stk_append(last_disc)

show_curr()

print("Finished?", stand_3.finished())
