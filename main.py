import pynput
from pynput.keyboard import Key, Listener, GlobalHotKeys
from pynput import keyboard
import logging
logging.basicConfig(level=logging.INFO)
count = 0
if __name__ == "__main__":
    def main():
        def write_file(count):
            with open("log.txt", "r+") as f:
                f.write("Amount of times <ctrl>+l pressed: "+str(count))
                f.close()

        def on_activate():
            logging.info("Ctrl + l pressed")
            global count
            count += 1
            write_file(count)

        hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+l'),on_activate)

        def for_canonical(f):
            return lambda k: f(l.canonical(k))       

        with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
            l.join()
    main()