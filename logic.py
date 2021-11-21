from random import sample  # imports to generate aleatory values
import cmdOutput  # imports the cmdOutput.py

"""
Function to generate the dices
"""

n_dices = cmdOutput.number_of_dices()  # input to choose the number of dices


def aleatory_dice():
    dice = sample(range(1, 6), n_dices)  # generate aleatory numbers in range of 1,6
    return dice  # return the dice


"""
Function responsible for the game logic
"""


def game_logic(dice):

    tentatives = 1  # number of tentatives

    while True:  # Menu loop
        option = cmdOutput.print_menu()  # Menu input

        if option == '1':  # Roll dices option
            dice = aleatory_dice()  # generates new aleatory numbers when the function is parameterized
            sum_dice = sum(dice)  # Sum of dices
            cmdOutput.print_dice(dice)  # print dice values
            cmdOutput.print_sum(sum_dice)  # print sum

            if sum_dice == 7:  # if win with sum == 7
                cmdOutput.win_output()  # win output from cmdOutput
                cmdOutput.print_tentatives(tentatives)  # print the number of tentatives
                break  # stop the program
            elif sum_dice == 11:  # if win with sum == 11
                cmdOutput.win_output()  # win output from cmdOutput
                cmdOutput.print_tentatives(tentatives)  # print the number of tentatives
                break  # stop the program
            else:
                tentatives = tentatives + 1  # sum the number of tentatives
                cmdOutput.lose_output()  # lose output from cmdOutput
        elif option == "0":  # exit option
            break  # stop the program


game_logic(aleatory_dice())  # passes the return of aleatory_dice to the game_logic
