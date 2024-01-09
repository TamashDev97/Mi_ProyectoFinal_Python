import json
import os

# Obtener la ruta absoluta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

def guardar_json():
    try:
        with open(os.path.join(current_dir, "data", "Ingresos.json"), 'w') as archivo_json:
            json.dump(lista_campers, archivo_json, indent=2)
            print("La lista de campers ha sido guardada de manera exitosa")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados o el archivo no existe.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def load_CampersData_json():
    try:
        with open(os.path.join(current_dir, "data", "Ingresos.json"), 'r') as archivo_json:
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido cargada")
            return lista_campers
    except FileNotFoundError:
        print("El archivo 'Ingresos.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

lista_campers = load_CampersData_json()

def listar_campers():
    if lista_campers:  # Si la lista no está vacía
        for camper in lista_campers:
            print(f"Nombre: {camper['Nombre']}, Apellido: {camper['Apellido']}, Identificacion: {camper['Identificacion']}")
    else:
        print("No hay campers para mostrar.")

def crear_camper():
    Nombre = input("Ingrese el nombre del camper a registrar: ")
    Apellido = input("Ingrese el apellido del camper a registrar: ")
    Identificacion = int(input("Ingrese el numero de documento de identificación del camper: "))
    Direccion = input("Ingrese la direccion de residencia del camper: ")
    Telefono = input("Ingrese el número de teléfono del camper: ")
    Acudiente = input("Ingrese nombre del acudiente o responsable del camper: ")
    NotaP = int(0)
    NotaT = int(0)
    camper = {
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Identificacion': Identificacion,
        'Direccion': Direccion,
        'Telefono': Telefono,
        'Acudiente': Acudiente,
        'NotaP': NotaP,
        'NotaT': NotaT
    }
    lista_campers.append(camper)  # Añade el nuevo camper a lista_campers
    guardar_json()

def modificar_camper():
    print("Seleccione el camper que desea modificar.")
    Nombre = input("Ingrese el nombre del camper a modificar: ")
    Apellido = input("Ingrese el apellido del camper a modificar: ")
    Identificacion = int(input("Ingrese el numero de documento de identificación del camper: "))
    Direccion = input("Ingrese la direccion de residencia del camper: ")
    Telefono = input("Ingrese el número de teléfono del camper: ")
    Acudiente = input("Ingrese nombre del acudiente o responsable del camper: ")
    NotaP = int(0)
    NotaT = int(0)
    camper = {
        'Nombre':Nombre,
        'Apellido': Apellido,
        'Identificacion': Identificacion,
        'Direccion': Direccion,
        'Telefono': Telefono,
        'Acudiente': Acudiente,
        'NotaP': NotaP,
        'NotaT': NotaT
    }

    lista_campers.append(camper)
    print("Se modificó el camper de manera exitosa")
    guardar_json()