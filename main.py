from usuario import Socio, Entrenador
from turno import Turno
from registro import Registro_de_turno
from pago import Pago
from datetime import date

if __name__ == '__main__':
    s=Socio('Juan', 'Perez','2645600343',11111111,111)
    e=Entrenador('John','Ramirez','2645781020',12111111,124,'musculacion')
    t1=Turno(date(2023,9,25),'08:00','10:00',15,e)
    t2=Turno(date(2023,9,26),'08:00','10:00',15,e)
    t2=Turno(date(2023,9,27),'08:00','10:00',15,e)
    t3=Turno(date(2023,9,28),'08:00','10:00',15,e)
    t4=Turno(date(2023,9,29),'08:00','10:00',15,e)
    t5=Turno(date(2023,9,25),'08:00','10:00',15,e)
    e.Agregar_turno(t1)
    e.Agregar_turno(t2)
    e.Agregar_turno(t3)
    e.Agregar_turno(t4)
    e.Agregar_turno(None)
    print('1) '+str(t1)+'\n2) '+str(t2)+'\n3) '+str(t3)+'\n4) '+str(t4)+'\n')
    x=int(input('Ingrese turno deseado'))
    while x>0 and x<5:
        match x:
            case 1:
                t1.sacar_turno(s)
            case 2:
                t2.sacar_turno(s)
            case 3:
                t3.sacar_turno(s)
            case 4:
                t4.sacar_turno(s)
        x=int(input('Ingrese turno deseado'))
    s.mostrar_registro()
    print ('sin cambios')
    s.MostrarDatos()
    s.Moddatos('Cardio')
    s.pagar_cuota()
    print('con cambios y ultima cuota pagada:')
    s.MostrarDatos()
    s.ult_pago()
    print ('sin cambios')
    e.MostrarDatos()
    e.Moddatos('Resistencia')
    print('con cambios')
    e.MostrarDatos()
        