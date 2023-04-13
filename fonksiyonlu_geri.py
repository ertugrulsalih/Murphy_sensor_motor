import RPi.GPIO as GPIO
import time

# GPIO pin numaralarını ayarlama
IN1_PIN = 15
IN2_PIN = 13
ENA_PIN = 11

# GPIO pinlerini kullanılabilir hale getirme
def geri():
    print("Motorlar ileri gidiyor")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1_PIN, GPIO.OUT)
    GPIO.setup(IN2_PIN, GPIO.OUT)
    GPIO.setup(ENA_PIN, GPIO.OUT)

# Motorun geriye dönmesini sağlama
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.HIGH)

# Motoru çalıştırma
    GPIO.output(ENA_PIN, GPIO.HIGH)

# Başlangıç zamanını kaydetme
    start_time = time.time()

# 2 saniye boyunca motorun çalışmasını sağlama
    while time.time() - start_time < 1.5:
        pass

# Motoru durdurma
    GPIO.output(ENA_PIN, GPIO.LOW)

    GPIO.cleanup()

geri()

    
