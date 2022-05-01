'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

°Ingredientes vegetarianos: Pimiento y tofu.
°Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes 
disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar 
por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

tipo_pizza = input("¿Quiere una piza vegetariana o no? (SI/NO): ")
ingredientes = None
pizza = None

if tipo_pizza.lower() == "si":
    pizza = "vegetariana"
    print("Ingredientes pizza vegetariana:\n1) Pimiento\n2) Tofu\n")
    seleccion = input("Elige un solo ingrediente: ")

    if seleccion == "1":
        ingredientes = "pimiento"
    elif seleccion == "2":
        ingredientes = "tofu"

else:
    pizza = "no vegetariana"
    print("Ingredientes pizza no vegetariana:\n1) Peperoni\n2) Jamón\n3) Salmón")
    seleccion = input("Elige un solo ingrediente: ")

    if seleccion == "1":
        ingredientes = "peperoni"
    elif seleccion == "2":
        ingredientes = "jamón"
    elif seleccion == "3":
        ingredientes = "salmón"


print("El tipo de pizza elegido es: " + pizza)
print("Los ingredientes son: mozzarella, tomate y " + ingredientes)
