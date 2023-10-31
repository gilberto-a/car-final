import serial
import time
import pynput
from pynput.keyboard import Key, Controller

# ax_offset = .14208
# ay_offset = .02292
# az_offset = 1.98639
# gx_offset = 498.5378
# gy_offset = .78230
# gz_offset = 275.1359
ax_offset = 0
ay_offset = 0
az_offset = 0
gx_offset = 0
gy_offset = 0
gz_offset = 0
flag = 0
forward = 0
backward = 0
keyboard = Controller()

def process_data(data):
    parts = data.split('; ')
    if len(parts) == 2:
        accel_part, gyro_part = parts[0], parts[1]

        # Split the accelerometer and gyroscope data into separate values
        accel_values = [int(val) / 1000 for val in accel_part.split(', ')]
        gyro_values = [int(val) / 1000 for val in gyro_part.split(', ')]

        # Store the values in separate variables
        accel_x, accel_y, accel_z = accel_values
        
        # Print the values (or perform further processing as needed)
        print(f"Accelerometer: X={accel_x},      Y={accel_y},       Z={accel_z} ")
        # print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

        return(accel_x, accel_y, accel_z) 

# def x_movement(value):
#     global flag 
#     global forward 
#     global backward 

#     if flag == 0 and value > 0.2 :
#         forward = 1
#         flag = 1 
#         keyboard.press('w')

#     elif (.05 < value < .07) and (forward == 1):
#         flag = 0
#         forward = 0
#         keyboard.release('w')

#     elif flag == 0 and value < -0.1 :
#         backward = 1
#         flag = 1
#         keyboard.press('s')
    
#     elif (.05 < value < .07) and (backward == 1) :
#         flag = 0
#         backward = 0
#         keyboard.release('s')


ser = serial.Serial(
    port='COM3',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print("Connected to: " + ser.portstr)

while True:
    data = ser.readline().decode('utf-8').strip()  # Assuming the data is sent as text
    if data:
        final_x, final_y, final_z = process_data(data)
        # x_movement(final_x)
        if flag == 0 and final_x > 0.2 :
            forward = 1
            flag = 1
            while flag == 1:
                keyboard.press('w')
                time.sleep(1)
                new_x, new_y, new_z = process_data(data)ww
                if (.05 < new_x < .07) and (forward == 1):
                    flag = 0
                    forward = 0
                    keyboard.release('w')

        elif flag == 0 and final_x < -0.1 :
            backward = 1
            flag = 1
            keyboard.press('s')
        
        elif (.05 < final_x < .07) and (backward == 1) :
            flag = 0
            backward = 0
            keyboard.release('s')



    

        


        




ser.close()
