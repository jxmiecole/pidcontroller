import random
import time

#PID Gains
kp = 0.5
ki = 0.1
kd = 0.3

setpoint = 25
integral_total = 0
previous_error = 0
dt = 5

#for a moving car
speed1 = random.randint(20, 22)
speed2 = random.randint(speed1, 23)
speed3 = random.randint(speed2, 24)
speed4 = random.randint(speed3, 25)
speed5 = random.randint(speed4, 26)
speed6 = random.randint(speed5, 27)
speed7 = random.randint(speed6, 28)
speed8 = random.randint(speed7, 29)
speed9 = random.randint(speed8, 30)
speed10 = random.randint(speed9, 31)
processvalue = [speed1, speed2, speed3, speed4, speed5, speed6, speed7, speed8, speed9, speed10]#for 10 seconds

i=0
def proportional_t(processvalue):
	global error
	global proportional
	error = setpoint - processvalue
	if kp == 0:
		proportional = float(error)
	else:
		proportional = float(kp * error)
	print(f'Proportional: {proportional}')

def integral_t():
	global integral
	global old_integral
	if ki == 0:
		integral_total = error * dt
	else:
		integral_total = ki * (error * dt)
	if i==0:
		integral = integral_total
	else:
		integral = old_integral + integral_total
	old_integral = integral_total
	print(f'Integral: {integral}')

def derivative_t(previous_error):
	global derivative
	if kd == 0:
		derivative = (previous_error - error) / dt
	else:
		derivative = kd * (previous_error - error) / dt
	print(f'Derivative: {derivative}')

while i < 10:
	time.sleep(dt)
	print(f'Current Speed: {processvalue[i]}')
	proportional_t(processvalue[i])
	integral_t()
	derivative_t(previous_error)
	previous_error = error
	output = float(proportional + integral + derivative)
	print(f'PID Controller (Output): {output}')
	speed2 = random.randint(speed1, 22)
	speed2_t = speed2 + output
	speed3 = random.randint(speed2, 23)
	speed3_t = speed3 + output
	speed4 = random.randint(speed3, 25)
	speed4_t = speed4 + output
	speed5 = random.randint(speed4, 26)
	speed5_t = speed5 + output
	speed6 = random.randint(speed5, 27)
	speed6_t = speed6 + output
	speed7 = random.randint(speed6, 28)
	speed7_t = speed7 + output
	speed8 = random.randint(speed7, 29)
	speed8_t = speed8 + output
	speed9 = random.randint(speed8, 30)
	speed9_t = speed9 + output
	speed10 = random.randint(speed9, 31)
	speed10_t = speed10 + output
	processvalue = [speed1, speed2_t, speed3_t, speed4_t, speed5_t, speed6_t, speed7_t, speed8_t, speed9_t, speed10_t]#for 10 seconds
	i+=1