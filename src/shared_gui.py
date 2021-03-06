"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Margaret Luffman, Emily Guajardo, Conner Ozatalar, Robert Kreft.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_movement_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """

    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Movement")
    straight_for_seconds_seconds_label = ttk.Label(frame, text="Speed for Robot to move")
    straight_for_seconds_speed_label = ttk.Label(frame, text="Seconds for Robot to move")
    straight_for_inches_using_seconds_inches_label = ttk.Label(frame, text="Speed for Robot to move (using seconds)")
    straight_for_inches_using_seconds_speed_label = ttk.Label(frame, text="Inches for Robot to move (using seconds)")
    straight_for_inches_using_encoder_inches_label = ttk.Label(frame, text="Speed for Robot to move (using sensors)")
    straight_for_inches_using_encoder_speed_label = ttk.Label(frame, text="Inches for Robot to move (using sensors)")

    # Creates input boxes
    straight_for_seconds_seconds_entry = ttk.Entry(frame, width=8)
    straight_for_seconds_speed_entry = ttk.Entry(frame, width=8)
    straight_for_inches_using_seconds_speed_entry = ttk.Entry(frame, width=8)
    straight_for_inches_using_seconds_inches_entry = ttk.Entry(frame, width=8)
    straight_for_inches_using_encoder_speed_entry = ttk.Entry(frame, width=8)
    straight_for_inches_using_encoder_inches_entry = ttk.Entry(frame, width=8)
    # left_speed_entry.insert(0, "100")
    # right_speed_entry.insert(0, "100")
    # The two commented out lines insert a initial value into the input box.

    straight_for_seconds_button = ttk.Button(frame, text="Go!")
    straight_for_inches_using_seconds_button = ttk.Button(frame, text="Go!")
    straight_for_inches_using_encoder_button = ttk.Button(frame, text="Go!")

    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    straight_for_seconds_seconds_label.grid(row=1, column=0)
    straight_for_seconds_seconds_entry.grid(row=2, column=0)
    straight_for_seconds_speed_label.grid(row=3, column=0)
    straight_for_seconds_speed_entry.grid(row=4, column=0)
    straight_for_seconds_button.grid(row=5, column=0)

    straight_for_inches_using_seconds_inches_label.grid(row=1, column=2)
    straight_for_inches_using_seconds_speed_label.grid(row=3, column=2)
    straight_for_inches_using_seconds_inches_entry.grid(row=2, column=2)
    straight_for_inches_using_seconds_speed_entry.grid(row=4, column=2)
    straight_for_inches_using_seconds_button.grid(row=5, column=2)

    straight_for_inches_using_encoder_inches_label.grid(row=1, column=3)
    straight_for_inches_using_encoder_speed_label.grid(row=3, column=3)
    straight_for_inches_using_encoder_inches_entry.grid(row=2, column=3)
    straight_for_inches_using_encoder_speed_entry.grid(row=4, column=3)
    straight_for_inches_using_encoder_button.grid(row=5, column=3)

    # Set the button callbacks:
    straight_for_seconds_button["command"] = lambda: straight_for_seconds(
        straight_for_seconds_seconds_entry, straight_for_seconds_speed_entry, mqtt_sender)
    straight_for_inches_using_seconds_button["command"] = lambda: straight_for_inches_using_seconds(
        straight_for_inches_using_seconds_speed_entry, straight_for_inches_using_seconds_inches_entry, mqtt_sender)
    straight_for_inches_using_encoder_button["command"] = lambda: straight_for_inches_using_encoder(
        straight_for_inches_using_encoder_inches_entry,straight_for_inches_using_encoder_speed_entry, mqtt_sender)

    return frame


def get_noise_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """

    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sounds")
    beep_label = ttk.Label(frame, text="Number of Beeps")
    tone_frequency_label = ttk.Label(frame, text="Duration of Tone (milliseconds)")
    tone_duration_label = ttk.Label(frame, text="Frequency of Tone (Hz)")
    phrase_label = ttk.Label(frame, text="Phrase for the Robot to speak)")

    # Creates input boxes
    beep_entry = ttk.Entry(frame, width=8)
    tone_frequency_entry = ttk.Entry(frame, width=8)
    tone_duration_entry = ttk.Entry(frame, width=8)
    phrase_entry = ttk.Entry(frame, width=8)
    # left_speed_entry.insert(0, "100")
    # right_speed_entry.insert(0, "100")
    # The two commented out lines insert a initial value into the input box.

    beep_button = ttk.Button(frame, text="Go!")
    tone_button = ttk.Button(frame, text="Go!")
    phrase_button = ttk.Button(frame, text="Go!")

    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    beep_label.grid(row=1, column=0)
    beep_entry.grid(row=2, column=0)
    beep_button.grid(row=3, column=0)

    tone_duration_label.grid(row=1, column=1)
    tone_frequency_label.grid(row=1, column=2)
    tone_duration_entry.grid(row=2, column=1)
    tone_frequency_entry.grid(row=2, column=2)
    tone_button.grid(row=3, column=1)

    phrase_label.grid(row=1, column=3)
    phrase_entry.grid(row=2, column=3)
    phrase_button.grid(row=3, column=3)

    # Set the button callbacks:
    beep_button["command"] = lambda: beep(
        beep_entry, mqtt_sender)
    tone_button["command"] = lambda: tone(
        tone_frequency_entry, tone_duration_entry, mqtt_sender)
    # we don't have a phrase command yet
    # phrase_button["command"] = lambda: handle_left(left_speed_entry, right_speed_entry, mqtt_sender)

    return frame


def get_cpc_frame(window,mqtt_sender):
    """
        Constructs and returns a frame on the given window, where the frame
        has Entry and Button objects that control the EV3 robot's motion
        by passing messages using the given MQTT Sender.
          :type  window:       ttk.Frame | ttk.Toplevel
          :type  mqtt_sender:  com.MqttClient
        """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame first the labels for Entrys
    frame_label = ttk.Label(frame, text="Color,Proximity, Camera")
    intensity_less_than_label = ttk.Label(frame, text="Intensity (less than)")
    intensity_less_than_speed_label = ttk.Label(frame, text= "Intensity (less than) speed")
    intensity_greater_than_label = ttk.Label(frame, text="Intensity (greater than)")
    intensity_greater_than_speed_label = ttk.Label(frame, text="Intensity (greater than) speed")
    straight_until_color_is_color_label = ttk.Label(frame, text = "Straight until color is")
    straight_until_color_is_speed_label = ttk.Label(frame, text = "Speed for straight util color is")
    straight_until_color_is_not_color_label = ttk.Label(frame, text="Straight until color is not")
    straight_until_color_is_not_speed_label = ttk.Label(frame, text="Speed for straight util color is not")
    distance_less_than_distance_label = ttk.Label(frame, text= "Distance less than")
    distance_less_than_speed_label = ttk.Label(frame, text= "Speed for Distance less than")
    distance_greater_than_distance_label = ttk.Label(frame, text="Distance greater than")
    distance_greater_than_speed_label = ttk.Label(frame, text="Speed for Distance greater than")
    distance_within_delta_label = ttk.Label(frame, text="Distance to go within")
    distance_within_distance_label = ttk.Label(frame, text = "Distance within")
    distance_within_speed_label = ttk.Label(frame, text = "Speed for Distance within")
    display_camera_label = ttk.Label(frame, text = "Camera is viewing:")
    spin_c_until_object_speed_label = ttk.Label(frame, text = "Clockwise spin speed")
    spin_c_until_object_area_label = ttk.Label(frame, text = "Clockwise spin object area")
    spin_cc_until_object_speed_label = ttk.Label(frame, text="Counterclockwise spin speed")
    spin_cc_until_object_area_label = ttk.Label(frame, text="Counterclockwise spin object area")

    # now entries

    intensity_less_than_entry = ttk.Entry(frame, width=8)
    intensity_less_than_speed_entry = ttk.Entry(frame, width=8)
    intensity_greater_than_entry = ttk.Entry(frame, width=8)
    intensity_greater_than_speed_entry = ttk.Entry(frame, width=8)
    straight_until_color_is_color_entry = ttk.Entry(frame, width=8)
    straight_until_color_is_speed_entry = ttk.Entry(frame, width=8)
    straight_until_color_is_not_color_entry = ttk.Entry(frame, width=8)
    straight_until_color_is_not_speed_entry = ttk.Entry(frame, width=8)
    distance_less_than_distance_entry = ttk.Entry(frame, width=8)
    distance_less_than_speed_entry = ttk.Entry(frame, width=8)
    distance_greater_than_distance_entry = ttk.Entry(frame, width=8)
    distance_greater_than_speed_entry = ttk.Entry(frame, width=8)
    distance_within_delta_entry = ttk.Entry(frame, width=8)
    distance_within_distance_entry = ttk.Entry(frame, width=8)
    distance_within_speed_entry = ttk.Entry(frame, width=8)
    spin_c_until_object_speed_entry = ttk.Entry(frame, width=8)
    spin_c_until_object_area_entry = ttk.Entry(frame, width=8)
    spin_cc_until_object_speed_entry = ttk.Entry(frame, width=8)
    spin_cc_until_object_area_entry = ttk.Entry(frame, width=8)

    # now buttons

    intensity_less_than_button = ttk.Button(frame, text="Go straight until intensity is less than")
    intensity_greater_than_button = ttk.Button(frame, text="Go straight until intensity is greater than")
    straight_until_color_button = ttk.Button(frame, text="Go straight until color is")
    straight_until_not_color_button = ttk.Button(frame, text="Go straight until color is not")
    distance_less_than_button = ttk.Button(frame, text="Go straight until distance is less than")
    distance_greater_than_button = ttk.Button(frame, text="Go Back until distance is greater than")
    distance_within_button = ttk.Button(frame,text= "Go until distance within")
    camera_button = ttk.Button(frame, text="Get Camera Data")
    spin_c_button = ttk.Button(frame, text="Spin Clockwise until object is seen")
    spin_cc_button = ttk.Button(frame, text="Spin CounterClockwise until object is seen")

    # griding

    frame_label.grid(row=0,column=3)
    intensity_less_than_entry.grid(row=1, column=0)
    intensity_less_than_speed_entry.grid(row=2,column=0)
    intensity_less_than_button.grid(row=3, column=0)
    intensity_greater_than_entry.grid(row=4,column=0)
    intensity_greater_than_speed_entry.grid(row=5,column=0)
    intensity_greater_than_button.grid(row=6, column=0)
    straight_until_color_is_color_entry.grid(row=7,column=0)
    straight_until_color_is_speed_entry.grid(row=8, column=0)
    straight_until_color_button.grid(row=9, column=0)
    straight_until_color_is_not_color_entry.grid(row=10, column=0)
    straight_until_color_is_not_speed_entry.grid(row=11, column=0)
    straight_until_not_color_button.grid(row=12, column=0)
    intensity_less_than_label.grid(row=1, column=1)
    intensity_less_than_speed_label.grid(row=2, column=1)
    intensity_greater_than_label.grid(row=4, column=1)
    intensity_greater_than_speed_label.grid(row=5, column=1)
    straight_until_color_is_color_label.grid(row=7, column=1)
    straight_until_color_is_speed_label.grid(row=8, column=1)
    straight_until_color_is_not_color_label.grid(row=10, column=1)
    straight_until_color_is_not_speed_label.grid(row=11, column=1)
    distance_less_than_distance_entry.grid(row=1, column=2)
    distance_less_than_speed_entry.grid(row=2, column=2)
    distance_less_than_button.grid(row=3, column=2)
    distance_greater_than_distance_entry.grid(row=4, column=2)
    distance_greater_than_speed_entry.grid(row=5, column=2)
    distance_greater_than_button.grid(row=6, column=2)
    distance_within_delta_entry.grid(row=7, column=2)
    distance_within_distance_entry.grid(row=8, column=2)
    distance_within_speed_entry.grid(row=9, column=2)
    distance_within_button.grid(row=10, column=2)
    distance_less_than_distance_label.grid(row=1, column=3)
    distance_less_than_speed_label.grid(row=2, column=3)
    distance_greater_than_distance_label.grid(row=4, column=3)
    distance_greater_than_speed_label.grid(row=5, column=3)
    distance_within_delta_label.grid(row=7, column=3)
    distance_within_distance_label.grid(row=8, column=3)
    distance_within_speed_label.grid(row=9, column=3)
    camera_button.grid(row=0, column=4)
    spin_c_until_object_speed_entry.grid(row=7, column=4)
    spin_c_until_object_area_entry.grid(row=8, column=4)
    spin_c_button.grid(row=9, column=4)
    spin_cc_until_object_speed_entry.grid(row=10, column=4)
    spin_cc_until_object_area_entry.grid(row=11, column=4)
    spin_cc_button.grid(row=12, column=4)
    spin_c_until_object_speed_label.grid(row=7, column=5)
    spin_c_until_object_area_label.grid(row=8, column=5)
    spin_cc_until_object_speed_label.grid(row=10, column=5)
    spin_cc_until_object_area_label.grid(row=11, column=5)

    # setting callbacks

    intensity_less_than_button["command"] = lambda: handle_intensity_less_than(
        intensity_less_than_entry, intensity_less_than_speed_entry, mqtt_sender)
    intensity_greater_than_button["command"]= lambda: handle_intensity_is_greater_than(
        intensity_greater_than_entry, intensity_greater_than_speed_entry,mqtt_sender)
    straight_until_color_button["command"] = lambda: handle_color(
        straight_until_color_is_color_entry,straight_until_color_is_speed_entry, mqtt_sender)
    straight_until_not_color_button["command"] = lambda: handle_not_color(
        straight_until_color_is_not_color_entry,straight_until_color_is_not_speed_entry, mqtt_sender)
    distance_less_than_button["command"] = lambda: handle_distance_less_than(
        distance_less_than_distance_entry, distance_less_than_speed_entry,mqtt_sender)
    distance_greater_than_button["command"] = lambda: handle_distance_greater_than(
        distance_greater_than_distance_entry,distance_greater_than_speed_entry,mqtt_sender)
    distance_within_button["command"] = lambda: handle_distance_within(
        distance_within_delta_entry,distance_within_distance_entry,distance_within_speed_entry,mqtt_sender)
    spin_c_button["command"] = lambda: handle_spin_c(
        spin_c_until_object_speed_entry,spin_c_until_object_area_entry,mqtt_sender)
    spin_cc_button["command"] = lambda: handle_spin_cc(
        spin_cc_until_object_speed_entry,spin_cc_until_object_area_entry,mqtt_sender)
    camera_button["command"] = lambda: handle_camera_data(mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################


def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("forward",[left_entry_box.get(),
                                        right_entry_box.get()])
    print("message got through")


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("backward",[left_entry_box.get(),
                                         right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("left",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("left",[left_entry_box.get(),
                                     right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("right",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("right",[left_entry_box.get(),
                                      right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("stop")
    mqtt_sender.send_message("stop")


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("raise_arm")
    mqtt_sender.send_message("raise_arm")


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("lower_arm")
    mqtt_sender.send_message("lower_arm")


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("calibrate_arm")
    mqtt_sender.send_message("calibrate_arm")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("move_arm_to_position")
    mqtt_sender.send_message("move_arm_to_position",[arm_position_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('is_quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()


################################################################################
# Handlers for Buttons in Movement frame
############################################################################

def straight_for_seconds(straight_for_seconds_seconds_entry,
                         straight_for_seconds_speed_entry,
                         mqtt_sender):
    # print("go_straight_for_seconds", straight_for_seconds_seconds_entry.get())
    mqtt_sender.send_message("go_straight_for_seconds",
                             [straight_for_seconds_speed_entry.get(),
                             straight_for_seconds_seconds_entry.get()])


def straight_for_inches_using_seconds(straight_for_inches_using_seconds_speed_entry,
                                      straight_for_inches_using_seconds_inches_entry,
                                      mqtt_sender):
    # print("go_straight_for_inches_using_time", straight_for_inches_using_seconds_entry.get())
    mqtt_sender.send_message("go_straight_for_inches_using_time",
                             [straight_for_inches_using_seconds_speed_entry.get(),
                             straight_for_inches_using_seconds_inches_entry.get()])


def straight_for_inches_using_encoder(straight_for_inches_using_encoder_inches_entry,
                                      straight_for_inches_using_encoder_speed_entry, 
                                      mqtt_sender):
    # print("straight_for_inches_using_encoder", straight_for_inches_using_encoder_entry.get())
    mqtt_sender.send_message("straight_for_inches_using_encoder",
                             [straight_for_inches_using_encoder_speed_entry.get(),
                              straight_for_inches_using_encoder_inches_entry.get()])


def beep(beep_entry,mqtt_sender):
    print("beep",beep_entry.get())
    mqtt_sender.send_message("beep",[beep_entry.get()])


def tone(tone_frequency_entry,tone_duration_entry,mqtt_sender):
    print("tone",[tone_duration_entry.get(),tone_frequency_entry.get()])
    mqtt_sender.send_message("tone",[tone_frequency_entry.get(),
                                     tone_duration_entry.get()])


def handle_intensity_less_than(intensity_less_than_entry, intensity_less_than_speed_entry, mqtt_sender):
    print("go_straight_until_intensity_is_less_than",intensity_less_than_entry.get(),
          intensity_less_than_speed_entry.get())
    mqtt_sender.send_message("go straight_until_intensity_is_less_than",[intensity_less_than_entry.get(),
                             intensity_less_than_speed_entry.get()])


def handle_intensity_is_greater_than(intensity_greater_than_entry, intensity_greater_than_speed_entry, mqtt_sender):
    print("go_straight_until_intensity_is_greater_than",intensity_greater_than_entry.get(),
          intensity_greater_than_speed_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_greater_than",[intensity_greater_than_entry.get(),
                                                                            intensity_greater_than_speed_entry.get()])


def handle_color(straight_until_color_is_color_entry, straight_until_color_is_speed_entry, mqtt_sender):
    print("go_straight_until_color_is",straight_until_color_is_color_entry.get(),
          straight_until_color_is_speed_entry.get())
    mqtt_sender.send_message("go_straight_until_color_is",[straight_until_color_is_color_entry.get(),
                                                           straight_until_color_is_speed_entry.get()])


def handle_not_color(straight_until_color_is_not_color_entry, straight_until_color_is_not_speed_entry, mqtt_sender):
    print("go_straight_until_color_is_not", straight_until_color_is_not_color_entry.get(),
          straight_until_color_is_not_speed_entry.get())
    mqtt_sender.send_message("go_straight_until_color_is_not", [straight_until_color_is_not_color_entry.get(),
                             straight_until_color_is_not_speed_entry.get()])


def handle_distance_less_than(distance_less_than_distance_entry,distance_less_than_speed_entry, mqtt_sender):
    print("go_forward_until_distance_is_less_than",distance_less_than_distance_entry.get(),
          distance_less_than_speed_entry.get())
    mqtt_sender.send_message("go_forward_until_distance_is_less_than",[distance_less_than_distance_entry.get(),
                                                                       distance_less_than_speed_entry.get()])


def handle_distance_greater_than(distance_greater_than_distance_entry,distance_greater_than_speed_entry, mqtt_sender):
    print("go_backward_until_distance_is_greater_than",distance_greater_than_distance_entry.get(),
          distance_greater_than_speed_entry.get())
    mqtt_sender.send_message("go_backward_until_distance_is_greater_than",[distance_greater_than_distance_entry.get(),
                                                                           distance_greater_than_speed_entry.get()])


def handle_distance_within(distance_within_delta_entry, distance_within_distance_entry,distance_within_speed_entry,mqtt_sender):
    print("go_to_distance_within",distance_within_delta_entry.get(), distance_within_distance_entry.get(),distance_within_speed_entry.get())
    mqtt_sender.send_message("go_to_distance_within",[distance_within_delta_entry.get(),
                                                      distance_within_distance_entry.get(),
                                                      distance_within_speed_entry.get()])


def handle_spin_c(spin_c_until_object_speed_entry,spin_c_until_object_area_entry,mqtt_sender):
    print("spin_clockwise_until_object",spin_c_until_object_speed_entry.get(),spin_c_until_object_area_entry.get())
    mqtt_sender.send_message("spin_clockwise_until_object",[spin_c_until_object_speed_entry.get(),
                                                            spin_c_until_object_area_entry.get()])


def handle_spin_cc(spin_cc_until_object_speed_entry,sping_cc_until_object_area_entry,mqtt_sender):
    print("spin_counterclockwise_until_object",spin_cc_until_object_speed_entry.get(),sping_cc_until_object_area_entry.get())
    mqtt_sender.send_message("spin_counterclockwise_until_object",[spin_cc_until_object_speed_entry.get(),
                                                                   sping_cc_until_object_area_entry.get()])

def handle_camera_data(mqtt_sender):
    print("display_camera_data")
    mqtt_sender.send_message("display_camera_data")
