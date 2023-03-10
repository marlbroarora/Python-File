import random
#global variavles
#__________________________________________________________
MAX_LINES=3
MAX_BET=100
MIN_BET=1           
ROWS=3
COLS=3
#__________________________________________________________
#symbols
symbol_count={"A":2,"B":4,"C":6,"D":8}
symbol_value={"A":6,"B":5,"C":4,"D":3}          
#___________________________________________________________
#winning function
#___________________________________________________________

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines
#____________________________________________________________
#spin function
#____________________________________________________________

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
#____________________________________________________________
#function to print slot machine
#____________________________________________________________

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i !=len(column)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()
#_____________________________________________________________
#deposit function
#_____________________________________________________________

def deposite():
    while True:
        amount = input("What would like to deposite? Rs. ")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than zero. ")
        else:
            print("Please enter a number.")
    return amount
#______________________________________________________________
#no. of lines checking function
#______________________________________________________________

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines
#_______________________________________________________________
#amount bet function
#_______________________________________________________________
def get_bet():
    while True:
        amount = input("what would like to bet on each line? Rs. ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(f"Amount most be betwwen Rs.{MIN_BET} - Rs.{MAX_BET} . ")
        else:
            print("Please enter a number")
    return amount
#_______________________________________________________________
#spin if amount is in balance
#_______________________________________________________________

def spin(balance):
    lines= get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You don't have enough to bet that amount,your current balance is : Rs. {balance}")
        else:
            break
    print(f"You are betting Rs. {bet} on {lines} lines. total bet is equal to :Rs. {total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines =check_winnings(slots,lines,bet,symbol_value)
    print(f"You won{winnings}")
    print(f"You won on lines:",*winning_lines)
    return winnings-total_bet
#_______________________________________________________________
# main function
#_______________________________________________________________
def main():
    balance=deposite()
    while True:
        print(f"Current balance is Rs. {balance}")
        answer = input("Press enter to play (q to puit). ")
        if answer=="q":
            break
        balance+= spin(balance)
    print(f"You left with Rs. {balance}")

#_______________________________________________________________
#main  function call
#_______________________________________________________________

main()
#_______________________________________________________________

"""no. of function.I declared in the program

"""
