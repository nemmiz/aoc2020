def calculate_adjacent(grid):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    adjacency = {}
    for pos in grid:
        adjacent = []
        for offset in offsets:
            tmp = (pos[0] + offset[0],pos[1] + offset[1])
            if tmp in grid:
                adjacent.append(tmp)
        adjacency[pos] = adjacent
    return adjacency

def calculate_visible(grid):
    max_pos = max(grid.keys())
    deltas = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visibility = {}
    for pos in grid:
        visible = []
        for delta in deltas:
            tmp = pos
            while True:
                tmp = (tmp[0] + delta[0], tmp[1] + delta[1])
                if tmp in grid:
                    visible.append(tmp)
                    break
                if tmp[0] < 0 or tmp[1] < 0 or tmp[0] > max_pos[0] or tmp[1] > max_pos[1]:
                    break
        visibility[pos] = visible
    return visibility

def count(grid, pos, adjacency):
    n = 0
    for tmp in adjacency[pos]:
        if grid[tmp] == '#':
            n += 1
    return n

def simulate(grid, adjacency, tolerance):
    changes = {}
    for pos, state in grid.items():
        n = count(grid, pos, adjacency)
        if state == 'L' and n == 0:
            changes[pos] = '#'
        elif state == '#' and n >= tolerance:
            changes[pos] = 'L'
    return changes

def simulate_until_stable(grid, vis_func, tolerance):
    adjacency = vis_func(grid)
    grid = grid.copy()
    while (changes := simulate(grid, adjacency, tolerance)):
        grid.update(changes)
    return list(grid.values()).count('#')

grid = {}
with open('../input/11.txt') as stream:
    for y, line in enumerate(stream):
        for x, c in enumerate(line):
            if c == 'L':
                grid[(x, y)] = c

print(simulate_until_stable(grid, calculate_adjacent, 4))
print(simulate_until_stable(grid, calculate_visible, 5))
