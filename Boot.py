try:
    #Se intenta importar el modulo usocket, si no esta disponible se importa sucket
    import usocket as socket
except:
    import socket

from machine import Pin    
import network
import time
import gc #modulo para la recoleccion de basura
 

class Boot:
    def __init__(self, red, password):
        #ejecutar recoleccion de basura
        gc.collect()
        #credenciales de la red Wi-Fi
        self.ssid = red
        self.password = password
    def conectar(self, l): #el parametro l define el pin que se va a encender para avisara al usuario de la conexion
        #conectar a la red
        station = network.WLAN(network.STA_IF) #crea instancia de la interfaz WLAN
        station.active(True)
        station.connect(self.ssid, self.password) #conecta a la red WiFi
        #Esperar a que la conexion sea exitosa
        while not station.isconnected():
            pass
        #Imprimir información de la conexión
        print('Conexion exitosa')
        print(station.ifconfig())
        #configurar led para avisar del estado de la conexion a la raspberry
        led = Pin(l, Pin.OUT)
        led.value(1)
        time.sleep(5)
        led.value(0)
        