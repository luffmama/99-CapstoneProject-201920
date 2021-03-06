import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui_delegate_on_robot
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
    sprint_3_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    #grid_frames(sprint_3_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    my_delegate = secondary_delegate()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect("bilbo", "baggins")

    root.mainloop()


#sets up a secondary delegate for the message sent to the laptop
class secondary_delegate(object):

    #recieves the color of the stop point frmo the robot
    def say_it(self, message):
        print("The project is completed, the robot stopped on the color:", message, "which if 5, is the color red. ")

def get_shared_frames(main_frame, mqtt_sender):
    sprint_3_frame=get_sprint_3_frame(main_frame,mqtt_sender)

    return sprint_3_frame

# def grid_frames(sprint_3_frame):
#     sprint_3_frame.grid()

#sprint 3 gui
def get_sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    ccw_label = ttk.Label(frame,text="Line following.     ")
    ccw_button=ttk.Button(frame,text="Start.")
    cw_label = ttk.Label(frame, text="Line following clockwise.     ")
    cw_button=ttk.Button(frame,text="Start. (cw)    ")
    speed_test_entry_label=ttk.Label(frame,text="Speed.     ")
    speed_test_entry=ttk.Entry(frame, width=8)
    pivot_speed_test_entry_label=ttk.Label(frame,text="Pivot Speed.     ")
    pivot_speed_test_entry=ttk.Entry(frame,width=8)
    read_intensity_label=ttk.Label(frame,text="Check Intensity.     ")
    read_intensity_button=ttk.Button(frame,text="Start Check.     ")
    slider_speed_label=ttk.Label(frame,text="0 -> Speed -> 100")
    slider=ttk.Scale(frame)
    i_value_label=ttk.Label(frame,text="Desired Intensity Value.     ")
    i_value_entry=ttk.Entry(frame,width=8)
    kpr_label=ttk.Label(frame,text="kpr value.     ")
    kpr_entry=ttk.Entry(frame,width=8)
    kpl_label=ttk.Label(frame,text="kpl value.     ")
    kpl_entry=ttk.Entry(frame,width=8)
    kdr_label=ttk.Label(frame,text="kdr value.     ")
    kdr_entry=ttk.Entry(frame,width=8)
    kdl_label=ttk.Label(frame,text="kdl value.     ")
    kdl_entry=ttk.Entry(frame,width=8)
    kir_label=ttk.Label(frame,text="kir value.     ")
    kir_entry=ttk.Entry(frame,width=8)
    kil_label=ttk.Label(frame,text="kil value.     ")
    kil_entry=ttk.Entry(frame,width=8)
    label1=ttk.Label(frame,text="kir/kil should be 0     ")
    label2=ttk.Label(frame,text="kdr/kdl should be ~2*mth.sqrt(kpr/kpl)")

    #cw_button["command"] = lambda: handle_cw_line_follow(mqtt_sender,slider,i_value_entry,kpr_entry,kpl_entry)
    ccw_button["command"] = lambda: handle_ccw_line_follow(mqtt_sender,slider,i_value_entry,kpr_entry,kpl_entry,kir_entry,kil_entry,kdr_entry,kdl_entry)
    read_intensity_button["command"]= lambda: handle_read_intensity(mqtt_sender)

    #cw_label.grid()
    #cw_button.grid(row=1,column=0)
    label1.grid()
    label2.grid(row=1,column=0)
    ccw_label.grid(row=0,column=2)
    ccw_button.grid(row=1, column=2)
    # speed_test_entry_label.grid(row=0,column=1)
    # speed_test_entry.grid(row=1,column=1)
    # pivot_speed_test_entry_label.grid(row=2,column=1)
    # pivot_speed_test_entry.grid(row=3,column=1)
    read_intensity_label.grid(row=8,column=1)
    read_intensity_button.grid(row=9,column=1)
    slider_speed_label.grid(row=6,column=1)
    slider.grid(row=7,column=1)
    i_value_label.grid(row=0,column=1)
    i_value_entry.grid(row=1, column=1)
    kpr_label.grid(row=2,column=0)
    kpr_entry.grid(row=3,column=0)
    kpl_label.grid(row=4,column=0)
    kpl_entry.grid(row=5,column=0)
    kdr_label.grid(row=2,column=2)
    kdr_entry.grid(row=3,column=2)
    kdl_label.grid(row=4,column=2)
    kdl_entry.grid(row=5,column=2)
    kir_label.grid(row=2,column=1)
    kir_entry.grid(row=3,column=1)
    kil_label.grid(row=4,column=1)
    kil_entry.grid(row=5,column=1)

    return frame

def handle_cw_line_follow(mqtt_sender,slider,i_value,kpr_entry,kpl_entry):
    #print(slider.get())
    mqtt_sender.send_message("cw_line_follow",[slider.get(),i_value.get(),kpr_entry.get(),kpl_entry.get()])

def handle_ccw_line_follow(mqtt_sender,slider,i_value,kpr_entry,kpl_entry,kir_entry,kil_entry,kdr_entry,kdl_entry):
    #print(slider.get())
    mqtt_sender.send_message("ccw_line_follow", [slider.get(),i_value.get(),kpr_entry.get(),kpl_entry.get(),kir_entry.get(),kil_entry.get(),kdr_entry.get(),kdl_entry.get()])

def handle_read_intensity(mqqt_sender):
    mqqt_sender.send_message("read_intensity",[])

main()