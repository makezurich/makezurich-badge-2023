# print("Hello World")

# import time
# import board
# import pwmio
# import digitalio
# import analogio
# import busio
# import countio
# from adafruit_motor import servo
# import adafruit_mpr121

# from grove_i2c_relay import Relay
# import grove_ultrasonic_ranger

# # Servo on pin D22
# pwm = pwmio.PWMOut(board.D22, duty_cycle=2 ** 15, frequency=50)
# servo1 = servo.Servo(pwm)

# # Digital output on pin D13 (led)
# led = digitalio.DigitalInOut(board.D13)
# led.direction = digitalio.Direction.OUTPUT

# # Button on pin D2
# button1 = digitalio.DigitalInOut(board.D2)
# button1.direction = digitalio.Direction.INPUT
# button1.pull = digitalio.Pull.UP

# # Pir on pin D4 (edge counter)
# pir = countio.Counter(board.D4, edge=countio.Edge.RISE_AND_FALL)

# # Pot on pin A1
# pot1 = analogio.AnalogIn(board.A1)

# # Lightssensor on pin A0
# light_sensor = analogio.AnalogIn(board.A0)

# # Ultrasonic ranger on pin D3
# sonar = grove_ultrasonic_ranger.GroveUltrasonicRanger(sig_pin=board.D3)


# # MPR121 capsense on I2C
# i2c = busio.I2C(board.SCL, board.SDA)
# mpr121 = adafruit_mpr121.MPR121(i2c,address=91)

# # Relay on I2C
# relay = Relay(i2c,
#         device_address=0x11,
#         num_relays=4,
#         debug_action=True)


# def servo_test():
#     for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
#         servo1.angle = angle
#         time.sleep(0.05)
#     for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
#         servo1.angle = angle
#         time.sleep(0.05)

# def relay_test(channels):
#     for i in range(channels):
#         relay.channel_on(i+1)
#         time.sleep(.5)
#         relay.channel_off(i+1)

# relay_test(4)


# while True:
#     if pir.count > 0:
#         relay.channel_on(1)
#     if pir.count > 1:
#         relay.channel_off(1)
#         pir.reset()

#     time.sleep(.1)


import board
import busio
import digitalio
import time
import supervisor
#Set UART Pin
uart = busio.UART(board.TX, board.RX, baudrate=9600)
get_input = True
message_started = False
message_print = []
allstring = ""
printshow = False
while True:
    if supervisor.runtime.serial_bytes_available:
        allstring=""
        userinput = input().strip() #input command
        b = bytes(userinput, 'utf-8')
        uart.write(b)
        continue
    byte_read = uart.readline()# read one line
    if byte_read != None:
        allstring += byte_read.decode()
        printshow = True
    else:
        if printshow == True:
            if allstring != "":
                print(allstring)
            allstring=""
            printshow ==False
