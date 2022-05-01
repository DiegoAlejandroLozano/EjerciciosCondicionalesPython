'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e
imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

CONTRASEÑA = "luna1852"

contraseña_usuario = input("Ingrese la contraseña: ").lower()

if CONTRASEÑA == contraseña_usuario:
    print("La contraseña es la correcta")
else:
    print("La contraseña no coincide")