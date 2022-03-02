import itertools
import os


logo = """

 _______  __   __  _______    _______  ___   _______    _______  _______  _______    _______  _______  _______ 
|       ||  | |  ||       |  |       ||   | |       |  |       ||   _   ||       |  |       ||       ||       |
|_     _||  |_|  ||    ___|  |_     _||   | |       |  |_     _||  |_|  ||       |  |_     _||   _   ||    ___|
  |   |  |       ||   |___     |   |  |   | |       |    |   |  |       ||       |    |   |  |  | |  ||   |___ 
  |   |  |       ||    ___|    |   |  |   | |      _|    |   |  |       ||      _|    |   |  |  |_|  ||    ___|
  |   |  |   _   ||   |___     |   |  |   | |     |_     |   |  |   _   ||     |_     |   |  |       ||   |___ 
  |___|  |__| |__||_______|    |___|  |___| |_______|    |___|  |__| |__||_______|    |___|  |_______||_______|

"""


def marking(mark):
    make_mark = True
    print(f"\n{mark}'s turn.\nChoose area to mark like 'x=2, y=3'!")
    while make_mark:
        x = input("x = ")
        if x not in ["1", "2", "3"]:
            print("Please choose 1, 2 or 3.")
            continue
        y = input("y = ")
        if y not in ["1", "2", "3"]:
            print("Please choose 1, 2 or 3.")
            continue
        num = int(x) + 3 * (int(y)-1)
        if mark_check(num):
            marks[num] = f"{mark}"
            make_mark = False
        else:
            print(f"There is {marks[num]}. Choose another area.")


def mark_check(num):
    if marks[num] == " ":
        return True
    else:
        return False


def result_check(mark):
    win_condition = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    mark_list = []
    for key, value in marks.items():
        if value == mark:
            mark_list.append(key)
    for team in itertools.combinations(mark_list, 3):
        if team in win_condition:
            show_picture()
            print(f"'{mark}' wins!")
            return False
    if " " not in marks.values():
        show_picture()
        print("Draw...")
        return False
    return True


def show_picture():
    os.system("cls")
    print(logo)
    print(
        f"   1   2   3\n1  {marks[1]} | {marks[2]} | {marks[3]} \n  -----------\n2  {marks[4]} | {marks[5]} | {marks[6]} \n  -----------\n3  {marks[7]} | {marks[8]} | {marks[9]} ")


marks = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
game_on = True
while game_on:
    show_picture()
    O_count = 0
    X_count = 0
    for mark in marks.values():
        if mark == "O":
            O_count += 1
        elif mark == "X":
            X_count += 1
    if O_count > X_count:
        marking("X")
        game_on = result_check("X")
    else:
        marking("O")
        game_on = result_check("O")