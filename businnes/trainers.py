import json
import os

def load_trainers_json():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "Data", "Trainers.json")
        with open(json_path, 'r') as archivo_json:
            lista_trainers = json.load(archivo_json)
            print("La lista de Trainers ha sido cargada")
            return lista_trainers
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

lista_trainers = load_trainers_json()

def crear_trainer():
    Nombre = input("Ingrese el nombre del trainer: ")
    Apellido = input("Ingrese el apellido del trainer: ")
    Horario = input("Ingrese el horario del trainer: ")
    Ruta = input("Ingrese la ruta del trainer: ")
    trainer = {
        'nombre': Nombre,
        'apellido': Apellido,
        'horario': Horario,
        'ruta': Ruta
    }
    lista_trainers.append(trainer)
    print("Se creó el trainer con éxito")
    guardar_json()

def guardar_json():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "Data", "Trainers.json")
        with open(json_path, 'w') as archivo_json:
            json.dump(lista_trainers, archivo_json, indent=2)
            print("La lista de trainers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya trainers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")

def buscar_trainer():
    print("Los trainers en campus son:")
    def nom_ap_p(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                if all(entry.get('nombre') is not None and entry.get('apellido') is not None for entry in data):
                    nombre_y_ape = [(entry['nombre'], entry['apellido']) for entry in data]
                    return nombre_y_ape
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []

    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "Data", "Trainers.json")
    nombres_apellidos = nom_ap_p(json_path)
    for Nombre, Apellido in nombres_apellidos:
        print(f"{Nombre} {Apellido}")

def modificar_trainer():
    nombre_buscar = input("Ingrese el nombre del trainer que desea modificar: ")
    apellido_buscar = input("Ingrese el apellido del trainer que desea modificar: ")
    encontrado = False

    for trainer in lista_trainers:
        if trainer['nombre'] == nombre_buscar and trainer['apellido'] == apellido_buscar:
            nuevo_nombre = input("Ingrese el nuevo nombre del trainer: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del trainer: ")
            nuevo_horario = input("Ingrese el nuevo horario del trainer: ")
            nuevo_ruta = input("Ingrese la nueva ruta del trainer: ")

            trainer['nombre'] = nuevo_nombre
            trainer['apellido'] = nuevo_apellido
            trainer['horario'] = nuevo_horario
            trainer['ruta'] = nuevo_ruta

            print("La información del trainer ha sido modificada con éxito")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún trainer con ese nombre y apellido")
