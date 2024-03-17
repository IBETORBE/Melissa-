def calcular_descuento(monto_total):
    descuento = 20

    if monto_total > 100:  # Aplicamos un descuento del 10% si el monto total es mayor a 100
        descuento = monto_total * 0.10

    return monto_total - descuento


def main():
    monto_total = float(input("Ingrese el monto total de la compra: "))
    monto_final = calcular_descuento(monto_total)
    print("El monto final a pagar es:", monto_final)


if __name__ == "__main__":
    main()