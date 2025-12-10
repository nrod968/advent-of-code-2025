from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str) -> list[list[int]]:
    manifold_diagram = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            out_line = []
            for i in range(len(line)):
                if line[i] == 'S':
                    out_line.append(i)
                    break
                elif line[i] == '^':
                    out_line.append(i)
            manifold_diagram.append(out_line)
    return manifold_diagram

def count_splits(file_name: str) -> int:
    manifold_diagram = parse_input(file_name)
    beams = set()
    beams.add(manifold_diagram[0][0])
    num_splits = 0
    for row in manifold_diagram:
        if row == []:
            continue
        next_beams = set()
        for beam in beams:
            if beam in row:
                num_splits += 1
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)
            else:
                next_beams.add(beam)
        beams = next_beams
    return num_splits

def count_timelines(file_name: str) -> int:
    manifold_diagram = parse_input(file_name)
    beams = {}
    beams[manifold_diagram[0][0]] = 1
    for row in manifold_diagram:
        if row == []:
            continue
        beam_set = set(beams.items())
        for beam, multiplier in beam_set:
            if beam in row:
                beam1 = beam - 1
                beam2 = beam + 1
                beams[beam] -= multiplier
                if beam1 not in beams:
                    beams[beam1] = 0
                if beam2 not in beams:
                    beams[beam2] = 0
                beams[beam1] += multiplier
                beams[beam2] += multiplier
    return sum(beams.values())

print(count_splits("input.txt"))
print(count_timelines("input.txt"))