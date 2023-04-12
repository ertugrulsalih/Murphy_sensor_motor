import RPi.GPIO as GPIO
import time

# GPIO pin numaraları
ENA = 17
IN1 = 27
IN2 = 22

def motor_calistir():
    # GPIO pinleri ayarla
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)

    # Motoru çalıştır
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)

    # Zaman sayacı
    start_time = time.time()
    while (time.time() - start_time) < 2:
        pass

    # Motoru durdur
    GPIO.output(ENA, GPIO.LOW)

    # GPIO pinlerini temizle
