import copy


def display_grid(grid):
    no_of_on_final = 0
    for no_of_lanes in range(len(grid)):
        print grid[no_of_lanes]
        no_of_on_final += grid[no_of_lanes].count("#")
    return no_of_on_final


def create_new_grid(grid, size):
    grid.insert(0, list("." * grid_size))
    grid.append(list("." * grid_size))
    for i in range(grid_size + 2):
        grid[i].insert(0, ".")
        grid[i].append(".")
    return grid


def check_new_val(grid, pos_i, pos_j):
    on = 0
    if grid[pos_i-1][pos_j-1] == "#":
        on += 1
    if grid[pos_i-1][pos_j] == "#":
        on += 1
    if grid[pos_i-1][pos_j+1] == "#":
        on += 1
    if grid[pos_i][pos_j-1] == "#":
        on += 1
    if grid[pos_i][pos_j+1] == "#":
        on += 1
    if grid[pos_i+1][pos_j-1] == "#":
        on += 1
    if grid[pos_i+1][pos_j] == "#":
        on += 1
    if grid[pos_i+1][pos_j+1] == "#":
        on += 1
    #print str(pos_i) + "..." + str(pos_j) + "..." + grid[pos_i][pos_j] + "..." + str(on)
    return on


def update_grid(grid_old, grid_new, pos_i, pos_j):
    if grid_old[i][j] == "#" and (no_of_on == 2 or no_of_on == 3):
        pass
    elif grid_old[i][j] == "#":
        grid_new[i][j] = "."
    elif grid_old[i][j] == "." and no_of_on == 3:
        grid_new[i][j] = "#"
    return grid_new

with open("day_18_2015_01.txt", "r") as f:
    input_grid = [list(line.strip()) for line in f]

no_of_steps = 100
grid_size = len(input_grid)

edit_grid = create_new_grid(input_grid,grid_size)

for turns in range(no_of_steps):
    copy_grid = copy.deepcopy(edit_grid)
    for i in range(1, grid_size+1):
        for j in range(1, grid_size+1):
            no_of_on = check_new_val(copy_grid, i, j)
            update_grid(copy_grid, edit_grid, i, j)

final_result = display_grid(edit_grid)
print "\n No of lights on at end : " + str(final_result)
