def calculate_structure_sum(data_structure):
    count = 0

    if isinstance(data_structure, str):
        count += len(data_structure)

    elif isinstance(data_structure, int):
        count += data_structure

    elif isinstance(data_structure, list):
        for el in data_structure:
            count += calculate_structure_sum(el)

    elif isinstance(data_structure, dict):
        for el in data_structure.items():
            count += calculate_structure_sum(el)

    elif isinstance(data_structure, tuple):
        for el in data_structure:
            count += calculate_structure_sum(el)

    elif isinstance(data_structure, set):
        for el in data_structure:
            count += calculate_structure_sum(el)

    return count


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)

