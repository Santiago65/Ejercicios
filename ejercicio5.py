"""Iteractiva"""

def get_int():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("El valor ingresado no es un número entero válido. Intente de nuevo.")

"""Recursiva"""
def get_int():
    try:
        num = int(input("Ingrese un número entero: "))
        return num
    except ValueError:
        print("El valor ingresado no es un número entero válido. Intente de nuevo.")
        return get_int()

numero = get_int()
print("El número ingresado es:", numero)
