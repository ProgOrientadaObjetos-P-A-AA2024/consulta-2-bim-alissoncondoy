class Estudiante:
    def __init__(self, nombres, apellidos, identificacion, edad):
        self.nombres_estudiante = nombres
        self.apellidos_estudiante = apellidos
        self.identificacion_estudiante = identificacion
        self.edad_estudiante = edad
    
    def establecer_nombres_estudiante(self, nombres):
        self.nombres_estudiante = nombres
    
    def establecer_apellidos_estudiante(self, apellidos):
        self.apellidos_estudiante = apellidos
    
    def establecer_identificacion_estudiante(self, identificacion):
        self.identificacion_estudiante = identificacion
    
    def establecer_edad_estudiante(self, edad):
        self.edad_estudiante = edad
    
    def obtener_nombres_estudiante(self):
        return self.nombres_estudiante
    
    def obtener_apellidos_estudiante(self):
        return self.apellidos_estudiante
    
    def obtener_identificacion_estudiante(self):
        return self.identificacion_estudiante
    
    def obtener_edad_estudiante(self):
        return self.edad_estudiante
    
    def __str__(self):
        return (f"Nombre: {self.nombres_estudiante}\n"
                f"Apellido: {self.apellidos_estudiante}\n"
                f"Identificación: {self.identificacion_estudiante}\n"
                f"Edad: {self.edad_estudiante}\n")


class EstudianteDistancia(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad, numero_asignaturas=0, costo_asignatura=0.0):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_asignaturas = numero_asignaturas
        self.costo_asignatura = costo_asignatura
        self.matricula_distancia = 0.0
    
    def establecer_numero_asignaturas(self, numero):
        self.numero_asignaturas = numero
    
    def establecer_costo_asignatura(self, costo):
        self.costo_asignatura = costo
    
    def calcular_matricula_distancia(self):
        self.matricula_distancia = self.numero_asignaturas * self.costo_asignatura
    
    def obtener_numero_asignaturas(self):
        return self.numero_asignaturas
    
    def obtener_costo_asignatura(self):
        return self.costo_asignatura
    
    def obtener_matricula_distancia(self):
        return self.matricula_distancia
    
    def __str__(self):
        return (f"Nombre: {self.nombres_estudiante}\n"
                f"Apellido: {self.apellidos_estudiante}\n"
                f"Identificación: {self.identificacion_estudiante}\n"
                f"Edad: {self.edad_estudiante}\n"
                f"Costo Asignatura: {self.costo_asignatura:.2f}\n"
                f"Número de Asignaturas: {self.numero_asignaturas}\n"
                f"Total Matrícula: {self.matricula_distancia:.2f}\n")


class EstudiantePresencial(Estudiante):
    def __init__(self, nombres, apellidos, identificacion, edad, numero_creditos=0, costo_credito=0.0):
        super().__init__(nombres, apellidos, identificacion, edad)
        self.numero_creditos = numero_creditos
        self.costo_credito = costo_credito
        self.matricula_presencial = 0.0
    
    def establecer_numero_creditos(self, numero):
        self.numero_creditos = numero
    
    def establecer_costo_credito(self, costo):
        self.costo_credito = costo
    
    def calcular_matricula_presencial(self):
        self.matricula_presencial = self.numero_creditos * self.costo_credito
    
    def obtener_numero_creditos(self):
        return self.numero_creditos
    
    def obtener_costo_credito(self):
        return self.costo_credito
    
    def obtener_matricula_presencial(self):
        return self.matricula_presencial
    
    def __str__(self):
        return (f"Nombre: {self.nombres_estudiante}\n"
                f"Apellido: {self.apellidos_estudiante}\n"
                f"Identificación: {self.identificacion_estudiante}\n"
                f"Edad: {self.edad_estudiante}\n"
                f"Número de Créditos: {self.numero_creditos}\n"
                f"Costo de Créditos: {self.costo_credito:.2f}\n"
                f"Valor Matrícula Presencial: {self.matricula_presencial:.2f}\n")


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    estudiantes_presenciales = []
    
    i = 0
    while i < len(data):
        nombre = data[i].strip()
        apellido = data[i + 1].strip()
        identificacion = data[i + 2].strip()
        edad = int(data[i + 3].strip())
        numero_creditos = int(data[i + 4].strip())
        costo_credito = float(data[i + 5].strip())
        
        estudiante = EstudiantePresencial(nombre, apellido, identificacion, edad, costo_credito=costo_credito, numero_creditos=numero_creditos)
        estudiante.calcular_matricula_presencial()
        estudiantes_presenciales.append(estudiante)
        
        i += 7  # Move to the next block of input
    
    for estudiante in estudiantes_presenciales:
        print(estudiante)


if __name__ == "__main__":
    main()
