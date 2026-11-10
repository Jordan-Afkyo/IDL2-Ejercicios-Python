"""
Ejercicio 8: Obtener el área respectiva de un terreno con la Forma A
(compuesto por un rectángulo de base B y altura C, y un triángulo de base B y altura A-C).
"""

def main() -> None:
    lado_a: float = float(input("Ingrese la altura mayor A (m): "))
    lado_b: float = float(input("Ingrese la base B (m): "))
    lado_c: float = float(input("Ingrese la altura menor C (m): "))

    area_rectangulo: float = lado_b * lado_c
    area_triangulo: float = (lado_b * (lado_a - lado_c)) / 2
    area_total: float = area_rectangulo + area_triangulo

    print(f"\nÁrea del rectángulo : {area_rectangulo:.2f} m²")
    print(f"Área del triángulo  : {area_triangulo:.2f} m²")
    print(f"Área total terreno  : {area_total:.2f} m²")

if __name__ == "__main__":
    main()