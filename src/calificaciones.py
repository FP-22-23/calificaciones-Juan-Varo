def calcula_nota(aciertos, errores, totalRespuestas):
    nota = (aciertos * 10)/totalRespuestas - (errores * 10)/(50 - totalRespuestas)
    return nota

def calcula_nota_cuatrimestre(cuestionarios, proyectos, nota_parciales):
    nota_cuatrimestre_1 = 0.1 * (cuestionarios[0]+ cuestionarios[1] + cuestionarios[2]) + 0.6 * nota_parciales[0] + proyectos[0]
    nota_cuatrimestre_2 = 0.1 * (cuestionarios[3] + cuestionarios[4] + cuestionarios[5]) + 0.6 * nota_parciales[1] + proyectos[1]
    return nota_cuatrimestre_1, nota_cuatrimestre_2

def calcula_nota_eval_continua(nota_cuatrimestre_1, nota_cuatrimestre_2):
    return (nota_cuatrimestre_1 + nota_cuatrimestre_2) / 2

def solicita_datos():
    aciertos = int(input("El número de aciertos es: "))
    errores = int(input("El número de errores es: "))
    totalRespuestas = int(input("El número total de respuestas es: "))
    return aciertos, errores, totalRespuestas

def solicita_nota_cuatrimestre():
    c1 = int(input("Nota del primer cuestionario: "))
    c2 = int(input("Nota del segundo cuestionario: "))
    c3 = int(input("Nota del tercer cuestionario: "))
    c4 = int(input("Nota del cuarto cuestionario: "))
    c5 = int(input("Nota del quinto cuestionario: "))
    c6 = int(input("Nota del sexto cuestionario: "))
    cuestionarios = (c1, c2, c3, c4, c5, c6)
    return cuestionarios

def solicita_nota_proyectos():
    p1 = int(input("Nota del primer proyecto: "))
    p2 = int(input("Nota del segundo proyecto: "))
    proyectos = (p1, p2)
    return proyectos

def solicita_nota_parciales():
    nota_primer_parcial = int(input("Nota del primer parcial: "))
    nota_segundo_parcial = int(input("Nota del segundo parcial: "))
    nota_parciales = (nota_primer_parcial, nota_segundo_parcial)
    return nota_parciales