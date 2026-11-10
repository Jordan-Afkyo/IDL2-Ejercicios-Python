"""
Ejercicio 6: Hacer un programa que muestre un cronómetro (hh:mm:ss) referencial.
"""
import time

def ejecutar_cronometro(segundos_limite: int) -> None:
    contador: int = 0
    for hh in range(24):
        for mm in range(60):
            for ss in range(60):
                print(f"\r Cronómetro: {hh:02d}:{mm:02d}:{ss:02d}", end="", flush=True)
                if contador >= segundos_limite:
                    print("\n¡Tiempo referencial completado!")
                    return
                time.sleep(0.05)  # Tiempo referencial acelerado
                contador += 1

if __name__ == "__main__":
    limite: int = int(input("¿Hasta cuántos segundos desea simular el cronómetro?: "))
    ejecutar_cronometro(limite)