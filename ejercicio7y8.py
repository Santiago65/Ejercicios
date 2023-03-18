class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion

    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        edad_minima = 18
        edad_maxima = 25
        edad_titular = self.get_titular().get_edad()
        return edad_titular >= edad_minima and edad_titular < edad_maxima

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        print("Cuenta Joven")
        print(f"Bonificación: {self.__bonificacion}%")
        super().mostrar()