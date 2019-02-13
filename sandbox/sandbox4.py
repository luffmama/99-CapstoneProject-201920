# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
# Robert Kreft
import time

def LED_cycle(self, frequency):
    self.robot.led_system.right_led.turn_on()
    self.robot.led_system.left_led.turn_off()
    k = 1
    while True:
        self.robot.led_system.right_led.turn_off()
        self.robot.led_system.left_led.turn_off()
        time.sleep(k * (self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) / int(frequency))
        self.robot.led_system.right_led.turn_on()
        self.robot.led_system.left_led.turn_off()
        time.sleep(k * (self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) / int(frequency))
