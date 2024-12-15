from time import sleep
import platform
import os
def show_balance():
    print (f"Your balance is: {balance:.2f}")
    sleep(1.5)

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount <= 0:
        print("invalid value!!")
        sleep(1.5)
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount: "))
    if amount > balance:
        print("Insufficient funds")
        sleep(1.5)
        return 0
    elif amount <0:
        print("The amount must be greater than Zero")
        sleep(1.5)
        return 0
    else:
        return amount



balance = 0

is_running = True

while is_running:
    print("===============================")
    print("Banking Program".center(30))
    print("===============================")
    print("   1 - Show Balance")
    print("   2 - Deposit")
    print("   3 - Withdraw")
    print("   4 - Exit")
    print("=========================")

    choice = input("Enter your choice (1-4):").strip()


    if choice == "1":
        show_balance()
    elif choice == "2":
        balance  += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid option!!")   

print("Thank you have a nice day!".upper())
