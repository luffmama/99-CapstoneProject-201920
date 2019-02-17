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
    # for sprints 1 and 2
    # teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame,pick_up_object_while_beeping_frame=get_shared_frames(main_frame,mqtt_sender)

    # for sprint 3
    finding_nemo_frame = sprint_3_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # for sprints 1 and 2
    # grid_frames(teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame, pick_up_object_while_beeping_frame)

    # for sprint 3
    grid_frames_sprint_3(finding_nemo_frame)
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

    return teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame, pick_up_object_while_beeping_frame(main_frame, mqtt_sender)


def grid_frames(teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame, pick_up_object_while_beeping_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    movement_frame.grid(row=3,column=0)
    beeper_frame.grid(row=4,column=0)
    pick_up_object_while_beeping_frame.grid(row=0, column=1)


def pick_up_object_while_beeping_frame(main_frame, mqtt_sender):
    pick_up_with_beeps_frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='groove')
    pick_up_with_beeps_frame.grid()

    # initial beep speed
    initial_beep_speed_label = ttk.Label(pick_up_with_beeps_frame, text='enter initial beeps per second:')
    initial_beep_speed_label.grid(row=0, column=0)
    initial_beep_speed_entry = ttk.Entry(pick_up_with_beeps_frame, width=8)
    initial_beep_speed_entry.grid(row=0, column=1)

    # beep acceleration
    beep_acceleration_label = ttk.Label(pick_up_with_beeps_frame, text='enter beep acceleration (0 to 100):')
    beep_acceleration_label.grid(row=1, column=0)
    beep_acceleration_entry = ttk.Entry(pick_up_with_beeps_frame, width=8)
    beep_acceleration_entry.grid(row=1, column=1)

    # button
    initial_beep_speed_button = ttk.Button(pick_up_with_beeps_frame, text='GO!')
    initial_beep_speed_button.grid(row=2, column=0)

    initial_beep_speed_button["command"] = lambda: handle_pick_up_object_while_beeping(
        initial_beep_speed_entry, beep_acceleration_entry, mqtt_sender)


    direction_label = ttk.Label(pick_up_with_beeps_frame, text='clockwise spin(cw) or counterclockwise spin(ccw):')
    direction_label.grid(row=3, column=0)
    direction_entry = ttk.Entry(pick_up_with_beeps_frame, width=8)
    direction_entry.grid(row=3, column=1)

    # spin speed
    spin_speed_label = ttk.Label(pick_up_with_beeps_frame, text='enter spin speed:')
    spin_speed_label.grid(row=4, column=0)
    spin_speed_entry = ttk.Entry(pick_up_with_beeps_frame, width=8)
    spin_speed_entry.grid(row=4, column=1)

    # button
    spin_till_see_object_button = ttk.Button(pick_up_with_beeps_frame, text='Spin GO!')
    spin_till_see_object_button.grid(row=5, column=0)

    spin_till_see_object_button['command'] = lambda: handle_spin_until_see_object_frame(
        initial_beep_speed_entry, beep_acceleration_entry, direction_entry, spin_speed_entry, mqtt_sender)

    return pick_up_with_beeps_frame


def handle_pick_up_object_while_beeping(initial_beep_speed_entry, beep_acceleration_entry, mqtt_sender):
    print('pick up object while beeping', initial_beep_speed_entry.get(), beep_acceleration_entry.get())
    mqtt_sender.send_message('pick_up_object_while_beeping', [initial_beep_speed_entry.get(), beep_acceleration_entry.get()])


def handle_spin_until_see_object_frame(initial_beep_speed_entry, beep_acceleration_entry, direction_entry, spin_speed_entry, mqtt_sender):
    print('Spin until see object',initial_beep_speed_entry.get(), beep_acceleration_entry.get(), direction_entry.get(), spin_speed_entry.get())
    mqtt_sender.send_message('m3_feature_10', [initial_beep_speed_entry.get(), beep_acceleration_entry.get(), direction_entry.get(), spin_speed_entry.get()])


def grid_frames_sprint_3(sprint_3_frame):
    sprint_3_frame.grid()


def sprint_3_frame(main_frame, mqtt_sender):
    finding_nemo_frame = ttk.Frame(main_frame, padding=10, borderwidth=5, relief='groove')
    finding_nemo_frame.grid()

    Title = ttk.Label(finding_nemo_frame, text='Finding Nemo!!!')
    Title.grid(row=0, column=0)

    going_into_deep_sea(finding_nemo_frame, mqtt_sender)
    dory_mode(finding_nemo_frame)

    return finding_nemo_frame


def going_into_deep_sea(finding_nemo_frame, mqtt_sender):
    deep_sea_label = ttk.Label(finding_nemo_frame, text='Entering Deep sea')
    deep_sea_label.grid(row=3, column=0)
    check_box_marlin = ttk.Checkbutton(finding_nemo_frame, text="Marlin")
    check_box_marlin.grid(row=3, column=1)
    check_box_nemo = ttk.Checkbutton(finding_nemo_frame, text="Nemo")
    check_box_nemo.grid(row=3, column=2)

    dory_mode_label, dory_mode_checkbutton, \
        dory_mode_excitement_label, dory_mode_excitement_entry, dory_mode_stop_button = dory_mode(finding_nemo_frame)
    dory_mode_label.grid(row=1, column=0)
    dory_mode_checkbutton.grid(row=1, column=1)
    dory_mode_excitement_label.grid(row=2, column=0)
    dory_mode_excitement_entry.grid(row=2, column=1)
    dory_mode_stop_button.grid(row=2, column=3)

    handle_deep_sea_button = ttk.Button(finding_nemo_frame, text="deep sea adventure")
    handle_deep_sea_button.grid(row=3, column=3)
    handle_deep_sea_button['command'] = lambda:\
        handle_deep_sea(check_box_marlin.instate(['selected']), check_box_nemo.instate(['selected']),
                        dory_mode_checkbutton.instate(['selected']), dory_mode_excitement_entry, mqtt_sender)

    dory_mode_stop_button["command"] = lambda: handle_quit(mqtt_sender)


def handle_deep_sea(check_box_marlin, check_box_nemo, check_box_dory_mode, dory_mode_excitement_entry, mqtt_sender):
    if check_box_nemo == check_box_marlin:
        print('select either Marlin OR Nemo')
    elif check_box_marlin is True:
        print('marlin is true')
        mqtt_sender.send_message('m3_marlin_deep_sea', [check_box_dory_mode, dory_mode_excitement_entry.get()])
    elif check_box_nemo is True:
        print('nemo is true')
        mqtt_sender.send_message('m3_nemo_deep_sea', [check_box_dory_mode, dory_mode_excitement_entry.get()])


def handle_quit(mqtt_sender):
    print('handle quit')
    mqtt_sender.send_message('now_quit')


def dory_mode(finding_nemo_frame):
    dory_mode_label = ttk.Label(finding_nemo_frame, text='Activate Dory mode')
    dory_mode_checkbutton = ttk.Checkbutton(finding_nemo_frame)

    dory_mode_excitement_label = ttk.Label(finding_nemo_frame, text="Enter Dory's excitement")
    dory_mode_excitement_entry = ttk.Entry(finding_nemo_frame, width=8)

    dory_mode_stop_button = ttk.Button(finding_nemo_frame, text="Stop Robot")

    return dory_mode_label, dory_mode_checkbutton, dory_mode_excitement_label, \
            dory_mode_excitement_entry, dory_mode_stop_button



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()