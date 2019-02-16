"""
    Code for sprint 3

    Authors:  Conner Ozatalar.
    Winter term, 2018-2019.
"""
import rosebot as rb
import time

# feature 1: going into deep sea
def m3_marlin_deep_sea(robot):
    print('Marlin deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
        robot.sound_system.speech_maker('stay in the shallow water')
        robot.drive_system.go(-10, -10)
        time.sleep(.5)
        robot.drive_system.stop()


def m3_nemo_deep_sea(robot):
    print('Nemo deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
    robot.sound_system.speech_maker('Time for an adventure')
    robot.drive_system.go_straight_for_inches_using_encoder(15, 100)
    robot.drive_system.go(-50, 50)
    start_time = time.localtime()
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 12:
            stop_from_sees_something(robot)
        elif time.localtime() - start_time >= 2:
            stop_from_full_rotation(robot)

def stop_from_sees_something(robot):
    robot.drive_system.stop()
    robot.drive_system.go(70, 70)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 3:
            robot.drive_system.stop()
            break

def stop_from_full_rotation(robot):
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(15, 70)
