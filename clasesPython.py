class Estudiante():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def hola(self):
        return "Mi nombre es %s" % self.nombre

e = Estudiante("Alexmar", 25)
e.hola()