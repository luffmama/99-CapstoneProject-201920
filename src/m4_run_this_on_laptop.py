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
    teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame,grab_frame=get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame,movement_frame,beeper_frame,grab_frame)

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

    return teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame,grab_frame

def grid_frames(teleop_frame, arm_frame, control_frame,movement_frame,beeper_frame,grab_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    movement_frame.grid(row=0,column=1)
    beeper_frame.grid(row=1,column=1)
    grab_frame.grid(row=0,column=2)

#gui for grabbing object with sensors
def get_grab_frame(window, mqqt_sender):

    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    grab_label=ttk.Label(frame,text="Grab Command")
    grab_button = ttk.Button(frame, text="Grab!")

    grab_label.grid()
    grab_button.grid(row=1,column=0)

    grab_button["command"] = lambda: handle_grab(mqqt_sender)

    return frame

#handle command for grab gui
def handle_grab(mqtt_sender):

    print("grab message")
    mqtt_sender.send_message("grab")

#gui for alternating led

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
