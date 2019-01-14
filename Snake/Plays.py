import random
import copy
from Snake import *


def new_prize():
    co = random.choice(empty_squares)
    empty_squares.remove(co)
    prize_coords.__init__(co)


def setup_snake():
    body.pop(0)
    x = int(grid_size/2); y = int(grid_size/2)
    body.append(piece(vert, x, y))
    body.append(piece(vert, x, y + 1))
    body.append(piece(vert, x, y + 2))
    for i in range(0, 2): empty_squares.remove(body[i].coordinates)


def play(last_i_d):
    temp_old_back_pos = [0,0]
    if next_dir == 0:
        direction = body[0].direction
    else:
        direction = next_dir
    new_front = find_new_front()
    if new_front[1] < 0 or new_front[1] >= grid_size or new_front[0] < 0 or new_front[0] >= grid_size:
        return [False, last_i_d, [0, 0]]
    for bod in body:
        if new_front == bod.coordinates:
            return [False, last_i_d, [0, 0]]
    body.insert(0, piece(direction, new_front[0], new_front[1]))
    if prize_coords != new_front:
        empty_squares.remove(body[0].coordinates)

        temp_old_back_pos = copy.copy(body[last_i_d + 1].coordinates)
        new_back = remove_old_last(last_i_d + 1)
        body.pop(last_i_d + 1)
        for i in range(0, 2): new_back[i] = int(new_back[i])
        empty_squares.append(temp_old_back_pos)
    last_i_d = len(body) - 1
    return [True, last_i_d, temp_old_back_pos]


grid_size = 6
speed = 3.8  # number of squares per second

empty_squares = list()


prize_coords = [0, 0]
if grid_size < 5: grid_size = 5

for x in range(0, grid_size):
    for y in range(0, grid_size):
        empty_squares.append([x, y])

new_prize()
setup_snake()
next_dir = 0
