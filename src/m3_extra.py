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
    robot.sound_system.speech_maker.speak('stay in the shallow water')
    robot.drive_system.go(-20, -20)
    time.sleep(1)
    robot.drive_system.stop()


def m3_nemo_deep_sea(robot):
    print('Nemo deep sea activated')
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 10:
            robot.drive_system.stop()
            break
    robot.sound_system.speech_maker.speak('Time for an adventure')
    robot.drive_system.go_straight_for_inches_using_encoder(25, 100)
    robot.drive_system.go(-50, 50)
    start_time = time.time()
    while True:
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 12:
            stop_from_sees_something(robot)
        elif time.time() - start_time >= 2.3:
            stop_from_time(robot)

def stop_from_sees_something(robot):
    robot.drive_system.stop()
    robot.drive_system.go(70, 70)
    while True:
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 5:
            robot.drive_system.stop()
            break

def stop_from_time(robot):
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(25, 70)
