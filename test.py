import tkinter as tk
from tkinter import messagebox # Para mostrar mensajes de error

def realizar_operacion(operacion):
    """
    Función que se ejecuta cuando se presiona un botón de operación.
    Realiza la suma, resta, multiplicación o división de los números.
    """
    try:
        num1_str = entrada_num1.get()
        num2_str = entrada_num2.get()

        # Validar que los campos no estén vacíos
        if not num1_str or not num2_str:
            messagebox.showwarning("Entrada Incompleta", "Por favor, ingrese ambos números.")
            return

        num1 = float(num1_str)
        num2 = float(num2_str)

        resultado = 0

        if operacion == 'sumar':
            resultado = num1 + num2
        elif operacion == 'restar':
            resultado = num1 - num2
        elif operacion == 'multiplicar':
            resultado = num1 * num2
        elif operacion == 'dividir':
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showerror("Error de División", "No se puede dividir por cero.")
                etiqueta_resultado.config(text="Resultado: Error")
                return
        
        etiqueta_resultado.config(text=f"Resultado: {resultado:.2f}") # Formatear a 2 decimales
        etiqueta_resultado.config(fg="blue") # Color azul para el resultado exitoso

    except ValueError:
        messagebox.showerror("Error de Entrada", "Por favor, ingrese solo números válidos.")
        etiqueta_resultado.config(text="Resultado: Error")
        etiqueta_resultado.config(fg="red") # Color rojo para el resultado de error
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
        etiqueta_resultado.config(text="Resultado: Error")
        etiqueta_resultado.config(fg="red")

def limpiar_campos():
    """
    Función para limpiar los campos de entrada y el resultado.
    """
    entrada_num1.delete(0, tk.END) # Borra desde el inicio (0) hasta el final (tk.END)
    entrada_num2.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado: ", fg="black") # Restablece el texto y color
    entrada_num1.focus_set() # Pone el foco en el primer campo para facilitar la nueva entrada

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Calculadora Amigable")
ventana.geometry("350x380") # Un poco más grande
ventana.resizable(False, False) # Evita que el usuario pueda redimensionar la ventana (opcional)
ventana.configure(bg="#e0e0e0") # Color de fondo gris claro para la ventana

# --- Estilos de Fuente ---
FONT_LABEL = ("Arial", 12)
FONT_ENTRY = ("Arial", 12)
FONT_BUTTON = ("Arial", 11, "bold") # Negrita para los botones
FONT_RESULT = ("Arial", 14, "bold") # Más grande y negrita para el resultado

# --- Crear y Posicionar los Widgets ---

# Frame para agrupar entradas y etiquetas
frame_entradas = tk.Frame(ventana, bg="#f0f0f0", bd=2, relief="groove") # Borde y relieve
frame_entradas.pack(pady=20, padx=20, fill="x") # pady para espacio vertical, padx para horizontal

tk.Label(frame_entradas, text="Número 1:", font=FONT_LABEL, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_num1 = tk.Entry(frame_entradas, font=FONT_ENTRY, bd=2, relief="sunken") # Borde hundido
entrada_num1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(frame_entradas, text="Número 2:", font=FONT_LABEL, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada_num2 = tk.Entry(frame_entradas, font=FONT_ENTRY, bd=2, relief="sunken")
entrada_num2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Configurar expansión de columna en el frame de entradas
frame_entradas.grid_columnconfigure(1, weight=1)

# Frame para agrupar botones de operación
frame_botones = tk.Frame(ventana, bg="#e0e0e0")
frame_botones.pack(pady=10, padx=20, fill="x")

# Botones de Operación
tk.Button(frame_botones, text="Sumar", font=FONT_BUTTON, relief="raised", bg="#c0e0ff", command=lambda: realizar_operacion('sumar')).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
tk.Button(frame_botones, text="Restar", font=FONT_BUTTON, relief="raised", bg="#c0e0ff", command=lambda: realizar_operacion('restar')).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
tk.Button(frame_botones, text="Multiplicar", font=FONT_BUTTON, relief="raised", bg="#c0e0ff", command=lambda: realizar_operacion('multiplicar')).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
tk.Button(frame_botones, text="Dividir", font=FONT_BUTTON, relief="raised", bg="#c0e0ff", command=lambda: realizar_operacion('dividir')).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Configurar expansión de columnas en el frame de botones
frame_botones.grid_columnconfigure(0, weight=1)
frame_botones.grid_columnconfigure(1, weight=1)

# Botón Limpiar
tk.Button(ventana, text="Limpiar", font=FONT_BUTTON, relief="groove", bg="#ffe0b3", command=limpiar_campos).pack(pady=10, padx=20, fill="x")

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=FONT_RESULT, bg="#e0e0e0", fg="black")
etiqueta_resultado.pack(pady=10) # pady para espacio vertical

# Poner el foco inicial en el primer campo de entrada
entrada_num1.focus_set()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()