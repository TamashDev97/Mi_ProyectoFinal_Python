from commons.menus import menu_aulas, menu_campers, menu_matriculas, menu_principal, menu_reportes, menu_trainers
from businnes.cammpers import crear_camper, listar_campers, modificar_camper
from businnes.reportes import inscritos, aprobados, lista_trainers, camp_bajo_rendimiento, camp_trainer, camp_ap_rep_ruta
from businnes.aulas import crearAulas, buscarAulas, modificarAulas
from businnes.matriculas import crearMatricula, modificarMatricula, buscarMatricula
from commons.utils import limpiar_pantalla
from businnes.trainers import crear_trainer, buscar_trainer, modificar_trainer

def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
        crear_camper()
        input("Clic cualquier teclas [continuar]: ")
    if op==2:
        listar_campers()
        input("Clic cualquier teclas [continuar]: ")
    if op==3:
        modificar_camper()
        input("Clic cualquier teclas [continuar]: ")

def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op == 1:
        crear_trainer()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        buscar_trainer()
        input("Clic cualquier teclas [continuar]: ")
    if op==3:
        modificar_trainer()
        input("Clic cualquier teclas [continuar]: ")

def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op == 1:
        crearMatricula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        buscarMatricula()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        modificarMatricula()

def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
    if op == 1:
        crearAulas()
        input("Clic cualquier teclas [continuar]: ")
    if op == 2:
        buscarAulas()
        input("Clic cualquier teclas [continuar]: ")
    if op == 3:
        modificarAulas()

def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op ==1:
        inscritos()
        input("Clic cualquier teclas [continuar]: ")
    elif op==2:
        aprobados()
        input("Clic cualquier teclas [continuar]: ")
    elif op==3:
        lista_trainers()
        input("Clic cualquier teclas [continuar]: ")
    elif op==4:
        camp_bajo_rendimiento()
        input("Clic cualquier teclas [continuar]: ")
    elif op==5:
        camp_trainer()
        input("Clic cualquier teclas [continuar]: ")
    elif op==6:
        camp_ap_rep_ruta()
        input("Clic cualquier teclas [continuar]: ")

#start
while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       trainers()
   elif op==3:
       matriculas()
   elif op==4:
       aulas()
   elif op==5:
       reportes()
   elif op==6:
       print("Saliendo")
       break