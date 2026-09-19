from abc import ABC, abstractmethod

class NoEsPlantaError(TypeError):
    pass

class Empresa:
    def __init__(self):
        self._lista_empleados = []

    def agregar_empleado(self, empleado):
        self._lista_empleados.append(empleado)

    def optimizar_sueldos(self,costo_por_hora,horas_minimas): #debe precarizar a todos los empleados de planta
        for empleado in self._lista_empleados:
            empleado.precarizar(costo_por_hora,horas_minimas)

    def mejor_sueldo(self):
        mejor_sueldo=0
        for empleado in self._lista_empleados:
            sueldo = empleado.sueldo_empleado()
            if sueldo > mejor_sueldo:
                mejor_sueldo = empleado.sueldo_empleado()
        return mejor_sueldo

    def total_sueldos_a_pagar(self):
        sueldos=0
        for empleado in self._lista_empleados:
            sueldos += empleado.sueldo_empleado()
        return sueldos

class Empleado(): #ContextStrategy
    def __init__(self, nombre, apellido, DNI, tipo_relacion_dependencia):
        self._nombre = nombre
        self._apellido = apellido
        self._DNI = DNI
        self._tipo_relacion_dependencia = tipo_relacion_dependencia #referencia a tipo relacion
        self._dias = []  #cada posición dentro de la lista representan las horas de ese día.

    @property
    def dias(self):
        return tuple(self._dias)

    def registrar_horas(self,dias): #voy cargando las horas trabajadas por el empleado
        for horas in dias:
            self._dias.append(horas)

    def sueldo_empleado(self):
        return self._tipo_relacion_dependencia.sueldo(self._dias) #envio como argumento las horas trabajadas por ese empleado.

    def efectivizar(self,nivel):
        self._tipo_relacion_dependencia = EmpleadoPlanta(nivel)

    def precarizar(self,costo_por_hora,horas_minimas):
        self._tipo_relacion_dependencia.precarizar_empleado(costo_por_hora,horas_minimas)

class PoliticaDependencia(ABC): #ContratoStrategy

    @abstractmethod
    def sueldo(self,dias):
        pass

    @abstractmethod
    def precarizar_empleado(self,costo_por_hora,horas_minimas):
        pass

class Contratado(PoliticaDependencia):
    def __init__(self,costo_por_hora,horas_minimas):
        self._costo_por_hora = costo_por_hora
        self._horas_minimas = horas_minimas

    def sueldo(self,dias):
        sueldo = 0
        for hora in dias:
            if hora >= self._horas_minimas:
                sueldo += self._costo_por_hora * self._horas_minimas #No se pagan horas extra
        return sueldo

    def precarizar_empleado(self,costo_por_hora,horas_minimas):
        pass

class EmpleadoPlanta(PoliticaDependencia): #contextoState
    def __init__(self, nivel):
        self._nivel = nivel

    def sueldo(self,dias):
        return self._nivel.calcular_sueldo(dias) #delega al metodo del nivel

    def precarizar_empleado(self,costo_por_hora,horas_minimas):
        return Contratado(costo_por_hora,horas_minimas)

class Nivel(ABC): #contratoState

    @abstractmethod
    def costo_por_hora(self):
        pass

    def calcular_sueldo(self, dias):
        horas = sum(dias) #en lugar de for, otra forma
        if horas <= 200:
            return horas * self.costo_por_hora()
        return 200 * self.costo_por_hora() + (horas - 200) * self.costo_por_hora() * 2

class Operativo(Nivel): #concretoState

    def costo_por_hora(self):
        return 500 #por ejemplo

class Tecnico(Nivel): #concretoState

    def costo_por_hora(self):
        return 1000 #por ejemplo

class Especialista(Nivel): #concretoState

    def costo_por_hora(self):
        return 2000  #por ejemplo

