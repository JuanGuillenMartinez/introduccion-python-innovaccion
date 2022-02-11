planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Neptuno']

planetaIngresado = input('Ingrese el nombre del planeta (La primer letra en mayúscula)')

indicePlaneta = planetas.index(planetaIngresado)

print('Los planetas mas cercanos al sol de ' + planetaIngresado + ' son: ')
print(planetas[0:indicePlaneta])

print('Los planetas mas lejanos del sol de ' + planetaIngresado + ' son:')
print(planetas[indicePlaneta + 1:])