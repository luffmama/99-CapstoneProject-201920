# By Margaret Luffman
# This is all the information for sprint 3. Th gui is first, then the handle functions, then the functions themselves.
# Due to some import errors I was getting there is also an exact copy of this code in m1_run_this_on_laptop (gui and
# handle functions) and shared_gui_delegate (everything else). Run the gui from m1_run_this_on_laptop.
#The gui for robocop

import mqtt_remote_method_calls as com
# import tkinter
from tkinter import ttk
from tkinter import *
import shared_gui
import rosebot
import math
import time
import shared_gui_delegate_on_robot as s



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



    # The handle functions for the buttons


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

    # Robot movment functions


def m1_meeting_criminal(self, size, distance, dangsize, box_entry, dangdist):
    # Meets criminal and either decides whether or not it is dangerous or runs away if it is a coward
    if self.m1_ID_the_criminal(size, distance) is True and self.m1_is_coward(box_entry) is True:
        self.m1_run_away()
    elif self.m1_ID_the_criminal(size,distance) is False:
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
    # figures out if a criminal is dangerous
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
    # chases the criminal
    self.align_the_robot()
    self.pick_up_object_while_beeping(3, 1)


def speak(self, word):
    self.robot.sound_system.speech_maker.speak(str(word))


def m1_is_coward(self, box_entry):
    # figures out if the robot is a coward
    if str(box_entry) == "coward":
        return True
    else:
        return False


def m1_run_away(self):
    # runs away
    self.speak("run away")
    self.backward(100, 100)