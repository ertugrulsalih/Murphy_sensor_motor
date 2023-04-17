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
