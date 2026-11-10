"""
Ejercicio 3: Para tributar se debe ser mayor de 18 años y tener ingresos >= S/3000 mensuales.
Mostrar si debe tributar o no, y el monto a tributar (5% del ingreso mensual).
"""

def main() -> None:
    edad: int = int(input("Ingrese su edad: "))
    ingresos: float = float(input("Ingrese sus ingresos mensuales (S/): "))

    if edad > 18 and ingresos >= 3000:
        impuesto: float = ingresos * 0.05
        print(f"\n[SÍ DEBE TRIBUTAR] Monto a pagar (5%): S/ {impuesto:,.2f}")
    else:
        print("\n[NO DEBE TRIBUTAR] No cumple con ambos requisitos para el impuesto.")

if __name__ == "__main__":
    main()