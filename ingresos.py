nombre = input("Hola mi perro, como se llama tu nombre?")
ventas = float(input(f"Hola {nombre}, cuanto has vendido en el mes?"))
print(ventas)
print("Deja calculo tus comisiones basadas en el 13% total")

resultado = round(ventas * 13 / 100,2)

print(f"El total de tus comisiones es: ${resultado}")
