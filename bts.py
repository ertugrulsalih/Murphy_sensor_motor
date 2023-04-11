import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BOARD)

ena = 11
in2 = 13
in1 = 15
in3 = 16 
in4 = 18
enb = 22

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

def ileri():
    print("Motorlar ileri gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def geri():
    print("Motorlar geri gidiyor")
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def sol():
    print("Motorlar saga gidiyor")
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def sag():
    print("Motorlar sola gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(ena,GPIO.HIGH)
    
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(enb,GPIO.HIGH) 
    
def dur():
    print("Motorlar durdu.")
    GPIO.output(ena,GPIO.LOW)
    GPIO.output(enb,GPIO.LOW) 
    
try:
    while True:
        ileri()
        time.sleep(2)
        dur()
        time.sleep(1)
        
        geri()
        time.sleep(2)
        dur()
        time.sleep(1)
        
        sol()
        time.sleep(2)
        dur()
        time.sleep(1)
        
        sag()
        time.sleep(2)
        dur()
        time.sleep(1)
        
    
except:
    GPIO.cleanup()
    
    
    
    
