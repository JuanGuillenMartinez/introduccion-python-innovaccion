n_planeta = ''
planetas = []

while n_planeta.lower() != 'Hecho':
    if n_planeta:
        planetas.append(n_planeta)
    n_planeta = input('Ingrese un nuevo planeta')
    