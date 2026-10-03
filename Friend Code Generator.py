import ctypes
import os
from random import randint

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def title(text):
    if os.name == "nt":
        ctypes.windll.kernel32.SetConsoleTitleW(text)

ver = "2.0.5"

def generator(amount, code_type):
    if code_type not in (0, 1, 2):
        raise ValueError("code type must be 0, 1, or 2")
    with open("codes.txt", "w", encoding="utf-8") as file:
        for total in range(1, amount + 1):
            match code_type:
                case 0:
                    friendcode = f"{str(randint(1000,9999))}-{str(randint(1000,9999))}-{str(randint(1000,9999))}"
                case 1:
                    friendcode = f"SW-{str(randint(1000,9999))}-{str(randint(1000,9999))}-{str(randint(1000,9999))}"
                case 2:
                    friendcode = str(randint(1,999999999))
            file.write(f"{friendcode}\n")
            if total == amount or total % 1000 == 0:
                title(f"Codes generated: {total}")
    try:
        input("Generation finished! Press enter to close")
    except EOFError:
        print()


def menu():
    clear()
    title(f"Friend Code Generator {ver}")
    while True:
        try:
            amount = int(input("Codes to generate: "))
        except EOFError:
            print()
            return
        except ValueError:
            print("Put a valid number.")
            continue
        if amount < 1:
            print("Put a valid number.")
            continue
        break
    clear()
    print("What type of code do you want to generate?")
    print(" 1 - 3ds/Wii-U friend code generator")
    print(" 2 - Switch friend code generator")
    print(" 3 - Steam friend code generator")
    print("")
    print(f"Generating - {amount} codes.")
    print("Type 1, 2 or 3 then press ENTER")
    while True:
        try:
            raw = input("")
        except EOFError:
            print()
            return
        try:
            choice = int(raw)
        except ValueError:
            print("Put a number")
            continue
        match choice:
            case 1:
                clear()
                generator(amount, 0)
                return
            case 2:
                clear()
                generator(amount, 1)
                return
            case 3:
                clear()
                generator(amount, 2)
                return
            case _:
                print("Put a number between 1-3")

if __name__ == "__main__":
    menu()
