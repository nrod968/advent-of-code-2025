from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str, ranges: list[tuple[int,int]]) -> list[int]:
    file_path = script_directory / file_name
    is_range = True
    ids = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                is_range = False
            elif is_range:
                split_line = line.split('-')
                ranges.append((int(split_line[0]), int(split_line[1])))
            else:
                ids.append(int(line))
    return ids

def num_fresh_ingredients(file_name: str) -> int:
    ranges = []
    ids = parse_input(file_name, ranges)
    count = 0
    for id in ids:
        for range_start, range_end in ranges:
            if range_start <= id <= range_end:
                count += 1
                break
    return count

def num_fresh_ingredients_in_range(file_name: str) -> int:
    ranges = []
    parse_input(file_name, ranges)
    ids = set()
    for range_start, range_end in ranges:
        for i in range(range_start, range_end+1):
            ids.add(i)
    return len(ids)

print(num_fresh_ingredients("input.txt"))
print(num_fresh_ingredients_in_range("input.txt"))