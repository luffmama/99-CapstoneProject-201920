"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Margaret Luffman
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot
#import m3_run_this_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_arm()
    # run_test_drive()
    real_thing()
    # m3_run_this_on_robot.test_beeper()
    # run_test_proximity_sensor()

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()
    robot.arm_and_claw.lower_arm()
    robot.arm_and_claw.move_arm_to_position(10*360)
    robot.arm_and_claw.lower_arm()
    robot.arm_and_claw.calibrate_arm()

def run_test_drive():
    robot = rosebot.RoseBot()
    robot.drive_system.go(100,100)
    time.sleep(3)
    robot.drive_system.stop()
    time.sleep(5)
    robot.drive_system.go_straight_for_seconds(3,100)
    time.sleep(5)
    robot.drive_system.go_straight_for_inches_using_time(24,100)
    time.sleep(5)
    robot.drive_system.go_straight_for_inches_using_encoder(24,100)

def run_test_proximity_sensor():
    robot = rosebot.RoseBot()
    robot.drive_system.go_backward_until_distance_is_greater_than(24,100)
    time.sleep(3)
    robot.drive_system.go_forward_until_distance_is_less_than(12,100)
    while True:
        print(robot.sensor_system.ir_proximity_sensor.get_distance())
        time.sleep(0.5)

    time.sleep(3)
    robot.drive_system.go_until_distance_is_within(6,100)

def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelagateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        #if delegate_that_receives.quit() == True:
            #break



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()