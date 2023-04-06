from copy import deepcopy

lines_values = [0, 4, 16, 25, 25, 49, 49]
lines_size = list(range(1, 8))


class global_int:

    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1


def flip_piece(q):
    return q[1], q[0]


def create_all_pieces():
    s = list()
    for i in range(7):
        for j in range(i, 7):
            s.append((i, j))
    return s


def print_pretty(current_setup):
    s = list()
    for line in current_setup:
        s.append(str(line) + "  " + str(sum_of_line(line)))
    print("\n".join(s))


def sum_of_line(line):
    s = 0
    for piece in line:
        s += (piece[0] + piece[1])
    return s


def sum_of_last_list(current_setup):
    s = 0
    for piece in current_setup[-1]:
        s += (piece[0] + piece[1])
    return s


def solve_rest_of_pyramid(current_setup, pieces, g):
    g.inc()
    if len(pieces) == 0:
        print_pretty(current_setup)
        print(g.value)
        exit(0)
        return

    line_idx = len(current_setup)-1
    position_idx = len(current_setup[-1])

    # The new line is empty. Let's add a domino
    if position_idx == 0:
        for i, piece in enumerate(pieces):
            # Without flip
            new_setup = deepcopy(current_setup)
            new_setup[-1].append(piece)
            new_pieces = deepcopy(pieces)
            del new_pieces[i]
            solve_rest_of_pyramid(new_setup, new_pieces, g)
            # With flip
            new_setup = deepcopy(current_setup)
            new_setup[-1].append(flip_piece(piece))
            new_pieces = deepcopy(pieces)
            del new_pieces[i]
            solve_rest_of_pyramid(new_setup, new_pieces, g)
        return

    if position_idx < lines_size[line_idx]:
        # Add in the middle of the line
        for i, piece in enumerate(pieces):
            if piece[0] == current_setup[-1][-1][1]:
                new_setup = deepcopy(current_setup)
                new_setup[-1].append(piece)
                new_pieces = deepcopy(pieces)
                del new_pieces[i]
                solve_rest_of_pyramid(new_setup, new_pieces, g)
            elif piece[1] == current_setup[-1][-1][1]:
                new_setup = deepcopy(current_setup)
                new_setup[-1].append(flip_piece(piece))
                new_pieces = deepcopy(pieces)
                del new_pieces[i]
                solve_rest_of_pyramid(new_setup, new_pieces, g)
    else:
        # The line is complete. Add a new line
        if sum_of_last_list(current_setup) != lines_values[line_idx]:
            return
        new_setup = deepcopy(current_setup)
        new_setup.append([])
        new_pieces = deepcopy(pieces)
        solve_rest_of_pyramid(new_setup, new_pieces, g)


def main():
    g = global_int()
    s = create_all_pieces()
    print(f"size of set={len(s)}\n{s}")
    print(f"sum sizes {sum(lines_size)}")
    lines = None
    solve_rest_of_pyramid([[]], s, g)


main()
