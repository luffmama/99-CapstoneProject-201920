"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Margaret Luffman.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
from tkinter import *
import shared_gui
import rosebot
import math
import time
import shared_gui_delegate_on_robot as s
import m1_extra

# Table of contents of this file
# get cpc frame 97-241
# handle functions for cpc 246-308
# foa frame 317-354
# foa handle functions 357-372
# robocop gui and handle functions 361-460



rosebot.RoseBot
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
    root.title("Capstone Project CSSE 120")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,padding=10,borderwidth=5,relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    robo_frame =  get_shared_frames(main_frame,mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(robo_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    #teleop = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    #arm = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    #control = shared_gui.get_control_frame(main_frame,mqtt_sender)
   # movment = shared_gui.get_movement_frame(main_frame,mqtt_sender)
    #noise = shared_gui.get_noise_frame(main_frame,mqtt_sender)
    #cpc_frame = shared_gui.get_cpc_frame(main_frame,mqtt_sender)
    #foa_frame = get_foa_frame(main_frame,mqtt_sender)
    robo_frame = get_robocop_frame(main_frame,mqtt_sender)

    return robo_frame


def grid_frames(robo_frame):
    # teleop_frame.grid(row=0,column=0)
    # arm_frame.grid(row=0,column=1)
    # control_frame.grid(row=3,column=1)
    # movment_frame.grid(row=1,column=0)
    # noise_frame.grid(row=1,column=1)
    # cpc_frame.grid(row=2,column=0)
    # foa_frame.grid(row=0,column=0)
    robo_frame.grid(row=0,column=0)

## gui for color and proximity and camra (work in progress)

##
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

    # Creating handle functions

def handle_camera_data(mqtt_sender):
    print("display_camera_data")
    mqtt_sender.send_message("display_camera_data")

def display_camera_data(self):
    x,y,w,h = self.robot.drive_system.display_camera_data()
    print("The center is",x,y)
    print("The width is",w)
    print("THe height is",h)


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
    # Creating shared gui delgate functions


#
## Gui for frequency oscillation and alignment using the camera



def get_foa_frame(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame,text="Frequency Oscillation and Alignment using the Camera")
    high_frequency_label = ttk.Label(frame,text="Maximum Frequency")
    low_frequency_label = ttk.Label(frame, text="Minimum Frequency")
    initial_frequency_duration_label = ttk.Label(frame, text="Initial Frequency Duration")
    c_or_cc_label = ttk.Label(frame, text = "enter c or cc")

    high_frequency_entry = ttk.Entry(frame,width=8)
    low_frequency_entry = ttk.Entry(frame, width=8)
    initial_frequency_duration_entry = ttk.Entry(frame, width=8)

    c_or_cc_entry = ttk.Entry(frame,width=8)

    approach_object_while_oscillating_button = ttk.Button(frame,text="Approach Object while oscillating")
    align_with_object_button = ttk.Button(frame,text="Turn, find object, and go to it")

    frame_label.grid(row=0,column=1)
    high_frequency_entry.grid(row=1,column=0)
    low_frequency_entry.grid(row=2,column=0)
    initial_frequency_duration_entry.grid(row=3, column=0)
    high_frequency_label.grid(row=1, column=1)
    low_frequency_label.grid(row=2, column=1)
    initial_frequency_duration_label.grid(row=3, column=1)
    approach_object_while_oscillating_button.grid(row=1, column=2)
    align_with_object_button.grid(row=2, column=2)
    c_or_cc_label.grid(row=4, column=1)
    c_or_cc_entry.grid(row=4,column=0)

    approach_object_while_oscillating_button["command"] = lambda: handle_oscillation(
        high_frequency_entry,low_frequency_entry,initial_frequency_duration_entry,mqtt_sender)
    align_with_object_button["command"] = lambda: handle_turn_and_go(
        c_or_cc_entry,high_frequency_entry,low_frequency_entry,initial_frequency_duration_entry,mqtt_sender)

    return frame

def handle_oscillation(high_frequency_entry, low_frequency_entry, initial_frequency_duration_entry, mqtt_sender):
    print("m1_f9",high_frequency_entry.get(), low_frequency_entry.get(), initial_frequency_duration_entry.get())
    mqtt_sender.send_message("oscillation_approach",[high_frequency_entry.get(),
                                                   low_frequency_entry.get(),
                                                   initial_frequency_duration_entry.get()])
def handle_alignment(mqtt_sender):
    print("align_the_robot")
    mqtt_sender.send_message("align_the_robot")

def handle_turn_and_go(c_or_cc_entry,high_frequency_entry, low_frequency_entry, initial_frequency_duration_entry,mqtt_sender):
    print("turn_and_go",c_or_cc_entry.get(),high_frequency_entry.get(), low_frequency_entry.get(), initial_frequency_duration_entry.get())
    mqtt_sender.send_message("turn_and_go",[c_or_cc_entry.get(),
                                            high_frequency_entry.get(),
                                            low_frequency_entry.get(),
                                            initial_frequency_duration_entry.get()])


def get_robocop_frame(window,mqtt_sender):
    # Creating the frame
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    # Creating Labels for buttons, entryboxes and the checkbox
    frame_label = ttk.Label(frame, text="Robocop")
    coward_label = ttk.Label(frame,text="Change the Bravery of Robocop")
    track_label = ttk.Label(frame, text = "Click to Track the Criminal for the number of seconds entered")
    meet_label = ttk.Label(frame, text = "Find out if there is a Criminal around")
    dangsize_label = ttk.Label(frame, text = "Enter how big a criminal must be to be dangerous")
    dangdist_label = ttk.Label(frame, text = "Enter how close a criminal must be to be dangerous")
    size_label = ttk.Label(frame,text = "Enter how big a criminal is")
    dist_label = ttk.Label(frame, text="Enter how far away a criminal is")
    # Creating Entry boxes
    size_entry = ttk.Entry(frame,width=8)
    dist_entry = ttk.Entry(frame,width=8)
    dangsize_entry = ttk.Entry(frame,width=8)
    dangdist_entry = ttk.Entry(frame,width=8)
    track_entry = ttk.Entry(frame,width=8)
    # Creating buttons
    track_button = ttk.Button(frame,text="Track")
    meet_button = ttk.Button(frame,text="Is there a criminal around?")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    # Creating the checkbox
    choices = {"coward","brave"}
    coward_var = StringVar(frame)
    coward_var.set("brave")
    coward_box = OptionMenu(frame,coward_var,*choices)
    def change_dropdown(*args):
        print(coward_var.get())
    coward_var.trace("w",change_dropdown)
    # Griding
    frame_label.grid(row=0,column=1)
    size_label.grid(row=1,column=0)
    size_entry.grid(row=1,column=2)
    dist_label.grid(row=2,column=0)
    dist_entry.grid(row=2,column=2)
    dangsize_label.grid(row=3,column=0)
    dangsize_entry.grid(row=3,column=2)
    dangdist_label.grid(row=4,column=0)
    dangdist_entry.grid(row=4,column=2)
    track_label.grid(row=5,column=0)
    track_entry.grid(row=5,column=1)
    track_button.grid(row=5,column=2)
    meet_label.grid(row=6,column=0)
    meet_button.grid(row=6,column=2)
    coward_label.grid(row=7,column=0)
    coward_box.grid(row=7,column=2)
    lower_arm_button.grid(row=8,column=0)
    # Commands
    meet_button["command"] = lambda: handle_meet(
        size_entry,dist_entry,dangsize_entry,coward_var,dangdist_entry,mqtt_sender)
    track_button["command"] = lambda: handle_track(track_entry,mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)

    return frame


def handle_meet(size_entry, dist_entry,coward_var, dangsize_entry, dangdist_entry, mqtt_sender):
    print("m1_meeting_criminal", [size_entry.get(),
                                  dist_entry.get(),
                                  coward_var.get(),
                                  dangsize_entry.get(),
                                  dangdist_entry.get()])
    mqtt_sender.send_message("m1_meeting_criminal", [size_entry.get(),
                                                  dist_entry.get(),
                                                     coward_var.get(),
                                                  dangsize_entry.get(),
                                                  dangdist_entry.get()])


def handle_track(track_entry,mqtt_sender):
    print("m1_track_the_criminal",track_entry.get())
    mqtt_sender.send_message("m1_track_the_criminal",[track_entry.get()])

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("lower_arm")
    mqtt_sender.send_message("lower_arm")


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()