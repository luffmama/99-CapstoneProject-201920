"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Robert Kreft, Conner Ozatalar, Emily Guajardo, Margaret Luffman.
  Winter term, 2018-2019.
"""
import time
import m3_extra
import m4_extra

class DelagateThatReceives(object):
    # This class creates a delagate for the robot.
    # It helps the robot know how to deal with commands
    # that the laptop sends to the robot.
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot"""
        self.robot = robot
        self.is_quit = False

    #robert kreft m4_extra

    def cw_line_follow(self,speed,pivot_speed):
        m4_extra.bang_bang_circ_line_follow_cw(self.robot,int(speed),int(pivot_speed))

    def ccw_line_follow(self,speed,pivot_speed):
        m4_extra.bang_bang_circ_line_follow_ccw(self.robot,int(speed),int(pivot_speed))

    def read_intensity(self):
        while True:
            m4_extra.print_intensity(self.robot)
            time.sleep(.25)

    #robot m4_extra ^^^.


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

    def now_quit(self):
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
            self.LED_cycle(frequency_entry,speed_entry)
        if str(spin_direction_entry) == "ccw":
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed_entry),int(area_entry))
            self.align_the_robot()
            self.LED_cycle(frequency_entry, speed_entry)

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
            print('turning cw')
            self.robot.drive_system.spin_clockwise_until_sees_object(int(spin_speed_entry), 50)
        if str(direction_entry) is 'ccw':
            print('turning ccw')
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(spin_speed_entry), 50)
        while True:
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            print(blob)
            if blob.center.x >= 170:
                self.robot.drive_system.go(-50, 50)
            elif blob.center.x <= 150:
                self.robot.drive_system.go(50, -50)
            else:
                self.robot.drive_system.stop()
                break
        self.pick_up_object_while_beeping(initial_beep_speed_entry, beep_acceleration_entry)

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
        print('*')
        while True:
            print(direction)
            if direction == 0:
                self.robot.drive_system.left_motor.turn_on(-int(speed))
                self.robot.drive_system.right_motor.turn_on(int(speed))
                if self.robot.sensor_system.camera.get_biggest_blob().center.x < 150:
                    self.robot.drive_system.left_motor.turn_off()
                    self.robot.drive_system.right_motor.turn_off()
                    break
            else:
                self.robot.drive_system.left_motor.turn_on(int(speed))
                self.robot.drive_system.right_motor.turn_on(-int(speed))
                if self.robot.sensor_system.camera.get_biggest_blob().center.x > 170:
                    self.robot.drive_system.left_motor.turn_off()
                    self.robot.drive_system.right_motor.turn_off()
                    break


# This method gets the robot to pick up an object (written by Emily)
    def m2_pick_up_object(self, speed):
        print('**')
        self.robot.drive_system.go(int(speed), int(speed))
        while True:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                break

# F9 Margaret Luffman

    def m1_f9(self,high_freq,low_freq,initial_freq_duration):
        t = int(initial_freq_duration)
        dt = int(initial_freq_duration) / self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        self.robot.drive_system.go(75,75)
        while True:

            self.robot.sound_system.tone_maker.play_tone(high_freq, t)
            x = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            t = t - dt

            self.robot.sound_system.tone_maker.play_tone(low_freq, t)
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

        while True:
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            print(int(blob.center.x))
            if blob.center.x < 150:
                self.right(50,50)
            elif blob.center.x > 170:
                self.left(50,50)
            else:
                self.robot.drive_system.stop()
                break


# Margaret Luffman functions for spint 3

    def m1_meeting_criminal(self, size, distance, dangsize, box_entry, dangdist):
        # Meets criminal and either decides whether or not it is dangerous or runs away if it is a coward
        if self.m1_ID_the_criminal(size, distance) is True and self.m1_is_coward(box_entry) is True:
            self.m1_run_away()
        elif self.m1_ID_the_criminal(size, distance) is False:
            self.speak("No criminals in sight")
        else:
            self.m1_is_dangerous(dangsize, dangdist)

    def m1_track_the_criminal(self, time_of_tracking):
        # Uses bang-bang line following to track a criminal's trail
        original = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        t = time.time()
        while True:
            elapsed_time = time.time() - t
            current = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            if abs(original - current) <= 5:
                self.robot.drive_system.go(75, 75)
            elif abs(original - current) > 5:
                self.right(75, 75)
            if elapsed_time >= int(time_of_tracking):
                self.robot.drive_system.stop()
                break

    def m1_ID_the_criminal(self, size, distance):
        # figures out if something is a criminal or not
        blob = self.robot.sensor_system.camera.get_biggest_blob()
        if blob.get_area() >= int(size) or self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= int(
                distance):
            self.speak("criminal detected")
            return True
        else:
            return False

    def m1_is_dangerous(self, dangsize, dangdist):
        blob = self.robot.sensor_system.camera.get_biggest_blob()
        if blob.get_area() >= int(
                dangsize) or self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= int(dangdist):
            self.speak("The criminal is dangerous")
            print("The criminal is dangerous, and is of size", blob.get_area(),
                  "while being", self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches(), "inches away")
            self.speak("This is robocop calling for backup")
        else:
            self.speak("The criminal is not dangerous")
            self.m1_chase_the_criminal()

    def m1_chase_the_criminal(self):
        self.align_the_robot()
        self.pick_up_object_while_beeping(3, 1)

    def speak(self, word):
        self.robot.sound_system.speech_maker.speak(str(word))

    def m1_is_coward(self, box_entry):
        if str(box_entry) == "coward":
            return True
        else:
            return False

    def m1_run_away(self):
        self.speak("run away")
        self.backward(100, 100)

    # End Margaret Luffman sprint 3 functions

    # Conner Ozatalar(m3) sprint 3
    def m3_marlin_deep_sea(self, check_box_dory_mode, dory_mode_excitement_entry):
        print('shared delegate m3_marlin', check_box_dory_mode, int(dory_mode_excitement_entry))
        m3_extra.m3_marlin_deep_sea(self.robot, check_box_dory_mode, int(dory_mode_excitement_entry))

    def m3_nemo_deep_sea(self, check_box_dory_mode, dory_mode_excitement_entry):
        print('shared delegate m3_nemo', check_box_dory_mode, int(dory_mode_excitement_entry))
        m3_extra.m3_nemo_deep_sea(self.robot, check_box_dory_mode, int(dory_mode_excitement_entry))

    def m3_find_nemo(self, find_nemo_speed_entry, find_nemo_turn_time, check_box_dory_mode, dory_mode_excitement_entry):
        print('shared delegate m3_find_nemo')
        m3_extra.m3_find_nemo(self.robot, int(find_nemo_speed_entry), int(find_nemo_turn_time), check_box_dory_mode, int(dory_mode_excitement_entry))

    def m2_play_waltz_of_the_flowers(self):
        T = self.robot.sound_system.tone_maker

        g3 = 196
        c4 = 261.63
        e4 = 329.63
        f4 = 349.23
        d4 = 293.66
        g4 = 392

        T.play_tone(g3, 400)
        T.play_tone(c4, 400)
        T.play_tone(e4, 400)
        T.play_tone(f4, 1000)
        T.play_tone(e4, 200)
        T.play_tone(e4, 2400)

        T.play_tone(g3, 400)
        T.play_tone(c4, 400)
        T.play_tone(e4, 400)
        T.play_tone(f4, 400)
        T.play_tone(e4, 600)
        T.play_tone(d4, 200)
        T.play_tone(g4, 800)
        T.play_tone(c4, 400)

    def m2_spin(self):
        self.robot.drive_system.go(25, -25)
        time.sleep(20) # change this variable so it goes in a circle
        self.robot.drive_system.stop()

    def m2_spin_and_move(self, left_wheel_speed, right_wheel_speed):
        while True:
            self.robot.drive_system.go(left_wheel_speed, right_wheel_speed)
            time.sleep(2)
            self.robot.drive_system.stop()
            self.m2_spin()
            if self.robot.sensor_system.ir_proximity_sensor.get_distance() <= 10:
                break

    def m2_color_dance(self, left_wheel_speed, right_wheel_speed, color):
        self.go_straight_until_color_is(color, left_wheel_speed)
        self.m2_spin()
        """
        self.robot.drive_system.go(left_wheel_speed, right_wheel_speed)
        while True:
            x = self.robot.sensor_system.color_sensor.get_color()
            print(x)
            if x == color:
                self.robot.drive_system.stop()
                self.m2_spin()
                break
        """

    def m2_pick_up_partner(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(left_wheel_speed, right_wheel_speed)
        while True:
            if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 4:
                self.robot.drive_system.stop()
                self.robot.arm_and_claw.raise_arm()
                self.m2_spin()
                self.robot.arm_and_claw.lower_arm()
                break

"""
    def m2_line_dance(self, left_wheel_speed, right_wheel_speed):
        print('***')
        original = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        original_time = time.time()
        print("orginial is: ", original)
        while True:
            current = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
            print("current is: ", current)
            if abs(original - current) <= 5:
                self.robot.drive_system.go(left_wheel_speed, right_wheel_speed)
            elif abs(original - current) > 5:
                self.robot.drive_system.stop()
                self.robot.drive_system.go(-25, 25)
            if int(time.time() - original_time) > 60:
                self.robot.drive_system.stop()
                break
"""
