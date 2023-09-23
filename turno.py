from datetime import date
from registro import Registro_de_turno
class Turno:
    __fecha: date
    __inicio: str
    __fin: str
    __cupo: int
    __entrenador: object
    __registros: list

    def __init__(self, fecha, inicio, fin, cupo=15,entrenador=None):
        self.__fecha = fecha
        self.__inicio = inicio
        self.__fin = fin
        self.__cupo = cupo
        self.__entrenador = entrenador
        self.__registros = []
    
    def __str__(self) -> str:
        return f'{self.__fecha} Inicia:{self.__inicio}  Finaliza:{self.__fin} Entrenador:{self.__entrenador.get_nombre()}'

    def set_entrenador(self, entrenador):
        self.__entrenador = entrenador
    
    def sacar_turno(self, socio):
        if self.__cupo==0:
            print('Sin cupo disponible.')
            return
        horario= self.__inicio+' - '+self.__fin
        reg=Registro_de_turno(self.__fecha,horario,self,socio)
        self.__cupo-=1
        self.__registros.append(reg)
        socio.turno(reg)
        print('Cupo disponible:'+str(self.__cupo))
