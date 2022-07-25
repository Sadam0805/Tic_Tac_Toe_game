
## Example to How to Play. And How to choose the correct place.
def example_to_play():
    print("\n\n\t\t\t\t\t\t\t\t\tHere! The Rules..")
    print("\n\n\t\t\t\t\t\t\t\t\tEXAMPLE Below:\n")
    print("\n\t\tChoose Your Place Number:↡\t\t\t\t\t\tIf You Want to Exit or End this Game.")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease Enter 'ZERO' in Number. (EX: '0' )")
    print("\t\t\t  1  |  2  |  3")
    print("\t\t\t-----------------")
    print("\t\t\t  4  |  5  |  6")
    print("\t\t\t-----------------")
    print("\t\t\t  7  |  8  |  9")


## Question to choose start with 'X or O' .
def start_with():
    global game_on
    question = input("\nDo You Want to Start with 'X or O' ? TYPE: X or O : ").lower()
    if question == "x":
        return "X"
    elif question == "o":
        return "O"
    elif question == '0':
        game_on = False
    else:
        print("\nSomething Went Wrong. Please Try Again Once More.")
        game_on = False


## sample table to show how to play this game.
def sample():
    print(f"\n\t\t\t\t\t  {one}  |  {two}  |  {three}")
    print("\t\t\t\t\t-----------------")
    print(f"\t\t\t\t\t  {four}  |  {five}  |  {six}")
    print("\t\t\t\t\t-----------------")
    print(f"\t\t\t\t\t  {seven}  |  {eight}  |  {nine}")


## Game function
def game_function():

    global one, two, three, four, five, six, seven, eight, nine, x_o, game_on

    ask = input("\nEnter Your Number: ")

    if ask == '0':
        game_on = False
        return game_on

    elif ask == '1':
        if one == "-":
            one = one.replace("-", x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '2':
        if two == "-":
            two = two.replace("-", x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(value=x_o)
            return x_o

    elif ask == '3':
        if three == "-":
            three = three.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '4':
        if four == "-":
            four = four.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '5':
        if five == "-":
            five = five.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '6':
        if six == "-":
            six = six.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '7':
        if seven == "-":
            seven = seven.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '8':
        if eight == "-":
            eight = eight.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    elif ask == '9':
        if nine == "-":
            nine = nine.replace('-', x_o)
        else:
            print("\n Try Any Other Box. That Box was Taken.\n")
            x_o = change_x_and_o(x_o)
            return x_o

    else:
        print("Please Retry Again!")
        x_o = change_x_and_o(x_o)
        return x_o

    print(f"\n\t\t\t\t\t  {one}  |  {two}  |  {three}")
    print("\t\t\t\t\t-----------------")
    print(f"\t\t\t\t\t  {four}  |  {five}  |  {six}")
    print("\t\t\t\t\t-----------------")
    print(f"\t\t\t\t\t  {seven}  |  {eight}  |  {nine}")

    ## check any one is win or lose or the game is draw.
    if check_the_winner_is_o():
        game_on = False
        return game_on

    elif check_the_winner_is_x():
        game_on = False
        return game_on

    elif check_the_game_is_draw():
        game_on = False
        return game_on

    return True


## Check there any one is win.

## solution for X
def check_the_winner_is_x():
    if one == 'X' and two == 'X' and three == 'X' or four == "X" and five == "X" and six == "X" or seven == "X" and eight == "X" and nine == "X":
        print("\n\t\t\t\t\t The 🏆 Winner 🏆 is")
        print("\n\t\t\t\t\t MR. XXXXXXXXXXXXXX")
        return True
    elif one == 'X' and four == 'X' and seven == 'X' or two == 'X' and five == 'X' and eight == 'X' or three == 'X' and six == 'X' and nine == 'X':
        print("\n\t\t\t\t\t The 🏆 Winner 🏆 is")
        print("\n\t\t\t\t\t MR. XXXXXXXXXXXXXX")
        return True
    elif one == 'X' and five == 'X' and nine == 'X' or three == 'X' and five == 'X' and seven == 'X':
        print("\n\t\t\t\t\t The 🏆 Winner 🏆 is")
        print("\n\t\t\t\t\t MR. XXXXXXXXXXXXXX")
        return True


## solution for O
def check_the_winner_is_o():
    if one == 'O' and two == 'O' and three == 'O' or four == "O" and five == "O" and six == "O" or seven == "O" and eight == "O" and nine == "O":
        print("\n\t\t\t\t\t The 🏆 Winner 🏆 is")
        print("\n\t\t\t\t\t MR. OOOOOOOOOOOOOO")
        return True
    elif one == 'O' and four == 'O' and seven == 'O' or two == 'O' and five == 'O' and eight == 'O' or three == 'O' and six == 'O' and nine == 'O':
        print("\n\t\t\t\t\t The 🏆 Winner 🏆 is")
        print("\n\t\t\t\t\t MR. OOOOOOOOOOOOOO")
        return True
    elif one == 'O' and five == 'O' and nine == 'O' or three == 'O' and five == 'O' and seven == 'O':
        print("\n\t\t\t\t\t The 🏆 Winner 🏆 is")
        print("\n\t\t\t\t\t MR. OOOOOOOOOOOOOO")
        return True


## Check the Game is Draw.
def check_the_game_is_draw():
    if one != "-" and two != "-" and three != "-" and four != "-" and five != "-" and six != "-" and seven != "-" and eight != "-" and nine != "-":
        print("\n\t\t\t\t\t The Game is Draw.")
        return True


## To change the X and O
def change_x_and_o(value):
    if value == "X":
        return x_o.replace("X", "O")
    elif value == "O":
        return x_o.replace("O", "X")


one = '-'
two = '-'
three = '-'
four = '-'
five = '-'
six = '-'
seven = '-'
eight = '-'
nine = '-'


game_on = True
print("\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the 'Tic Tac Toe' Game.\n\n")
example_to_play()
x_o = start_with()
sample()


while game_on:
    game_on = game_function()
    x_o = change_x_and_o(x_o)
