from abc import ABC,abstractmethod
import hashlib
from pago import Pago
class Usuario(ABC):
    __nombre: str
    __apellido: str
    __telefono: str
    __dni: int
    __contrasenia: str
    
    def __init__(self,nombre,apellido,telefono,dni,contrasenia):
        self.__nombre = nombre
        self.__apellido =apellido
        self.__telefono =telefono
        self.__dni = dni
        self.__contrasenia =contrasenia
    
    def get_contrasenia(self):
        return self.__contrasenia
    
    def get_dni(self):
        return self.__dni
    
    def get_nombre(self):
        return self.__nombre+'\n'+self.__apellido

    def MostrarDatos(self):
        print (f'Nombre y apellido: {self.__nombre} {self.__apellido} \t Dni: {self.__dni} \t Telefono:{self.__telefono}')
    
    @abstractmethod
    def Moddatos(self):
        pass


class Socio(Usuario):
    __cuotas: int
    __tipo: str
    __reg_turnos: list
    __pagos: list
    
    def __init__(self, nombre,apellido,telefono,dni,contrasenia,tipo='Musculación'):
        super().__init__(nombre,apellido,telefono,dni,contrasenia)
        self.__cuotas = 0
        self.__tipo = tipo
        self.__reg_turnos = []
        self.__pagos = []

    def __del__(self):
        for pago in self.__pagos:
            print (str(pago)+'\tELIMINADO\n')
            del pago

    
    def pagar_cuota(self,pago=7000):
        pago=Pago(pago)
        self.__cuotas+=1
        self.__pagos.append(pago)
    
    def ult_pago(self):
        print (self.__pagos[self.__cuotas-1])

    def turno(self,reg_turn):
        self.__reg_turnos.append(reg_turn)
    
    def mostrar_registro(self):
        for turno in self.__reg_turnos:
            print (str(turno)+'\n')

    def Moddatos(self,t):
        self.__tipo=t
    
    def MostrarDatos(self):
        super().MostrarDatos()
        print(f'Tipo de entrenamiento:{self.__tipo}\t Cuotas pagadas:{self.__cuotas}')


class Entrenador(Usuario):
    __capacitacion:str
    
    def __init__(self, nombre, apellido, telefono, dni, contrasenia,capacitacion):
        super().__init__(nombre, apellido, telefono, dni, contrasenia)
        self.__capacitacion=capacitacion
        self.__turnos=[]
        
    def Agregar_turno(self,turno):
        if len(self.__turnos)<4:
            self.__turnos.append(turno)
        else:
            print('Ya tiene 4 turnos asignados')
    
    def MostrarDatos(self):
        super().MostrarDatos()
        print(f'Capacitacion: {self.__capacitacion}')
    
    def Moddatos(self,capacitacion):
        self.__capacitacion=capacitacion