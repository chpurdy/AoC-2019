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

# Need to make a list of asteroids that current asteroid can see
# Only add an asteroid of no other asteroids have the same "slope"

# Write a function blocking(atAst,ast1, ast2) that returns True
# if ast2 is blocking ast1 from atAst.
