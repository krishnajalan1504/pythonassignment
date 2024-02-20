def read_file_to_dict(file_path, delimiter=':'):
    result_dict = {}

    with open(file_path, 'r') as file:
        for line in file:
            key, value = map(str.strip, line.split(delimiter, 1))
            result_dict[key] = value

    return result_dict

file_path = "f3.txt"
my_dict = read_file_to_dict(file_path)

print(my_dict)
