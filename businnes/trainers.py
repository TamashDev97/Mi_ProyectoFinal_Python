import json
import os

def load_trainers_json():
    try:
        json_path = os.path.join("data", "Trainers.json")
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
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Horario': Horario,
        'Ruta': Ruta
    }
    lista_trainers.append(trainer)
    print("Se creó el trainer con éxito")
    guardar_json()

def guardar_json():
    try:
        json_path = os.path.join("data", "Trainers.json")
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
    nombre_trainer = input("Ingrese el nombre del trainer: ")
    for trainer in lista_trainers:
        if trainer['Nombre'] == nombre_trainer:
            print(trainer)
            break

def modificar_trainer():
    nombre_buscar = input("Ingrese el nombre del trainer que desea modificar: ")
    apellido_buscar = input("Ingrese el apellido del trainer que desea modificar: ")
    encontrado = False

    for trainer in lista_trainers:
        if trainer['Nombre'] == nombre_buscar and trainer['Apellido'] == apellido_buscar:
            nuevo_nombre = input("Ingrese el nuevo nombre del trainer: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del trainer: ")
            nuevo_horario = input("Ingrese el nuevo horario del trainer: ")
            nuevo_ruta = input("Ingrese la nueva ruta del trainer: ")

            trainer['Nombre'] = nuevo_nombre
            trainer['Apellido'] = nuevo_apellido
            trainer['Horario'] = nuevo_horario
            trainer['Ruta'] = nuevo_ruta

            print("La información del trainer ha sido modificada con éxito")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró ningún trainer con ese nombre y apellido")