"""
Ejercicio 3: Para tributar se debe ser mayor de 18 años y tener ingresos >= S/3000 mensuales.
Mostrar si debe tributar o no, y el monto a tributar (5% del ingreso mensual).
"""

def main() -> None:
    # --- 1. INICIO ---
    
    # --- 2. DECLARACIÓN E INICIALIZACIÓN DE VARIABLES ---
    TASA_IMPUESTO: float = 0.05  # Porcentaje de tributación (5%)
    edad: int = 0                # Edad del usuario (Entero)
    ingresos: float = 0.0        # Ingresos mensuales en soles (Real)
    impuesto: float = 0.0        # Monto calculado a tributar (Real)

    # --- 3. CUERPO DEL ALGORITMO ---
    edad = int(input("Ingrese su edad: "))
    ingresos = float(input("Ingrese sus ingresos mensuales (S/): "))

    if edad > 18 and ingresos >= 3000:
        impuesto = ingresos * TASA_IMPUESTO
        print(f"\n[SÍ DEBE TRIBUTAR] Monto a pagar (5%): S/ {impuesto:,.2f}")
    else:
        print("\n[NO DEBE TRIBUTAR] No cumple con ambos requisitos para el impuesto.")
        
    # --- 4. FIN ---

if __name__ == "__main__":
    main()
