from sense_hat import SenseHat
import time

sense = SenseHat()

sense.show_message("One small step for Pi!", text_colour=(255, 0, 0))

time.sleep(2)  # Pause for 2 seconds to allow the message to be read

sense.clear()  # Clear the LED matrix after displaying the message