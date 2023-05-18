import datetime
import os
import autopy
from pynput.keyboard import Key, Listener

# on press function
def on_press(key):
    check_key(key)
    if key in exit_combination:
        currently_pressed.add(key)
        # print("Exit condition has been activated.")
        Listener.stop()


# on release function
def on_release(key):
    try:
        currently_pressed.remove(key)
    except KeyError:
        pass

# if key is ptrscrn
def check_key(key):
    if key == Key.print_screen:
        # print("pressed")
        shot = autopy.bitmap.capture_screen()
        now = datetime.datetime.now()
        timenow = now.strftime("%H_%M_%S")
        path = r"E:\new_work\automation\company-website\cbash\shots\" + str(datetime.date.today())
        try:
            shot.save(path+ '//' +timenow+'.png')
        except FileNotFoundError:
            os.makedirs(path)
            shot.save(path+'//'+timenow+'.png')

# exit conditions: Ctrl_l + PtrScn
exit_combination = {Key.ctrl_l, Key.print_screen}
currently_pressed = set()

# create folder
path = r"E:\new_work\automation\company-website\cbash\shots\" + str(datetime.date.today())
try:
    os.makedirs(path)
except FileExistsError:
    pass


# collect events until released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        
        listener.join()