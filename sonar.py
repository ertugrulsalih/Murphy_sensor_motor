import RPi.GPIO as GPIO

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

# Fonksiyonu tanımlayın
def measure_distance_and_trigger_buzzer():
    # TRIG_PIN'i yüksek seviyeye ayarlayarak bir ping gönderin
    GPIO.output(TRIG_PIN, True)
    GPIO.output(TRIG_PIN, False)

    # ECHO_PIN'deki yüksek seviye süresini ölçün
    GPIO.wait_for_edge(ECHO_PIN, GPIO.RISING)
    pulse_start = time.time()
    GPIO.wait_for_edge(ECHO_PIN, GPIO.FALLING)
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
    except KeyboardInterrupt:
        # Ctrl+C ile kesildiğinde GPIO pinlerini temizle ve çık
        GPIO.cleanup()
        break
