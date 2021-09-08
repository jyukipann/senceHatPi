import datetime
dt_now = datetime.datetime.now()
import getAllInfo
import csv
import time
#start_time = time.time()
dt_now = dt_now.strftime('%Y-%m-%d_%H:%M:%S')+".csv"
from sense_hat import SenseHat
sense = SenseHat()
stop = False
def stopWriting():
	global stop
	stop = True
sense.stick.direction_any = stopWriting

with open(dt_now, 'w') as f:
	writer = csv.writer(f)
	data = getAllInfo.getAllInfo()
	writer.writerow(data.keys())
	writer.writerow(data.values())
	while True:
		try:
			data = getAllInfo.getAllInfo()
			writer.writerow(data.values())
			if stop:
				break
		except KeyboardInterrupt:
			break