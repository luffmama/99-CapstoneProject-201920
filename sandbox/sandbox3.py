# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.
#Conner_Ozatalar
def pick_up_object_while_beeping(self):
    self.DriveSystem.go(100)
    while True:
        self.SoundSystem.beeper.beep()
        if self.SensorSystem.ir_proximity_sensor.get.distance() <= 4:
            self.DriveSystem.stop()
            self.ArmAndClaw.lower_arm()