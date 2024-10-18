import tkinter as tk
from tkinter import messagebox

# Tasa de conversión fija
TASA_CONVERSION = 600.0  # Ejemplo: 1 USD = 600 CRC

def convertir():
    try:
        valor_usd = float(entry_dolares.get())
        if valor_usd < 0:
            raise ValueError("El valor no puede ser negativo.")
        resultado = valor_usd * TASA_CONVERSION
        etiqueta_resultado.config(text=f"{resultado:.2f} CRC")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un valor válido en dólares.")

def limpiar():
    entry_dolares.delete(0, tk.END)
    etiqueta_resultado.config(text="")

def on_closing():
    if messagebox.askokcancel("Salir", "¿Quieres salir?"):
        root.destroy()

# Ventana principal
root = tk.Tk()
root.title("Conversor de Moneda")
root.geometry("300x200")
root.protocol("WM_DELETE_WINDOW", on_closing)

# Entrada de datos
tk.Label(root, text="Monto en USD:").grid(row=0, column=0)
entry_dolares = tk.Entry(root)
entry_dolares.grid(row=0, column=1)

# Botones
btn_convertir = tk.Button(root, text="Convertir", command=convertir)
btn_convertir.grid(row=1, column=0)

btn_limpiar = tk.Button(root, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=1, column=1)

# Mostrar resultado
etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.grid(row=2, columnspan=2)

root.mainloop()
