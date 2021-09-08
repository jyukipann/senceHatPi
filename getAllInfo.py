from sense_hat import SenseHat
sense = SenseHat()
import time

def getAllInfo():
	global sense
	#[time,accel,gyro,mag,temp,humidty,pressure]
	return {
		"time":time.time(),
		"accel_row":sense.accel_raw,
		"gyro_raw":sense.gyro_raw,
		"compass_raw":sense.compass_raw,
		"temp":sense.temp,
		"pressure":sense.pressure,
	}


if __name__ == "__main__":
	for key, val in getAllInfo().items():
		print(key,val)
