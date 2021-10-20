import datetime
import math
import time

import pyautogui
from blessed import Terminal
from pynput import keyboard


def get_time():
    return int(time.time())


term = Terminal()

max_time = 100  # 4 minutes 10 seconds
# max_time = 10
cont = True
char_count = 0
wiggle_count = 0
distance = 0
last_change = get_time()
mouse_position = pyautogui.position()
old_mouse_position = mouse_position


def wiggle():
    global last_change, wiggle_count
    old_position = pyautogui.position()
    pyautogui.moveTo(1, 1)
    pyautogui.press('shift')
    pyautogui.moveTo(old_position)
    last_change = get_time()
    wiggle_count += 1


def on_press(key):
    global char_count, last_change
    char_count += 1
    last_change = get_time()


def check_mouse_movement():
    global last_change, mouse_position, old_mouse_position, distance
    mouse_position = pyautogui.position()
    if mouse_position == old_mouse_position:
        return False
    else:
        last_change = get_time()
        d = int(calc_distance(old_mouse_position, mouse_position))
        distance += d
        old_mouse_position = mouse_position
        return True


def asleep():
    epoch_time = get_time()
    time_since_last_change = epoch_time - last_change
    ret = time_since_last_change >= max_time
    return ret


def print_time():
    epoch_time = get_time()
    time_since_last_change = epoch_time - last_change
    with term.hidden_cursor():
        print(term.clear)
        print(term.move_xy(1, 1) +
              f't:{str(datetime.timedelta(seconds=time_since_last_change)):<8}'
              f'c:{char_count:<5}'
              f'w:{wiggle_count:<3}'
              f'd:{distance}')


def calc_distance(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


listener = keyboard.Listener(on_press=on_press)
listener.start()

while cont:
    print_time()
    pyautogui.sleep(1)
    check_mouse_movement()
    if asleep():
        wiggle()
    cont = mouse_position != (0, 0)
    if not cont:
        break
