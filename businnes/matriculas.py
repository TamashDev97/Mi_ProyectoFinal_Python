import json
import os
from commons.utils import *

def guardarMatricula_json():
    try:
        file_path = os.path.join("data", "CampersData.json")
        with open(file_path, 'w') as archivo_json:
            json.dump(lista_matriculas, archivo_json, indent=2)
            print("La lista de matrículas ha sido guardada de manera exitosa")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya matrículas guardadas o el archivo no existe.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def cargarMatriculas_json():
    try:
        file_path = os.path.join("data", "CampersData.json")
        with open(file_path, 'r') as archivo_json:
            lista_matriculas = json.load(archivo_json)
            print("La lista de matrículas ha sido cargada")
            return lista_matriculas
    except FileNotFoundError:
        print("El archivo 'CampersData.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

lista_matriculas = cargarMatriculas_json()

def crearMatricula():
    print("Ingrese los datos del nuevo camper a registrar")
    Nombre = input("Ingrese el nombre del nuevo camper: ")
    Apellido = input("Ingrese el apellido del camper: ")
    Identificacion = input("Ingrese el numero de documento de identificación del camper: ")
    Direccion = input("Ingrese la dirección de residencia del camper: ")
    Telefono = input("Ingrese el teléfono de contacto del camper: ")
    Acudiente = input("Ingrese el nombre del acudiente del camper: ")
    Ruta = input("Ingrese la ruta de aprendizaje del camper: ")
    Horario = input("Ingrese el horario establecido para el camper: ")
    Profesor = input("Ingrese el profesor asignado para el camper: ")
    Salon = input("Ingrese el salón asignado para el camper: ")
    Modulo = input("Ingrese el módulo al que ingresará: ")
    Fecha_Inicio = input("Ingrese la fecha de inicio del entrenamiento: ")
    Fecha_Fin = input("Ingrese la fecha estimada de finalización del entrenamiento: ")
   
    camper = {
        'Nombre': Nombre,
        'Apellido': Apellido,
        'Identificacion': Identificacion,
        'Direccion': Direccion,
        'Telefono': Telefono,
        'Acudiente': Acudiente,
        'Ruta': Ruta,
        'Horario': Horario,
        'Profesor': Profesor,
        'Salon': Salon,
        'Modulo': Modulo,
        'Fecha Inicio': Fecha_Inicio,
        'Fecha Fin': Fecha_Fin 
    }

    lista_matriculas.append(camper)
    print("Se creó el camper con éxito")
    guardarMatricula_json()

def modificarMatricula():
    pass

def buscarMatricula():
    def buscar_por_id(json_path, palabra_ingresada):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)
                identificacion_coincidente = [entry for entry in data if entry.get('Identificacion') == palabra_ingresada]

                if identificacion_coincidente:
                    print(f"El camper con identificación '{palabra_ingresada}' existe. Datos del estudiante:")
                    for entry in identificacion_coincidente:
                        print(f"Nombre: {entry['Nombre']}, Apellido: {entry['Apellido']}")
                        print(f"Dirección: {entry['Direccion']}")
                        print(f"Teléfono: {entry['Telefono']}")
                        print(f"Acudiente: {entry['Acudiente']}")
                        print(f"Ruta: {entry['Ruta']}")
                        print(f"Horario: {entry['Horario']}")
                        print(f"Profesor: {entry['Profesor']}")
                        print(f"Salón: {entry['Salon']}")
                        print(f"Módulo: {entry['Modulo']}")
                else:
                    print(f"El numero de identificación no coincide con ningún registro '{palabra_ingresada}'.")

        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("data", "CampersData.json")
    palabra_ingresada = input("Ingrese el número de identificación del camper: ")
    buscar_por_id(json_path, palabra_ingresada)