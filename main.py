import keyboard
import time

# Open the file in read mode
with open('text.txt', 'r') as file:
    # Read the contents of the file and store it in a variable
    text = file.read()

time.sleep(3)
keyboard.write(text)

print("Done!")
