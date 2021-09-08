from sense_hat import SenseHat
sense = SenseHat()
import time

def getAllInfo():
	global sense
	#[time,accel,gyro,mag,temp,humidty,pressure]
	ac = sense.accel_raw
	gy = sense.gyro_raw
	co = sense.compass_raw
	return {
		"time":time.time(),
		"accel_row_x":ac["x"],
		"accel_row_y":ac["y"],
		"accel_row_z":ac["z"],
		"gyro_raw_x":gy["x"],
		"gyro_raw_y":gy["y"],
		"gyro_raw_z":gy["z"],
		"compass_raw_x":co["x"],
		"compass_raw_y":co["y"],
		"compass_raw_z":co["z"],
		"temp":sense.temp,
		"pressure":sense.pressure,
	}


if __name__ == "__main__":
	for key, val in getAllInfo().items():
		print(key,val)
