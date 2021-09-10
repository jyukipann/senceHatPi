from sense_hat import SenseHat
sense = SenseHat()
import time
import math

#calib
G = 9.80665
#accel sensor norm
gs_delta = 0.975374592

#last current
t_l_c = [0,0]
a_l_c = [0,0]
v_l_c = [0,0]
x_l_c = [0,0]

def norm(x,y,z):
	return math.sqrt(x**2 + y**2+ z**2)

def trapezoidal(last, current, dt):
	return ((last + current)/2)*dt

def getAllInfo():
	global sense,t_l_c,a_l_c,v_l_c,x_l_c,G,gs_delta
	#[time,accel,gyro,mag,temp,humidty,pressure]
	ac = sense.accel_raw
	gy = sense.gyro_raw
	co = sense.compass_raw
	t_l_c[0] = t_l_c[1]
	t_l_c[1] = time.time()
	dt = t_l_c[1] - t_l_c[0]
	a_l_c[0] = a_l_c[1]
	a_l_c[1] = (norm(*ac.values())-gs_delta)*G
	v_l_c[0] = v_l_c[1]
	v_l_c[1] += trapezoidal(*a_l_c, dt)
	x_l_c[0] = x_l_c[1]
	x_l_c[1] += trapezoidal(*v_l_c, dt)
	return {
		"time":t_l_c[1],
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
		"velocity":v_l_c[1],
		"displacement":x_l_c[1],
	}


if __name__ == "__main__":
	for key, val in getAllInfo().items():
		print(key,val)
