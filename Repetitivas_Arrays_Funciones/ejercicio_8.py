"""
Ejercicio 8: Registro de N asistentes a una fiesta (edades y sexos).
Calcular total de asistentes, hombres y mujeres, promedio de edad por sexo,
y la edad de la persona menor y mayor que asistió.
"""

type Asistente = tuple[int, str]

def registrar_asistentes() -> list[Asistente]:
    asistentes: list[Asistente] = []
    while True:
        edad: int = int(input("\nIngrese la edad del asistente: "))
        while (sexo := input("Ingrese el sexo (H = Hombre / M = Mujer): ").strip().upper()) not in ("H", "M"):
            print(" Ingrese únicamente 'H' o 'M'.")

        asistentes.append((edad, sexo))

        continuar: str = input("¿Desea registrar a otra persona? (S/N): ").strip().upper()
        if continuar != "S":
            break
    return asistentes

def mostrar_reporte(asistentes: list[Asistente]) -> None:
    edades_totales: list[int] = [e for e, _ in asistentes]
    edades_hombres: list[int] = [e for e, s in asistentes if s == "H"]
    edades_mujeres: list[int] = [e for e, s in asistentes if s == "M"]

    prom_h: float = sum(edades_hombres) / len(edades_hombres) if edades_hombres else 0.0
    prom_m: float = sum(edades_mujeres) / len(edades_mujeres) if edades_mujeres else 0.0

    print("\n--- Reporte Final de la Fiesta ---")
    print(f"• Total de asistentes        : {len(asistentes)}")
    print(f"• Cantidad de hombres        : {len(edades_hombres)}")
    print(f"• Cantidad de mujeres        : {len(edades_mujeres)}")
    print(f"• Promedio de edad (Hombres) : {prom_h:.2f} años")
    print(f"• Promedio de edad (Mujeres) : {prom_m:.2f} años")
    print(f"• Persona de menor edad      : {min(edades_totales)} años")
    print(f"• Persona de mayor edad      : {max(edades_totales)} años")

if __name__ == "__main__":
    datos = registrar_asistentes()
    mostrar_reporte(datos)