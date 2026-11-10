"""
Ejercicio 10: Para N estudiantes (mínimo 5, máximo 20), leer sus notas validadas entre 0 y 20.
La nota mínima aprobatoria es 13. Calcular las métricas de la a) a la k).
"""

NOTA_APROBATORIA: int = 13

def solicitar_cantidad_estudiantes() -> int:
    while not (5 <= (n := int(input("Ingrese cantidad de estudiantes (5 a 20): "))) <= 20):
        print(" Error: La cantidad debe estar entre 5 y 20.")
    return n

def leer_notas(n: int) -> list[int]:
    notas: list[int] = []
    for i in range(1, n + 1):
        while not (0 <= (nota := int(input(f"Ingrese nota del estudiante {i} (0 a 20): "))) <= 20):
            print(" Error: La nota debe estar entre 0 y 20.")
        notas.append(nota)
    return notas

def generar_estadisticas(notas: list[int]) -> None:
    total: int = len(notas)
    mayor_nota: int = max(notas)
    menor_nota: int = min(notas)

    cant_mayor: int = notas.count(mayor_nota)
    cant_menor: int = notas.count(menor_nota)
    promedio: float = sum(notas) / total

    pares: int = sum(1 for n in notas if n % 2 == 0)
    impares: int = total - pares

    aprobados: int = sum(1 for n in notas if n >= NOTA_APROBATORIA)
    desaprobados: int = total - aprobados

    porc_aprobados: float = (aprobados / total) * 100
    porc_desaprobados: float = (desaprobados / total) * 100

    print("\n================ REPORTE DE CALIFICACIONES ================")
    print(f"a) La mayor nota                                   : {mayor_nota}")
    print(f"b) La menor nota                                   : {menor_nota}")
    print(f"c) Cantidad de alumnos que obtuvieron mayor nota   : {cant_mayor}")
    print(f"d) Cantidad de alumnos que obtuvieron menor nota   : {cant_menor}")
    print(f"e) El promedio de notas del salón                  : {promedio:.2f}")
    print(f"f) La cantidad de notas pares                      : {pares}")
    print(f"g) La cantidad de notas impares                    : {impares}")
    print(f"h) La cantidad de alumnos aprobados (>=13)         : {aprobados}")
    print(f"i) La cantidad de alumnos desaprobados (<13)       : {desaprobados}")
    print(f"j) El porcentaje de alumnos aprobados              : {porc_aprobados:.2f}%")
    print(f"k) El porcentaje de alumnos desaprobados           : {porc_desaprobados:.2f}%")

if __name__ == "__main__":
    cantidad = solicitar_cantidad_estudiantes()
    calificaciones = leer_notas(cantidad)
    generar_estadisticas(calificaciones)