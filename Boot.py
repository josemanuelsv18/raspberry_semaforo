try:
    #Se intenta importar el modulo usocket, si no esta disponible se importa sucket
    import usocket as socket
except:
    import socket
    
import network
import _thread

import gc #modulo para la recoleccion de basura
gc.collect() #ejecutar recoleccion de basura

class Boot:
    def __init__(self, red, password):
        #credenciales de la red Wi-Fi
        self.ssid = red
        self.password = password
    def conectar(self):
        #conectar a la red
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while not wlan.isconnected():
            pass
        # Imprimir información de la conexión
        print('Conexion exitosa')
        print(wlan.ifconfig())
        #obtener la ip
        ip = wlan.ifconfig()[0]
        print(f'Conectado a {self.ssid} con IP: {ip}')