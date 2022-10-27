# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:21:33 2022

@author: aquar
"""
#Code for arduino/rasberry pi  serial code sending  

import serial as s #importing serial function 
import time   #import time functions to have delays in commands that the pi sends

if __name__ == '_main_' : 
    ser = s.Serial('/dev/ttyACM0', 9600, timeout = 1) #Check if adruino is ACM1 or ACM0 by using powershell of Raspberry Pi 
    ser.flush()  
     
    def sendInt(servo_angle):
        send_string=str(servo_angle)
        send_string += "\n"
        ser.write(send_string.encode('utf-8'))
        ser.flush()


        sendInt(60) #send 60 deg to servo
        time.sleep(2.5)
        sendInt(0) #send 0 to servo to stop the DCmotor and set servo to 90 deg 
        
    while True: 
        if ser.in_waiting > 0: 
            line = ser.readline().decode('utf-8').rstrip() 
            print(line) 
            if float(line) <= 60: 
                ser.write(b"myservo.write(pos)\n")   
                
                