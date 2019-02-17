"""
    Code for sprint 3

    Authors:  Conner Ozatalar.
    Winter term, 2018-2019.
"""
import time


def m3_marlin_deep_sea(robot, check_box_dory_mode, dory_mode_excitement_entry):  # feature 1: going into deep sea
    print('Marlin deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return
    robot.sound_system.speech_maker.speak('stay in the shallow water')
    robot.drive_system.go(-20, -20)
    time.sleep(1)
    robot.drive_system.stop()


def m3_nemo_deep_sea(robot, check_box_dory_mode, dory_mode_excitement_entry):
    print('Nemo deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return
    robot.sound_system.speech_maker.speak('Time for an adventure')
    robot.drive_system.go_straight_for_inches_using_encoder(25, 100)
    robot.drive_system.go(-50, 50)
    start_time = time.time()
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 12:
            stop_from_sees_something(robot)
            break
        elif time.time() - start_time >= 3:
            stop_from_time(robot)
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return


def stop_from_sees_something(robot):
    print('stop_from_sees_something')
    robot.drive_system.stop()
    robot.drive_system.go(70, 70)
    while True:
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 4:
            robot.drive_system.stop()
            break


def stop_from_time(robot):
    print('stop from time')
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(25, 70)


def dory_mode_toggle(robot, check_box_dory_mode):
    if check_box_dory_mode is True:
        if robot.sensor_system.camera.get_biggest_blob().get_area() > 50:
            return True
    return False


def dory_mode_activated(robot, dory_mode_excitement_entry):
    print('Dory mode has been activated')
    c = 262.626
    d = 293.665
    b = 246.943
    e = 329.628
    t = 60000/(dory_mode_excitement_entry + 100)
    song = [(c, t, 5), (e, t, 5), (c, t, 5), (e, t, 5), (c, t, 5), (d, t/2, 5), (d, t/2, 5), (b, t, 5), (c, t, 5)]
    while True:
        robot.sound_system.tone_maker.play_tone_sequence(song).wait()
        if robot.ArmandClaw.touch_sensor.is_pressed():
            break
        time.sleep(.5)
