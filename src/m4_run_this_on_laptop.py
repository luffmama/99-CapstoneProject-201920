"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Robert Kreft.
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
    teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame,grab_frame,LED_frame,color_drive_frame=get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame,grab_frame,LED_frame,color_drive_frame)

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
    grab_frame=get_grab_frame(main_frame,mqtt_sender)
    LED_frame=get_LED_frame(main_frame,mqtt_sender)
    color_drive_frame=get_color_drive_frame(main_frame,mqtt_sender)

    return teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame,grab_frame,LED_frame,color_drive_frame

def grid_frames(teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame,grab_frame,LED_frame,color_drive_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    movement_frame.grid(row=0,column=1)
    beeper_frame.grid(row=1,column=1)
    grab_frame.grid(row=2,column=1)
    LED_frame.grid(row=3,column=1)
    color_drive_frame.grid(row=3,column=0)

#gui for grabbing object with sensors
def get_grab_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    grab_label=ttk.Label(frame,text="Grab Command")
    grab_button = ttk.Button(frame, text="Grab!")

    grab_label.grid()
    grab_button.grid(row=1,column=0)

    grab_button["command"] = lambda: handle_grab(mqtt_sender)

    return frame

#handle command for grab gui
def handle_grab(mqtt_sender):

    print("grab message")
    mqtt_sender.send_message("grab")

#gui for alternating led
def get_LED_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frequency_label=ttk.Label(frame,text="LED Frequency command")
    frequency_entry = ttk.Entry(frame, width=8)
    frequency_entry_label=ttk.Label(frame,text="<- initial rate of change of freq")
    start_button = ttk.Button(frame, text="Start!")

    frequency_label.grid()
    frequency_entry.grid(row=1,column=0)
    frequency_entry_label.grid(row=1,column=1)
    start_button.grid(row=2,column=0)

    start_button["command"] = lambda: handle_LED(mqtt_sender,frequency_entry)

    return frame

#handle command for alternating led gui
def handle_LED(mqtt_sender,frequency_entry):

    print("LED message",frequency_entry.get())
    mqtt_sender.send_message("LED_cycle",[frequency_entry.get()])

#gui for color drive frame
def get_color_drive_frame(window, mqtt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    main_label = ttk.Label(frame, text="Drive Color Commands")
    note_label=ttk.Label(frame, text="0: No color that is, cannot classify the color")
    note_label1=ttk.Label(frame,text="as one of the following, 1: Black, 2: Blue,")
    note_label2=ttk.Label(frame,text="3: Green, 4: Yellow, 5: Red, 6: White, 7: Brown")
    drive_until_not_label=ttk.Label(frame, text="Drive until not:")
    drive_until_label=ttk.Label(frame, text="Drive until:")
    drive_until_int_is_less_than_label=ttk.Label(frame, text="Drive until Intensity is < :")
    drive_until_int_is_greater_than_label=ttk.Label(frame, text="Drive until Intensity is > :")

    drive_until_not_button=ttk.Button(frame, text="Start! (d_u_n)")
    drive_until_button=ttk.Button(frame, text="Start! (d_u)")
    drive_until_int_is_less_than_button=ttk.Button(frame, text="Start! (d_u_i_i_l_t)")
    drive_until_int_is_greater_than_button=ttk.Button(frame, text="Start! (d_u_i_i_g_t)")

    color_entry = ttk.Entry(frame, width=8)
    intensity_entry = ttk.Entry(frame, width=8)
    label1=ttk.Label(frame, text="color int ->")
    label2=ttk.Label(frame, text="intensity ->")

    drive_until_not_button["command"] = lambda:handle_drive_until_color_is_not(mqtt_sender,color_entry)
    drive_until_button["command"] = lambda:handle_drive_until_color_is(mqtt_sender,color_entry)
    drive_until_int_is_less_than_button["command"] = lambda:go_straight_until_intensity_is_less_than(mqtt_sender,color_entry)
    drive_until_int_is_greater_than_button["command"] = lambda:go_straight_until_intensity_is_greater_than(mqtt_sender,color_entry)

    main_label.grid()
    drive_until_not_label.grid(row=2,column=0)
    drive_until_label.grid(row=2,column=1)
    drive_until_int_is_less_than_label.grid(row=2,column=2)
    drive_until_int_is_greater_than_label.grid(row=2,column=3)
    color_entry.grid(row=3,column=1)
    intensity_entry.grid(row=3,column=3)
    drive_until_not_button.grid(row=4,column=0)
    drive_until_button.grid(row=4,column=1)
    drive_until_int_is_less_than_button.grid(row=4,column=2)
    drive_until_int_is_greater_than_button.grid(row=4,column=3)
    label1.grid(row=3,column=0)
    label2.grid(row=3,column=2)
    note_label.grid(row=0,column=4)
    note_label1.grid(row=1,column=4)
    note_label2.grid(row=2,column=4)

    return frame

def handle_drive_until_color_is_not(mqtt_sender,color_entry):

    print("handle_drive_until_color_is_not",color_entry.get())
    mqtt_sender.send_message("handle_drive_until_color_is_not",[color_entry.get()])

def handle_drive_until_color_is(mqtt_sender,color_entry):

    print("handle_drive_until_color_is",color_entry.get())
    mqtt_sender.send_message("handle_drive_until_color_is",[color_entry.get()])

def go_straight_until_intensity_is_greater_than(mqtt_sender,intensity_entry):

    print("go_straight_until_intensity_is_greater_than",intensity_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_greater_than",[intensity_entry.get()])

def go_straight_until_intensity_is_less_than(mqtt_sender,intensity_entry):

    print("go_straight_until_intensity_is_less_than",intensity_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_less_than",[intensity_entry.get()])

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
