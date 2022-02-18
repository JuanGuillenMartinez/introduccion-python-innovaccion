def generate_report(main_tank, external_tank, hydrogen_tank):
    total_average = (main_tank + external_tank + hydrogen_tank) / 3
    return f"""Fuel Report:
    Total Average: {total_average}%
    Main tank: {main_tank}%
    External tank: {external_tank}%
    Hydrogen tank: {hydrogen_tank}% 
    """

print(generate_report(80, 70, 85))
    
# Función promedio 
def average(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

average([80, 85, 81]) 