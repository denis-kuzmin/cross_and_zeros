import game_logic


def print_field(field):
    print_synonyms = {
        game_logic.empty: ".",
        game_logic.cross: "X",
        game_logic.zero: "0"
    }
    for y in range(3):
        print(print_synonyms[field[0][y]], "\t", print_synonyms[field[1][y]], "\t", print_synonyms[field[2][y]], sep="")
