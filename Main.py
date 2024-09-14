import uasyncio as asyncio
from Semaforo import Semaforo

class Main:
    def __init__(self) -> None:
        pass
    
    async def main(self):
        # Pines para el primer semáforo
        pin_rojo1 = 0
        pin_amarillo1 = 1
        pin_verde1 = 2
        semaforo1 = [True, pin_rojo1, pin_amarillo1, pin_verde1]
        
        # Pines para el segundo semáforo
        pin_rojo2 = 5
        pin_amarillo2 = 4
        pin_verde2 = 3
        semaforo2 = [False, pin_rojo2, pin_amarillo2, pin_verde2]
        
        # Crear los objetos semáforos
        obj_semaforo1 = Semaforo(semaforo1[0], semaforo1[1], semaforo1[2], semaforo1[3])
        obj_semaforo2 = Semaforo(semaforo2[0], semaforo2[1], semaforo2[2], semaforo2[3])
        
        # Crear tareas para los semáforos
        tarea_semaforo1 = asyncio.create_task(obj_semaforo1.encender_semaforo())
        tarea_semaforo2 = asyncio.create_task(obj_semaforo2.encender_semaforo())
        
        # Ejecutar las tareas en paralelo
        await asyncio.gather(
            tarea_semaforo1,
            tarea_semaforo2
        )

# Llamada al main
if __name__ == '__main__':
    asyncio.run(Main().main())