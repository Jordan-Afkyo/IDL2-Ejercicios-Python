"""
Ejercicio 5: Determinar cuánto ahorrará una persona en un año si al final de cada mes
deposita cantidades variables de dinero. Mostrar el acumulado mes a mes y el ahorro final.
"""

def gestionar_ahorro_anual() -> None:
    # --- 1. INICIO ---
    
    # --- 2. DECLARACIÓN E INICIALIZACIÓN DE VARIABLES ---
    MESES: tuple[str, ...] = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )
    deposito_mensual: float = 0.0   # Monto ingresado en el mes actual (Real)
    ahorro_acumulado: float = 0.0   # Acumulador del ahorro anual (Real)
    mes_actual: str = ""            # Variable iteradora del nombre del mes (Texto)

    # --- 3. CUERPO DEL ALGORITMO ---
    for mes_actual in MESES:
        deposito_mensual = float(input(f"Depósito de {mes_actual:<10} (S/): "))
        ahorro_acumulado = ahorro_acumulado + deposito_mensual
        print(f"  -> Ahorro acumulado hasta {mes_actual}: S/ {ahorro_acumulado:,.2f}")

    print(f"\n Ahorro total al finalizar los 12 meses: S/ {ahorro_acumulado:,.2f}")
    
    # --- 4. FIN ---

if __name__ == "__main__":
    gestionar_ahorro_anual()
