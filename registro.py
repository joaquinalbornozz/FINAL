from datetime import date

class Registro_de_turno:
    __fecha_reserva: date
    __fecha_turno: date
    __Horario: str

    def __init__(self,f_turno,horario,turno,socio):
        self.__fecha_reserva = date.today()
        self.__fecha_turno=f_turno
        self.__horario = horario
        self.__turno = turno
        self.__socio = socio
    
    def __str__(self) -> str:
        return f'Reservado:{self.__fecha_reserva} Fecha de turno:{self.__fecha_turno} Horario:{self.__horario}'
