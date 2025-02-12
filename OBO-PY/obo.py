import os
import readchar

screen_clear_flag = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    clear_screen()
    print("OBO PY Edition 2.0 - https://github.com/furcanomer/obo-py\n--------------------------------------------------------------------------------")
    print("Press 'D' to move right.\tPress 'R' to restart.\n")
    print("Press 'A' to move left.\tPress 'X' to exit.")
    print("--------------------------------------------------------------------------------\n")

def restart_game():
    global screen_clear_flag
    screen_clear_flag = True

def make_beep_sound():
    print("\a", end='', flush=True)

start_game()

steps = 0

while True:
    if screen_clear_flag:
        start_game()
        screen_clear_flag = False
        steps = 0

    key = readchar.readkey()

    if key.lower() == 'd':
        if steps < 19:
            print("--> ", end='', flush=True)
            steps += 1
        else:
            make_beep_sound()

    elif key.lower() == 'a':
        if steps > 0:
            print("\n<--", end='', flush=True)
            for _ in range(steps, 1, -1):
                print(" <--", end='')
            print("\n")
            steps = 0
        else:
            make_beep_sound()

    elif key.lower() == 'x':
        clear_screen()
        break

    elif key.lower() == 'r':
        restart_game()
        continue

    else:
        continue
