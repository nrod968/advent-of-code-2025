from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str) -> list[str]:
    diagram = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            diagram.append(list(line))
    return diagram

def tally_adjacent(tally_diagram: list[list[int]], row: int, col: int, tally_value) -> None:
    for i in range(max(0, row-1), min(len(tally_diagram[row]), row+2)):
        for j in range(max(0, col-1), min(len(tally_diagram), col+2)):
            if i != row or j != col:
                tally_diagram[i][j] += tally_value

def init_tally_diagram(height: int, width: int) -> list[list[int]]:
    tally_diagram = []
    for _ in range(height):
        tally_diagram.append([0] * width)
    return tally_diagram

def create_tally_diagram(diagram: list[str]) -> list[list[int]]:
    tally_diagram = init_tally_diagram(len(diagram), len(diagram[0]))
    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if diagram[row][col] == '@':
                tally_adjacent(tally_diagram, row, col, 1)
    return tally_diagram

def get_accessible_rolls_count_in_row(tally_row: list[int], diagram_row: str) -> int:
    count = 0
    for i in range(len(diagram_row)):
        if diagram_row[i] == '@' and tally_row[i] < 4:
            count += 1
    return count

def get_accessible_rolls_count(file_name: str) -> int:
    diagram = parse_input(file_name)
    tally_diagram = create_tally_diagram(diagram)
    count = 0
    for i in range(len(diagram)):
        count += get_accessible_rolls_count_in_row(tally_diagram[i], diagram[i])
    return count

def update_tally_diagram(tally_diagram: list[list[int]], tally_update: list[list[int]]) -> None:
    for row in range(len(tally_diagram)):
        for col in range(len(tally_diagram[row])):
            tally_diagram[row][col] += tally_update[row][col]

def get_accessible_rolls_count_in_diagram(tally_diagram: list[list[int]], diagram: list[str], tally_update: list[list[int]]) -> int:
    count = 0
    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            if diagram[row][col] == '@' and tally_diagram[row][col] < 4:
                count += 1
                diagram[row][col] = 'x'
                tally_adjacent(tally_update, row, col, -1)
    return count

def get_accessible_rolls_count_iterative(file_name: str) -> int:
    diagram = parse_input(file_name)
    tally_diagram = create_tally_diagram(diagram)
    count = 0
    while True:
        tally_update = init_tally_diagram(len(diagram), len(diagram[0]))
        count_diff = get_accessible_rolls_count_in_diagram(tally_diagram, diagram, tally_update)
        count += count_diff
        if count_diff == 0:
            break
        update_tally_diagram(tally_diagram, tally_update)
    return count

print(get_accessible_rolls_count("input.txt"))
print(get_accessible_rolls_count_iterative("input.txt"))