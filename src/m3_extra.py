"""
    Code for sprint 3

    Authors:  Conner Ozatalar.
    Winter term, 2018-2019.
"""
import rosebot as rb
import time

def m3_marlin_deep_sea():
    robot = rb.RoseBot()
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
        robot.sound_system.speech_maker('stay in the shallow water')
        robot.drive_system.go(-10, -10)
        time.sleep(.5)
        robot.drive_system.stop()


def m3_nemo_deep_sea():
    robot = rb.RoseBot()
    robot.drive_system.go(50,50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
    robot.sound_system.speech_maker('Time for an adventure')
    robot.drive_system.go_straight_for_inches_using_encoder(15, 100)
    robot.drive_system.go(-50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 12:
            robot.drive_system.stop()