#robert kreft's code

import rosebot as rb
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

# #bang bang method of line following
# def bang_bang_straight_line_follow(self,speed):
#     intensity=10
#     self.robot.drive_system.go(speed,speed)
#     #assume on right side of line when gets off
#     while True: #first loop
#         if self.robot.sensor_system.color_sensor.get_reflected_light_intensity()>intensity: #if robot leaves black line:
#             self.robot.drive_system.go(.75*speed,speed) #turns slightly to the left
#             time.sleep(.25) #after some time
#             self.robot.drive_system.go(speed,speed) #goes straight
#             time_set=time.clock() #timer check
#             while True: #second loop
#                 if self.robot.sensor_system.color_sensor.get_reflected_light_intensity()<intensity: #if it gets back on the black line
#                     self.robot.drive_system.go(speed,-speed) #spins right
#                     time.sleep(.1)
#                     break #break second loop
#                 if time_set-time.time()>=1: #if time exceeds 1 second, must be on left side of line
#                     self.robot.drive_system(speed,.75*speed) #turn right
#                     time.sleep(.5)
#                     self.robot.drive_system.go(speed,speed)
#                     while True: #third loop
#                         if self.robot.sensor_system.color_sensor.get_reflected_light_intensity()<intensity: #if it gets back on the black line
#                             self.robot.drive_system(-speed,speed) #spins left
#                             time.sleep(.1)
#                             break #break third loop
#                     break #break second loop
#         if self.robot.sensor_system.touch_sensor.is_pressed():
#             self.robot.drive_system.stop()
#             break #break first loop
#
#counts number of times an object is seen by the camera
def count_number_of_time_object_is_seen(robot,count):
    #if something is seen
        #count=count+1
    return count

#bang bang method of line following circle in the clockwise direction
def bang_bang_circ_line_follow_cw(robot,speed):
    count=0
    robot.drive_system.go(speed,speed)
    while True:
        if robot.sensor_system.touch_sensor.is_pressed():
            robot.drive_system.stop()
            break
        if robot.sensor_system.color_sensor.get_reflected_light_intensity()>10: #if robot gets off the line
            robot.drive_system.go(speed,-speed)
            while True:
                if robot.sensor_system.touch_sensor.is_pressed():
                    robot.drive_system.stop()
                    break
                if robot.sensor_system.color_sensor.get_reflected_light_intensity() < 10:
                    robot.drive_system.go(speed,speed)
                    break

# bang bang method of line following circle in the counter clockwise direction
def bang_bang_circ_line_follow_ccw(robot,speed):
    count=0
    robot.drive_system.go(speed,speed)
    while True:
        if robot.sensor_system.touch_sensor.is_pressed():
            robot.drive_system.stop()
            break
        if robot.sensor_system.color_sensor.get_reflected_light_intensity()>10: #if robot gets off the line
            robot.drive_system.go(-speed,speed)
            while True:
                if robot.sensor_system.touch_sensor.is_pressed():
                    robot.drive_system.stop()
                    break
                if robot.sensor_system.color_sensor.get_reflected_light_intensity() < 10:
                    robot.drive_system.go(speed,speed)
                    break

# def bang_bang_straight_line_follow_sor(self,speed):
#     self.robot.drive_system.go(speed,speed)
#     while True:
#         if self.robot.sensor_system.touch_sensor.is_pressed():
#             self.robot.drive_system.stop()
#             break
#         self.bang_bang(speed)
#
# def bang_bang(self,speed):
#     if self.robot.sensor_system.color_sensor.get_reflected_light_intensity() > 10:  # if robot gets off the line
#         self.robot.drive_system.go(speed, -speed)
#         while True:
#             if self.robot.sensor_system.touch_sensor.is_pressed():
#                 self.robot.drive_system.stop()
#                 break
#             if self.robot.sensor_system.color_sensor.get_reflected_light_intensity() < 10:
#                 self.robot.drive_system.go(speed, speed)
#                 break