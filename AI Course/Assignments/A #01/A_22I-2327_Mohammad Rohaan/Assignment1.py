from collections import deque

# ----------- Small helper functions -----------

def inside_grid(col, row, width, height):
    return 0 <= col < width and 0 <= row < height


def is_obstacle(grid, col, row):
    return grid[row][col] == 'X'


def forced_direction_if_oneway(grid, col, row):
    # If robot is CURRENTLY on a one-way cell, next move is forced. Returns (dcol, drow) or None if
    # not one-way.
    cell = grid[row][col]
    if cell == '^':
        return (0, 1)   # up
    if cell == 'v':
        return (0, -1)  # down
    if cell == '<':
        return (-1, 0)  # left
    if cell == '>':
        return (1, 0)   # right
    return None


def advance_checkpoint_index(col, row, checkpoints, checkpoint_index):
    # If current position equals the next required checkpoint, move checkpoint_index forward.
    while checkpoint_index < len(checkpoints) and (col, row) == checkpoints[checkpoint_index]:
        checkpoint_index += 1
    return checkpoint_index


def reconstruct_path(parent, end_state):
    # Reconstructs path as a list of (col,row) from start to end. parent[state] = previous_state 
    path_reverse = []
    cur = end_state
    while cur is not None:
        col, row, cp_idx, t = cur
        path_reverse.append((col, row))
        cur = parent[cur]
    path_reverse.reverse()
    return path_reverse


# ----------- Input reading -----------

def read_input_file(filename="input.txt"):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    idx = 0
    height, width = map(int, lines[idx].split())
    idx += 1

    # Read grid from TOP row to BOTTOM row
    grid_top_to_bottom = []
    for _ in range(height):
        grid_top_to_bottom.append(lines[idx])
        idx += 1

    # Convert to our internal format where grid[row][col] and row=0 is bottom
    grid = [""] * height
    for row in range(height):
        grid[row] = grid_top_to_bottom[height - 1 - row]

    robot_count = int(lines[idx])
    idx += 1

    robots = []
    for _ in range(robot_count):
        robot_id, priority, energy_limit = map(int, lines[idx].split())
        idx += 1

        start_col, start_row = map(int, lines[idx].split())
        idx += 1

        goal_col, goal_row = map(int, lines[idx].split())
        idx += 1

        checkpoint_count = int(lines[idx])
        idx += 1

        checkpoints = []
        for _ in range(checkpoint_count):
            cp_col, cp_row = map(int, lines[idx].split())
            idx += 1
            checkpoints.append((cp_col, cp_row))

        robots.append({
            "id": robot_id,
            "priority": priority,
            "energy_limit": energy_limit,
            "start": (start_col, start_row),
            "goal": (goal_col, goal_row),
            "checkpoints": checkpoints
        })

    return height, width, grid, robots


# ----------- BFS for one robot -----------

def bfs_plan_one_robot(grid, width, height, robot, reservations):
    
    # BFS in time-expanded state space

    # State = (col, row, checkpoint_index, time)

    # reservations is a set of (col,row,time) that are blocked because higher-priority robots use those 
    # cells at those times.
    

    start_col, start_row = robot["start"]
    goal_col, goal_row = robot["goal"]
    checkpoints = robot["checkpoints"]
    energy_limit = robot["energy_limit"]

    # If start is already occupied at time 0, no solution
    if (start_col, start_row, 0) in reservations:
        return None

    start_cp_idx = advance_checkpoint_index(start_col, start_row, checkpoints, 0)
    start_state = (start_col, start_row, start_cp_idx, 0)

    queue = deque([start_state])
    parent = {start_state: None}
    visited = set([start_state])

    while queue:
        col, row, cp_idx, time = queue.popleft()

        # Goal test: at goal AND all checkpoints visited
        if (col, row) == (goal_col, goal_row) and cp_idx == len(checkpoints):
            return reconstruct_path(parent, (col, row, cp_idx, time))

        # Stop expanding if we reached energy limit
        if time >= energy_limit:
            continue

        # Generate possible next positions
        next_positions = []

        forced = forced_direction_if_oneway(grid, col, row)
        if forced is not None:
            # one-way cell: forced move only (no wait)
            dcol, drow = forced
            ncol, nrow = col + dcol, row + drow
            if inside_grid(ncol, nrow, width, height) and not is_obstacle(grid, ncol, nrow):
                next_positions.append((ncol, nrow))
        else:
            # normal cell: up, down, left, right, wait
            moves = [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]
            for dcol, drow in moves:
                ncol, nrow = col + dcol, row + drow
                if inside_grid(ncol, nrow, width, height) and not is_obstacle(grid, ncol, nrow):
                    next_positions.append((ncol, nrow))

        # Try each next position
        for (ncol, nrow) in next_positions:
            ntime = time + 1

            # Reservation collision check
            if (ncol, nrow, ntime) in reservations:
                continue

            ncp_idx = advance_checkpoint_index(ncol, nrow, checkpoints, cp_idx)
            next_state = (ncol, nrow, ncp_idx, ntime)

            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (col, row, cp_idx, time)
                queue.append(next_state)

    return None


def reserve_path(reservations, path, reserve_horizon):
    
    # Add reservations for each (col,row,time) in the path. Also reserve the goal cell after arrival 
    # until reserve_horizon.
    
    for time, (col, row) in enumerate(path):
        reservations.add((col, row, time))

    goal_col, goal_row = path[-1]
    arrival_time = len(path) - 1

    # Reserve goal for remaining time steps (so others can't collide with finished robot)
    for time in range(arrival_time, reserve_horizon + 1):
        reservations.add((goal_col, goal_row, time))


# ----------- Output writing -----------

def write_output_file(paths_by_id, filename="output.txt"):
    output_lines = []

    first = True
    for robot_id in sorted(paths_by_id.keys()):
        if not first:
            output_lines.append("")  # blank line between robots
        first = False

        path = paths_by_id[robot_id]

        if path is None:
            output_lines.append(f"Error: No valid path found for Robot {robot_id}")
            continue

        path_text = " -> ".join([f"({c},{r})" for (c, r) in path])
        total_time = len(path) - 1
        total_energy = total_time

        output_lines.append(f"Robot {robot_id}:")
        output_lines.append(f"Path: {path_text}")
        output_lines.append(f"Total Time: {total_time}")
        output_lines.append(f"Total Energy: {total_energy}")

    # Write to file
    with open(filename, "w") as f:
        for line in output_lines:
            f.write(line + "\n")

    # ALSO print to terminal
    for line in output_lines:
        print(line)


# ----------- Main solve function -----------

#def main():
height, width, grid, robots = read_input_file("input9.txt")

    # Sort robots by descending priority
robots_sorted = sorted(robots, key=lambda r: r["priority"], reverse=True)

    # Store results by robot ID
paths_by_id = {r["id"]: None for r in robots}

    # Reservation table
reservations = set()

    # Choose a simple reservation horizon: max energy limit among all robots
reserve_horizon = max(r["energy_limit"] for r in robots) if robots else 0

    # Plan each robot in priority order
for robot in robots_sorted:
        path = bfs_plan_one_robot(grid, width, height, robot, reservations)
        paths_by_id[robot["id"]] = path

        # If path found, reserve it for later robots
if path is not None:
            reserve_path(reservations, path, reserve_horizon)

write_output_file(paths_by_id, "output.txt")


#if __name__ == "__main__":
#    main()