import Semaforo
import threading
#import Boot

class Main:
    #inicializacion de la clase
    def __init__(self) -> None:
        pass
    
    def main(self):
        #Cambiar el input por el numero del pin que asociado a los leds
        #variables para el primer semaforo
        pin_rojo1 = 0
        pin_amarillo1 = 1
        pin_verde1= 2
        semaforo1 = [True, pin_rojo1, pin_amarillo1, pin_verde1]
        #variables para el segundo semaforo
        pin_rojo2 = 5
        pin_amarillo2 = 4
        pin_verde2 = 3
        semaforo2 = [False, pin_rojo2,pin_amarillo2,pin_verde2]
        #Crear y establecer conexion Wi-Fi
        #ssid = input('Ingrese el nombre de la red Wi-Fi')
        #password = input('Ingrese la contraseña de la red')
        #obj_conexion = Boot.Boot(ssid, password)
        #obj_conexion.conectar()
        #Crear los obj semaforos y llamar los metodos  
        obj_semaforo1 = Semaforo.semaforo(semaforo1[0],semaforo1[1],semaforo1[2],semaforo1[3])
        obj_semaforo2 = Semaforo.semaforo(semaforo2[0],semaforo2[1],semaforo2[2],semaforo2[3])
        #Crear hilos para que ambos semaforos funcionen en paralelo
        thread_semaforo1 = threading.Thread(obj_semaforo1.encender_semaforo())
        thread_semaforo2 = threading.Thread(obj_semaforo2.encender_semaforo())
        #iniciar los hilos
        thread_semaforo1.start()
        thread_semaforo2.start()
        #esperar el final de los hilos (a pesar de que se tienen bucles infinitos)
        thread_semaforo1.join()
        thread_semaforo2.join()
        

#llamada al main
if __name__ == '__main__':
    app = Main()
    app.main()