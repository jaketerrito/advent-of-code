from advent.year24.problem6.solution import get_loops, get_obstacles_player_position, get_patrol_path, get_visited_count

def test_get_obstacles_player_position():
    input = ['..#','.^.','#..']
    input = [list(line) for line in input]

    player_position, obstacles = get_obstacles_player_position(input)
    assert player_position == (1,1)
    assert sorted(obstacles) == [(0,2), (2,0)]


def test_example():
    input = ['....#.....',
        '.........#',
        '..........',
        '..#.......',
        '.......#..',
        '..........',
        '.#..^.....',
        '........#.',
        '#.........',
        '......#...'
    ]
    input = [list(line) for line in input]

    visited = get_visited_count(input)
    assert visited == 41

    loops = get_loops(input)
    assert loops == 6