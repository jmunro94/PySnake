horiz = 1  # left is -1, right is 1
vert = -2  # up is -2, down is 2


class piece:
    def __init__(self, direction, x, y):
        self.direction = direction
        self.coordinates = [x, y]


def find_new_front():
    x = 0; y = 0;
    front = body[0]
    if abs(front.direction) == 2:
        y = front.direction / 2
    else:
        x = front.direction
    pos = [front.coordinates[0] + x, front.coordinates[1] + y]
    return pos


def remove_old_last(last_i_d):
    x = 0; y = 0
    back = body[last_i_d]
    if abs(back.direction) == 2:
        y = back.direction / 2
    else:
        x = back.direction
    pos = [back.coordinates[0] + x, back.coordinates[1] + y]
    return pos


body = list([piece(-vert, 0, 0)])
