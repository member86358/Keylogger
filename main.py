import pynput
from pynput.keyboard import Key, Listener, GlobalHotKeys
from pynput import keyboard
from pynput import mouse
import logging
logging.basicConfig(level=logging.DEBUG)
count = 0


def write_file(count):
    with open("log.txt", "r+") as f:
        f.write(str(count))
        f.close()

def on_press(key):
    global count
    if (key != Key.esc):
        if (str(key) == '\x0c'):
            print("{0} pressed".format(key))
            logging.debug('on_press')
            count += 1
            write_file(count)

def on_release(key):
    if (key == Key.esc):
        logging.debug('Esc')
        return False


def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))       

hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+l'),on_activate)
#Keyboard listener
#with Listener(on_press=on_press, on_release=on_release) as listener:
#    listener.join()

with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
    l.join()
