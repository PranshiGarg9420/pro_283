from controller import Robot
from controller import Motor
from controller import Altimeter
import math

class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timestep=32
        
        self.distanceSensor= self.getDevice('ds0')
        self.distanceSensor.enable(self.timestep)

        self.accelerometer= self.getDevice('accelerometer')
        self.accelerometer.enable(self.timestep)
        
        self.front_led= self.getDevice("front led")
        self.back_led= self.getDevice("back led")
        self.left_led= self.getDevice("left led")
        self.right_led= self.getDevice("right led")
        
        self.left_motor= self.getDevice("left wheel motor")
        self.left_motor.setPosition(math.inf)
        self.right_motor= self.getDevice("right wheel motor")
        self.right_motor.setPosition(math.inf)
        
        self.left_motor.setVelocity(0.5)
        self.right_motor.setVelocity(0.5)
        self.direction_switch=True
        self.accValues=[]
        
     
    def run(self):
        while self.step(self.timestep)!= -1:
            print(self.accelerometer.getValues())
            for i in range(3):
                self.accValues.append(self.accelerometer.getValues())
                
                if(abs(self.accvalues[1])> abs(self.accValues[0])):
                    self.front_led.set(false)
                    self.back_led.set(false)
                    self.left_led.set(self.accValues[1]>0.0)
                    self.right_led.set(self.accValues[1]<0.0)
                else:
                    self.front_led.set(self.accValues[1]<0.0)
                    self.back_led.set(self.accValues[1]>0.0)
                    self.left_led.set(false)
                    self.right_led.set(true) 
                self.accValues=[]

controller= MyController()
controller.run()        