1. ¿Es necesario realizar cambios sobre la lógica inicial del método
total_sueldos_a_pagar cuando se agreguen nuevos tipos de empleados? Justificar
conceptualmente.

No, no es necesario ya que el método "total_sueldos_a_pagar" obtiene los sueldos de los respectivos empleados, delegando
en el método "sueldo_empleado()" que a su vez delega en el metodo de cada tipo de empleado "tipo_relacion_dependencia.sueldo()".

Por lo tanto si se incorporara un nuevo tipo de empleado, bastaría unicamente con crear la nueva clase correspondiente
a la nueva categoría, en donde el metodo total_sueldos_a_pagar, no sufriria ningun cambio.

2. ¿Qué concepto del paradigma orientado a objetos se rompería al utilizar IF en el método
optimizar_sueldos? Justificar conceptualmente.

Se rompería el polimorfismo, ya que de esa forma Empresa debería conocer el tipo de cada empleado para decidir si aplicar
o no el metodo "precarizar()". 

Sin la presencia del IF empresa simplemente llama, dentro del metodo "optimizar_sueldos()",
al metodo "precarizar()" de Empleado. A su vez, Empleado delega la operación en el objeto que representa su relación de 
dependencia, mediante el metodo "precarizar_empleado()". De esta forma, cada implementación de PoliticaDependencia 
define su propio comportamiento.
# PP5_parcial2024
