import tkinter as tk
from tkinter import ttk

# Base de datos de libros en forma de lista de diccionarios
libros = [
    {"título": "El imperio final", "género": "Fantasía", "autor": "Brandon Sanderson", "calificación": 4.9},
    {"título": "Orgullo y prejuicio", "género": "Romance", "autor": "Jane Austen", "calificación": 4.8},
    {"título": "Jane Eyre", "género": "Romance", "autor": "Charlotte Brontë", "calificación": 4.6},
    {"título": "Heartstopper", "género": "Romance", "autor": "Alice Oseman", "calificación": 4.9},
    {"título": "La casa en el mar más azul", "género": "Fantasía", "autor": "TJ Klune", "calificación": 4.8},
    {"título": "Una corte de rosas y espinas", "género": "Fantasía", "autor": "Sarah J. Maas", "calificación": 4.7},
    {"título": "Seis de cuervos", "género": "Fantasía", "autor": "Leigh Bardugo", "calificación": 4.8},
    {"título": "Hija de humo y hueso", "género": "Fantasía", "autor": "Laini Taylor", "calificación": 4.6},
    {"título": "Una llama entre cenizas", "género": "Fantasía", "autor": "Sabaa Tahir", "calificación": 4.7},
    {"título": "El príncipe cruel", "género": "Fantasía", "autor": "Holly Black", "calificación": 4.7},
]

# Función para recomendar libros según el género o autor preferido
def recomendar_libros(genero_preferido, autor_preferido):
    recomendaciones = []
    for libro in libros:
        if libro["género"] == genero_preferido or libro["autor"] == autor_preferido:
            libro_copia = libro.copy()
            if libro["género"] == genero_preferido and libro["autor"] == autor_preferido:
                libro_copia["razon"] = "Recomendado por género y autor"
            elif libro["género"] == genero_preferido:
                libro_copia["razon"] = "Recomendado por género"
            elif libro["autor"] == autor_preferido:
                libro_copia["razon"] = "Recomendado por autor"
            recomendaciones.append(libro_copia)
    recomendaciones.sort(key=lambda x: x["calificación"], reverse=True)
    return recomendaciones

# Función para manejar el clic en el botón de recomendar
def manejar_recomendacion():
    genero_preferido = entrada_genero.get()
    autor_preferido = entrada_autor.get()
    recomendaciones = recomendar_libros(genero_preferido, autor_preferido)

    # Limpiar el cuadro de resultados antes de mostrar nuevas recomendaciones
    for widget in cuadro_resultados.winfo_children():
        widget.destroy()

    if recomendaciones:
        for libro in recomendaciones:
            frame_libro = tk.Frame(cuadro_resultados, bg='#ffe4e1', bd=2, relief='groove')
            frame_libro.pack(fill='x', padx=10, pady=5)

            titulo = tk.Label(frame_libro, text=f"Título: {libro['título']}", font=('Arial', 12, 'bold'), bg='#ffe4e1')
            titulo.pack(anchor='w', padx=5, pady=2)

            autor = tk.Label(frame_libro, text=f"Autor: {libro['autor']}", font=('Arial', 11), bg='#ffe4e1')
            autor.pack(anchor='w', padx=5)

            genero = tk.Label(frame_libro, text=f"Género: {libro['género']}", font=('Arial', 11), bg='#ffe4e1')
            genero.pack(anchor='w', padx=5)

            calificacion = tk.Label(frame_libro, text=f"Calificación: {libro['calificación']}", font=('Arial', 11), bg='#ffe4e1')
            calificacion.pack(anchor='w', padx=5)

            razon = tk.Label(frame_libro, text=f"Razón: {libro['razon']}", font=('Arial', 11, 'italic'), bg='#ffe4e1')
            razon.pack(anchor='w', padx=5, pady=2)
    else:
        no_recomendaciones = tk.Label(cuadro_resultados, text="No hay recomendaciones disponibles para las preferencias seleccionadas.", font=('Arial', 12), bg='#ffe4e1')
        no_recomendaciones.pack(pady=10)

# Configuración de la interfaz gráfica usando Tkinter
ventana = tk.Tk()
ventana.title("Sistema de Recomendación de Libros")
ventana.geometry("600x600")
ventana.configure(bg='#ffe4e1')  

estilo = {
    'bg': '#ffc0cb',  
    'font': ('Arial', 12),
    'padx': 10,
    'pady': 5
}

# Etiquetas y campos de entrada para el género y autor preferido
etiqueta_genero = tk.Label(ventana, text="Género preferido:", **estilo)
etiqueta_genero.pack(pady=5)
entrada_genero = tk.Entry(ventana, font=('Arial', 12))
entrada_genero.pack(pady=5)

etiqueta_autor = tk.Label(ventana, text="Autor preferido:", **estilo)
etiqueta_autor.pack(pady=5)
entrada_autor = tk.Entry(ventana, font=('Arial', 12))
entrada_autor.pack(pady=5)

# Botón para obtener recomendaciones
boton_recomendar = tk.Button(ventana, text="Recomendar Libros", command=manejar_recomendacion, **estilo)
boton_recomendar.pack(pady=20)

# Cuadro para mostrar las recomendaciones con scrollbar
cuadro_scroll = tk.Scrollbar(ventana)
cuadro_scroll.pack(side='right', fill='y')
cuadro_resultados = tk.Canvas(ventana, bg='#ffe4e1', yscrollcommand=cuadro_scroll.set)
cuadro_resultados.pack(fill='both', expand=True, padx=10, pady=10)
cuadro_scroll.config(command=cuadro_resultados.yview)

# Frame interno para los resultados
frame_resultados = tk.Frame(cuadro_resultados, bg='#ffe4e1')
cuadro_resultados.create_window((0, 0), window=frame_resultados, anchor='nw')

# Configurar el ajuste automático del scrollbar
frame_resultados.bind(
    "<Configure>", lambda e: cuadro_resultados.configure(scrollregion=cuadro_resultados.bbox("all"))
)

# Ejecutar la aplicación
ventana.mainloop()
