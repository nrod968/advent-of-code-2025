from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str) -> list[tuple[str, str]]:
    id_ranges = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            ranges = line.split(',')
            for id_range in ranges:
                splitRange = id_range.split('-')
                id_ranges.append((splitRange[0], splitRange[1]))
    return id_ranges

def sum_invalid_ids(file_name: str) -> int:
    invalid_id_sum = 0
    id_ranges = parse_input(file_name)
    for range_start, range_end in id_ranges:
        range_start_int = int(range_start)
        range_end_int = int(range_end)
        range_start_digits = len(range_start)
        range_end_digits = len(range_end)
        if range_start_digits % 2 == 1:
            range_start_digits += 1
        else:
            start_num_half = int(range_start[:(range_start_digits // 2)])
            end_num_half = int(10 ** ((range_start_digits / 2)))
            if range_start_digits == range_end_digits:
                end_num_half = int(range_end[:(range_start_digits // 2)]) + 1
            for i in range(start_num_half, end_num_half):
                invalid_id = int((i * (10 ** (range_start_digits / 2))) + i)
                if range_start_int <= invalid_id <= range_end_int:
                    print(invalid_id)
                    invalid_id_sum += invalid_id
                else:
                    break
            range_start_digits += 2
        for num_digits in range(range_start_digits, range_end_digits + 1, 2):
            start_num_half = int(10 ** ((num_digits / 2) - 1))
            end_num_half = int(10 ** ((num_digits / 2)))
            if num_digits == range_end_digits:
                end_num_half = int(range_end[:(num_digits // 2)]) + 1
            for i in range(start_num_half, end_num_half):
                invalid_id = int((i * (10 ** (num_digits / 2))) + i)
                if range_start_int <= invalid_id <= range_end_int:
                    print(invalid_id)
                    invalid_id_sum += invalid_id
                else:
                    break
    return invalid_id_sum

print(sum_invalid_ids("input.txt"))

## Too Low