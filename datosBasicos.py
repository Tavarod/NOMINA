def empleado():
    tipoID = input("Ingrese su tipo de documento: ")
    nombre1 = input("Ingrese su primer nombre: ")
    nombre2 = input("Ingrese su segundo nombre: ")
    apellido1 = input("Ingrese su primer apellido: ")
    apellido2 = input("Ingrese su segundo apellido: ")

    print(f"Tipo de documento: {tipoID}")
    print(f"Nombre: {nombre1} {nombre2}")
    print(f"Apellido: {apellido1} {apellido2}")

def prima(dias, salario):
    if dias <= 180:
        primaC = dias * salario / 180
        return primaC
    else:
        print("El número de días no puede superar 180 para el calculo de la prima")

def cesantias(dias, salario):
    cesantiasC = dias * salario / 360
    return cesantiasC

dias = int(input("Dias trabajados: "))
while dias > 180:
    print("El número de días no puede superar 180 para el calculo de la prima")
    dias = int(input("Dias trabajados: "))

salario = int(input("Ingrese su salario"))

print(prima(dias, salario))

print(f"La prima es: {prima(dias, salario)}")
print(f"Las cesantías son: {cesantias(dias, salario)}")
empleado()

