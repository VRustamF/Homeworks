def  custom_write(file_name, strings):
    strings_dict = {}
    file = open(file_name, "a", encoding="utf-8")
    count = 1
    for string in strings:
        byte_position = file.tell()
        file.write(f"{string}\n")
        strings_dict[(count, byte_position)] = string
        count += 1
    return strings_dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)