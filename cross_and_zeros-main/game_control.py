import game_logic
import console_user_iterface
import random
import copy


def available_steps(field):
    steps = []
    for x in range(3):
        for y in range(3):
            if field[x][y] == game_logic.empty:
                steps.append([x, y])
    return steps


def win_step(field, isCross):
    steps = available_steps(field)
    for step in steps:
        local_field = copy.deepcopy(field)
        game_logic.do_step(local_field, step[0], step[1], isCross)
        if game_logic.check_win(local_field) != 0:
            return step


def player_step():
    answer = int(input("enter number 1-9:"))
    x, y = [(answer - 1) % 3, (answer - 1) // 3]

    return x, y


def bot_step(field, isCross):
    bot_win = win_step(field, isCross)
    if bot_win:
        print("haha i win")
        return bot_win
    player_win = win_step(field, not isCross)
    if player_win:
        print("haha die humans")
        return player_win
    steps_available = available_steps(field)
    return random.choice(steps_available)


def step(isCross: bool, field: list, isPlayer) -> bool:
    player = "Cross" if isCross else "zero"
    print(player, "step")
    x, y = player_step() if isPlayer else bot_step(field, isCross)
    return game_logic.do_step(field, x, y, isCross)


def run_game():
    isCross = True
    field = game_logic.create_field()
    first_step = input("do u wonna do first step? y/n: ")
    isPlayerStep = first_step == "y"
    while True:
        if isPlayerStep:
            console_user_iterface.print_field(field)
        if step(isCross, field, isPlayerStep, ):
            isCross = not isCross
            isPlayerStep = not isPlayerStep
        if not game_logic.check_win(field) == 0:
            console_user_iterface.print_field(field)
            break