primerPlaneta = input('Ingrese la distancia del primer planeta en KM ')
segundoPlaneta = input('Ingrese la distancia del segundo planeta en KM ')

primerPlaneta = int(primerPlaneta)
segundoPlaneta = int(segundoPlaneta)

distanciaKm = segundoPlaneta - primerPlaneta
print(distanciaKm)

distanciaMillas = distanciaKm * 0.621
print(abs(distanciaMillas))