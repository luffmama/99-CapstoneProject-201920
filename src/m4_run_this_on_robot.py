"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Robert Kreft.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()

def real_thing():

    robot = rosebot.RoseBot()
    delagate_that_recieves=shared_gui_delegate_on_robot.DelagateThatReceives(robot)
    mqtt_reciever=com.MqttClient(delagate_that_recieves)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(.01)
        if delagate_that_recieves.is_quit:
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()