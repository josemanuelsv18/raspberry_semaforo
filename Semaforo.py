import gpiozero

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
    

    def encender_semaforo(self):
        pass