from sense_hat import SenseHat
import time
sense = SenseHat()

time.sleep(1)  # Allow time for the sensor to initialize

pressures = [sense.get_pressure() for _ in range(5)]
avg_pressure = sum(pressures) / len(pressures)
print("Average Pressure: %.1f millibars" % avg_pressure)