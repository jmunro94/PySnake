from graphics import *
import time
import Plays


# returns tl and br
def get_grid_coords(_x, _y, buffer, square_size):
    tl = Point(buffer + (square_size[0] * _x), buffer + square_size[1] * _y)
    br = Point(buffer + (square_size[0] * (_x + 1)), buffer + square_size[1] * (_y + 1))
    return [tl, br]


def draw_grid(top, left, bot, right, window, grid_size, square_size):
    rect = Rectangle(Point(top, left), Point(bot, right))
    rect.setFill("grey")
    rect.draw(window)
    for a in range(1, grid_size):
        tl = Point(top, left + a * square_size[1])
        br = Point(bot, left + a * square_size[1])
        line = Line(tl, br)
        line.draw(window)
        tl = Point(top + a * square_size[0], left)
        br = Point(top + a * square_size[0], right)
        line = Line(tl, br)
        line.draw(window)


def draw_in_pos(xy, col, window, buffer, square_size):
    pos = get_grid_coords(xy[0], xy[1], buffer, square_size)
    rec = Rectangle(pos[0], pos[1])
    rec.setFill(col)
    rec.draw(window)
    return rec


def reset_pos(xy, window, buffer, square_size):
    pos = get_grid_coords(xy[0], xy[1], buffer, square_size)
    rec = Rectangle(pos[0], pos[1])
    rec.setFill("grey")
    rec.draw(window)


def key_controller(k):
    key_switch = {
        "Up": _up,
        "Down": _down,
        "Left": _left,
        "Right": _right,
    }
    try:
        fun = key_switch.get(k)
        if dir(fun):
            return fun(0)

    except TypeError:
        return 0


def _up(d):
    if d == 0: return -2
    else: return 2


def _down(d):
    return _up(1)


def _left(r):
    if r == 0: return -1
    else: return 1


def _right(r):
    return _left(1)


def draw_player(window, buffer, square_size, plays, first):
    if first:
        for bod in plays.body:
            draw_in_pos(bod.coordinates, "blue", window, buffer, square_size)
    else:
        draw_in_pos(plays.body[0].coordinates, "blue", window, buffer, square_size)


def eat_prize(window, buffer, square_size, plays):
    score = 0
    if plays.body[0].coordinates == plays.prize_coords:
        score = 10
        plays.new_prize()
        draw_in_pos(plays.prize_coords, "red", window, buffer, square_size)
    return score


def main():
    plays = Plays
    score = 0
    playing = True  # has the player not won or lost

    size = [500, 500]
    buffer = 20
    window = GraphWin("Snake", size[0], size[1])
    top = left = buffer
    bot = size[0] - buffer
    right = size[1] - buffer

    grid_size = plays.grid_size
    square_size = [(size[0] - 2 * buffer) / grid_size, (size[1] - 2 * buffer) / grid_size]

    draw_grid(top, left, bot, right, window, grid_size, square_size)
    draw_player( window, buffer, square_size, plays, True)
    draw_in_pos(plays.prize_coords, "red",  window, buffer, square_size)

    last_i_d = 2
    score_text = Text(Point(50, 10), "Score: " + str(score))
    score_text.draw(window)
    while playing:
        key = window.checkKey()
        if key == "q": playing = False; break
        new_dir = key_controller(key)
        if new_dir != -plays.body[0].direction:
            plays.next_dir = new_dir
        else:
            plays.next_dir = 0
        playing, last_i_d, rs = plays.play(last_i_d)
        point_bonus = eat_prize(window, buffer, square_size, plays)
        score += point_bonus
        if point_bonus == 0 and playing:
            reset_pos(rs, window, buffer, square_size)
        else:
            score_text.setText("Score: " + str(score))
        draw_player(window, buffer, square_size, plays, False)
        if playing: time.sleep(1 / plays.speed)

    if len(plays.body) == (grid_size * grid_size): playing = True
    if playing: w_text = "Win"
    else: w_text = "Lose"
    rec = Rectangle(Point(size[0] / 6, size[1] / 6),Point(size[0] * 5 / 6, size[1] * 5 / 6))
    rec.setFill("White")
    rec.draw(window)
    win_lose_text = Text(Point(size[0] / 2, size[1] / 2), "You " + w_text + "!!!!!!!")
    win_lose_text.draw(window)

    win_lose_text = Text(Point(size[0] / 2, size[1] / 1.8), "Press any key to quit. Score: " + str(score))
    win_lose_text.draw(window)

    k = window.getKey()
    window.close()
    return k
