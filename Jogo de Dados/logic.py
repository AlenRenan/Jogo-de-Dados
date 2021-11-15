from random import randint
import cmdOutput


def aleatory_dice():

    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    cmdOutput.print_dice(dice1, dice2)
    return dice1, dice2


def game_logic(dice1, dice2):

    sumDide = dice1 + dice2
    cmdOutput.print_sum(sumDide)

    if sumDide == 7:
        cmdOutput.win_output()
    elif sumDide == 11:
        cmdOutput.win_output()
    else:
        cmdOutput.lose_output()


game_logic(*aleatory_dice())
