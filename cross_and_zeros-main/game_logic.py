empty = 0
cross = 1
zero = 2


def check_win_conrete_player(field: list, player_id):
    for x in range(3):
        if field[x][0] == field[x][1] and field[x][1] == field[x][2] and field[x][0] == player_id:
            return True
    for y in range(3):
        if field[0][y] == field[1][y] and field[1][y] == field[2][y] and field[0][y] == player_id:
            return True
    if field[0][0] == field[1][1] and field[1][1] == field[2][2] and field[0][0] == player_id:
        return True
    if field[2][0] == field[1][1] and field[1][1] == field[0][2] and field[2][0] == player_id:
        return True

    return False


def check_win(field: list) -> int:
    if check_win_conrete_player(field, cross):
        return cross
    elif check_win_conrete_player(field, zero):
        return zero
    else:
        return empty


def do_step(field: list, x: int, y: int, isCross: bool) -> bool:
    if field[x][y] == empty:
        field[x][y] = cross if isCross else zero
        return True
    else:
        return False


def create_field() -> list:
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


