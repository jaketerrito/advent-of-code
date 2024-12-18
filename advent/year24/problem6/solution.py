  
import argparse
import copy


DIRECTIONS = [(-1, 0),(0,1), (1, 0), (0, -1)]


def get_obstacles_player_position(map: list[str]) -> tuple[tuple[int,int], set[tuple[int,int]]]:
    obstacles = set()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                obstacles.add((i,j))
            if map[i][j] == '^':
                player_position = (i,j)
    return player_position, obstacles


def get_patrol_path(player_position: tuple[int,int], obstacles: set[tuple[int, int]], rows: int, cols: int) -> set[tuple[int, int]]:
    direction_index = 0
    visited = set()

    while player_position[0] >= 0 and player_position[0] < rows and player_position[1] >= 0 and player_position[1] < cols:
        if player_position not in visited:
            visited.add(player_position)
            last_new = player_position
            last_new_dir = direction_index
        else:
            if player_position == last_new and last_new_dir == direction_index:
                raise Exception("infinite loop")

        new_position = tuple((sum(x) for x in zip(player_position, DIRECTIONS[direction_index])))
        if new_position in obstacles:
            direction_index += 1
            if direction_index == len(DIRECTIONS):
                direction_index = 0
        else:
            player_position = new_position
    return visited


def get_visited_count(map: list[list]) -> set[tuple[int,int]]:
    player_position, obstacles = get_obstacles_player_position(map)
    return len(get_patrol_path(player_position, obstacles, len(map), len(map[0])))


def get_loops(map: list[list]) -> int:
    player_position, obstacles = get_obstacles_player_position(map)
    visited = get_patrol_path(player_position, obstacles, len(map), len(map[0]))

    visited.remove(player_position)
    
    loops = 0
    for point in visited:
        new_obstacles = obstacles.copy()
        new_obstacles.add(point)

        try:
            get_patrol_path(player_position, new_obstacles, len(map), len(map[0]))
        except:
            loops += 1
    return loops
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()

    with open(args.file_name) as file:
        lines = file.read().splitlines()
        map = [list(line) for line in lines]
        print(f"visited {get_visited_count(map)} distinct positions")
        print(f"{get_loops(map)} seperate loops possible by placing single obstacle")

            

        



