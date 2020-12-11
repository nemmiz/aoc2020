def count_adjacent(grid, pos, max_pos):
    n = 0
    for offset in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
        if grid.get((pos[0]+offset[0],pos[1]+offset[1])) == '#':
            n += 1
    return n

def count_visible(grid, pos, max_pos):
    n = 0
    for delta in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        tmp = pos
        while True:
            tmp = (tmp[0] + delta[0], tmp[1] + delta[1])
            if tmp in grid:
                if grid.get(tmp) == '#':
                    n += 1
                break
            if tmp[0] < 0 or tmp[1] < 0 or tmp[0] > max_pos[0] or tmp[1] > max_pos[1]:
                break
    return n

def simulate(grid, count_func, tolerance):
    new_grid = {}
    max_pos = max(grid.keys())
    for pos, state in grid.items():
        new_state = state
        n = count_func(grid, pos, max_pos)
        if state == 'L' and n == 0:
            new_state = '#'
        elif state == '#' and n >= tolerance:
            new_state = 'L'
        new_grid[pos] = new_state
    return new_grid

def simulate_until_stable(grid, count_func, tolerance):
    while (new_grid := simulate(grid, count_func, tolerance)) != grid:
        grid = new_grid
    return list(new_grid.values()).count('#')

grid = {}
with open('../input/11.txt') as stream:
    for y, line in enumerate(stream):
        for x, c in enumerate(line):
            if c == 'L':
                grid[(x, y)] = c

print(simulate_until_stable(grid, count_adjacent, 4))
print(simulate_until_stable(grid, count_visible, 5))
