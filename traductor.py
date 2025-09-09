import tkinter as tk
from tkinter import ttk, messagebox

# Diccionario Español → Mixteco
diccionario = {
    "hola": "nacumi chiun",
    "adiós": "yati lee",
    "gracias": "tia'vi ndio",
    "amor": "kuaa",
    "hermano": "yanii",
    "mujer": "ña’a",
    "pinotepa de don luis": "ñuu ndoo yu'u",
    "comer": "cachi",
    "beber": "co'o",
    "casa": "ve'e"
}

def traducir():
    palabra = entrada.get().lower()
    traduccion = diccionario.get(palabra, "Traducción no encontrada")
    resultado_var.set(traduccion)

# Ventana principal
ventana = tk.Tk()
ventana.title("Traductor Español → Mixteco")
ventana.geometry("400x300")
ventana.configure(bg="#f0f5f5")

# Etiqueta de título
titulo = tk.Label(ventana, text="Traductor Español → Mixteco tu'un savi", 
                  font=("Arial", 16, "bold"), bg="#f0f5f5", fg="#2c3e50")
titulo.pack(pady=10)

# Entrada de texto
entrada_label = tk.Label(ventana, text="Escribe una palabra en español:", 
                         font=("Arial", 12), bg="#f0f5f5")
entrada_label.pack(pady=5)

entrada = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada.pack(pady=5)

# Botón traducir
boton = ttk.Button(ventana, text="Traducir", command=traducir)
boton.pack(pady=10)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_var, 
                           font=("Arial", 18, "bold"), fg="#16a085", bg="#f0f5f5")
resultado_label.pack(pady=20)

# Pie de página
pie = tk.Label(ventana, text="VERSION BETA BY: ÑA'A ÑUU NDOO YU'U", 
               font=("Arial", 9), bg="#eef1f3", fg="#1118eb")
pie.pack(side="bottom", pady=20)

ventana.mainloop()