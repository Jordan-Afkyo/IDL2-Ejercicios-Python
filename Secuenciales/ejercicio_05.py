"""
Ejercicio 5: Un individuo desea invertir su capital en un banco y desea saber
cuánto dinero ganará después de un año si el banco paga a razón de 2% mensual.
"""

TASA_MENSUAL: float = 0.02
MESES: int = 12

def main() -> None:
    capital: float = float(input("Ingrese el capital a invertir (S/): "))

    # Interés simple (2% mensual fijo durante 12 meses = 24% anual)
    ganancia_simple: float = capital * TASA_MENSUAL * MESES
    monto_final_simple: float = capital + ganancia_simple

    # Interés compuesto (reinvertido mes a mes)
    monto_final_compuesto: float = capital * ((1 + TASA_MENSUAL) ** MESES)
    ganancia_compuesta: float = monto_final_compuesto - capital

    print("\n--- Resultados después de 1 año (12 meses) ---")
    print(f"[Interés Simple]    Ganancia: S/ {ganancia_simple:,.2f} | Total: S/ {monto_final_simple:,.2f}")
    print(f"[Interés Compuesto] Ganancia: S/ {ganancia_compuesta:,.2f} | Total: S/ {monto_final_compuesto:,.2f}")

if __name__ == "__main__":
    main()