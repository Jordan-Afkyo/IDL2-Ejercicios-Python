"""
Ejercicio 7: Calcular el pago de una llamada telefónica:
- Primeros 5 minutos: S/ 1.00 c/u
- Siguientes 3 minutos (6 al 8): S/ 0.80 c/u
- Siguientes 2 minutos (9 al 10): S/ 0.70 c/u
- A partir del décimo minuto (>10): S/ 0.50 c/u
Impuesto: 3% si es domingo (diurno), 5% si es domingo de turno nocturno.
"""

def calcular_costo_base(minutos: int) -> float:
    match minutos:
        case m if m <= 5:
            return m * 1.00
        case m if m <= 8:
            return (5 * 1.00) + ((m - 5) * 0.80)
        case m if m <= 10:
            return (5 * 1.00) + (3 * 0.80) + ((m - 8) * 0.70)
        case m:
            return (5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((m - 10) * 0.50)

def main() -> None:
    minutos: int = int(input("Ingrese la duración de la llamada en minutos: "))
    es_domingo: str = input("¿La llamada se realizó en domingo? (S/N): ").strip().upper()

    tasa_impuesto: float = 0.0
    if es_domingo == "S":
        turno: str = input("Ingrese el turno (D = Diurno / N = Nocturno): ").strip().upper()
        tasa_impuesto = 0.05 if turno == "N" else 0.03

    subtotal: float = calcular_costo_base(minutos)
    impuesto: float = subtotal * tasa_impuesto
    total: float = subtotal + impuesto

    print(f"\nCosto por tiempo ({minutos} min) : S/ {subtotal:.2f}")
    print(f"Impuesto aplicado ({tasa_impuesto*100:.0f}%)   : S/ {impuesto:.2f}")
    print(f"Total a pagar              : S/ {total:.2f}")

if __name__ == "__main__":
    main()