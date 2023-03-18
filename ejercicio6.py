class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, edad):
        if edad < 0:
            print("La edad no puede ser negativa.")
        else:
            self.edad = edad
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, dni):
        if len(dni) != 9:
            print("El DNI debe tener 9 caracteres.")
        else:
            self.dni = dni
    
    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)
    
    def es_mayor_de_edad(self):
        return self.edad >= 18

p = Persona()
p.set_nombre("Santiago")
p.set_edad(51)
p.set_dni("196099906")

p.mostrar()
print("¿Es mayor de edad?", p.es_mayor_de_edad())


