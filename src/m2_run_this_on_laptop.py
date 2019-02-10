"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Emily Guajardo.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame = get_shared_frames(main_frame, mqtt_sender)
    movement_frame = get_movement_frame(main_frame, mqtt_sender)
    noise_frame = get_noise_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, movement_frame, noise_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control = shared_gui.get_control_frame(main_frame, mqtt_sender)
    return teleop, arm, control


def grid_frames(teleop_frame, arm_frame, control_frame, movement_frame, noise_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    movement_frame.grid(row=0, column=1)
    noise_frame.grid(row=1, column=1)




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
    straight_for_seconds_label = ttk.Label(frame, text="Seconds for Robot to move")
    straight_for_inches_using_seconds_label = ttk.Label(frame, text="Inches for Robot to move (using seconds)")
    straight_for_inches_using_encoder_label = ttk.Label(frame, text="Inches for Robot to move (using sensors)")

    # Creates input boxes
    straight_for_seconds_entry = ttk.Entry(frame, width=8)
    straight_for_inches_using_seconds_entry = ttk.Entry(frame, width=8)
    straight_for_inches_using_encoder_entry = ttk.Entry(frame, width=8)
    # left_speed_entry.insert(0, "100")
    # right_speed_entry.insert(0, "100")
    # The two commented out lines insert a initial value into the input box.

    straight_for_seconds_button = ttk.Button(frame, text="Go!")
    straight_for_inches_using_seconds_button = ttk.Button(frame, text="Go!")
    straight_for_inches_using_encoder_button = ttk.Button(frame, text="Go!")

    # Grid the widgets:
    frame_label.grid(row=1, column=0)
    straight_for_seconds_label.grid(row=1, column=0)
    straight_for_seconds_entry.grid(row=2, column=0)
    straight_for_seconds_button.grid(row=3, column=0)

    straight_for_inches_using_seconds_label.grid(row=1, column=1)
    straight_for_inches_using_seconds_entry.grid(row=2, column=1)
    straight_for_inches_using_seconds_button.grid(row=3, column=1)

    straight_for_inches_using_encoder_label.grid(row=1, column=2)
    straight_for_inches_using_encoder_entry.grid(row=2, column=2)
    straight_for_inches_using_encoder_button.grid(row=3, column=2)

    """
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
    """

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
    tone_frequency_label = ttk.Label(frame, text="Frequency of Tone")
    tone_duration_label = ttk.Label(frame, text="Duration of Tone")
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

    """
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
    """

    return frame
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()