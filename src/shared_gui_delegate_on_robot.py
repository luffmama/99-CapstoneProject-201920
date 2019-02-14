"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Robert Kreft, Conner Ozatalar, Emily Guajardo, Margaret Luffman.
  Winter term, 2018-2019.
"""
import time
#import m1_run_this_on_laptop

class DelagateThatReceives(object):
    # This class creates a delagate for the robot.
    # It helps the robot know how to deal with commands
    # that the laptop sends to the robot.
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot
        self.is_quit = False

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
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position_entry))

    def go_straight_for_seconds(self, seconds, speed):
        print("got to robot")
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        print("got to robot")
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def straight_for_inches_using_encoder(self, inches, speed):
        print("got to robot")
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def beep(self, number_of_beeps):
        for k in range(int(number_of_beeps)):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, tone_frequency_entry, tone_duration_entry):
        self.robot.sound_system.tone_maker.play_tone(int(tone_frequency_entry), int(tone_duration_entry))

    def is_quit(self):
        print("quit")
        self.is_quit = True

    # def grab(self):
    #     self.robot.drive_system.go_forward_until_distance_is_less_than(2,100)
    #     if self.robot.drive_system.left_motor.turn_off():
    #         self.raise_arm()

    #alligns the robot with the object/blob before calling LED_cylce to go grab the object
    def LED_cycle_feature10(self,frequency_entry,speed_entry,area_entry,spin_direction_entry):
        #m4 Robert Kreft
        if str(spin_direction_entry) == "cw":
            self.robot.drive_system.spin_clockwise_until_sees_object(int(speed_entry),int(area_entry))
            self.align_the_robot()
            self.LED_cycle(frequency_entry,spin_direction_entry)
        if str(spin_direction_entry) == "ccw":
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed_entry),int(area_entry))
            self.align_the_robot()
            self.LED_cycle(frequency_entry, spin_direction_entry)

    #approaches and grabs the object while blinking leds at a faster pace as it approaches
    def LED_cycle(self,frequency_entry,speed_entry): #person 3, led cycle and go and pick up
        #m4 Robert Kreft
        self.robot.drive_system.go(int(speed_entry),int(speed_entry))
        self.robot.led_system.right_led.turn_on()
        self.robot.led_system.left_led.turn_off()
        k = 1
        while True:
            self.robot.led_system.right_led.turn_off()
            self.robot.led_system.left_led.turn_on()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<=1:
                break
            time.sleep(k * (self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) / int(frequency_entry))
            self.robot.led_system.right_led.turn_on()
            self.robot.led_system.left_led.turn_off()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()<=1:
                break
            time.sleep(k * (self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) / int(frequency_entry))
        self.robot.drive_system.go(-100,-100)
        time.sleep(.1)
        self.robot.drive_system.stop()
        self.robot.arm_and_claw.raise_arm()

    def go_straight_until_intensity_is_less_than(self,intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def go_straight_until_intensity_is_greater_than(self,intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def go_straight_until_color_is(self,color, speed):
        self.robot.drive_system.go_straight_until_color_is(int(color), int(speed))

    def go_straight_until_color_is_not(self,color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(int(color), int(speed))

    def go_forward_until_distance_is_less_than(self,distance, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(distance), int(speed))

    def go_backward_until_distance_is_greater_than(self,distance, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(distance), int(speed))

    def go_to_distance_within(self,delta, distance, speed):
        self.robot.drive_system.go_until_distance_is_within(int(delta), int(distance), int(speed))

    def spin_clockwise_until_object(self,speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_object(self,speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))

    def oscillation_approach(self, high_freq, low_freq, initial_freq_duration):
        t = int(initial_freq_duration)
        dt = int(initial_freq_duration) / self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        dx = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / int(initial_freq_duration)
        while True:

            self.robot.sound_system.tone_maker.play_tone(high_freq, t).wait()
            self.robot.drive_system.go_straight_for_inches_using_time(1, 100)
            x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            t = t - dt

            self.robot.sound_system.tone_maker.play_tone(low_freq, t).wait()
            self.robot.drive_system.go_straight_for_inches_using_time(1, 100)
            x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            t = t - dt

            if x <= 1:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break

    # next 2 are features 9 and 10 for Conner Ozatalar
    def pick_up_object_while_beeping(self, initial_beep_speed_entry, beep_acceleration_entry):
        self.robot.drive_system.go(75, 75)
        while True:
            print(self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 3:
                self.robot.drive_system.stop()
                break
            self.robot.sound_system.beeper.beep().wait()
            time.sleep(.3 + 1/int(initial_beep_speed_entry) - (int(beep_acceleration_entry)/100)/((int(initial_beep_speed_entry)) * self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()))
        self.robot.arm_and_claw.raise_arm()

    def m3_feature_10(self, initial_beep_speed_entry, beep_acceleration_entry,  direction_entry, spin_speed_entry):
        if str(direction_entry) is 'cw':
            self.robot.drive_system.spin_clockwise_until_sees_object(int(spin_speed_entry), 50)
        if str(direction_entry) is 'ccw':
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(spin_speed_entry), 50)
        blob = self.robot.sensor_system.camera.get_biggest_blob()
        while True:
            if blob.center.x >= 170:
                self.robot.drive_system.go(-50, 50)
            if blob.center.x <= 150:
                self.robot.drive_system.go(50, -50)
            if 150 <= blob.center.x <= 170:
                break
        DelagateThatReceives.pick_up_object_while_beeping(self, initial_beep_speed_entry, beep_acceleration_entry)

    def display_camera_data(self):
        x, y, w, h = self.robot.drive_system.display_camera_data()
        print("The center is", x, y)
        print("The width is", w)
        print("THe height is", h)

# This makes the robot play tones at increasing frequency as it gets closer to an object (written by Emily)
    def tone_as_closer(self, initial_frequency, delta_frequency):
        self.robot.drive_system.go(100, 100)
        k = 0
        while True:
            self.robot.sound_system.tone_maker.play_tone(initial_frequency + (delta_frequency * k), 500)
            k += 1
            if self.robot.sensor_system.ir_proximity_sensor.get_distance() <= 3:
                self.robot.drive_system.stop()
                break
        self.robot.arm_and_claw.raise_arm()

    # This method gets the robot to face objects (written by Emily)
    def m2_face_object(self, speed, direction):
        while True:
            if direction == 0:
                if self.robot.sensor_system.camera.get_biggest_blob().center.x < 160:
                    self.robot.drive_system.left_motor.turn_on(-speed)
                    self.robot.drive_system.right_motor.turn_on(speed)
            if direction == 1:
                if self.robot.sensor_system.camera.get_biggest_blob().center.x > 160:
                    self.robot.drive_system.left_motor.turn_on(speed)
                    self.robot.drive_system.right_motor.turn_on(-speed)
            if self.robot.sensor_system.camera.get_biggest_blob().center.x == 160:
                self.robot.drive_system.left_motor.turn_off()
                self.robot.drive_system.right_motor.turn_off()
                break

# This method gets the robot to pick up an object (written by Emily)
    def m2_pick_up_object(self, speed):
        self.robot.drive_system.go(speed, speed)
        if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
            self.robot.drive_system.stop()
            self.robot.arm_and_claw.raise_arm()

# F9 Margaret Luffman

    def m1_f9(self,high_freq,low_freq,initial_freq_duration):
        t = int(initial_freq_duration)
        dt = int(initial_freq_duration) / self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        while True:

            self.robot.sound_system.tone_maker.play_tone(high_freq, x).wait(t)
            self.robot.drive_system.go_straight_for_inches_using_time(1, 100)
            x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            t = t - dt

            self.robot.sound_system.tone_maker.play_tone(low_freq, x).wait(t)
            self.robot.drive_system.go_straight_for_inches_using_time(1, 100)
            x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            t = t - dt

            if x <= 2:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break

# F 10 Margaret Luffman

    def turn_and_go(self, c_or_cc_entry, high_freq, low_freq, initial_freq_duration):
        if str(c_or_cc_entry) == "c":
            self.robot.drive_system.spin_clockwise_until_sees_object(50, 50)
            self.align_the_robot()
            self.m1_f9(int(high_freq), int(low_freq), int(initial_freq_duration))
        if str(c_or_cc_entry) == "cc":
            self.robot.drive_system.spin_counterclockwise_until_sees_object(50, 50)
            self.align_the_robot()
            self.m1_f9(int(high_freq), int(low_freq), int(initial_freq_duration))

    def align_the_robot(self):

        blob = self.robot.sensor_system.camera.get_biggest_blob()
        while True:
            if blob.center.x < 150:
                self.left(50,-50).wait(0.05)
                self.robot.drive_system.stop()
            if blob.center.x > 170:
                self.right(-50,50).wait(0.05)
                self.robot.drive_system.stop()
            if blob.center.x >= 150 and blob.center.x <= 170:
                break