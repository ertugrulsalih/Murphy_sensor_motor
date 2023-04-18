import RPi.GPIO as GPIO
import time

# GPIO pin numaralarını tanımlayın
TRIG_PIN = 29
ECHO_PIN = 31
BUZZER_PIN = 33

# BCM modunu kullanarak GPIO'yu yapılandırın
GPIO.setmode(GPIO.BCM)

# TRIG_PIN'i çıkış olarak ayarlayın ve ECHO_PIN'i giriş olarak ayarlayın
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
# BUZZER_PIN'i çıkış olarak ayarlayın
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# TRIG_PIN'i düşük seviyeye ayarlayarak sensörü başlatın
GPIO.output(TRIG_PIN, False)
time.sleep(0.5)

# Fonksiyonu tanımlayın
def measure_distance_and_trigger_buzzer():
    # TRIG_PIN'i yüksek seviyeye ayarlayarak bir ping gönderin
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # ECHO_PIN'deki yüksek seviye süresini ölçün
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Mesafeyi hesaplayın
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    # Mesafeyi ekrana yazdırın
    print("Mesafe: {} cm".format(distance))

    # Mesafe 80 cm'den küçükse buzzer'ı çal
    if distance < 80:
        GPIO.output(BUZZER_PIN, True)
    else:
        GPIO.output(BUZZER_PIN, False)

# Sonsuz bir döngüde sensörü okuyun ve buzzer'ı kontrol edin
while True:
    try:
        measure_distance_and_trigger_buzzer()
        time.sleep(1)
    except KeyboardInterrupt:
        # Ctrl+C ile kesildiğinde GPIO pinlerini temizle ve çık
        GPIO.cleanup()
        break
