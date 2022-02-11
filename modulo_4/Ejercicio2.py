planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

title = f'datos de gravedad sobre {nombre}'

hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""

plantilla = f"""{title.title()} 
{hechos} 
""" 
print(hechos)

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

print(hechos)
nuevaPlantilla = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(nuevaPlantilla.format(nombre=nombre, planeta=planeta, gravedad=gravedad))
# Pista: print(nueva_plantilla.format(variables))
print(nuevaPlantilla.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))