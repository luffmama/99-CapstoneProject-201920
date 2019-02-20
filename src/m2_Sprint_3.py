"""
Here is Emily Guajardo's Sprint 3 code:
"""
import tkinter as ttk
import mqtt_remote_method_calls as com
import time

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
    root = ttk.Tk()
    root.title("CSSE 120 Capstone Project")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root)
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, movement_frame, noise_frame)

    get_user_controlled_dance_frame(main_frame, mqtt_sender).grid(row=0, column=0)
    get_automatic_dance_frame(main_frame, mqtt_sender).grid(row=1, column=0)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


# This method constructs a frame that gives the user controls to make the Robot Dance.
def get_user_controlled_dance_frame(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window)
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Dance Controls")
    left_speed_label = ttk.Label(frame, text="Left wheel speed:")
    right_speed_label = ttk.Label(frame, text="Right wheel speed:")

    left_speed_entry = ttk.Entry(frame, width=8)
    right_speed_entry = ttk.Entry(frame, width=8)

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

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

    return frame


def get_automatic_dance_frame(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window)
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Automatic Dance Controls")
    left_speed_label = ttk.Label(frame, text="Left wheel speed:")
    right_speed_label = ttk.Label(frame, text="Right wheel speed:")
    color_label = ttk.Label(frame, text="Color:")

    left_speed_entry = ttk.Entry(frame, width=8)
    right_speed_entry = ttk.Entry(frame, width=8)
    color_entry = ttk.Entry(frame, width=8)

    spin_and_move_button = ttk.Button(frame, text="Spin and Move Forward!")
    color_dance_button = ttk.Button(frame, text="Dance Based on Color!")
    line_dance_button = ttk.Button(frame, text="Line Dance!")
    music_button = ttk.Button(frame, text="Play Music!")

    # Grid the widgets:
    frame_label.grid(row=0, column=0)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=2, column=0)
    color_label.grid(row=3, column=0)
    left_speed_entry.grid(row=1, column=1)
    right_speed_entry.grid(row=2, column=1)
    color_entry.grid(row=3, column=1)

    spin_and_move_button.grid(row=4, column=0)
    color_dance_button.grid(row=4, column=1)
    line_dance_button.grid(row=5, column=0)
    music_button.grid(row=5, column=1)

    # Set the button callbacks:
    spin_and_move_button["command"] = lambda: handle_spin_and_move(
        left_speed_entry, right_speed_entry, mqtt_sender)
    color_dance_button["command"] = lambda: handle_color_dance(
        left_speed_entry, right_speed_entry, color_entry, mqtt_sender)
    # line_dance_button["command"] = lambda: handle_left(
    #     left_speed_entry, right_speed_entry, mqtt_sender)
    music_button["command"] = lambda: handle_music(mqtt_sender)

    return frame


# This gives the forward button functionality
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    print("forward",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("forward",[left_entry_box.get(),
                                        right_entry_box.get()])
    print("message got through")


# This give the backward button functionality
def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    print("backward",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("backward",[left_entry_box.get(),
                                         right_entry_box.get()])


# This give the left button functionality
def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    print("left",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("left",[left_entry_box.get(),
                                     right_entry_box.get()])


# This give the right button functionality
def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    print("right",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("right",[left_entry_box.get(),
                                      right_entry_box.get()])


# This give the stop button functionality
def handle_stop(mqtt_sender):
    print("stop")
    mqtt_sender.send_message("stop")


def handle_spin_and_move(left_speed_entry, right_speed_entry, mqtt_sender):
    mqtt_sender.send_message("m2_spin_and_move", [left_speed_entry.get(), right_speed_entry.get()])


def handle_color_dance(left_speed_entry, right_speed_entry, color_entry, mqtt_sender):
    mqtt_sender.send_message("m2_color_dance", [left_speed_entry.get(),
                                                right_speed_entry.get(),
                                                color_entry.get()])


def handle_line_dance(mqtt_sender):
    pass


def handle_music(mqtt_sender):
    mqtt_sender.send_message("m2_play_waltz_of_the_flowers")
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()





def line_dance(self):
    pass

