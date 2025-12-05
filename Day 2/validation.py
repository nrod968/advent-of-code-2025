from pathlib import Path
from math import sqrt, floor

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
                    invalid_id_sum += invalid_id
                else:
                    continue
            range_start_digits += 2
        for num_digits in range(range_start_digits, range_end_digits + 1, 2):
            start_num_half = int(10 ** ((num_digits / 2) - 1))
            end_num_half = int(10 ** ((num_digits / 2)))
            if num_digits == range_end_digits:
                end_num_half = int(range_end[:(num_digits // 2)]) + 1
            for i in range(start_num_half, end_num_half):
                invalid_id = int((i * (10 ** (num_digits / 2))) + i)
                if range_start_int <= invalid_id <= range_end_int:
                    invalid_id_sum += invalid_id
                else:
                    continue
    return invalid_id_sum

def sum_invalid_ids_complex(file_name: str) -> int:
    invalid_id_sum = 0
    id_ranges = parse_input(file_name)
    for start, end in id_ranges:
        start_int = int(start)
        end_int = int(end)
        start_digit_len = len(start)
        end_digit_len = len(end)

        for num_digits in range(start_digit_len, end_digit_len + 1):
            divisors = get_divisors(num_digits)
            invalid_ids = set()
            for divisor in divisors:
                start_portion = int(10 ** ((num_digits / divisor) - 1))
                invalid_ids.update(sum_invalidated_ids_in_range(num_digits, end_digit_len, start_portion, end, start_int, end_int, divisor))
            invalid_id_sum += sum(invalid_ids)
    return invalid_id_sum

def sum_invalidated_ids_in_range(num_digits_start: int, num_digits_end: int, start_portion: int, end: str, start_int: int, end_int: int, divisor: int) -> set[int]:
    invalid_ids = set()
    end_portion = int(10 ** ((num_digits_start / divisor)))
    if num_digits_start == num_digits_end:
        end_portion = int(end[:(num_digits_start // divisor)]) + 1
    for i in range(start_portion, end_portion):
        invalid_id = int(str(i) * divisor)
        if start_int <= invalid_id <= end_int:
            invalid_ids.add(invalid_id)
        else:
            continue
    return invalid_ids

def get_divisors(num: int) -> list[int]:
    divisors = []
    max_divisor = int(floor(sqrt(num)))
    for i in range(1, max_divisor + 1):
        if num % i == 0:
            if i != 1:
                divisors.append(i)
            if i * i != num:
                divisors.append(num // i)
    return divisors

print(sum_invalid_ids("input.txt"))
print(sum_invalid_ids_complex("input.txt"))