'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))

if divisor == 0:
    print("Error!!! Divisor no puede ser 0")
else:
    print("El resultado de la división es: %0.4f" % (dividendo/divisor))