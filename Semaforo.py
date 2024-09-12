import gpiozero
import time

class semaforo:
    #metodo constructor
    def __init__(self, r, a, v): #recibe el numero del pin al que esta conectado cada led
        #atributos
        self.rojo = gpiozero.LED(r)
        self.amarillo = gpiozero.LED(a)
        self.verde = gpiozero.LED(v)

    #getters
    def get_rojo(self):
        return self.rojo
    def get_amarillo(self):
        return self.amarillo
    def get_verde(self):
        return self.verde

    def encender_semaforo(self, verde): #verde parametro booleano que determina si la posicion inicial del semaforo es o no verde
        if verde:
            while True:
                self.verde.on
                time.sleep(5)
                self.verde.off

                self.amarillo.on
                time.sleep(2)
                self.amarillo.off

                self.rojo.on
                time.sleep(7)
                self.rojo.off
        else:
            while True:
                self.rojo.on
                time.sleep(7)
                self.rojo.off

                self.verde.on
                time.sleep(5)
                self.verde.off

                self.amarillo.on
                time.sleep(2)
                self.amarillo.off