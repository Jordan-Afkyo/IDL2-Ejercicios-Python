"""
Ejercicio 10: Costo de llamadas telefónicas internacionales según clave de zona.
Mostrar el nombre de la zona y el costo total de la llamada.
"""

def obtener_tarifa_zona(codigo: int) -> tuple[str, float] | None:
    match codigo:
        case 10: return ("América del norte", 2.2)
        case 12: return ("América del centro", 2.5)
        case 20: return ("América del sur", 1.2)
        case 22: return ("Asia", 3.5)
        case 30: return ("Europa", 3.0)
        case 32: return ("África", 3.2)
        case _:  return None

def main() -> None:
    print("Claves disponibles: 10, 12, 20, 22, 30, 32")
    codigo: int = int(input("Ingrese el código de la zona geográfica: "))
    minutos: float = float(input("Ingrese el número de minutos hablados: "))

    if datos := obtener_tarifa_zona(codigo):
        zona, costo_minuto = datos
        costo_total: float = minutos * costo_minuto
        print(f"\nZona geográfica a la que llamó : {zona}")
        print(f"Costo por minuto               : S/ {costo_minuto:.2f}")
        print(f"Costo total de la llamada      : S/ {costo_total:.2f}")
    else:
        print("\n Código de zona no válido.")

if __name__ == "__main__":
    main()