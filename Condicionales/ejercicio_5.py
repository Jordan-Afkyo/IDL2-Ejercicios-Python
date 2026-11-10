"""
Ejercicio 5: Ingresar 3 lados de un triángulo y determinar si es:
- Equilátero: Mostrar el perímetro.
- Isósceles: Indicar qué lados son iguales.
- Escaleno: Mostrar el área del triángulo (Fórmula de Herón).
"""
import math

def main() -> None:
    a: float = float(input("Ingrese el lado A: "))
    b: float = float(input("Ingrese el lado B: "))
    c: float = float(input("Ingrese el lado C: "))

    # Validación de existencia de un triángulo
    if not (a + b > c and a + c > b and b + c > a):
        print("\nError: Los lados ingresados NO forman un triángulo válido.")
        return

    match (a == b, b == c, a == c):
        case (True, True, True):
            perimetro: float = a + b + c
            print(f"\nTriángulo EQUILÁTERO -> Perímetro: {perimetro:.2f}")
        case (True, False, False):
            print(f"\nTriángulo ISÓSCELES -> Los lados A y B son iguales ({a}).")
        case (False, True, False):
            print(f"\nTriángulo ISÓSCELES -> Los lados B y C son iguales ({b}).")
        case (False, False, True):
            print(f"\nTriángulo ISÓSCELES -> Los lados A y C son iguales ({a}).")
        case _:
            s: float = (a + b + c) / 2
            area: float = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"\nTriángulo ESCALENO -> Área: {area:.2f}")

if __name__ == "__main__":
    main()