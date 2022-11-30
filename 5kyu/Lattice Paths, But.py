# https://www.codewars.com/kata/598c84db8ba6103bc40000ad/train/python
def lattice_paths(grid):
    sentinel = [0] * (1 + len(grid[0]));
    sentinel[1] = 1
    for i, g in enumerate(grid[0][1:], 2):
        sentinel[i] = sentinel[i - 1] and g

    for r in grid[1:]:  # runs through the grid
        for i, v in enumerate(r, 1):
            sentinel[i] = sum(sentinel[i - 1:i + 1]) * v

    return sentinel[-1]