import tkinter as tk
"""
Funcion calcular
 Esta función comienza obteniendo el texto de la entrada de salario con la función "get()" y lo almacena en la 
variable "salario_text". Si la entrada de salario está vacía, la función muestra un mensaje en la etiqueta 
"salario_label" y finaliza la función con "return". De lo contrario, intenta convertir el valor de la entrada 
de salario a un número de 
punto flotante usando la función "float()". Si ocurre un error en la conversión 
(por ejemplo, si el usuario ingresa un valor no numérico), la entrada de salario se borra y se muestra un mensaje en 
la etiqueta "salario_label". La función luego verifica si el salario ingresado es mayor o igual a 1,160,000. 
Si no lo es, se borra la entrada de salario y se muestra un mensaje de error en la etiqueta "salario_label". 
Si todo está bien con el salario, la función obtiene el valor de la entrada de días trabajados y lo convierte a un 
número de punto flotante, de manera similar a la entrada de salario. La función luego llama a las 
funciones "valor_cesantias()" y "valor_prima()" y almacena los valores de retorno en "empleado1cesantia" y
 "empleado1prima", 
respectivamente. Finalmente, la función actualiza las etiquetas "cesantias_label" y "prima_label" con los valores 
calculados. se toma tambien como base 1.160.000 ya que es el salario minimo legal vigente para 2023 en colombia 
"""

def calcular():
    salario_text = salario_entrada.get()
    if not salario_text:  # si la entrada está vacía
        salario_label.config(text="Ingrese un valor válido!", fg="blue")
        return

    try:
        salario = float(salario_text)
    except ValueError:
        salario_entrada.delete(0, tk.END)  # borra la entrada incorrecta
        salario_label.config(text="Por favor ingrese un valor válido", fg="purple")
        return

    if salario < 1160000:
        salario_entrada.delete(0, tk.END)
        salario_label.config(text="Por favor ingrese un salario mayor o igual a $1,160,000 ☻", fg="purple")
        return

    salario_label.config(text="Por favor ingrese salario", fg="orange")
    dias_trabajados_text = dias_entrada.get()

    try:
        dias_trabajados = float(dias_trabajados_text)
    except ValueError:
        dias_entrada.delete(0, tk.END)  # borra la entrada incorrecta
        dias_label.config(text="Si no a trabajado, ni un día no se le paga Daaaaa", fg="red")
        return

    empleado1cesantia = valor_cesantias(salario, dias_trabajados)
    empleado1prima = valor_prima(salario, dias_trabajados)

    cesantias_label.config(text=f"Las cesantías a pagar son: {empleado1cesantia:.0f}")
    prima_label.config(text=f"La prima a pagar es de: {empleado1prima:.0f}")


def valor_cesantias(salario_mensual, dias_trabajados):
    cesantias = salario_mensual * dias_trabajados / 360
    # siempre se debe calcular el interés de las cesantías
    interes = cesantias * 0.12 * dias_trabajados / 360
    total_cesantias = cesantias + interes
    return total_cesantias


def valor_prima(salario_mensual, dias_trabajados):
    prima = salario_mensual * dias_trabajados / 360
    total_prima = prima
    return total_prima



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

