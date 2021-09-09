import csv
import numpy as np

file_path = input("csv path")
with open(file_path,"r") as f:
	csvreader = csv.reader(f)
	data = list(csvreader)
header = data[0]
data = np.vectorize(np.float64)(data[1:])
print(header)
print(data.shape)

#重力加速度
G = 9.80665
gs_delta = 0.974966009
acx, acy, acz = [header.index('accel_row_x'),header.index('accel_row_y'),header.index('accel_row_z')]
accel2x = data[:,acx:acx+1]**2
accel2y = data[:,acy:acy+1]**2
accel2z = data[:,acz:acz+1]**2
accel2 = accel2x + accel2y + accel2z
print(accel2.shape,accel2x.shape,accel2y.shape,accel2z.shape)
accel_raw_norm = np.sqrt(accel2)
print(accel_raw_norm.shape)
# print(accel_raw_norm[0])
# print(accel_raw_norm[1])
# print(accel_raw_norm[2])
accel_norm = (accel_raw_norm - gs_delta)*G
print(accel_raw_norm.shape)
print(accel_norm.shape)


#積分準備
velocity = np.zeros(accel_norm.shape,dtype=np.float64)
displacement = np.zeros(accel_norm.shape,dtype=np.float64)
ht = header.index("time")
t = data[:,ht:ht+1]
accel_time = np.concatenate([accel_norm,t],axis=1)
print(accel_time.shape)

#加速度と速度で積分⇒変位
x = np.array([0],dtype=np.float64)
v = np.array([0],dtype=np.float64) #current
last_time = accel_time[0][1]
for i, a_t in enumerate(accel_time):
	dt = a_t[1] - last_time
	v[0] += a_t[0] * dt
	velocity[i][0] = v[0]
	x[0] += v[0] * dt
	displacement[i][0] = x[0]

# a_t_v_d = np.concatenate([accel_time,velocity,displacement],axis=1)
# print(a_t_v_d[:10])

header = header + ["velocity", "displacement"]
data = np.concatenate([data,velocity,displacement],axis=1)
print(data.shape)
with open(file_path,"w") as f:
	writer = csv.writer(f, lineterminator="\n")
	writer.writerow(header)
	for row in data:
		writer.writerow(row)