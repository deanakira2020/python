#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
irSensor = InfraredSensor (Port.S2)
motor = Motor
touchsensor = TouchSensor (Port.S3)


# Write your program here.


# Initialize two motors with default settings on Port B and Port C.
left_motor = Motor(Port.B) 
right_motor = Motor(Port.C)
# The wheel diameter of the Robot Educator is 56 millimeters. # The distance between wheels (axle_track) is 114 millimeters.
wheel_diameter = 43.2
axle_track = 145
# Create a DriveBase object. The wheel_diameter and axle_track values are needed to move robot correct speed/distance when you give drive commands.
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)


 # This drives at 100 mm/sec straight


import random
a = random.randint(-90,90)


while True:
    robot.drive(200,0)

    while irSensor.distance() < 50:
        a = random.randint(0,100)
        b = random.randint(45,180)
        c = random.randint(-180,-45)
        robot.straight(-50)
        if a <= 50: 
            robot.turn(b)
        else:
            robot.turn(c)

        

    while touchsensor.pressed():
        robot.straight(-50)
        a = random.randint(0,100)
        b = random.randint(45,180)
        c = random.randint(-180,-45)
        if a <= 50 :
            robot.turn(b)
            sound.beep()
        else:
            robot.turn(c)
            sound.beep
        
        
