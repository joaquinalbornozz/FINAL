from datetime import date, datetime
from random import random
class Pago:
    __Fecha_pago: date
    __Pago: float
    __Codigo: int

    def __init__(self,pago) -> None:
        self.__Fecha_pago = datetime.today()
        self.__Codigo = random()
        self.__Pago = pago
    
    def __str__(self):
        return f'Fecha de pago: {self.__Fecha_pago}\t Importe: {self.__Pago}\t Código: {self.__Codigo}\n'