print('Ejercicio de condicionales if, else, elif\nIngrese el tamaño del asteroide')
tamañoAsteroide = int(input())
print('Ingrese la velocidad del asteroide')
velocidadAsteroide = int(input())

if (tamañoAsteroide > 25 and tamañoAsteroide < 1000) :
    print('Peligro: el tamaño del asteroide es muy grande')  
else :
    print('No hay peligro')
if (velocidadAsteroide > 25) :
    print('Advertencia: el asteroide se acerca muy rápido')
else :
    print('No hay peligro')
    