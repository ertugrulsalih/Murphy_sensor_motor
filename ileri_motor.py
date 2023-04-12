import RPi.GPIO as GPIO
import time

# L298N motor sürücüsü için GPIO pinlerini tanımlayın
ENA = 17
IN1 = 27
IN2 = 22

# GPIO pinlerini BCM modunda yapılandırın
GPIO.setmode(GPIO.BCM)

# GPIO pinlerini çıkış olarak ayarlayın
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Fonksiyon tanımlama
def run_motor():
    # Motoru 2 saniye boyunca çalıştırın
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)
    start_time = time.time()
    while (time.time() - start_time) < 2:
        continue

    # Motoru durdurun
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# GPIO pinlerini temizleme
GPIO.cleanup()
