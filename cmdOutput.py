def win_output():
    print("You win :)")


def lose_output():
    print("You lose :(")


def print_dice(dice):
    print("\n\nDices:", dice)


def print_sum(sum_dice):
    print("Dice sum: ", sum_dice)


def print_tentatives(tentatives):
    print(f"You won with: {tentatives} tentatives")


def print_menu():

    print(
        '\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\nEnter "1" roll the dices\nEnter "0" to exit\n')
    return str(input('Choose an option: '))


def number_of_dices():
    return int(input("Number of Dices (1 to 5): "))
