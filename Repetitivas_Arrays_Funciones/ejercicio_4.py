"""
Ejercicio 4: De una lista de N números determinar simultáneamente el máximo y mínimo número.
"""

def encontrar_min_max_simultaneo(numeros: list[float]) -> tuple[float, float]:
    minimo = maximo = numeros[0]
    for num in numeros[1:]:
        if num < minimo:
            minimo = num
        elif num > maximo:
            maximo = num
    return minimo, maximo

if __name__ == "__main__":
    n: int = int(input("Ingrese la cantidad de números (N): "))
    lista: list[float] = [float(input(f"Ingrese número {i + 1}: ")) for i in range(n)]

    menor, mayor = encontrar_min_max_simultaneo(lista)
    print(f"\nMínimo encontrado: {menor}")
    print(f"Máximo encontrado: {mayor}")