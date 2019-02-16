# The gui for robocop

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
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
    coward_label = ttk.Label(frame,text="check=coward")
    track_label = ttk.Label(frame, text = "click to track the criminal")
    meet_label = ttk.Label(frame, text = "find out if there is a criminal around")
    dangsize_label = ttk.Label(frame, text = "enter how big a criminal must be to be dangerous")
    dangdist_label = ttk.Label(frame, text = "enter how close a criminal must be to be dangerous")
    size_label = ttk.Label(frame,text = "enter how big a criminal is")
    dist_label = ttk.Label(frame, text="enter how far away a criminal is")
    # Creating Entry boxes
    size_entry = ttk.Entry(frame,width=8)
    dist_entry = ttk.Entry(frame,width=8)
    dangsize_entry = ttk.Entry(frame,width=8)
    dangdist_entry = ttk.Entry(frame,width=8)
    # Creating buttons
    track_button = ttk.Button(frame,text="Track")
    meet_button = ttk.Button(frame,text="Is there a criminal around?")
    # Creating the checkbox
    coward_box = ttk.Checkbutton(frame)
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
    track_button.grid(row=5,column=2)
    meet_label.grid(row=6,column=0)
    meet_button.grid(row=6,column=2)
    coward_label.grid(row=7,column=0)
    coward_box.grid(row=7,column=2)
    # Commands
    meet_button["command"] = lambda: handle_meet(
        size_entry,dist_entry,dangsize_entry,dangdist_entry,mqtt_sender)
    track_button["command"] = lambda: handle_track(mqtt_sender)

    return frame


    # The handle functions for the buttons


def handle_meet(size_entry, dist_entry, dangsize_entry, dangdist_entry, mqtt_sender):
    print("m1_meeting_criminal", [size_entry.get(),
                                  dist_entry.get(),
                                  dangsize_entry.get(),
                                  dangdist_entry.get()])
    mqtt_sender.send_message("m1_meeting_criminal", [size_entry.get(),
                                                  dist_entry.get(),
                                                  dangsize_entry.get(),
                                                  dangdist_entry.get()])


def handle_track(mqtt_sender):
    print("m1_track_the_criminal")
    mqtt_sender.send_message("m1_track_the_criminal")

    # Robot movment functions

def track_the_criminal(self):
    original = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
    t = time.time()
    while True:
        elapsed_time = time.time() - t
        current = self.robot.sensor_system.color_sensor.get_reflected_light_intensity()
        if abs(original - current) <= 5:
            self.robot.drive_system.forward(75,75)
        elif abs(original - current) > 5:
            self.robot.drive_system.right(75,75)
        if elapsed_time >= 10:
            self.robot.drive_system.stop()
            break


def ID_the_criminal(self,size,distance):
    blob = self.robot.sensor_system.camera.get_biggest_blob()
    if blob.get_area() >= int(size) or self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= int(distance):
        self.speak("criminal detected")
        return True
    else:
        self.speak("No criminals in sight")


def is_dangerous(self,dangsize,dangdist):
    blob = self.robot.sensor_system.camera.get_biggest_blob()
    if blob.get_area() >= int(dangsize) or self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= int(dangdist):
        self.speak("The criminal is dangerous")
        print("The criminal is dangerous, and is of size",blob.get_area(),
              "while being",self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches(),"inches away")
        self.speak("This is robocop calling for backup")
    else:
        self.speak("The criminal is not dangerous")
        self.chase_the_criminal()


def chase_the_criminal(self):
    self.align_the_robot()
    self.s.pick_up_object_while_beeping(3,1)


def speak(self,word):
    self.robot.sound_system.speach_maker.speak(str(word))


def is_coward(self,box_entry):
    if int(box_entry) == 1:
        return True
    else:
        return False


def meeting_criminal(self,size,distance,box_entry,dangsize,dangdist):
    if self.ID_the_criminal(size,distance) is True and self.is_coward(box_entry) is True:
        self.run_away()
    else:
        self.is_dangerous(dangsize,dangdist)


def run_away(self):
    self.speak("run away")
    self.backwards(100,100)