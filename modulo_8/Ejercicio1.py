planeta = {
    'nombre': 'Marte',
    'lunas': 2
}
# Muestra el nombre del planeta y el número de lunas que tiene.

print(f'{planeta["nombre"]} tiene {planeta["lunas"]} luna/s')

planeta['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planeta["nombre"]} tiene una circunferencia polar de {planeta["circunferencia (km)"]["polar"]}Km')