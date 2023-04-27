import tkinter as tk


def valor_pago():
    smlv = float(smlv_entry.get())
    while smlv < 1160000:
        result_label.config(text="El salario no puede ser menor a un SMLV")
        return

    dias_trabajados = float(dias_trabajados_entry.get())
    while dias_trabajados < 1:
        result_label.config(text="Los dias trabajados deben ser mayores o iguales 1")
        return

    valor_dia = smlv / 30
    pago_salario = dias_trabajados * valor_dia

    result_label.config(text=f"{nombre_entry.get()}, el valor total de su salario es de: {pago_salario:.0f}")


# crear ventana "window"
window = tk.Tk()
window.title("Calculadora de salario")

# tamaño de la ventana
window.geometry("400x220")

# color ventana fondo
window.configure(bg="#1a1a1a")

# Etiquetas creacion
nombre_label = tk.Label(window, text="Nombre completo por favor:", bg="#848484")
nombre_label.grid(column=0, row=0, padx=10, pady=11)

smlv_label = tk.Label(window, text="Ingrese por favor su salario:", bg="#848484")
smlv_label.grid(column=0, row=1, padx=10, pady=11)

dias_trabajados_label = tk.Label(window, text="Ingrese por favor sus dias trabajados:", bg="#848484")
dias_trabajados_label.grid(column=0, row=2, padx=10, pady=11)

result_label = tk.Label(window, text="")
result_label.grid(column=0, row=4, padx=10, pady=11)

# creacion campos de entrada
nombre_entry = tk.Entry(window, bg="#BDBDBD")
nombre_entry.grid(column=1, row=0)

smlv_entry = tk.Entry(window, bg="#BDBDBD")
smlv_entry.grid(column=1, row=1)

dias_trabajados_entry = tk.Entry(window, bg="#BDBDBD")
dias_trabajados_entry.grid(column=1, row=2)

# crear boton de calcular se usa un color azul para diferenciar
calcular_button = tk.Button(window, text="Calcular", command=valor_pago, bg="#5882FA")
calcular_button.grid(column=0, row=3, pady=10)

# correr ventana
window.mainloop()