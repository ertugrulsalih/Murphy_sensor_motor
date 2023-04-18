import RPi.GPIO as GPIO
import time

# GPIO pin numaralarını tanımlayın
TRIG_PIN = 29
ECHO_PIN = 31
BUZZER_PIN = 33

# Yeni sensör pin numaralarını tanımlayın
TRIG_PIN_2 = 32
ECHO_PIN_2 = 36

# BCM modunu kullanarak GPIO'yu yapılandırın
GPIO.setmode(GPIO.BCM)

# TRIG_PIN_2'yi çıkış olarak ayarlayın ve ECHO_PIN_2'yi giriş olarak ayarlayın
GPIO.setup(TRIG_PIN_2, GPIO.OUT)
GPIO.setup(ECHO_PIN_2, GPIO.IN)

def measure_distance_2():
    # TRIG_PIN_2'yi yüksek seviyeye ayarlayarak bir ping gönderin
    GPIO.output(TRIG_PIN_2, True)
    GPIO.output(TRIG_PIN_2, False)

    # ECHO_PIN_2'deki yüksek seviye süresini ölçün
    GPIO.wait_for_edge(ECHO_PIN_2, GPIO.RISING)
    pulse_start = time.time()
    GPIO.wait_for_edge(ECHO_PIN_2, GPIO.FALLING)
    pulse_end = time.time()

    # Mesafeyi hesaplayın
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    # Mesafeyi ekrana yazdırın
    print("Mesafe 2: {} cm".format(distance))

# Sonsuz bir döngüde sensörü okuyun ve buzzer'ı kontrol edin
while True:
    try:
        measure_distance_and_trigger_buzzer()
        measure_distance_2()
    except KeyboardInterrupt:
        # Ctrl+C ile kesildiğinde GPIO pinlerini temizle ve çık
        GPIO.cleanup()
        break
