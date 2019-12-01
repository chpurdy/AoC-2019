def fuel_required(mass):
    return (mass // 3) - 2


def advanced_fuel(mass):
    total = 0
    fuel_mass = fuel_required(mass)
    while fuel_mass > 0:
        total += fuel_mass
        fuel_mass = fuel_required(fuel_mass)
    return total




with open('input.txt') as f:
    total = 0
    for line in f.readlines():
        total += advanced_fuel(int(line))
    
print(total)