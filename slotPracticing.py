MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("The amount must be greater than 0.")
        else:
            print("Please enter only the numbers.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines 1-" + str(MAX_LINE) + "? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Please enter the valid number of line.")
        else:
            print("Please enter only the numbers.")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The bet amount must be greater than {MIN_BET}")
        else:
            print("Please enter only the numbers.")
    return amount

def main():

    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = lines * bet
    print(f"You are betting {lines} lines with {bet}$ each which is equals {total_bet}")

main()