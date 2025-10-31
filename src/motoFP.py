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

def maximo_dias_sin_ganar(lista:list[CarreraFP], nombre_piloto:str)->int:
    




