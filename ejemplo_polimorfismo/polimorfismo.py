from abc import ABC, abstractmethod

class Arriendo(ABC):
    def __init__(self, nombre, cuota_base):
        self.nombre_arrendatario = nombre
        self.cuota_base = cuota_base
        self.arriendo_mensual = 0.0

    def establecer_nombre_arrendatario(self, nombre):
        self.nombre_arrendatario = nombre

    def establecer_cuota_base(self, cuota_base):
        self.cuota_base = cuota_base

    @abstractmethod
    def establecer_arriendo_mensual(self):
        pass

    def obtener_nombre_arrendatario(self):
        return self.nombre_arrendatario

    def obtener_cuota_base(self):
        return self.cuota_base

    def obtener_arriendo_mensual(self):
        return self.arriendo_mensual


class ArriendoLocalComercial(Arriendo):
    def __init__(self, nombre, cuota_base):
        super().__init__(nombre, cuota_base)
        self.valor_adicional_fijo = 0.0

    def establecer_nombre_arrendatario(self, nombre):
        self.nombre_arrendatario = nombre.upper()

    def establecer_valor_adicional_fijo(self, valor):
        self.valor_adicional_fijo = valor

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = self.obtener_cuota_base() + self.obtener_valor_adicional_fijo()

    def obtener_valor_adicional_fijo(self):
        return self.valor_adicional_fijo

    def __str__(self):
        return (f"Arriendo de Local Comercial\n"
                f"Nombre Arrendatario: {self.obtener_nombre_arrendatario()}\n"
                f"Cuota base: {self.obtener_cuota_base():.2f}\n"
                f"Valor adicional fijo: {self.obtener_valor_adicional_fijo():.2f}\n"
                f"Arriendo Total: {self.obtener_arriendo_mensual():.2f}\n")


class ArriendoLocalComida(Arriendo):
    def __init__(self, nombre, cuota_base, valor_luz=0.0, valor_agua=0.0, iva=0.0):
        super().__init__(nombre, cuota_base)
        self.valor_luz = valor_luz
        self.valor_agua = valor_agua
        self.iva = iva

    def establecer_valor_luz(self, valor):
        self.valor_luz = valor

    def establecer_valor_agua(self, valor):
        self.valor_agua = valor

    def establecer_iva(self, iva):
        self.iva = iva

    def establecer_arriendo_mensual(self):
        subtotal = self.obtener_valor_agua() + self.obtener_valor_luz() + self.obtener_cuota_base()
        self.arriendo_mensual = subtotal + (subtotal * (self.obtener_iva() / 100))

    def obtener_valor_luz(self):
        return self.valor_luz

    def obtener_valor_agua(self):
        return self.valor_agua

    def obtener_iva(self):
        return self.iva

    def __str__(self):
        return (f"Arriendo de Local Comida\n"
                f"Nombre Arrendatario: {self.obtener_nombre_arrendatario()}\n"
                f"Cuota base: {self.obtener_cuota_base():.2f}\n"
                f"Valor luz: {self.obtener_valor_luz():.2f}\n"
                f"Valor agua: {self.obtener_valor_agua():.2f}\n"
                f"Porcentaje iva: {self.obtener_iva():.2f}\n"
                f"Arriendo Total: {self.obtener_arriendo_mensual():.2f}\n")


class ArriendoLocalSesiones(Arriendo):
    def __init__(self, nombre, cuota_base):
        super().__init__(nombre, cuota_base)
        self.valor_sillas = 0.0
        self.valor_amplificacion = 0.0

    def establecer_valor_sillas(self, valor):
        self.valor_sillas = valor

    def establecer_valor_amplificacion(self, valor):
        self.valor_amplificacion = valor

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = (self.obtener_cuota_base() +
                                 self.obtener_valor_sillas() +
                                 self.obtener_valor_amplificacion())

    def obtener_valor_sillas(self):
        return self.valor_sillas

    def obtener_valor_amplificacion(self):
        return self.valor_amplificacion

    def __str__(self):
        return (f"Arriendo de Local Sesiones\n"
                f"Nombre Arrendatario: {self.obtener_nombre_arrendatario()}\n"
                f"Cuota base: {self.obtener_cuota_base():.2f}\n"
                f"Valor sillas: {self.obtener_valor_sillas():.2f}\n"
                f"Valor amplificación: {self.obtener_valor_amplificacion():.2f}\n"
                f"Arriendo Total: {self.obtener_arriendo_mensual():.2f}\n")


def main():
    lista_arriendos = []

    arriendo_comida = ArriendoLocalComida("Christian Shepherd", 300)
    arriendo_comida.establecer_iva(10)  # en porcentaje
    arriendo_comida.establecer_valor_agua(20.2)  # en $
    arriendo_comida.establecer_valor_luz(40.2)  # en $

    arriendo_comida2 = ArriendoLocalComida("Christian Cruz", 300, 10, 20.2, 40.2)

    arriendo_comercial = ArriendoLocalComercial("Andrew Schroeder", 400)
    arriendo_comercial.establecer_valor_adicional_fijo(100)  # en $

    arriendo_sesiones = ArriendoLocalSesiones("Angela Watson", 350)
    arriendo_sesiones.establecer_valor_sillas(10)  # en $
    arriendo_sesiones.establecer_valor_amplificacion(20)  # en $

    lista_arriendos.extend([arriendo_comida, arriendo_comercial, arriendo_sesiones])

    for arriendo in lista_arriendos:
        arriendo.establecer_arriendo_mensual()  # se llama al método abstracto
        print(arriendo)
        print()


if __name__ == "__main__":
    main()
