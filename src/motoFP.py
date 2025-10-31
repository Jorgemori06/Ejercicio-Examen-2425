from typing import NamedTuple
from datetime import datetime
import csv
Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])

def lee_carreras(ruta_fichero:str)->list[CarreraFP]:
    lista_carreras=[]
    
    with open(ruta_fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for campos in lector:
            fecha_hora = datetime.strptime(campos[0], "%Y-%m-%d %H:%M")
            circuito = campos[1]
            pais = campos[2]
            seco = campos[3].strip().lower() == 'seco'
            tiempo = float(campos[4])
            piloto1=campos[5]
            escuderia1=campos[6]
            piloto2=campos[7]
            escuderia2=campos[8]
            piloto3=campos[9]
            escuderia3=campos[10]
            podio=[Piloto(piloto1, escuderia1),Piloto(piloto2, escuderia2),Piloto(piloto3, escuderia3)]
            carrera = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
            lista_carreras.append(carrera)
        return lista_carreras
    

"""Implemente una función `maximo_dias_sin_ganar` que reciba 
una lista de tuplas de tipo `CarreraFP` y el nombre de un piloto, 
y devuelva el tiempo máximo (en días) que ese piloto estuvo sin ganar 
una carrera. Es decir, el número máximo de días transcurridos 
entre dos carreras ganadas por el piloto. Si el piloto no ha ganado 
al menos dos carreras, la función debe devolver `None`."""
def dias_entre_fechas(fecha1:datetime, fecha2:datetime)->int:
    dias= (fecha2 - fecha1).days
    return dias

def maximo_dias_sin_ganar(carreras:list[CarreraFP], nombre_piloto:str)->int:
    fechas_ganadas=[]
    for carrera in carreras:
        if carrera.podio[0].nombre==nombre_piloto:
            fechas_ganadas.append(carrera.fecha_hora)
    maximo_dias_sin_ganar=0
    if len(fechas_ganadas)<2:         
        return None
    if len(fechas_ganadas)>1:         
        for carrera in fechas_ganadas:
            if dias_entre_fechas(fechas_ganadas[0], fechas_ganadas[1])>maximo_dias_sin_ganar:
                maximo_dias_sin_ganar=dias_entre_fechas(fechas_ganadas[0], fechas_ganadas[1])
    return maximo_dias_sin_ganar


        





