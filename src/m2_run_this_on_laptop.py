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
    # teleop_frame, arm_frame, control_frame, movement_frame, noise_frame = get_shared_frames(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # Done: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, movement_frame, noise_frame)

    face_and_pick_up_object_frame(main_frame, mqtt_sender).grid(row=0, column=0)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control = shared_gui.get_control_frame(main_frame, mqtt_sender)
    movement = shared_gui.get_movement_frame(main_frame, mqtt_sender)
    noise = shared_gui.get_noise_frame(main_frame, mqtt_sender)
    return teleop, arm, control, movement, noise


def grid_frames(teleop_frame, arm_frame, control_frame, movement_frame, noise_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    movement_frame.grid(row=0, column=1)
    noise_frame.grid(row=1, column=1)



def tone_as_closer (self, initial_frequency, delta_frequency):
    self.robot.drive_system.go(100)
    k = 0
    while True:
        self.soundsystem.tone_maker.ToneMaker(initial_frequency + (delta_frequency * k), 50)
        k += 1
        if self.soundsystem.Sensorsystem.ir_proximity_sensor.get_distance() <= 4:
            self.robot.drive_system.stop()
            break
    self.robot.arm_and_claw.raise_arm()

# This method creates a frame for feature 10
def face_and_pick_up_object_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Pick up Objects")
    label = ttk.Label(frame, text="Get the robot to point towards an object!")
    direction_label_1 = ttk.Label(frame, text="Enter 0 for Clockwise")
    direction_label_2 = ttk.Label(frame, text="And 1 for Counterclockwise")
    direction_label = ttk.Label(frame, text="Direction:")
    speed_label = ttk.Label(frame, text="Speed:")

    direction_entry = ttk.Entry(frame, width=8)
    speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)

    button1 = ttk.Button(frame, text="Point towards an object")
    button2 = ttk.Button(frame, text="Face an object")
    button3 = ttk.Button(frame, text="Pick up object")

    # Grid the widgets:
    frame_label.grid(row=0, column=0)
    direction_label_1.grid(row=1, column=0)
    direction_label_2.grid(row=1, column=1)
    direction_label.grid(row=2, column=0)
    speed_label.grid(row=2, column=1)
    direction_entry.grid(row=3, column=0)
    speed_entry.grid(row=3, column=1)

    button1.grid(row=1, column=2)
    button2.grid(row=2, column=2)
    button3.grid(row=3, column=2)

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