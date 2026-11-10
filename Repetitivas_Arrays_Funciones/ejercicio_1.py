"""
Ejercicio 1: Calcular la suma y promedio de los números pares e impares
por separado, de 1 hasta N.
"""

def analizar_rango(n: int) -> None:
    pares: list[int] = [i for i in range(1, n + 1) if i % 2 == 0]
    impares: list[int] = [i for i in range(1, n + 1) if i % 2 != 0]

    suma_pares: int = sum(pares)
    prom_pares: float = suma_pares / len(pares) if pares else 0.0

    suma_impares: int = sum(impares)
    prom_impares: float = suma_impares / len(impares) if impares else 0.0

    print(f"\n--- Resultados del 1 al {n} ---")
    print(f"PARES   -> Suma: {suma_pares} | Promedio: {prom_pares:.2f}")
    print(f"IMPARES -> Suma: {suma_impares} | Promedio: {prom_impares:.2f}")

if __name__ == "__main__":
    limite: int = int(input("Ingrese el valor de N: "))
    analizar_rango(limite)