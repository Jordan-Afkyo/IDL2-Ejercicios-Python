"""
Ejercicio 4: Colegiatura según número de materias (S/100 c/u).
Si el promedio >= 18, se hace un descuento del 50% sobre la mitad de los cursos;
si es menor que 18, paga la colegiatura completa.
"""

COSTO_MATERIA: float = 100.0

def main() -> None:
    materias: int = int(input("Ingrese el número de materias que cursa: "))
    promedio: float = float(input("Ingrese el promedio obtenido en el último periodo: "))

    colegiatura_base: float = materias * COSTO_MATERIA

    # 50% de descuento sobre la mitad de los cursos equivale al 25% del costo total
    descuento: float = (colegiatura_base / 2) * 0.50 if promedio >= 18 else 0.0
    total_pagar: float = colegiatura_base - descuento

    print(f"\nCosto base ({materias} materias) : S/ {colegiatura_base:.2f}")
    print(f"Descuento por estímulo     : S/ {descuento:.2f}")
    print(f"Total a pagar por el alumno: S/ {total_pagar:.2f}")

if __name__ == "__main__":
    main()