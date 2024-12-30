def add_everything_up(numb, line):
    try:
        return round(numb + line, 3)
    except TypeError:
        return str(numb) + str(line)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))