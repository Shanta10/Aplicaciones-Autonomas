from umqtt.simple import MQTTClient
import network
import time
from machine import Pin, PWM

# Configuración de WiFi
ssid = 'Santiago'
password = '12345678'
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    pass

# Configuración de Thinger.io
user = 'shanta10'
device = 'Temp'
password_thinger = 'Sl1234.'

# Inicialización del cliente MQTT con usuario y contraseña
client = MQTTClient(client_id=device, server='backend.thinger.io', user=user, password=password_thinger, ssl=True)

# Configuración de botón y servo motor
button = Pin(23, Pin.IN, Pin.PULL_UP)  # Pin del botón
servo_pin = Pin(14)  # Pin del servo motor
servo = PWM(servo_pin, freq=50)  # Configurar el servo motor con frecuencia de 50 Hz
angle = 0  # Variable para almacenar el ángulo actual del servo
increment = 40  # Incremento de ángulo

# Función para mover el servo motor
def move_servo(angle):
    duty = 30 + (angle / 180) * 140  # Convertir ángulo a ciclo de trabajo (30 a 170)
    servo.duty(int(duty))
    return angle

# Función para controlar el servo motor según el estado del botón
def control_servo():
    global angle
    if button.value() == 0:  # Si se presiona el botón
        angle += increment  # Aumentar el ángulo
        if angle > 180:  # Si supera 180 grados
            angle = 0  # Regresar a 0 grados
        angle_sent = move_servo(angle)  # Mover el servo y obtener el ángulo enviado
        send_to_thinger(angle_sent)  # Enviar el ángulo a Thinger.io
        print("Ángulo enviado a Thinger.io:", angle_sent)  # Imprimir el ángulo en la consola
        time.sleep(0.5)  # Esperar un tiempo para evitar rebotes del botón

# Función para enviar el ángulo a Thinger.io
def send_to_thinger(angle_sent):
    topic = 'v2/users/{}/devices/{}/Data/Temp'.format(user, device)
    message = '{{"angle": {}}}'.format(angle_sent)
    client.connect()
    client.publish(topic, message)
    client.disconnect()

# Bucle principal
while True:
    control_servo()
    time.sleep(0.1)  # Pequeña pausa para evitar el uso excesivo de CPU
