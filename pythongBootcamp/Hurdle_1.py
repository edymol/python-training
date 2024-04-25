def turn_right():
    steps = 0
    while steps < 3:
        turn_left()
        steps += 1
def full_path():
    path = 0
    while path < 6:
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        path += 1

full_path()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
