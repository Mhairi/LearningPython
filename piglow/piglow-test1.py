from pyglow import PyGlow # imports PyGlow module
from time import sleep

pyglow = PyGlow() # defines pyglow as the function PyGlow
pyglow.all(0) # sets all lights off

pyglow.led(1, 100)
sleep(1)
pyglow.led(1, 0)
sleep(1)

pyglow.update_leds()
