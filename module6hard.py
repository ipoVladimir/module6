# Задание "Они все так похожи":
# 2D? 3D? Даже 4D?.... Настолько глубоко мы заходить конечно же не будем, 4D подождёт, но вот с двумерными и трёхмерными фигурами можем поэкспериментировать.
# Вы когда-нибудь задумывались как устроены графические библиотеки для языков программирования?
# Безусловно, там выполняются огромные расчёты при помощи вашей видеокарты, но... Что лежит в основе удобного использования таких объектов?
#
# По названию задачи можно понять, что все геометрические фигуры обладают схожими свойствами, такими как: длины сторон, цвет и др.
#
# Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете замечать схожие классы, уже написанные кем-то ранее):
#
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
#
# Подробное ТЗ:
#
# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
#
#     Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
#     Атрибуты(публичные): filled(закрашенный, bool)
#
# И методами:
#
#     Метод get_color, возвращает список RGB цветов.
#     Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
#     Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
#     Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
#     Метод get_sides должен возвращать значение я атрибута __sides.
#     Метод __len__ должен возвращать периметр фигуры.
#     Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
#
#
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
#
#     Все атрибуты и методы класса Figure
#     Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
#     Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
#
#
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
#
#     Все атрибуты и методы класса Figure
#     Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
#
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
#
#     Все атрибуты и методы класса Figure.
#     Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
#     Метод get_volume, возвращает объём куба.
#
#
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
#
# Код для проверки:
# circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
#
# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77) # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15) # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# print(cube1.get_sides())
# circle1.set_sides(15) # Изменится
# print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())
#
#
# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216
#
# Примечания (рекомендации):
#
#     Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
#     Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
#     Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
#     Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
#     Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
import math


class Figure:
    SIDE_DEFAULT = 1
    COLOR_DEFAULT = 0

    sides_count = 0

    def __init__(self, *args):
        self.filled = False             # Атрибуты(публичные): filled(закрашенный, bool)

        if len(args) > 0 and self.is_rgb_param(args[0], True):
            r, g, b = args[0]
            self.set_color(r, g, b)
        else:
            self.__color = [Figure.COLOR_DEFAULT]*3        #  __color(список цветов в формате RGB)

        self.__sides = [Figure.SIDE_DEFAULT]*self.sides_count
        if len(args) > 0:
            side_lst = [*args[1:]] if self.is_rgb_param(args[0]) else [*args]
            if len(side_lst) == self.sides_count:
                self.set_sides(*side_lst)

    """
    Проверяет является ли параметр RGP цветом
    """
    def is_rgb_param(self, lst, valid_value=False):

        if ((isinstance(lst, tuple) or isinstance(lst, list) or isinstance(lst, set)) and len(lst) == 3):
            if valid_value:
                return self.__is_valid_color(lst[0], lst[1], lst[2])
            else:
                return True
        return False
    """
    Метод get_color, возвращает список RGB цветов.
    """
    def get_color(self):
        return self.__color

    """
    Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет 
    корректность переданных значений перед установкой нового цвета. 
    Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно)."""
    def __is_valid_color(self, r, g, b) -> bool:
        rng_rgb = range(256)
        return r in rng_rgb and g in rng_rgb and b in rng_rgb

    """
    Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color 
    на соответствующие значения, предварительно проверив их на корректность. 
    Если введены некорректные данные, то цвет остаётся прежним.    
    """
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    """
    Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, 
    возвращает True если все стороны целые положительные числа и 
    кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    """
    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for sd in args:
                if not (isinstance(sd, int) and sd > 0):
                    return False
            return True
        return False

    """
    Метод get_sides должен возвращать значение я атрибута __sides.
    """
    def get_sides(self):
        return self.__sides

    """
    Метод __len__ должен возвращать периметр фигуры.
    """
    def __len__(self):
        res = 0
        for it in self.__sides:
            res += it
        return res

    """
    Метод set_sides(self, *new_sides) должен принимать новые стороны, 
    если их количество не равно sides_count, то не изменять, в противном случае - менять.
    """
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(*new_sides):
                if len(self.__sides) == 0:
                    self.__sides = [Figure.SIDE_DEFAULT]*self.sides_count
                for i in range(self.sides_count):
                    self.__sides[i] = new_sides[i]


class Circle(Figure):
    """
    Атрибуты класса Circle: sides_count = 1
    Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    
    Все атрибуты и методы класса Figure
    Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).    
    """
    sides_count = 1

    def __init__(self, *args):
        super().__init__(*args)
        self.__radius = self.get_radius_by_side(super().get_sides()[0])

    def get_radius_by_side(self, side_len):
        return side_len / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    """
    Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    """
    def get_square(self):
        return math.pi * self.__radius**2


class Triangle(Figure):
    """
    Атрибуты класса Triangle: sides_count = 3
    Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure
    """
    sides_count = 3

    def __init__(self, *args):
        super().__init__(*args)

    """
    Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
    """
    def get_square(self):
        p = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

class Cube(Figure):
    """
    Атрибуты класса Cube: sides_count = 12
    Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    Все атрибуты и методы класса Figure.
    Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    """
    sides_count = 12

    def __init__(self, *args):
        super().__init__(*args)

        if len(args) > 0:
            side_lst = [*args[1:]] if super().is_rgb_param(args[0]) else [*args]
            if len(side_lst) == 1:
                self.set_sides(*side_lst)

    """
    Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
    """
    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().set_sides(*[new_sides[0]]*self.sides_count)

    """
    Метод get_volume, возвращает объём куба.
    """
    def get_volume(self):
        return self.get_sides()[0]**3


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

circle2 = Circle(10)
print(f"circle2.get_sides()={circle2.get_sides()}")
print(f"circle2.get_color()={circle2.get_color()}")
print(f"circle2.get_radius()={circle2.get_radius()}")
print(f"circle2.get_square()={circle2.get_square()}")

triangle_ = Triangle((255, 101, 0), 2, 5, 4)
print(f"triangle_.get_sides()={triangle_.get_sides()}")
print(f"triangle_.get_color()={triangle_.get_color()}")
print(f"triangle_.get_square()={triangle_.get_square()}")

cube2 = Cube((256, 101, 0), 2, 5, 4)
print(f"cube2.get_sides()={cube2.get_sides()}")
print(f"cube2.get_color()={cube2.get_color()}")
print(f"cube2.get_volume()={cube2.get_volume()}")

f1 = Figure((100, 100, 100), 1)
print(f1.get_color())
f1.set_color(300, 300, 300)
print(f1.get_color())


class Sixter(Figure):
    sides_count = 6

f4 = Sixter([5, 5, 5], 5, 6, 7, 8, 9, 10)
print(f4.get_color())
f4.set_color(300, 300, 300)
print(f4.get_color())

cube = Cube((2, 2, 2), 3)
print(cube.get_sides())
