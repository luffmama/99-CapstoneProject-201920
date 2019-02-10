"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Conner Ozatalar.
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
    # real_thing()
    test_play_tone_sequence()
    test_beeper()

def test_play_tone_sequence():
    robot = rosebot.RoseBot()
    d = 587.33
    c = 523.251
    bf = 466.164
    f = 698.456
    mary_had_a_little_lamb = [(d, 600, 10), (c, 600, 10), (bf, 600, 10), (c, 600, 10), (d, 600, 10), (d, 600, 10), (d, 600, 10),
                              (c, 600, 10), (c, 600, 10), (c, 600, 10), (d, 600, 10), (f, 600, 10), (f, 600, 600),
                              (d, 600, 10), (c, 600, 10), (bf, 600, 10), (c, 600, 10), (d, 600, 10), (d, 600, 10), (d, 600, 10),
                              (d, 600, 10), (c, 600, 10), (c, 600, 10), (d, 600, 10), (c, 600, 10), (bf, 1200, 10)]
    robot.sound_system.tone_maker.play_tone_sequence(mary_had_a_little_lamb)

def test_beeper():
    time.sleep(1)
    robot = rosebot.RoseBot()
    for k in range(5):
        robot.sound_system.beeper.beep()
        time.sleep(.3+.1*k)

def real_thing():
    bot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelagateThatReceives(bot)
    mqtt_reciever = com.MqttClient(delegate_that_receives)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)
        # if delegate_that_receives.quit():
            # break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()