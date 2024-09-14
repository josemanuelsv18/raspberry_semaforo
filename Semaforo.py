from machine import Pin
import uasyncio as asyncio

class Semaforo:
    def __init__(self, inicial, r, a, v):
        self.rojo = Pin(r, Pin.OUT)
        self.amarillo = Pin(a, Pin.OUT)
        self.verde = Pin(v, Pin.OUT)
        self.inicial = inicial

    async def encender_semaforo(self):
        if self.inicial:
            while True:
                self.verde.value(1)
                self.amarillo.value(0)
                self.rojo.value(0)
                print('Semáforo 1 VERDE')
                await asyncio.sleep(5)
                self.verde.value(0)

                self.amarillo.value(1)
                print('Semáforo 1 AMARILLO')
                await asyncio.sleep(2)
                self.amarillo.value(0)

                self.rojo.value(1)
                print('Semáforo 1 ROJO')
                await asyncio.sleep(7)
                self.rojo.value(0)
        else:
            while True:
                self.rojo.value(1)
                self.amarillo.value(0)
                self.verde.value(0)
                print('Semáforo 2 ROJO')
                await asyncio.sleep(7)
                self.rojo.value(0)

                self.verde.value(1)
                print('Semáforo 2 VERDE')
                await asyncio.sleep(5)
                self.verde.value(0)

                self.amarillo.value(1)
                print('Semáforo 2 AMARILLO')
                await asyncio.sleep(2)
                self.amarillo.value(0)