<<<<<<< HEAD
'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad")
=======
'''Crear un temporizador ascendente'''

from datetime import date, time, datetime, timedelta


class Temporizador:

    def __init__(self, minutos_temporizar):
        self.__minutos_temporizar = self.__set_time(minutos_temporizar)
        self.__fin_temporizador = datetime.now() + timedelta(minutes=self.__minutos_temporizar)
        self.__hora_creación = datetime.now()

    def __set_time(self, _tiempo):
        '''
        Verifica que la variable tiempo _tiempo no sea mayor a 59 ni 
        menor a 0
        '''
        if _tiempo > 59:
            return 59
        elif _tiempo < 1:
            return 1
        else:
            return _tiempo

    def temporizar(self):
        #Si el tiempo actual es igual al tiempo temporizado
        if self.__fin_temporizador.strftime("%I:%M:%S %p") == datetime.now().strftime("%I:%M:%S %p"):
            return True
        else:
            return False

    def get_hora_fin_temp(self):
        return self.__fin_temporizador

    def get_hora_creación(self):
        return self.__hora_creación

continuar = True

tiempo_a_temporizar = int(input("Ingrese los minutos que quiere temporizar (valor entero entre 1 y 59 ): "))

#Vamos a temporizar 1 minuto
temporizador = Temporizador(tiempo_a_temporizar)
hora_fin_temporizador = temporizador.get_hora_fin_temp()
hora_inicio_temp = temporizador.get_hora_creación()

while continuar:

    print("Inicio temporizador: %-20sFin temporizador: %-20sHora actual: %-20s" % ( hora_inicio_temp.strftime("%I:%M:%S %p"), hora_fin_temporizador.strftime("%I:%M:%S %p"), datetime.now().strftime("%I:%M:%S %p") ))

    if temporizador.temporizar():
        continuar = False 
>>>>>>> ba8b20cb1369f6211d547d751fa1ee735de53563
