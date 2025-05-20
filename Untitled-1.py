cantidad_perros = int(input("ingrese la cantidad de perros"))
cuota_minima = int(input("ingrese la cuota minima de conejos"))
cumplieron = 0
no_cumplieron = 0
for i in range (1, cantidad_perros + 1):
    conejos = int(input(f"ingrese la cantidad de conejos que trajo el perro {i}:"))
    if conejos >= cuota_minima:
        print(f"el perro {i} cumplio la cuota. ¡recibe filete!")
    else:
        print(f"el perro {i} no cumplio la cuota. se queda sin filete")
    no_cumplieron += 0

    print(f"perros que cumplieron la cuota: {cumplieron}")
    print(f"perro que no cumplieron la cuota: {no_cumplieron}")