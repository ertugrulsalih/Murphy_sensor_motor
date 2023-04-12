import RPi.GPIO as GPIO
import time

# GPIO pin numaraları
ENA = 17
IN1 = 27
IN2 = 22

def motor_calistir():
    # GPIO pinlerini ayarla
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)

    # Motoru çalıştır
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(ENA, GPIO.HIGH)

    # Zamanlayıcı başlat
    t0 = time.time()

    # 2 saniye boyunca motoru çalıştır
    while time.time() - t0 < 2:
        pass

    # Motoru durdur
    GPIO.output(ENA, GPIO.LOW)

    # Zaman sayacını durdur ve ekrana yazdır
    elapsed_time = time.time() - t0
    print("Motor çalışma süresi: {:.2f} saniye".format(elapsed_time))

    # GPIO pinlerini temizle
    GPIO.cleanup()

# Fonksiyonu çağır
motor_calistir()
