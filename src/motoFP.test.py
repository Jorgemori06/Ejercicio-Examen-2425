from motoFP import*
ruta = 'data/mundial_motofp.csv'
def test_lee_carreras():
    lee_carreras(ruta)

def funcion_principal():
    test_lee_carreras()


if __name__=="__main__":
    funcion_principal()