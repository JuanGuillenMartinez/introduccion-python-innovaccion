text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
arrayOraciones = text.split('.')
print('Resumen')
for oracion in arrayOraciones :
    if( oracion.find('average') != -1 or oracion.find('temperature') != -1 or oracion.find('distance') != -1) :
        print(oracion)
        if (oracion.find('C') != -1) :
            nuevoTexto = oracion.replace('C', 'Celsius')
            print('La nueva oracion es', nuevoTexto)