from machine import Pin, ADC, PWM
import utime
import dht
import network

# Define el pin al que está conectado el sensor DHT11
pin_dht = Pin(15, Pin.IN)

# Crea una instancia del objeto DHT11
sensor_dht = dht.DHT11(pin_dht)

# Configuración de la red WiFi
ssid = "Extreme 1"
password = "bamajpfm2225"
hostname = "santiago"

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(dhcp_hostname=hostname)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass

    print("Conexión a la red exitosa")

# Comprobar la conexión WiFi una vez
connect_to_wifi()

# Entrar en el bucle de medición si hay conexión WiFi
while True:
    sensor_dht.measure()
    print("Temperatura=" + str(sensor_dht.temperature()) + "°C, Humedad=" + str(sensor_dht.humidity()))
    utime.sleep(4)
