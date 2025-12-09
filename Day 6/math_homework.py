from pathlib import Path

# Get the path of the current script
script_path = Path(__file__)

# Get the parent directory of the script
script_directory = script_path.parent

def parse_input(file_name: str) -> list[list[str]]:
    homework = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split()
            homework.append(line)
    return homework

def grand_total(file_name: str) -> int:
    worksheet = parse_input(file_name)
    cur_sum = 0

    for col in range(len(worksheet[0])):
        operation = worksheet[-1][col]
        col_val = 0
        if operation == '*':
            col_val = 1
        for row in range(len(worksheet) - 1):
            if operation == '+':
                col_val += int(worksheet[row][col])
            else:
                col_val *= int(worksheet[row][col])
        cur_sum += col_val
    return cur_sum

def parse_input_r_l(file_name: str) -> list[list[str]]:
    homework = []
    temp = []
    file_path = script_directory / file_name
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip('\n\r')
            temp.append(line)

    end_line = temp[-1]
    sizes = []
    cur_size = 1
    for char in end_line[1:]:
        if char == '+' or char == '*':
            sizes.append(cur_size - 1)
            cur_size = 1
        else:
            cur_size += 1
    sizes.append(cur_size)

    for line in temp[:-1]:
        cur_index = 0
        out_line = []
        for size in sizes:
            out_line.append(line[cur_index:cur_index+size])
            cur_index += size + 1
        homework.append(out_line)
    homework.append(temp[-1].split())
    return homework

def rotate_numbers(worksheet: list[list[str]]) -> list[list]:
    output = []
    for col in range(len(worksheet[0])):
        out_line = [0] * len(worksheet[0][col])
        for row in range(len(worksheet)):
            num = worksheet[row][col]
            if row == len(worksheet) - 1:
                out_line.append(num)
                continue
            for i in range(len(num)):
                char = num[i]
                if char == ' ':
                    continue
                out_line[i] = out_line[i] * 10 + int(char)
        output.append(out_line)
    return output

def grand_total_r_l(file_name: str) -> int:
    worksheet = parse_input_r_l(file_name)
    worksheet = rotate_numbers(worksheet)
    cur_sum = 0

    for row in worksheet:
        operation = row[-1]
        val = 0
        if operation == '*':
            val = 1
        for num in row[:-1]:
            if operation == '+':
                val += num
            else:
                val *= num
        cur_sum += val
    return cur_sum

print(grand_total("input.txt"))
print(grand_total_r_l("input.txt"))