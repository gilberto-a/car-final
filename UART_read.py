import serial
import time
import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MController

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
mouse = MController()

def process_data(data):
    # Split the data into accelerometer and gyroscope parts
    parts = data.split('; ')
    if len(parts) == 2:
        accel_part, gyro_part = parts[0], parts[1]
        # Split the accelerometer and gyroscope data into separate values
        accel_values = [int(val) / 1000 for val in accel_part.split(', ')]
        gyro_values = [int(val) / 1000 for val in gyro_part.split(', ')]
        # Store the values in separate variables
        accel_x, accel_y, accel_z = accel_values
        gyro_x, gyro_y, gyro_z = gyro_values
        # accel_x = accel_x -ax_offset 
        # accel_y = accel_y -ay_offset 
        # accel_z = accel_z -az_offset
        # gyro_x = gyro_x - gx_offset
        # gyro_y = gyro_y - gy_offset
        # gyro_z = gyro_z - gz_offset

        
        # Print the values (or perform further processing as needed)
        # print(f"Accelerometer: X={accel_x},      Y={accel_y},       Z={accel_z} ")
        print(f"Gyroscope: X={gyro_x}, Y={gyro_y}, Z={gyro_z}")

        return(accel_x, accel_y, accel_z) 

def x_movement(value):
    
    global flag 
    global forward 
    global backward 

    if flag == 0 and value > 0.1 :
        forward = 1
        flag = 1 
        keyboard.press('w')
    elif (-.01 < value < .01) and (forward == 1):
        flag = 0
        forward = 0
        keyboard.release('w')
    elif  flag == 0 and value < -0.1 :
        backward = 1
        flag = 1
        keyboard.press('s')
    elif (-.01 < value < .01) and (backward == 1) :
        flag = 0
        backward = 0
        keyboard.release('s')

def z_movement(value):
    if value > 1.2 :
        mouse.click(Button.right, 1)

    
    





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
        x_movement(final_y)
        z_movement(final_z)
        


        




ser.close()
