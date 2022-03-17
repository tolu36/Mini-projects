import random
from program import my_func
from mymainpackage.some_main_script import report_main
from mymainpackage.mysubpackages.mysubscript import sub_report
import pdb

pdb.set_trace()

my_func()
report_main()
sub_report()


def tic_tac():
    """
    This a tic-tac-toe game that randomly deteremines who goes first.
    The function will notify who the winner is and when there is a draw.
    """
    game = "begin"
    position_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
    }
    win = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]
    moves = []
    player1_choice = []
    player2_choice = []
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(
        "Welcome to the Tic Tac Toe!\nYour position options ranges from 1-9, as shown below.\n"
    )
    disp = display(game, position_dict)
    print(disp)

    game = "start"
    disp, position_dict = display(game, position_dict)
    print(disp)
    order = goes_first()
    if len(order) < 3:
        first, second = order
    else:
        return order
    players = [first, second]

    while moves.sort() != position_list:
        game = "playing"
        game_on = True

        while game_on:
            for player in players:
                current_player = input(f"{player}, pick a postion from 1-9.")
                if (
                    current_player.isdigit() == False
                    or int(current_player) not in position_list
                    or int(current_player) in moves
                ):
                    print("Wrong choice.\n")
                    keep_playing = input("Keep playing Yes/No?")
                    if keep_playing == "Yes":
                        continue
                    else:
                        return f"{player} forfeits, {[x for x in players if x not in player][0]} wins!! Thanks for playing!"
                else:
                    game_on = False

                current_player = int(current_player)
                moves.append(current_player)
                if player == first:
                    player1_choice.append(current_player)
                else:
                    player2_choice.append(current_player)

                position = list(position_dict.keys())[current_player - 1]
                disp, position_dict = display(game, position_dict, player, position)
                print("\n" * 100)
                print(disp)

                if len(moves) > 4:
                    if len(player1_choice) > 2:
                        for i in win:
                            if set(i).issubset(set(player1_choice)):
                                return f"{first} wins!!"
                    if len(player2_choice) > 2:
                        for i in win:
                            if set(i).issubset(set(player2_choice)):
                                return f"{second} wins!!"
                    if len(moves) == 9:
                        return "Draw!"

with open('practic.txt','w+') as f:
    f.write('testing testing testing')
def display(
    game,
    position_dict,
    player_flag=None,
    position=None,
):
    if game == "begin":
        a = position_dict["a"]
        b = position_dict["b"]
        c = position_dict["c"]
        d = position_dict["d"]
        e = position_dict["e"]
        f = position_dict["f"]
        g = position_dict["g"]
        h = position_dict["h"]
        i = position_dict["i"]
        return f"{a}|{b}|{c}\n-----\n{d}|{e}|{f}\n-----\n{g}|{h}|{i}\n"

    elif game == "start":
        position_dict = dict.fromkeys(position_dict, " ")
        a = position_dict["a"]
        b = position_dict["b"]
        c = position_dict["c"]
        d = position_dict["d"]
        e = position_dict["e"]
        f = position_dict["f"]
        g = position_dict["g"]
        h = position_dict["h"]
        i = position_dict["i"]
        return f"{a}|{b}|{c}\n-----\n{d}|{e}|{f}\n-----\n{g}|{h}|{i}\n", position_dict

    elif game == "playing":
        position_dict[position] = player_flag
        a = position_dict["a"]
        b = position_dict["b"]
        c = position_dict["c"]
        d = position_dict["d"]
        e = position_dict["e"]
        f = position_dict["f"]
        g = position_dict["g"]
        h = position_dict["h"]
        i = position_dict["i"]
        return f"{a}|{b}|{c}\n-----\n{d}|{e}|{f}\n-----\n{g}|{h}|{i}\n", position_dict


def goes_first():
    choice = "start"
    choice2 = ""
    while choice not in ["X", "O"]:
        choice = input("Player 1, X or O?").upper()
        if choice not in ["X", "O"]:
            print("\nWrong choice.\n")
            keep_playing = input("Keep playing Yes/No?")
            if keep_playing == "Yes":
                continue
            else:
                return "Thanks for playing!"
    if choice == "X":
        choice2 = "O"
    else:
        choice2 = "X"

    print(f"Player 1 is {choice} and Player 2 is {choice2}.\n")

    n = ""
    m = ""
    while n == m:
        n = random.randint(1, 9)
        m = random.randint(1, 9)
    if n > m:
        print(f"{choice} is first.\n")
        first = choice
        second = choice2
    else:
        print(f"{choice2} is first.\n")
        first = choice2
        second = choice
    return first, second
