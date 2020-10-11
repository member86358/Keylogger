import pynput
from pynput.keyboard import Key, Listener, GlobalHotKeys
from pynput import keyboard
from pynput import mouse
import logging
logging.basicConfig(level=logging.DEBUG)
count = 0


def main():
    def write_file(count):
        with open("log.txt", "r+") as f:
            f.write(str(count))
            f.close()

    def on_activate():
        print('Global hotkey activated!')
        global count
        count += 1
        write_file(count)

    hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+l'),on_activate)

    def for_canonical(f):
        return lambda k: f(l.canonical(k))       

    with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
        l.join()
main()