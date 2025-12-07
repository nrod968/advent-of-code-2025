from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str) -> list[int]:
    diagram = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            diagram.append(list(line))
    return diagram