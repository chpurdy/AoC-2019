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
# for planet in orbits.keys():
#     print(planet)
#     curr_plan = planet
#     while curr_plan in list(orbits.keys()):
#         count += 1
#         curr_plan = orbits[curr_plan][0]
# print(count)


stop = orbits['SAN'][0]
#print(orbits)
#count = 0
curr_plan = orbits['YOU'][0]

you_jumps = []

while curr_plan in list(orbits.keys()) and orbits[curr_plan][0] != stop:
    you_jumps.append(curr_plan)
    curr_plan = orbits[curr_plan][0]

curr_plan = orbits['SAN'][0]

san_jumps = []
while curr_plan not in you_jumps:
    san_jumps.append(curr_plan)
    curr_plan = orbits[curr_plan][0]

print(you_jumps.index(curr_plan)+len(san_jumps))


