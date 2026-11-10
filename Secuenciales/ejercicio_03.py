"""
Ejercicio 3: Tres personas deciden invertir su dinero para fundar una empresa.
Obtener el porcentaje que cada uno invierte respecto al total.
"""

def main() -> None:
    inversiones: list[float] = [
        float(input(f"Monto invertido por la persona {i} (S/): "))
        for i in range(1, 4)
    ]
    total_invertido: float = sum(inversiones)

    print(f"\nInversión Total: S/ {total_invertido:,.2f}")
    for idx, monto in enumerate(inversiones, start=1):
        porcentaje: float = (monto / total_invertido) * 100 if total_invertido > 0 else 0.0
        print(f"Persona {idx}: S/ {monto:,.2f} -> {porcentaje:.2f}%")

if __name__ == "__main__":
    main()