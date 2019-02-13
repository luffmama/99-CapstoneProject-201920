"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Conner Ozatalar.
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
    mqtt_sender=com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root=tkinter.Tk()
    root.title("CSSE120 Capstone Project, W 18-19")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame=ttk.Frame(root,padding=10,borderwidth=5,relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame,pick_up_object_while_beeping_frame, spin_until_see_object_frame=get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame, pick_up_object_while_beeping_frame, spin_until_see_object_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame=shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
    movement_frame=shared_gui.get_movement_frame(main_frame,mqtt_sender)
    beeper_frame=shared_gui.get_noise_frame(main_frame,mqtt_sender)

    return teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame, pick_up_object_while_beeping_frame(main_frame, mqtt_sender), spin_until_see_object_frame(main_frame, mqtt_sender)


def grid_frames(teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame, pick_up_object_while_beeping_frame, spin_until_see_object_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    movement_frame.grid(row=0,column=1)
    beeper_frame.grid(row=1,column=1)
    pick_up_object_while_beeping_frame.grid(row=0, column=2)
    spin_until_see_object_frame.grid(row=1, column=2)


def pick_up_object_while_beeping_frame(main_frame, mqtt_sender):
    pick_up_with_beeps_frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='groove')
    pick_up_with_beeps_frame.grid()

    # initial beep speed
    initial_beep_speed_label = ttk.Label(pick_up_with_beeps_frame, text='enter initial beeps per second:')
    initial_beep_speed_label.grid(row=0, column=0)
    initial_beep_speed_entry = ttk.Entry(pick_up_with_beeps_frame, width=8)
    initial_beep_speed_entry.grid(row=0, column=1)

    # beep acceleration
    beep_acceleration_label = ttk.Label(pick_up_with_beeps_frame, text='enter beep acceleration:')
    beep_acceleration_label.grid(row=1, column=0)
    beep_acceleration_entry = ttk.Entry(pick_up_with_beeps_frame, width=8)
    beep_acceleration_entry.grid(row=1, column=1)

    # button
    initial_beep_speed_button = ttk.Button(pick_up_with_beeps_frame, text='GO!')
    initial_beep_speed_button.grid(row=2, column=0)

    initial_beep_speed_button["command"] = lambda: handle_pick_up_object_while_beeping(
        initial_beep_speed_entry, beep_acceleration_entry, mqtt_sender)

    return pick_up_with_beeps_frame


def spin_until_see_object_frame(main_frame, mqtt_sender):
    spin_till_see_object_frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='groove')
    spin_till_see_object_frame.grid()

    # turn direction
    direction_label = ttk.Label(spin_till_see_object_frame, text='clockwise spin(cw) or counterclockwise spin(ccw):')
    direction_label.grid(row=0, column=0)
    direction_entry = ttk.Entry(spin_till_see_object_frame, width=8)
    direction_entry.grid(row=0, column=1)

    # spin speed
    spin_speed_label = ttk.Label(spin_till_see_object_frame, text='enter spin speed:')
    spin_speed_label.grid(row=1, column=0)
    spin_speed_entry = ttk.Entry(spin_till_see_object_frame, width=8)
    spin_speed_entry.grid(row=1, column=1)

    # button
    spin_till_see_object_button = ttk.Button(spin_till_see_object_frame, text='GO!')
    spin_till_see_object_button.grid(row=2, column=0)

    spin_till_see_object_button['command'] = lambda: handle_spin_until_see_object_frame(
        direction_entry, spin_speed_entry, mqtt_sender)

    return spin_till_see_object_frame


def handle_pick_up_object_while_beeping(initial_beep_speed_entry, beep_acceleration_entry, mqtt_sender):
    print('pick up object while beeping', initial_beep_speed_entry.get(), beep_acceleration_entry.get())
    mqtt_sender.send_message('pick_up_object_while_beeping', [initial_beep_speed_entry.get(), beep_acceleration_entry.get()])


def handle_spin_until_see_object_frame(direction_entry, spin_speed_entry, mqtt_sender):
    print('Spin until see object', direction_entry.get(), spin_speed_entry.get())
    mqtt_sender.send_message('pick_up_object_while_beeping', [direction_entry.get(), spin_speed_entry.get()])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()