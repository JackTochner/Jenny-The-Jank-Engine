import gpiozero


def obstacle_avoid():

    while True:
        pwm1.value = 0.5
        pwm2.value = 0.5

        

    
    


if __name__ == "__main__":
    sensorFront1 = gpiozero.DistanceSensor(echo=23,trigger=5)     
    sensorFront2 = gpiozero.DistanceSensor(echo=24,trigger=6)     
    sensorSide1 = gpiozero.DistanceSensor(echo=25,trigger=7) 
    sensorSide2 = gpiozero.DistanceSensor(echo=26,trigger=8) 
    
    pwm1 = gpiozero.PWMOutputDevice(pin=12,active_high=True,initial_value=0,frequency=50000)
    pwm2 = gpiozero.PWMOutputDevice(pin=13,active_high=True,initial_value=0,frequency=50000)
    
    direction1 = gpiozero.OutputDevice(pin=4)
    direction2 = gpiozero.OutputDevice(pin=27)
   
    forward = not direction1.value
    
    error = 0.1

    distanceFront1 = sensorFront1.distance * 100 
    distanceFront2 = sensorFront2.distance * 100  

    obstacle_avoid()
