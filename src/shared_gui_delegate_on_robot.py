"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Robert Kreft, Conner Ozatalar, Emily Guajardo, Margaret Luffman.
  Winter term, 2018-2019.
"""

class DelagateThatReceives(object):
    # This class creates a delagate for the robot.
    # It helps the robot know how to deal with commands
    # that the laptop sends to the robot.
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot
        self.quit = False

    def forward(self, left_wheel_speed, right_wheel_speed):
        print("got to shared gui")
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))
        print("got to delegate")

    def backward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), -int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        self.robot.drive_system.stop()

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position_entry):
        self.robot.arm_and_claw.move_arm_to_position(arm_position_entry)

    def straight_for_seconds_entry(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches, speed)

    def beep_entry(self, number_of_beeps):
        for k in range(number_of_beeps):
            self.robot.sound_system.beeper()

    def tone_duration_entry(self, tone_duration_entry, tone_frequency_entry):
        self.robot.sound_system.tone_maker(tone_frequency_entry, tone_duration_entry)
        
    #def quit(self):
        #self.quit = True

