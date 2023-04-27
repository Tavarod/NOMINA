import tkinter as tk

def Valor_cesantias(salario_mensual, dias_trabajados):
    cesantias = salario_mensual * dias_trabajados / 360
    #Siempre se debe calcular el interes de las cesantias
    interes = cesantias * 0.12 * dias_trabajados / 360
    total_cesantias = cesantias + interes
    return total_cesantias

def Valor_prima(salario_mesual, dias_trabajados):
    prima = salario_mesual * dias_trabajados / 360
    total_prima = prima
    return total_prima

def calcular():
    salario = float(salario_entrada.get())
    dias_trabajados = float(dias_entrada.get())
    empleado1cesantia = Valor_cesantias(salario, dias_trabajados)
    empleado1prima = Valor_prima(salario, dias_trabajados)
    cesantias_label.config(text=f"Las cesantías a pagar son: {empleado1cesantia:.0f}")
    prima_label.config(text=f"La prima a pagar es de: {empleado1prima:.0f}")

window = tk.Tk()
window.title("Calculo Basico de Prima y Cesantias")
window.geometry("400x200")
window.configure(bg="#95b8f6")

salario_label = tk.Label(window, text="Por favor ingrese salario", bg="#c3f8ff")
salario_label.grid(column=0, row=0, padx=11, pady=11)

salario_entrada = tk.Entry(window)
salario_entrada.grid(column=1, row=0)

dias_label = tk.Label(window, text="Por favor indique los dias trabajados", bg="#c3f8ff")
dias_label.grid(column=0, row=1, padx=11, pady=11)

dias_entrada = tk.Entry(window)
dias_entrada.grid(column=1, row=1)

calcular_button = tk.Button(window, text="Calcular", command=calcular, bg="#e1b1bc")
calcular_button.grid(column=0, row=2, columnspan=2, pady=10)

cesantias_label = tk.Label(window, text="☺", bg="#a0d2f3")
cesantias_label.grid(column=0, row=3, columnspan=2)

prima_label = tk.Label(window, text="☻", bg="#a0d2f3")
prima_label.grid(column=0, row=4, columnspan=2)

window.mainloop()

