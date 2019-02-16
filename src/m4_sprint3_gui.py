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
    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    sprint_3_frame=get_sprint_3_frame(main_frame,mqtt_sender)

    return sprint_3_frame

# def grid_frames(sprint_3_frame):
#     sprint_3_frame.grid()

def get_sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    ccw_label = ttk.Label(frame,text="Line following counter-clockwise.     ")
    ccw_button=ttk.Button(frame,text="Start. (ccw)     ")
    cw_label = ttk.Label(frame, text="Line following clockwise.     ")
    cw_button=ttk.Button(frame,text="Start. (cw)    ")
    speed_test_entry_label=ttk.Label(frame,text="Speed.     ")
    speed_test_entry=ttk.Entry(frame, width=8)

    cw_button["command"] = lambda: handle_cw_line_follow(mqtt_sender,speed_test_entry)
    ccw_button["command"] = lambda: handle_ccw_line_follow(mqtt_sender,speed_test_entry)

    cw_label.grid()
    cw_button.grid(row=1,column=0)
    ccw_label.grid(row=0,column=2)
    ccw_button.grid(row=1, column=2)
    speed_test_entry_label.grid(row=0,column=1)
    speed_test_entry.grid(row=1,column=1)

    return frame

def handle_cw_line_follow(mqtt_sender,speed_entry):
    mqtt_sender.send_message("cw_line_follow",[speed_entry.get()])

def handle_ccw_line_follow(mqtt_sender,speed_entry):
    mqtt_sender.send_message("ccw_line_follow", [speed_entry.get()])

main()