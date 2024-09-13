import Semaforo
import Boot

class Main:
    #inicializacion de la clase
    def __init__(self) -> None:
        pass
    
    def main(self):
        #Cambiar el input por el numero del pin que asociado a los leds
        #variables para el primer semaforo
        pin_rojo1 = input('Ingrese el numero de pin para el led rojo del semaforo 1')
        pin_amarillo1 = input('Ingrese el numero de pin para el led amarillo del semaforo 1')
        pin_verde1= input('Ingrese el numero de pin para el led verde del semaforo 1')
        semaforo1 = [True, pin_rojo1, pin_amarillo1, pin_verde1]
        #variables para el segundo semaforo
        pin_rojo2 = input('Ingrese el numero de pin para el led rojo del semaforo 2')
        pin_amarillo2 = input('Ingrese el numero de pin para el led amarillo del semaforo 2')
        pin_verde2 = input('Ingrese el numero de pin para el led amarillo del semaforo 2')
        semaforo2 = [False, pin_rojo2,pin_amarillo2,pin_verde2]
        #Crear y establecer conexion Wi-Fi
        ssid = input('Ingrese el nombre de la red Wi-Fi')
        password = input('Ingrese la contraseña de la red')
        obj_conexion = Boot.Boot(ssid, password)
        obj_conexion.conectar()
        #Crear los obj semaforos y llamar los metodos  
        obj_semaforo1 = Semaforo.semaforo(semaforo1[0],semaforo1[1],semaforo1[2],semaforo1[3])
        obj_semaforo2 = Semaforo.semaforo(semaforo2[0],semaforo2[1],semaforo2[2],semaforo2[3])
        obj_semaforo1.encender_semaforo()
        obj_semaforo2.encender_semaforo()

#llamada al main
if __name__ == '__main__':
    app = Main()
    app.main()