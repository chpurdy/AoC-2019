from collections import defaultdict

data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())

orbits = defaultdict(list)

for pair in data:
    mapping = pair.split(")")
    orbits[mapping[1]] += [mapping[0]]

count = 0
for planet in orbits.keys():
    #print(planet)
    curr_plan = planet
    while curr_plan in list(orbits.keys()):
        count += 1
        curr_plan = orbits[curr_plan][0]
print(count)
