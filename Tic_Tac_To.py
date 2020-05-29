import sys

value = {i: ' ' for i in range(1, 10)}
valid_play = set()


def display_board():
    print((value[7] + "|" + value[8] + "|" + value[9]))
    print("-----")
    print(value[4] + '|' + value[5] + '|' + value[6])
    print("-----")
    print(value[1] + '|' + value[2] + '|' + value[3])


def clearBoard():
    global value
    global valid_play
    value = {i: ' ' for i in range(1, 10)}
    valid_play = set()


def validate():
    if (value[1] == 'X' and value[2] == 'X' and value[3] == 'X') or (
            value[1] == 'O' and value[2] == 'O' and value[3] == 'O'):
        print("Correct!!!!!")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()

    elif (value[4] == "X" and value[5] == "X" and value[6] == "X") or (
            value[4] == "O" and value[5] == "O" and value[6] == "O"):
        print("Correct!!!!!")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()
    elif (value[7] == "X" and value[8] == "X" and value[9] == "X") or (
            value[7] == "O" and value[8] == "O" and value[9] == "O"):
        print("Correct")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()
    elif (value[1] == "X" and value[4] == "X" and value[7] == "X") or (
            value[1] == "O" and value[4] == "O" and value[7] == "O"):
        print("Correct")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()
    elif (value[3] == "X" and value[5] == "X" and value[7] == "X") or (
            value[3] == "O" and value[5] == "O" and value[7] == "O"):
        print("Correct")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()
    elif (value[1] == "X" and value[5] == "X" and value[9] == "X") or (
            value[1] == "O" and value[5] == "O" and value[9] == "O"):
        print("Correct")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()
    elif (value[2] == "X" and value[5] == "X" and value[8] == "X") or (
            value[2] == "O" and value[5] == "O" and value[8] == "O"):
        print("Correct")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()
    elif (value[3] == "X" and value[6] == "X" and value[9] == "X") or (
            value[3] == "O" and value[6] == "O" and value[9] == "O"):
        print("Correct")
        ply = input("Do you want to play again (Y/n) :").lower()
        if ply == 'y':
            clearBoard()
            main()
        else:
            sys.exit()


def main():
    while True:
        try:
            play = int(input("1 to 9 :"))
            if play not in valid_play:
                user = input("X or O :").capitalize()
                if user == 'X' or user == "O":
                    value[play] = user
                    valid_play.add(play)
                    display_board()
                else:
                    print("Enter Letter (X or O) not Zero")
            else:
                print('Position has been taken')
                display_board()

        except (ValueError, ZeroDivisionError):
            print("Type Number 1 to 9")

        validate()


main()
