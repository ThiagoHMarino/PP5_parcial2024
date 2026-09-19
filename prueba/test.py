import pytest

from solucion.pedido import *

#----------------------------------------------------------------------------------------------------------------------

# Incorporar nuevos empleados indicando sus datos personales y su categoría.

def test_incorporar():

    assert Empleado("Thiago","Marino",4444,Contratado(300,8))
    assert Empleado("Juan", "Perez", 1111, Contratado(250, 6))
    assert Empleado("Ramiro","Gonzalez",3333,EmpleadoPlanta(Operativo()))

#----------------------------------------------------------------------------------------------------------------------

# Calcular el sueldo de cada empleado según su categoría a fin de mes.

def test_calcular_sueldo_Contratado():

    empleado = Empleado("Thiago", "Marino", 4444, Contratado(300, 8))

    diasEnero_Thiago = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ] # 22 días con 8 horas
    # 22 * 8 * 300 = 52.800

    empleado.registrar_horas(diasEnero_Thiago)

    assert empleado.sueldo_empleado()==52800

def test_calcular_sueldo_Planta():

    empleado = Empleado("Ramiro","Gonzalez",3333,EmpleadoPlanta(Operativo()))

    diasEnero_Ramiro = [
        8, 8, 8, 8, 8,
        8, 8, 8, 8, 8,
        4, 4, 4, 4, 4,
        8, 8, 8, 8, 8,
        8, 8, 8, 8, 8,
        8, 8, 6, 7, 7
    ] #216 horas
    # 200 horas normales + 16 extra
    # 200 * 500 (lo que cobra Operativo en mi ejemplo) + (16 * 500) * 2 = 116000

    empleado.registrar_horas(diasEnero_Ramiro)

    assert empleado.sueldo_empleado()==116000

#----------------------------------------------------------------------------------------------------------------------

# Obtener el total de sueldos que deben pagarse a fin de mes
# Obtener cuál es el mejor sueldo del mes.

def test_total_sueldos_a_pagarse():

    empleado_planta_operativo = Empleado("Ramiro", "Gonzalez", 3333, EmpleadoPlanta(Operativo()))
    empleado_contratado = Empleado("Thiago", "Marino", 4444, Contratado(300, 8))

    diasEnero_Ramiro = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]

    empleado_planta_operativo.registrar_horas(diasEnero_Ramiro)

    diasEnero_Thiago = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]

    empleado_contratado.registrar_horas(diasEnero_Thiago)

    empresa = Empresa()

    empresa.agregar_empleado(empleado_contratado)
    empresa.agregar_empleado(empleado_planta_operativo)

    assert empresa.total_sueldos_a_pagar() == (52800+116000)
    assert empresa.mejor_sueldo() == 116000 # También podría obtener el empleado modificando el for.

#----------------------------------------------------------------------------------------------------------------------

# Efectivizar empleados contratados, asignándoles un determinado nivel de planta.

def test_efectivizar_empleados():

    empleado_contratado1 = Empleado("Thiago", "Marino", 4444, Contratado(300, 8))
    empleado_contratado2 = Empleado("Ramon", "Castro", 1111, Contratado(350, 6))

    empleado_contratado1.efectivizar(Especialista()) #gana 2000
    empleado_contratado2.efectivizar(Tecnico()) #gana 1000

    diasEnero_Thiago = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]#200 × 2000 = 400000 + 16 × 2000 × 2 = 64000
    #TOTAL = 464000

    empleado_contratado1.registrar_horas(diasEnero_Thiago)

    diasEnero_Ramon = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]#200 × 1000 = 200000 + 16 * 1000 * 2 = 32000
    #TOTAL = 232000

    empleado_contratado2.registrar_horas(diasEnero_Ramon)

    assert empleado_contratado1.sueldo_empleado() == 464000
    assert empleado_contratado2.sueldo_empleado() == 232000

#----------------------------------------------------------------------------------------------------------------------

# Precarizar empleados de planta, asignándoles el contrato correspondiente.

def test_precarizar_empleados():

    empleado_planta_operativo = Empleado("Ramiro", "Gonzalez", 3333, EmpleadoPlanta(Operativo()))

    diasEnero_Ramiro = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]

    empleado_planta_operativo.registrar_horas(diasEnero_Ramiro)

    assert empleado_planta_operativo.sueldo_empleado() == 116000

    empleado_planta_operativo2 = Empleado("Juan", "Perez", 3333, EmpleadoPlanta(Tecnico()))

    diasEnero_Juan = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]

    empleado_planta_operativo2.registrar_horas(diasEnero_Juan)

    assert empleado_planta_operativo2.sueldo_empleado() == 232000

    empleado_contratado1 = Empleado("Thiago", "Marino", 4444, Contratado(300, 8))

    diasEnero_Thiago = [
        8, 8, 8, 8, 8,
        8, 4, 8, 4, 4,
        4, 8, 8, 8, 8,
        8, 8, 6, 7, 8,
        8, 4, 8, 8, 8,
        8, 8, 7, 8, 8
    ]

    empleado_contratado1.registrar_horas(diasEnero_Thiago)

    assert empleado_contratado1.sueldo_empleado() == 52800

    empresa = Empresa()

    empresa.agregar_empleado(empleado_contratado1)
    empresa.agregar_empleado(empleado_planta_operativo2)
    empresa.agregar_empleado(empleado_planta_operativo)

    empresa.optimizar_sueldos(300,8) #todos los sueldos a 300/h y 8 horas como minimo.

    assert empresa.total_sueldos_a_pagar() == 158400






