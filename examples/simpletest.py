from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


def angle_to_pulse(angle):
  angle = angle % 180
  return (2.5*angle)+150

def move_motor(motorN, inputAngle):
  motorN = (motorN-1)*4
  
  pwm = Adafruit_PCA9685.PCA9685(address=0x40)

  servo_min = 150  # Min pulse length out of 4096
  servo_max = 600  # Max pulse length out of 4096
                               
  pwm.set_pwm_freq(60)
  
  pwm.set_pwm(motorN, 0, angle_to_pulse(inputAngle))
  time.sleep(2)
  pwm.set_pwm(0, 0, angle_to_pulse(90))
  pwm.set_pwm(4, 0, angle_to_pulse(90))
  pwm.set_pwm(8, 0, angle_to_pulse(90))
  
def move_lamp_no():
  
  pwm = Adafruit_PCA9685.PCA9685(address=0x40)

  servo_min = 150  # Min pulse length out of 4096
  servo_max = 600  # Max pulse length out of 4096         
  pwm.set_pwm_freq(60)
  
  pwm.set_pwm(0, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(0, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(0, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(0, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
    
  pwm.set_pwm(0, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(0, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(0, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(0, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
  
  pwm.set_pwm(4, 0, angle_to_pulse(90))
      
      
def move_lamp_yes():
  pwm = Adafruit_PCA9685.PCA9685(address=0x40)

  servo_min = 150  # Min pulse length out of 4096
  servo_max = 600  # Max pulse length out of 4096         
  pwm.set_pwm_freq(60)
  
  pwm.set_pwm(4, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(4, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(4, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(4, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
    
  pwm.set_pwm(4, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(4, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(4, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(4, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
  pwm.set_pwm(4, 0, angle_to_pulse(90))
                
def move_lamp_yes_1():
  pwm = Adafruit_PCA9685.PCA9685(address=0x40)

  servo_min = 150  # Min pulse length out of 4096
  servo_max = 600  # Max pulse length out of 4096         
  pwm.set_pwm_freq(60)
  
  pwm.set_pwm(8, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(8, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(8, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(8, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
    
  pwm.set_pwm(8, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(8, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(8, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(8, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
  pwm.set_pwm(8, 0, angle_to_pulse(90))
  
def motor_test():
  pwm = Adafruit_PCA9685.PCA9685(address=0x40)

  servo_min = 150  # Min pulse length out of 4096
  servo_max = 600  # Max pulse length out of 4096         
  pwm.set_pwm_freq(60)
  
  pwm.set_pwm(0, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(0, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(0, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(0, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
  
  pwm.set_pwm(4, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(4, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(4, 0, angle_to_pulse(60))
  
  for i in range(0,30):
    pwm.set_pwm(4, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
  pwm.set_pwm(8, 0, angle_to_pulse(30))
  
  for i in range(0,30):
    pwm.set_pwm(8, 0, angle_to_pulse(30+i))
    time.sleep(0.05)
      
  pwm.set_pwm(8, 0, angle_to_pulse(60))
  
  for i in range(8,30):
    pwm.set_pwm(0, 0, angle_to_pulse(60-i))
    time.sleep(0.05)
    
  pwm.set_pwm(0, 0, angle_to_pulse(90))
  pwm.set_pwm(4, 0, angle_to_pulse(90))
  pwm.set_pwm(8, 0, angle_to_pulse(90))
  
  
  
  
  
                
