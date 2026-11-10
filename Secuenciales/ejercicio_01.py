"""
Ejercicio 1: Determina la velocidad final de un auto si su velocidad inicial es 0 km/h,
su aceleración es 0.8 m/s² y el tiempo transcurrido es de 30 segundos.
"""

def calcular_velocidad_final(v_inicial_ms: float = 0.0, aceleracion: float = 0.8, tiempo: float = 30.0) -> None:
    v_final_ms: float = v_inicial_ms + (aceleracion * tiempo)
    v_final_kmh: float = v_final_ms * 3.6

    print(f"Velocidad inicial : {v_inicial_ms:.2f} m/s")
    print(f"Aceleración       : {aceleracion:.2f} m/s²")
    print(f"Tiempo            : {tiempo:.2f} s")
    print(f"Velocidad Final   : {v_final_ms:.2f} m/s ({v_final_kmh:.2f} km/h)")

if __name__ == "__main__":
    calcular_velocidad_final()