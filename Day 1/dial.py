from typing import List
from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str) -> List[int]:
    rotations = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            negative_bit = -1 if line[0] == 'L' else 1
            rotation = int(line[1:]) * negative_bit
            rotations.append(rotation)
    return rotations

def get_times_dial_hits_zero(input_file_name: str) -> int:
    current_num = 50
    times_hit_zero = 0
    rotations = parse_input(input_file_name)
    for rotation in rotations:
        current_num = (current_num + rotation) % 100
        if current_num == 0:
            times_hit_zero += 1
    return times_hit_zero

def get_times_dial_passes_zero(input_file_name: str) -> int:
    current_num = 50
    times_passed_zero = 0
    rotations = parse_input(input_file_name)
    for rotation in rotations:
        rotation_passes_zero = rotation // 100 if rotation > 0 else (rotation * -1) // 100
        adjusted_rotation = rotation % 100 if rotation > 0 else ((rotation * -1) % 100) * -1
        temp = current_num + adjusted_rotation
        times_passed_zero += rotation_passes_zero
        if current_num != 0:
            if temp == 0 or temp < 0 or temp > 99:
                times_passed_zero += 1
        current_num = temp % 100
    return times_passed_zero
print(get_times_dial_hits_zero("input.txt"))
print(get_times_dial_passes_zero("input.txt"))