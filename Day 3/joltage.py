from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

BATTERY_PACK_SIZE = 12

def parse_input(file_name: str) -> list[str]:
    battery_banks = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            battery_banks.append(line)
    return battery_banks

def max_output_joltage(file_name: str) -> int:
    battery_banks = parse_input(file_name)
    battery_banks = convert_battery_banks_to_ints(battery_banks)
    max_output_joltage = 0
    for battery_bank in battery_banks:
        max_output_joltage += get_max_joltage(battery_bank)
    return max_output_joltage


def get_max_joltage(battery_bank: list[int]) -> int:
    left_battery = battery_bank[0]
    right_battery = 0
    for battery in battery_bank[1:]:
        if battery > right_battery:
            right_battery = battery
        if right_battery == 9:
            break
    return left_battery * 10 + right_battery

def convert_battery_banks_to_ints(battery_banks: list[str]) -> list[list[int]]:
    battery_banks_ints = []
    for battery_bank in battery_banks:
        battery_bank_int = []
        left_battery_index = 0
        max_left_battery = 0
        for i in range(len(battery_bank)):
            battery = int(battery_bank[i])
            if battery > max_left_battery and i != len(battery_bank) - 1:
                max_left_battery = battery
                left_battery_index = i
            battery_bank_int.append(battery)
        battery_banks_ints.append(battery_bank_int[left_battery_index:])
    return battery_banks_ints

def get_max_joltage_overjolted(battery_bank: str) -> int:
    battery_pack = []
    prev_index = -1
    for i in range(BATTERY_PACK_SIZE):
        max_battery = '0'
        for j in range(prev_index+1, len(battery_bank) - (BATTERY_PACK_SIZE - i - 1)):
            battery = battery_bank[j]
            if battery > max_battery:
                max_battery = battery
                prev_index = j
            if battery == 9:
                break
        battery_pack.append(max_battery)

    return int("".join(battery_pack))

def max_output_joltage_overjolted(file_name: str) -> int:
    battery_banks = parse_input(file_name)
    max_output_joltage = 0
    for battery_bank in battery_banks:
        max_output_joltage += get_max_joltage_overjolted(battery_bank)
        print(get_max_joltage_overjolted(battery_bank))
    return max_output_joltage
7
print(max_output_joltage("input.txt"))
print(max_output_joltage_overjolted("input.txt"))