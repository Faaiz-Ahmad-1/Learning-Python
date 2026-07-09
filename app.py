import time
from random import randint
import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.title("Unfair R.P.S.")
logo = tk.PhotoImage(file="Unfair R.P.S. Logo.png")
window.iconphoto(True, logo)

window.mainloop()

print("Hello, welcome to A.I. VS Human rock, paper, scissors.\n\n\n")


def countdown(start, end, interval, wait):
    for countdown in range(int(start), int(end), int(interval)):
        print(countdown)
        time.sleep(int(wait))
    print("GO!")


replay = "y"
name = input("Enter your name: ")

print(f"\nAlright, {name} choose your weapon.")
if name.casefold() == "exit":
    exit()

if name.casefold() == "fair":
    while replay.casefold() == "y":
        weapon = input("So you chose: ")
        ai_attack = randint(1, 3)
        countdown(3, 0, -1, 1)
        time.sleep(0.2)
        if weapon == "":
            print("Choose a damn weapon, as a punishment you restart the entire process.")
            exit()
        elif ai_attack == 1:
            print("Alright, I choose scissors")
            replay = input("Would you like to play another round (y/n)?\n> ")
        elif ai_attack == 2:
            print("Alright, I choose paper")
            replay = input("Would you like to play another round (y/n)?\n> ")
        elif ai_attack == 3:
            print("Alright, I choose rock")
            replay = input("Would you like to play another round (y/n)?\n> ")
        else:
            print("ERROR")
            exit()
else:
    while replay.casefold() == "y":
        weapon = input("So you chose: ")
        countdown(3, 0, -1, 1)
        time.sleep(0.2)
        if weapon == "":
            print("Choose a damn weapon, as a punishment you restart the entire process.")
            exit()
        elif weapon.casefold() == "paper":
            print("Alright, I choose scissors")
            time.sleep(0.2)
            print("Ha, you lost! Wanna retry? (y/n)")
            replay = input("> ")
        elif weapon.casefold() == "rock":
            print("Alright, I choose paper haha")
            time.sleep(0.2)
            print("You wont be able to guess why I won. Will you try again? (y/n)")
            replay = input("> ")
        elif weapon.casefold() == "scissors":
            print("Alright, I choose rock hehe")
            time.sleep(0.2)
            print("I won! Try again? (y/n)")
            replay = input("> ")
        else:
            print("ERROR")
            exit()
