import abc
from abc import abstractmethod


class ComputerColor(abc.ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class RGBColor(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, *args):
        super().__init__()
        self.rgb = tuple(map(self._normalize, args))

    def _normalize(self, value):
        return max(min(value, 255), 0)

    def __str__(self):
        return f'{RGBColor.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{RGBColor.MOD}●{RGBColor.END}{RGBColor.MOD}'

    def __eq__(self, other):
        if isinstance(other, RGBColor):
            return self.rgb == other.rgb
        raise TypeError('Неподходящие типы данных')

    @staticmethod
    def _add(a, b):
        return a + b

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return RGBColor(*map(self._add, self.rgb, other.rgb))
        raise TypeError('Неподходящие типы данных')

    def __hash__(self):
        return hash(self.red + self.green + self.blue)

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        if (other > 0) and (other < 1):
            cl = -256 * (1 - other)
            f = 259 * (cl + 255)/(255 * (259 - cl))
            return RGBColor(*[int(f * (color - 128) + 128) for color in self.rgb])

    def __rmul__(self, other):
        return self.__mul__(other)


class HSLColor(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, *args):
        super().__init__()
        self.rgb = tuple((0, 0, 0))

    def __str__(self):
        return f'{RGBColor.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{RGBColor.MOD}●{RGBColor.END}{RGBColor.MOD}'

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        return self

    def __rmul__(self, other):
        return self


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
    [bg_color] * 19,
    [bg_color] * 9 + [color] + [bg_color] * 9,
    [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
    [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
    [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
    [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
    [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
    [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
    [bg_color] * 19,
    ]
    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    red = RGBColor(255, 0, 0)
    gg = RGBColor(0, 100, 0)
    print(red)
    print(0.5 * red)
    print(0.1 * red)
    print(red + gg)
    print_a(gg)
    hsl_gg = HSLColor(0, 100, 100)
    print_a(hsl_gg)



