"""
    Code for sprint 3

    Authors:  Conner Ozatalar.
    Winter term, 2018-2019.
"""
import time

# feature 1: going into deep sea


def m3_marlin_deep_sea(robot, check_box_dory_mode, dory_mode_excitement_entry):
    print('Marlin deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 5:
            robot.drive_system.stop()
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return
    robot.sound_system.speech_maker.speak('stay in the shallow water')
    robot.drive_system.go(-30, -30)
    time.sleep(1.8)
    robot.drive_system.stop()


def m3_nemo_deep_sea(robot, check_box_dory_mode, dory_mode_excitement_entry):
    # nemo in the black circle
    print('Nemo deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 5:
            robot.drive_system.stop()
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return
    robot.sound_system.speech_maker.speak('Time for an adventure')
    nemo_on_the_run(robot, check_box_dory_mode, dory_mode_excitement_entry)


def nemo_on_the_run(robot, check_box_dory_mode, dory_mode_excitement_entry):
    # nemo running out of the black circle
    robot.drive_system.go_straight_for_inches_using_encoder(25, 100)
    robot.drive_system.go(-50, 50)
    start_time = time.time()
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 9:
            stop_from_sees_something(robot)
            break
        elif time.time() - start_time >= 2.8:
            stop_from_time(robot)
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return


def stop_from_sees_something(robot):
    # nemo sees something after exiting the black circle
    print('stop_from_sees_something')
    robot.drive_system.stop()
    robot.drive_system.go(70, 70)
    while True:
        # print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 3:
            robot.drive_system.stop()
            break


def stop_from_time(robot):
    # nemo returns to the black circle after leaving it and spinning
    print('stop from time')
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(25, 70)


def m3_find_nemo(robot, find_nemo_speed_entry, find_nemo_turn_time, check_box_dory_mode, dory_mode_excitement_entry):
    robot.drive_system.go(find_nemo_speed_entry, find_nemo_speed_entry)
    while True:
        # print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 3:
            obstacle_found(robot, find_nemo_speed_entry, find_nemo_turn_time)
            robot.drive_system.go(find_nemo_speed_entry, find_nemo_speed_entry)
        elif robot.sensor_system.touch_sensor.is_pressed():
            found_nemo(robot)
            break
        elif dory_mode_toggle(robot, check_box_dory_mode):
            dory_mode_activated(robot, dory_mode_excitement_entry)
            return


def obstacle_found(robot, find_nemo_speed_entry, find_nemo_turn_time):
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go(find_nemo_speed_entry, -find_nemo_speed_entry)
    time.sleep(find_nemo_turn_time/25)
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()
    time.sleep(.1)
    robot.drive_system.go(-find_nemo_speed_entry, find_nemo_speed_entry)
    time.sleep(find_nemo_turn_time/25)
    robot.drive_system.stop()
    time.sleep(.1)


def found_nemo(robot):
    robot.drive_system.stop()
    robot.sound_system.speech_maker.speak('I found nemo')


def dory_mode_toggle(robot, check_box_dory_mode):
    # print('dory mode toggle', check_box_dory_mode)
    if check_box_dory_mode is True:
        # print(robot.sensor_system.camera.get_biggest_blob().get_area())
        if robot.sensor_system.camera.get_biggest_blob().get_area() > 50:
            return True
    return False


def dory_mode_activated(robot, dory_mode_excitement_entry):
    robot.drive_system.stop()
    print('Dory mode has been activated')
    song = notes(dory_mode_excitement_entry)
    start_time = time.time()
    while True:
        robot.sound_system.tone_maker.play_tone_sequence(song).wait()
        if robot.sensor_system.touch_sensor.is_pressed():
            print('stopped from push sensor')
            break
        elif time.time() - start_time >= 10:
            print('stopped from time')
            break
        time.sleep(.75)


def notes(dory_mode_excitement_entry):
    c = 262.626
    d = 293.665
    b = 246.943
    e = 329.628
    t = 60000/(dory_mode_excitement_entry + 100)
    song = [(c, t, 5), (e, t, 5), (c, t, 5), (e, t, 5), (c, t, 5), (d, t / 2, 5), (d, t / 2, 5), (b, t, 5), (c, t, 5)]
    return song
