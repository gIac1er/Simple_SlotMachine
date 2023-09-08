import random

# global constants
G_MAXLINES = 3
G_MAXBET = 10
G_MINBET = 1
G_ROW = 3
G_COL = 3

# global variables
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}  # Dictionary for symbols per column

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def deposit():  # fx header#
    print("-----------------------------------------------------------")
    while True:
        deposit = input("Enter the amount you would like to deposit: $")
        if deposit.isdigit():    # number input validation
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Please enter a value bigger than 0")
        else:
            print("Please enter an int value")

    return deposit


def getLines():
    print("-----------------------------------------------------------")
    while True:
        line = input(
            "Enter number of lines to bet on (1-" + (str(G_MAXLINES))+")? ")
        if line.isdigit():
            line = int(line)
            if 0 < line < (G_MAXLINES + 1):
                break
            else:
                print("Please enter a value between 1 and " + (str(G_MAXLINES)))
        else:
            print("Please enter a value between 1 and " + (str(G_MAXLINES)))

    return line


def getBet(balance, lines):
    print("-----------------------------------------------------------")
    while True:
        print("Place your bet")
        # same as js
        bet = input(f"(Min. bet: ${G_MINBET}, Max. bet: ${G_MAXBET}): $")
        if bet.isdigit():    # number input validation
            bet = int(bet)
            if (bet * lines) > balance:
                print("You entered a bet greater than your balance of $%d" % (balance))
                print("Please deposit more to continue play the game!")
                return False
            elif G_MINBET <= bet <= G_MAXBET:
                break
            else:
                print(
                    f"Please enter a value between than ${G_MINBET} and ${G_MAXBET}")
        else:
            print("Please enter an int value")

    return bet


def spinSlotMachine(rows, cols, symbols):
    allSymbols = []     # empty array
    for key, value in symbols.items():
        for _ in range(value):   # anon variable, when lcv is not needed
            allSymbols.append(key)

    columns = []
    for _ in range(cols):
        column = []
        # make a copy of allSymbols ('= allSymbols' just copies the address)
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            selected = random.choice(currentSymbols)
            currentSymbols.remove(selected)
            column.append(selected)

        columns.append(column)

    return (columns)


# def printSlotMachine(columns):  # transposing
#    print("-----------------------------------------------------------")
#    for row in range(len(columns[0])):
#        for column in columns:
#            print("|" + column[row], end="| ")
#        print()


# transpose the dataset instead of print the temp. transposed version
def transposeSlot(slots):
    temp = []
    outcome = []
    for x in range(len(slots[0])):
        for y in range(len(slots)):
            temp.append(slots[y][x])
        outcome.append(temp)
        temp = []

    return outcome


def printUpdated(slots):
    print("-----------------------------------------------------------")
    for x in (slots):
        for y in (x):
            print("|" + y + "| ", end="")
        print()


def checkWin(slots, lines, bet, values):
    winnings = 0
    for x in range(lines):
        compared = slots[x][0]
        for y in range(len(slots[x])):
            if slots[x][y] != compared:
                break
        else:
            winnings += values[compared] * bet

    return winnings


def game():  # main function
    isDeposit = True
    spending = 0
    winnings = 0

    while (True):
        if isDeposit == True:
            balance = deposit()
            print("You deposited: $%d" % (balance))

        line = getLines()
        print("You will bet on %d line(s)" % (line))
        #
        # Bet 1 Line = Bet on top
        # Bet 2 Lines = Bet on top, middle
        # Bet 3 Lines = Bet on all
        #
        bet = getBet(balance, line)
        if bet != False:
            totalBet = bet * line
            balance -= totalBet
            spending += totalBet
            print("You bet $%d on %d line(s) for a total of $%d" %
                  (bet, line, totalBet))
            slots = spinSlotMachine(G_ROW, G_COL, symbol_count)
            updatedSlots = transposeSlot(slots)
            printUpdated(updatedSlots)
            print("-----------------------------------------------------------")

            outcome = checkWin(updatedSlots, line, bet, symbol_value)
            if outcome == 0:
                print("You didn't win, good luck next time!")
            else:
                print("You won $%d!" % (outcome))
                balance += outcome
                winnings += outcome

        print("-----------------------------------------------------------")
        print("Keep Playing?")
        choice = input("Press ENTER to continue\nPress SPACE + ENTER to leave")
        if choice == " ":
            print("-----------------------------------------------------------")
            print("Thanks for playing!")
            print("You spend a total of: $%d" % (spending))
            print("You won a total of: $%d" % (winnings))
            print("You still have: $%d" % (balance))
            break
        else:
            print("-----------------------------------------------------------")
            print(
                "Your balance is $%d, would you like to top-up your balance?" % (balance))
            choice = input(
                "Enter 'yes' to top-up\nEnter anything else to continue without topping up\n")
            if choice == "yes":
                isDeposit = True
            else:
                isDeposit = False


game()  # calls main function
