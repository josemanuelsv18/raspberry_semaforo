from machine import Pin
import time

class semaforo:
    #metodo constructor
    def __init__(self,inicial,r, a, v): #recibe el numero del pin al que esta conectado cada led
        #atributos
        self.rojo = Pin(r, Pin.OUT)
        self.amarillo = Pin(a, Pin.OUT)
        self.verde = Pin(v, Pin.OUT)
        self.inicial = inicial

    #getters
    def get_rojo(self):
        return self.rojo
    def get_amarillo(self):
        return self.amarillo
    def get_verde(self):
        return self.verde
    def get_inicial(self):
        return self.inicial

    def encender_semaforo(self): 
        if self.inicial: #inicial parametro booleano que determina si la posicion inicial del semaforo es o no verde
            while True:
                self.verde.value(1)
                self.amarillo.value(0)
                self.rojo.value(0)
                print('Semaforo 1 VERDE')
                time.sleep(5)
                self.verde.off()

                self.amarillo.value(1)
                print('Semaforo 1 AMARILLO')
                time.sleep(2)
                self.amarillo.value(0)

                self.rojo.value(1)
                print('Semaforo 1 ROJO')
                time.sleep(7)
                self.rojo.value(0)
        else:
            while True:
                self.rojo.value(1)
                self.amarillo.value(0)
                self.verde.value(0)
                print('Semaforo 2 ROJO')
                time.sleep(7)
                self.rojo.value(0)

                self.verde.value(1)
                print('Semaforo 2 VERDE')
                time.sleep(5)
                self.verde.value(0)

                self.amarillo.value(1)
                print('Semaforo 2 AMARILLO')
                time.sleep(2)
                self.amarillo.value(0)