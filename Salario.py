#smlv (salario minimo legal vigente) 2023 1160000
#sub transporte 140606

def Valor_pago(dias_trabajados, smlv):
    valor_dia = smlv / 30
    pago_salario = dias_trabajados * valor_dia
    return pago_salario

nombre_Empleado = input("Nombre completo por favor")

smlv = float(input("Ingrese por favor su salario"))
while smlv < 1160000:
    print("El salario no puede ser menor a un SMLV")
    smlv = float(input("Ingrese por favor su salario,no menor a un SMLV de 2023"))

dias_trabajados = float(input("Ingrese por favor sus dias trabajados"))
while dias_trabajados < 1:
    print("Los dias trabajados deben ser mayores o iguales 1")
    dias_trabajados = float(input("Ingrese por favor sus dias trabajados"))

salario_total = Valor_pago(dias_trabajados, smlv)

print(f"{nombre_Empleado},El valor total de su salario es de: {salario_total:.0f}")

