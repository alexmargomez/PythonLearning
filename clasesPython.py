class Estudiante():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def hola(self):
        return "Mi nombre es %s" % self.nombre

def run():
    e = Estudiante("Alexmar", 25)
    e.hola()

if __name__=='__main__':
    run()