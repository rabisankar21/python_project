# import webbrowser
# import time
# import random
# import string
#
# # Define the URL of the online editor you want to use
# editor_url = "https://www.editpad.org/"  # Replace with the actual URL
#
# # Define a function to generate a random letter
# def generate_random_letter():
#     return random.choice(string.ascii_letters)
#
# # Open the online editor and write a random letter every 5 minutes
# webbrowser.open(editor_url)
#
# while True:
#
#     random_letter = generate_random_letter()
#     print(f"Writing: {random_letter}")
#     time.sleep(200)  # 300 seconds = 5 minutes


import pyautogui
import time

# Define the time interval in seconds
time_interval = 5  # Adjust this as needed

while True:
    try:
        # Get the current mouse cursor position
        current_x, current_y = pyautogui.position()

        # Print the current position (optional)
        print(f"Current position: ({current_x}, {current_y})")

        # Change the mouse cursor position (you can set your own coordinates)
        new_x = current_x + 1  # Example: move 50 pixels to the right
        new_y = current_y + 1  # Example: move 50 pixels down

        pyautogui.moveTo(new_x, new_y, duration=0.25)  # Duration is the time taken to move

        # Wait for the specified time interval
        time.sleep(time_interval)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
