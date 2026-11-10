"""
Ejercicio 2: Pedir 10 números y determinar e imprimir cuántos son
pares, impares, positivos, neutros (0) y negativos.
"""

def clasificar_numeros(numeros: list[int]) -> None:
    pares = sum(1 for n in numeros if n != 0 and n % 2 == 0)
    impares = sum(1 for n in numeros if n % 2 != 0)
    positivos = sum(1 for n in numeros if n > 0)
    neutros = sum(1 for n in numeros if n == 0)
    negativos = sum(1 for n in numeros if n < 0)

    print("\n--- Resumen de los 10 números ---")
    print(f"- Pares (sin contar 0) : {pares}")
    print(f"- Impares              : {impares}")
    print(f"- Positivos            : {positivos}")
    print(f"- Neutros (Cero)       : {neutros}")
    print(f"- Negativos            : {negativos}")

if __name__ == "__main__":
    lista_numeros: list[int] = [
        int(input(f"Ingrese el número {i}/10: "))
        for i in range(1, 11)
    ]
    clasificar_numeros(lista_numeros)