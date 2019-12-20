data = """.#..#
.....
#####
....#
...##"""


map = data.splitlines()
for row in map:
    print(row)

asteroids = {}

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '#':
            asteroids[(x,y)] = []


