from gpiozero import OutputDevice
from time import sleep

# GPIO pin numaralarını ayarlama
IN1_PIN = 15
IN2_PIN = 13
ENA_PIN = 11

# GPIO pinlerini kullanılabilir hale getirme
def ileri():
    print("Motorlar ileri gidiyor")
    in1 = OutputDevice(IN1_PIN)
    in2 = OutputDevice(IN2_PIN)
    ena = OutputDevice(ENA_PIN)

    # Motorun ileriye dönmesini sağlama
    in1.on()
    in2.off()

    # Motoru çalıştırma
    ena.on()

    # Başlangıç zamanını kaydetme
    start_time = time.time()

    # 2 saniye boyunca motorun çalışmasını sağlama
    while time.time() - start_time < 1.5:
        pass

    # Motoru durdurma
    ena.off()

ileri()

#veya

import gpiozero
import time

# GPIO pin numaralarını ayarlama
IN1_PIN = 15
IN2_PIN = 13
ENA_PIN = 11

# Motorun geriye dönmesini sağlama
def geri():
    print("Motorlar geriye gidiyor")
    motor = gpiozero.Motor(IN1_PIN, IN2_PIN, pwm=True)
    motor.backward()

# Motoru çalıştırma
    motor.enable = True

# Başlangıç zamanını kaydetme
    start_time = time.time()

# 1.5 saniye boyunca motorun çalışmasını sağlama
    while time.time() - start_time < 1.5:
        pass

# Motoru durdurma
    motor.enable = False
    motor.close()

geri()
