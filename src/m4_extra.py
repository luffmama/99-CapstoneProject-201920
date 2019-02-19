#robert kreft's code

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot
import math

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

#PID Control Proportional, Integral, Differential Control line following
# def PID_cw_control(robot,slider_constant,i_value,kpr_value,kpl_value):
#     base_speed, kpr, kpl, kir, kil, previous_error, summed_error = 100, kpr_value, -kpl_value, 0, 0, 0, 0
#     kdr, kdl = 2 * math.sqrt(abs(kpr)), -2 * math.sqrt(abs(kpl))
#     while True:
#         error, change_in_error, summed_error, previous_error = \
#             error_accumulator(robot,i_value, previous_error, summed_error)
#         robot.drive_system.go(
#             max(min(base_speed * slider_constant + (
#                     kpl * error + kil * summed_error + kdl * change_in_error), 100), 10),
#             max(min(base_speed * slider_constant + (
#                     kpr * error + kir * summed_error + kdr * change_in_error), 100), 10))
#         if robot.sensor_system.touch_sensor.is_pressed():
#             robot.drive_system.stop()
#             break

#PID Control Proportional, Integral, Differential Control line following
def PID_ccw_control(robot,slider_constant,i_value,kpr_value,kpl_value,kir_value,kil_value,kdr_value,kdl_value):
    print("Got to Command")
    # base_speed, kpr, kpl, kir, kil, previous_error, summed_error = 100, 1, -1, 0, 0,  0, 0
    # kdr, kdl = 2*math.sqrt(kpr), -2*math.sqrt(kpr)
    # while True:
    #     error, change_in_error, summed_error, previous_error = error_accumulator(robot,previous_error,summed_error)
    #     robot.drive_system.go(max(min(base_speed * slider_constant + (kpl * error + kil * summed_error + kdl * change_in_error),100),10),
    #                           max(min(base_speed * slider_constant + (
    #                                       kpr * error + kir * summed_error + kdr * change_in_error), 100), 10))
    #     if robot.sensor_system.touch_sensor.is_pressed():
    #         robot.drive_system.stop()
    #         break

    base_speed, kpr, kpl, kir, kil, previous_error, summed_error = 100, -kpr_value, kpl_value, -kir_value, kil_value, 0, 0
    kdr, kdl = -kdr_value, kdl_value#-2 * math.sqrt(abs(kpr)), 2 * math.sqrt(abs(kpl))
    while True:
        error, change_in_error, summed_error, previous_error = \
            error_accumulator(robot,i_value, previous_error, summed_error)
        robot.drive_system.go(
            max(min(base_speed * slider_constant + (
                    kpl * error + kil * summed_error + kdl * change_in_error), 100),10),
            max(min(base_speed * slider_constant + (
                    kpr * error + kir * summed_error + kdr * change_in_error), 100), 10))
        if robot.sensor_system.touch_sensor.is_pressed():
            robot.drive_system.stop()
            break
        if robot.sensor_system.color_sensor.get_color()==5:
            robot.drive_system.stop()
            got_to_the_end(robot)
            break

#has the robot send a message back to the laptop with the color stoppped on
def got_to_the_end(robot):
    mqtt_client = com.MqttClient()
    mqtt_client.connect("baggins", "bilbo")
    time.sleep(1)
    mqtt_client.send_message("say_it", [robot.sensor_system.color_sensor.get_color()])

#does error calculations for PID line following
def error_accumulator(robot,i_value,previous_error,summed_error):
    # perfect = 4
    # error = abs(perfect - robot.sensor_system.color_sensor.get_reflected_light_intensity())
    # change_in_error = abs(error - previous_error)
    # summed_error = summed_error + error
    # previous_error = error
    # return error, change_in_error, summed_error, previous_error

    perfect=i_value
    error=(perfect-robot.sensor_system.color_sensor.get_reflected_light_intensity())
    change_in_error=(error-previous_error)
    summed_error=summed_error+error
    previous_error=error
    return error, change_in_error, summed_error, previous_error

# #bang bang method of line following circle in the clockwise direction
# def bang_bang_circ_line_follow_cw(robot,speed,pivot_speed):
#     count=0
#     robot.drive_system.go(speed,speed)
#     while True:
#         if robot.sensor_system.touch_sensor.is_pressed():
#             robot.drive_system.stop()
#             break
#         if robot.sensor_system.color_sensor.get_reflected_light_intensity()>10: #if robot gets off the line
#             robot.drive_system.go(pivot_speed,-pivot_speed)
#             while True:
#                 if robot.sensor_system.touch_sensor.is_pressed():
#                     robot.drive_system.stop()
#                     break
#                 if robot.sensor_system.color_sensor.get_reflected_light_intensity() < 10:
#                     robot.drive_system.go(speed,speed)
#                     break
#
# # bang bang method of line following circle in the counter clockwise direction
# def bang_bang_circ_line_follow_ccw(robot,speed,pivot_speed):
#     count=0
#     robot.drive_system.go(speed,speed)
#     while True:
#         if robot.sensor_system.touch_sensor.is_pressed():
#             robot.drive_system.stop()
#             break
#         if robot.sensor_system.color_sensor.get_reflected_light_intensity()>10: #if robot gets off the line
#             robot.drive_system.go(-pivot_speed,pivot_speed)
#             while True:
#                 if robot.sensor_system.touch_sensor.is_pressed():
#                     robot.drive_system.stop()
#                     break
#                 if robot.sensor_system.color_sensor.get_reflected_light_intensity() < 10:
#                     robot.drive_system.go(speed,speed)
#                     break

#reads off values for intensity
def print_intensity(robot):
    while True:
        print("intensity:" ,robot.sensor_system.color_sensor.get_reflected_light_intensity(), "color:" , robot.sensor_system.color_sensor.get_color())
        time.sleep(.25)
        if robot.sensor_system.touch_sensor.is_pressed():
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