import pandas as pd
import numpy as np
import csv

# Definimos la clase principal
class Libro:
    """
    Clase para representar el libro en el sistema de recomendacion.

    Attributos:
    ----------
    titulo : str
        Titulo del libro.
    autor : str
        Author del libro.
    genero : str
        Genero del libro.
    puntuacion : float
        Rating del libro(debe ser un decimal entre 0 y 5).
    """

    def __init__(self, titulo, autor, genero, puntuacion):
        """
        Inicializamos un nuevo objeto 'Libro'.

        Parameters:
        ----------
    titulo : str
        Titulo del libro.
    autor : str
        Author del libro.
    genero : str
        Genero del libro.
    puntuacion : float
        Rating del libro(debe ser un decimal entre 0 y 5).

        Raises:
        ------
        ValueError:
            SI la puntuacion no se encuentra entre 0 y 5.
        """
        if not 0 <= puntuacion <= 5:
            raise ValueError("La puntuación debe estar entre 0 y 5.")
        
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

    def __str__(self):
        """
        Regresa un string que representa el objeto 'Libro'.

        Returns:
        -------
        str:
            String que representa al libro con su titulo, autor, genero, y puntuacion.
        """
        return f"'titulo: {self.titulo}' - autor: {self.autor} - Genre: {self.genero}, puntuacion: {self.puntuacion}"

# Inicializa la lista de libros
lista_libros = []

# Creamos las funcionalidades
def agregar_libro(lista_libros):
    """
    Solicita al usuario que ingrese el título, autor, género y puntuación de un libro,
    crea un objeto Libro y lo agrega a la lista de libros.

    Parameters:
    ----------
    lista_libros : list
        La lista donde se almacenan los objetos de la clase Libro.
    """
    try:
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        genero = input("Ingrese el género del libro: ")
        puntuacion = float(input("Ingrese la puntuación del libro (0-5): "))

        libro = Libro(titulo, autor, genero, puntuacion)
        lista_libros.append(libro)
        print(f"Libro '{titulo}' agregado exitosamente.")
    except ValueError as e:
        print(f"Error: {e}")

def buscar_libros_por_genero(lista_libros):
    """
    Solicita al usuario que ingrese un género y muestra los títulos de libros 
    correspondientes a ese género en la lista de libros.

    Parameters:
    ----------
    lista_libros : list
        La lista donde se almacenan los objetos de la clase Libro.
    """
    genero = input("Ingrese el género que desea buscar: ")
    libros_encontrados = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero.lower()]

    if libros_encontrados:
        print(f"Libros encontrados en el género '{genero}':")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print(f"No se encontraron libros en el género '{genero}'.")

def recomendar_libro(lista_libros):
    """
    Solicita al usuario que ingrese un género y recomienda el libro con la puntuación 
    más alta en ese género.

    Parameters:
    ----------
    lista_libros : list
        La lista donde se almacenan los objetos de la clase Libro.
    """
    genero = input("Ingrese el género para la recomendación: ")
    libros_en_genero = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]

    if libros_en_genero:
        mejor_libro = max(libros_en_genero, key=lambda libro: libro.puntuacion)
        print(f"Recomendación: '{mejor_libro.titulo}' por {mejor_libro.autor} con una puntuación de {mejor_libro.puntuacion}.")
    else:
        print(f"No hay libros para recomendar en el género '{genero}'.")

def cargar_libros_desde_csv(ruta_archivo, lista_libros):
    """
    Lee un archivo CSV que contiene detalles sobre los libros, crea objetos de la clase Libro
    y los agrega a la lista de libros.

    Parameters:
    ----------
    ruta_archivo : str
        La ruta al archivo CSV que contiene los datos de los libros.
    lista_libros : list
        La lista donde se almacenan los objetos de la clase Libro.

    Raises:
    ------
    FileNotFoundError:
        Si el archivo CSV no se encuentra en la ruta especificada.
    ValueError:
        Si algún dato en el archivo CSV no es válido para crear un objeto Libro.
    """
    try:
        with open(ruta_archivo, newline='', encoding='utf-8') as csvfile:
            lector = csv.reader(csvfile)
            next(lector)  # Saltar la cabecera del CSV
            for fila in lector:
                try:
                    titulo, autor, genero, puntuacion = fila
                    puntuacion = float(puntuacion)  # Convertir puntuación a float
                    libro = Libro(titulo, autor, genero, puntuacion)
                    lista_libros.append(libro)
                except ValueError as e:
                    print(f"Error en los datos de la fila: {fila}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'.")

# Creamos funcion para el orquestado delp programa
def ejecutar_sistema_recomendacion():
    """
    Ejecuta el sistema de recomendación de libros. Presenta un menú de opciones
    al usuario para agregar libros, buscar por género, recomendar libros, cargar
    libros desde un archivo CSV o salir del programa.
    """
    lista_libros = []

# Ejecutamos el programa
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar Libro")
        print("2. Buscar Libros por Género")
        print("3. Recomendar Libro")
        print("4. Cargar Libros desde CSV")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_libro(lista_libros)
        elif opcion == '2':
            buscar_libros_por_genero(lista_libros)
        elif opcion == '3':
            recomendar_libro(lista_libros)
        elif opcion == '4':
            ruta_csv = input("Ingrese la ruta del archivo CSV: ")
            cargar_libros_desde_csv(ruta_csv, lista_libros)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_sistema_recomendacion()