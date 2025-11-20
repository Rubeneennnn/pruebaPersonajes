print("Hola Mundo")

class Persona:
    def __init__(self, name, surname, surname2="", edad=17):
        self.name = name
        self.surname = surname
        self.surname2 = surname2

    def saludar(self):
        return f"Hola {self.name} {self.surname}"

class Estudiante(Persona):
    def __init__(self, name, surname, surname2="", curso="", edad=17):
        super().__init__(name, surname, surname2="", edad=17)
        self.curso = curso

    def info(self):
        return f"Estudiante; Nombre: {self.name}, Apellido: {self.surname} y su curso es {self.curso}"

persona = "Acher Montuenga"
personaObject = Persona("Samuel", "Pañart", "Santolaria", 16)
personaObject2 = Persona("Rubén", "Iñiguez", "", 16)
student1 = Estudiante("Cristiano", "Ronaldo", "", "2 Bachiller", "")

print(f"Hola {persona}")
print(f"Hola {personaObject.name}")
print(personaObject2.saludar())
print(student1.info())