"""
Ejercicio 3: Ingresar un conjunto de N números y un número más X. Mostrar:
- Porcentaje de números menores que X.
- Porcentaje de números mayores de X.
- Porcentaje de números iguales a X.
- Porcentaje de números comprendidos entre 1 y X (inclusive).
- Porcentaje de números que no cumplen ninguna condición.
"""

def evaluar_conjunto(numeros: list[float], x: float) -> None:
    total: int = len(numeros)
    if total == 0:
        return

    lim_inf, lim_sup = min(1.0, x), max(1.0, x)

    menores = sum(1 for n in numeros if n < x)
    mayores = sum(1 for n in numeros if n > x)
    iguales = sum(1 for n in numeros if n == x)
    entre_1_y_x = sum(1 for n in numeros if lim_inf <= n <= lim_sup)
    ninguna = sum(1 for n in numeros if not (n < x or n > x or n == x or (lim_inf <= n <= lim_sup)))

    print(f"\n--- Estadísticas respecto a X = {x} ---")
    print(f"• Menores que X            : {(menores / total) * 100:.2f}%")
    print(f"• Mayores que X            : {(mayores / total) * 100:.2f}%")
    print(f"• Iguales a X              : {(iguales / total) * 100:.2f}%")
    print(f"• Comprendidos entre 1 y X : {(entre_1_y_x / total) * 100:.2f}%")
    print(f"• Ninguna condición        : {(ninguna / total) * 100:.2f}%")

if __name__ == "__main__":
    n: int = int(input("¿Cuántos números (N) desea ingresar?: "))
    datos: list[float] = [float(input(f"Número {i + 1}: ")) for i in range(n)]
    valor_x: float = float(input("Ingrese el número de referencia X: "))
    evaluar_conjunto(datos, valor_x)