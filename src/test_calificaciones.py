from calificaciones import *
def test_solicita_datos():
    print("Calcula tu nota en el cuestionario: ")
    aciertos, errores, totalRespuestas = solicita_datos()
    return aciertos, errores, totalRespuestas

def test_calcula_nota(aciertos, errores, totalRespuestas):
    nota = calcula_nota(aciertos, errores, totalRespuestas)
    print(nota)


if __name__ == '__main__':
    aciertos, errores, totalRespuestas = test_solicita_datos()
    test_calcula_nota(aciertos, errores, totalRespuestas)
