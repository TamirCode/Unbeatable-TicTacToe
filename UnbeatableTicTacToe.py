import random

black = "\033[30m"
green = "\033[32m"
white = "\033[37m"
yellow = "\033[33m"
red = "\033[31m"
blue = "\033[34m"
reset = "\033[0m"

player1 = f"{red}X{reset}"
player2 = f"{blue}O{reset}"


def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}\n{board[3]} | {board[4]} | {board[5]}\n{board[6]} | {board[7]} | {board[8]}\n")


def input_turn():
    global current_player
    position = input(f"{current_player}{yellow}'s turn.\nChoose a spot between 1-9: {reset}")
    while True:
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input(f"{yellow}Invalid. Choose between 1-9: {reset}")
            continue
        elif not board[int(position) - 1].isdigit():
            position = input(f"{yellow}You can't go there. Try again: {reset}")
            continue
        else:
            board[int(position) - 1] = current_player
            break


def check_for_winner():
    global winner, game_is_active
    row_1 = board[0] == board[1] == board[2]
    row_2 = board[3] == board[4] == board[5]
    row_3 = board[6] == board[7] == board[8]
    col_1 = board[0] == board[3] == board[6]
    col_2 = board[1] == board[4] == board[7]
    col_3 = board[2] == board[5] == board[8]
    dia_1 = board[0] == board[4] == board[8]
    dia_2 = board[2] == board[4] == board[6]
    if row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or dia_1 or dia_2:
        if row_1 or col_1:
            winner = board[0]
        elif row_2 or col_2 or dia_1 or dia_2:
            winner = board[4]
        else:
            winner = board[8]
        game_is_active = False


def check_for_tie():
    global game_is_active
    if not does_list_have_digits(board):
        game_is_active = False


def switch_player():
    global current_player, turn
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    turn += 1


def computer_turn_random():
    global current_player
    position = random.randint(1, 9)
    while True:
        if not board[int(position) - 1].isdigit():
            position = random.randint(1, 9)
            continue
        else:
            board[int(position) - 1] = current_player
            break


def does_list_have_duplicates(list_):
    # Check if given list contains any duplicates
    for each in list_:
        if list_.count(each) > 1:
            return True
    return False


def does_list_have_digits(list_):
    return any(each.isdigit() for each in list_)


possible_winners = []
possible_orders = []
possible_win_p1 = None
possible_win_p2 = None


def check_if_can_win():
    global possible_winners, possible_orders, possible_win_p1, possible_win_p2
    possible_winners = []
    possible_orders = []
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]

    col1 = [board[0], board[3], board[6]]
    col2 = [board[1], board[4], board[7]]
    col3 = [board[2], board[5], board[8]]

    dia1 = [board[0], board[4], board[8]]
    dia2 = [board[2], board[4], board[6]]

    if does_list_have_duplicates(row1) and does_list_have_digits(row1):
        possible_orders.append("row1")
        if player1 in row1:
            possible_winners.append(player1)
            possible_win_p1 = "row1"
        if player2 in row1:
            possible_winners.append(player2)
            possible_win_p2 = "row1"
    if does_list_have_digits(row2) and does_list_have_duplicates(row2):
        possible_orders.append("row2")
        if player1 in row2:
            possible_winners.append(player1)
            possible_win_p1 = "row2"
        if player2 in row2:
            possible_winners.append(player2)
            possible_win_p2 = "row2"
    if does_list_have_duplicates(row3) and does_list_have_digits(row3):
        possible_orders.append("row3")
        if player1 in row3:
            possible_winners.append(player1)
            possible_win_p1 = "row3"
        if player2 in row3:
            possible_winners.append(player2)
            possible_win_p2 = "row3"

    if does_list_have_duplicates(col1) and does_list_have_digits(col1):
        possible_orders.append("col1")
        if player1 in col1:
            possible_winners.append(player1)
            possible_win_p1 = "col1"
        if player2 in col1:
            possible_winners.append(player2)
            possible_win_p2 = "col1"
    if does_list_have_digits(col2) and does_list_have_duplicates(col2):
        possible_orders.append("col2")
        if player1 in col2:
            possible_winners.append(player1)
            possible_win_p1 = "col2"
        if player2 in col2:
            possible_winners.append(player2)
            possible_win_p2 = "col2"
    if does_list_have_duplicates(col3) and does_list_have_digits(col3):
        possible_orders.append("col3")
        if player1 in col3:
            possible_winners.append(player1)
            possible_win_p1 = "col3"
        if player2 in col3:
            possible_winners.append(player2)
            possible_win_p2 = "col3"

    if does_list_have_duplicates(dia1) and does_list_have_digits(dia1):
        possible_orders.append("dia1")
        if player1 in dia1:
            possible_winners.append(player1)
            possible_win_p1 = "dia1"
        if player2 in dia1:
            possible_winners.append(player2)
            possible_win_p2 = "dia1"
    if does_list_have_digits(dia2) and does_list_have_duplicates(dia2):
        possible_orders.append("dia2")
        if player1 in dia2:
            possible_winners.append(player1)
            possible_win_p1 = "dia2"
        if player2 in dia2:
            possible_winners.append(player2)
            possible_win_p2 = "dia2"

    if possible_orders != []:
        return True
    else:
        return False


def computer_turn_hard():
    global current_player, turn, turn2
    print(f"{current_player}{yellow}'s turn.{reset}")

    if turn == 2:
        if board[0] == player1 or board[2] == player1 or board[6] == player1 or board[8] == player1:
            turn2 = "corner"  # playing against corner
            board[4] = current_player
        elif board[1] == player1 or board[3] == player1 or board[5] == player1 or board[7] == player1:
            turn2 = "edge"
            if board[1] == player1:
                board[0] = current_player
            elif board[3] == player1:
                board[6] = current_player
            elif board[7] == player1:
                board[8] = current_player
            elif board[5] == player1:
                board[2] = current_player
        else:
            turn2 = "center"
            board[0] = current_player
            
    elif check_if_can_win():
        if player2 in possible_winners:
            if possible_win_p2 == "row1":
                if board[0].isdigit():
                    board[0] = current_player
                elif board[1].isdigit():
                    board[1] = current_player
                else:
                    board[2] = current_player
            elif possible_win_p2 == "row2":
                if board[3].isdigit():
                    board[3] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[5] = current_player
            elif possible_win_p2 == "row3":
                if board[6].isdigit():
                    board[6] = current_player
                elif board[7].isdigit():
                    board[7] = current_player
                else:
                    board[8] = current_player
            elif possible_win_p2 == "col1":
                if board[0].isdigit():
                    board[0] = current_player
                elif board[3].isdigit():
                    board[3] = current_player
                else:
                    board[6] = current_player
            elif possible_win_p2 == "col2":
                if board[1].isdigit():
                    board[1] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[7] = current_player
            elif possible_win_p2 == "col3":
                if board[2].isdigit():
                    board[2] = current_player
                elif board[5].isdigit():
                    board[5] = current_player
                else:
                    board[8] = current_player
            elif possible_win_p2 == "dia1":
                if board[0].isdigit():
                    board[0] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[8] = current_player
            elif possible_win_p2 == "dia2":
                if board[2].isdigit():
                    board[2] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[6] = current_player

        elif player1 in possible_winners:
            if possible_win_p1 == "row1":
                if board[0].isdigit():
                    board[0] = current_player
                elif board[1].isdigit():
                    board[1] = current_player
                else:
                    board[2] = current_player
            elif possible_win_p1 == "row2":
                if board[3].isdigit():
                    board[3] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[5] = current_player
            elif possible_win_p1 == "row3":
                if board[6].isdigit():
                    board[6] = current_player
                elif board[7].isdigit():
                    board[7] = current_player
                else:
                    board[8] = current_player
            elif possible_win_p1 == "col1":
                if board[0].isdigit():
                    board[0] = current_player
                elif board[3].isdigit():
                    board[3] = current_player
                else:
                    board[6] = current_player
            elif possible_win_p1 == "col2":
                if board[1].isdigit():
                    board[1] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[7] = current_player
            elif possible_win_p1 == "col3":
                if board[2].isdigit():
                    board[2] = current_player
                elif board[5].isdigit():
                    board[5] = current_player
                else:
                    board[8] = current_player
            elif possible_win_p1 == "dia1":
                if board[0].isdigit():
                    board[0] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[8] = current_player
            elif possible_win_p1 == "dia2":
                if board[2].isdigit():
                    board[2] = current_player
                elif board[4].isdigit():
                    board[4] = current_player
                else:
                    board[6] = current_player
        else:
            computer_turn_random()

    elif turn == 4:
        if turn2 == "center":
            if board[8] == player1:
                board[2] = current_player
        elif turn2 == "corner":
            if board[5] == player1:
                board[1] = current_player
            elif board[7] == player1:
                board[3] = current_player
            elif board[8] == player1:
                board[1] = current_player
        elif turn2 == "edge":
            if board[1] == player1 and board[0] == player2:
                if board[3] == player1 or board[6] == player1 or board[8] == player1:
                    board[4] = current_player
                elif board[2] == player1:
                    board[3] = current_player
                elif board[5] == player1:
                    board[6] = current_player
            elif board[3] == player1 and board[7] == player2:
                if board[7] == player1 or board[8] == player1 or board[2] == player1:
                    board[4] = current_player
                elif board[0] == player1:
                    board[7] = current_player
                elif board[1] == player1:
                    board[8] = current_player
            elif board[7] == player1 and board[8] == player2:
                if board[5] == player1 or board[2] == player1 or board[0] == player1:
                    board[4] = current_player
                elif board[6] == player1:
                    board[5] = current_player
                elif board[3] == player1:
                    board[2] = current_player
            elif board[5] == player1 and board[2] == player2:
                if board[1] == player1 or board[0] == player1 or board[6] == player1:
                    board[4] = current_player
                elif board[8] == player1:
                    board[1] = current_player
                elif board[7] == player1:
                    board[0] = current_player
    else:
        computer_turn_random()


# start of game
while True:
    # reset variables
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    winner = None
    current_player = player1
    game_is_active = True
    turn = 1
    
    # choose gamemode
    gamemode = input(f"{yellow}Type {green}1 {yellow}to play against computer, Type {green}2 {yellow}to play multiplayer.{reset} ")
    while True:
        if gamemode not in ["1", "2"]:
            gamemode = input(f"{yellow}Invalid. Type 1 or 2: {reset}")
            continue
        else:
            break
    if gamemode == "1":
        print(f"{yellow}Gamemode selected: {green}Singleplayer{reset}")
        # choose difficulty if gamemode is singleplayer
        difficulty = input(f"{yellow}Type {green}1 {yellow}for easy, Type {green}2 {yellow}for hard.{reset} ")
        while True:
            if difficulty not in ["1", "2"]:
                difficulty = input(f"{yellow}Invalid. Type 1 or 2: {reset}")
                continue
            else:
                break
        if difficulty == "1":
            print(f"{yellow}Difficulty selected: {green}Easy{reset}")
        else:
            print(f"{yellow}Difficulty selected: {green}Hard{reset}")
    else:
        print(f"{yellow}Gamemode selected: {green}Multiplayer{reset}")


    print(f"{black}=============================================================================\n{reset}")

    # start game
    display_board()
    while game_is_active:
        # handle turn
        if gamemode == "1":
            if current_player == player1:
                input_turn()
            else:
                print(f"{current_player}{yellow}'s turn.{reset}")
                if difficulty == "1":
                    computer_turn_random()
                else:
                    computer_turn_hard()
        else:
            input_turn()
        print(f"{black}=============================================================================\n{reset}")

        display_board()
        check_for_winner()
        check_for_tie()
        switch_player()

    if winner == player1 or winner == player2:
        print(f"{winner} {yellow}won the game!{reset}")
    else:
        print(f"{yellow}The game ended in a TIE!{reset}")
