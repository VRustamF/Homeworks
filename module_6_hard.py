import math

class Figure:
    sides_count = 0
    def __init__(self, colors: list, *sides):
        self.__color = colors
        self.filled = False

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else: self.__sides = [1] * self.sides_count

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(color, int) and 0 <= color <= 255 for color in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else: return "Ошибка! Цвет должен быть в диапазоне от 0 до 255"

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else: return "Проверьте количество введеных сторон. Все стороны должны быть целыми положительными числа."


class Circle(Figure):
    sides_count = 1
    def __init__(self, color, side):
        super().__init__(color, side)
        self.__radius = side / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, side):
        super().__init__(color, side)
        self.__sides = [side] * self.sides_count


    def get_volume(self):
        side = self.__sides[0]
        return side ** 3

    def get_sides(self):
        return self.__sides


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())


# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())


# Проверка периметра (круга), это и есть длина:
print(len(circle1))


# Проверка объёма (куба):
print(cube1.get_volume())
