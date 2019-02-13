"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Emily Guajardo.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    # run_test_arm()
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(10*360)
    robot.arm_and_claw.lower_arm()

def running_gui():
    robot = rosebot.RoseBot()
    delagate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delagate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)

def spin_until_object():
    robot = rosebot.RoseBot()
    while robot.sensor_system.camera.get_biggest_blob() is None:



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()