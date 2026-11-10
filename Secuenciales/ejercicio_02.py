"""
Ejercicio 2: Un estudiante realiza cuatro exámenes con la misma ponderación.
Obtener el promedio de las calificaciones obtenidas.
"""
from statistics import mean

def main() -> None:
    notas: list[float] = [
        float(input(f"Ingrese la calificación del examen {i}: "))
        for i in range(1, 5)
    ]
    promedio: float = mean(notas)
    print(f"\nEl promedio de los 4 exámenes es: {promedio:.2f}")

if __name__ == "__main__":
    main()