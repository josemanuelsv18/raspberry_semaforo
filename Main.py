import Semaforo

class Main:
    #inicializacion de la clase
    def __init__(self) -> None:
        pass
    
    def main(self):
        #Cambiar el None por los valores de los pins que se conecten a los leds en la placa
        #variables para el primer semaforo
        pin_rojo1 = None
        pin_amarillo1 = None
        pin_verde1= None
        semaforo1 = [True, pin_rojo1, pin_amarillo1, pin_verde1]
        #variables para el segundo semaforo
        pin_rojo2 = None
        pin_amarillo2 = None
        pin_verde2 = None
        semaforo2 = [False, pin_rojo2,pin_amarillo2,pin_verde2]
        #Crear los obj semaforos y llamar los metodos
        obj_semaforo1 = Semaforo.semaforo(semaforo1[0],semaforo1[1],semaforo1[2],semaforo1[3])
        obj_semaforo2 = Semaforo.semaforo(semaforo2[0],semaforo2[1],semaforo2[2],semaforo2[3])
        obj_semaforo1.encender_semaforo()
        obj_semaforo2.encender_semaforo()

#llamada al main
if __name__ == '__main__':
    app = Main()
    app.main()