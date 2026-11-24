# Nombre del estudiante: Lizeth Nayive Clavijo Rey
# Grupo: 213022_1113
# Programa: Ingeniería de Sistemas
# Curso: Fundamentos de Programación
# Problema 3: Control de inventario y reabastecimiento
# Código fuente: Autoría propia

def calcular_reabastecimiento(stock_actual, stock_minimo):
    """
    Calcula cuántas unidades se deben solicitar.
    Si el stock actual está por debajo del mínimo, devuelve la diferencia.
    En caso contrario, devuelve cero.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def controlar_inventario():
    """Recorre la matriz y muestra el estado de reabastecimiento."""
    inventario = [
        [101, "Cuadernos", 5, 20],
        [102, "Lapices", 30, 15],
        [103, "Borradores", 3, 10],
        [104, "Reglas", 8, 12],
        [105, "Colores", 25, 20]
    ]

    print("=" * 55)
    print("           SISTEMA DE CONTROL DE INVENTARIO")
    print("=" * 55)
    print("{:<8} {:<15} {:>12} {:>12} {:>12}".format(
        "Codigo", "Articulo", "Stock actual", "Stock minimo", "A pedir"
    ))
    print("-" * 65)

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_reabastecimiento(
            stock_actual, stock_minimo
        )

        print("{:<8} {:<15} {:>12} {:>12} {:>12}".format(
            codigo, nombre, stock_actual, stock_minimo, cantidad_pedir
        ))

        if cantidad_pedir > 0:
            print("  Estado: Necesita reabastecimiento.")
        else:
            print("  Estado: Stock suficiente.")

    print("-" * 65)
    print("Proceso finalizado.")


if __name__ == "__main__":
    controlar_inventario()
