"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Margaret Luffman
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_arm()
    run_test_drive()

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

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()