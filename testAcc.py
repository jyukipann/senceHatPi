from sense_hat import SenseHat
sense = SenseHat()

acceleration = sense.get_accelerometer_raw()
x = str( round( acceleration['x'],1 ) )
y = str( round( acceleration['y'],1 ) )
z = str( round( acceleration['z'],1 ) )