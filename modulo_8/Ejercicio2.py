planeta_lunas = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

lunas = planeta_lunas.values()

planetas = len(planeta_lunas.keys())

total_lunas = 0
for luna in lunas:
    total_lunas = total_lunas + luna

average = total_lunas / planetas

print(average)