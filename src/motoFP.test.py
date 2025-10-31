from motoFP import*
ruta = 'data/mundial_motofp.csv'
def test_lee_carreras():
    carreras=lee_carreras(ruta)
    print('Las dos primeras carreras son:', carreras[0:2], ', las 2 últimas carreras son', carreras[-2])
def test_maximo_dias():
    carreras = lee_carreras(ruta)
    piloto = "Francesco Bagnaia"
    dias = maximo_dias_sin_ganar(carreras, piloto)
    print(f"Máximo número de días sin ganar de {piloto}: {dias}")

def funcion_principal():
    test_lee_carreras()
    test_maximo_dias()


if __name__=="__main__":
    funcion_principal()