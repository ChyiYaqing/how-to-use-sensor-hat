from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %.1f C" % temp)

# Get the current temperature in degrees Celsius from the humidity sensor
temp = sense.get_temperature_from_humidity()
print("Temperature from humidity sensor: %.1f C" % temp)

# Get the current temperature in degrees Celsius from the pressure sensor
temp = sense.get_temperature_from_pressure()
print("Temperature from pressure sensor: %.1f C" % temp)
