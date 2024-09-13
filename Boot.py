try:
    #Se intenta importar el modulo usocket, si no esta disponible se importa sucket
    import usocket as socket
except:
    import socket
    
import network
from machine import Pin #modulo Pin de la biblioteca machine

import gc #modulo para la recoleccion de basura
gc.collect() #ejecutar recoleccion de basura

class Boot:
    def __init__(self, red, password):
        #credenciales de la red Wi-Fi
        self.ssid = red
        self.password = password
    def conectar(self):
        station = network.WLAN(network.STA_IF) #instancia de la interfaz WLAN
        station.active(True) #activar la interfaz
        station.connect(self.ssid, self.password) #conectar a la red Wi-Fi
        #Espera la conexion exitosa
        while station.isconnected() == False:
            pass
        #informar sobre la conexion
        print('conexion establecida correctamente')
        print(station.ifconfig())