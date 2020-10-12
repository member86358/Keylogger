import pynput
from pynput.keyboard import Key, Listener, GlobalHotKeys
from pynput import keyboard
import logging
import datetime
import time
import datetime
logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG,format='%(asctime)s %(message)s')
count = 0
if __name__ == "__main__":
    def main():
        def write_file(count):
            with open("data.txt", "r+") as f:
                logging.debug("Saving to data.txt")
                localtime = str(datetime.datetime.now())
                f.write(localtime + " Amount of times <ctrl>+l pressed: "+str(count))
                f.close()

        def on_activate():
            global count
            count += 1
            write_file(count)

        hotkey = keyboard.HotKey(keyboard.HotKey.parse('<cmd>'),on_activate)

        def for_canonical(f):
            return lambda k: f(l.canonical(k))       

        with keyboard.Listener(on_press=for_canonical(hotkey.press),on_release=for_canonical(hotkey.release)) as l:
            l.join()
    main()