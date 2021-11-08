import json
import keyword as kw


class ColorizeMixin:
    def __init__(self, color_code: int = 33):
        self.repr_color_code = color_code


class Advert(ColorizeMixin):
    """
    Класс для чтения данных из json
    Наследуется от ColorizeMixin - Миксин с полем
     - repr_color_code - код цвета для печати текста в консоль
    """
    def __init__(self, json_dict: dict):
        super().__init__()
        for k, v in json_dict.items():
            k_good = k
            # Если ключ - ключевое слово добавляем к нему '_'
            if kw.iskeyword(k_good):
                k_good += '_'
            # Если значение поля - словарь рекурсивно запускаем инициализацию класса уже для него
            if isinstance(v, dict):
                self.__setattr__(k_good, Advert(v))
            else:
                # Проверяем, что поле 'price' имеет неотрицательное значение
                if k_good == 'price' and v < 0:
                    print('Цена должна быть неотрицательной!')
                    exit()
                self.__setattr__(k_good, v)

    def __getattribute__(self, item):
        try:
            val = super().__getattribute__(item)

        except AttributeError:
            if item == 'price':
                return 0
            val = None
        return val

    def __setattr__(self, key, value):
        __dict__ = super().__getattribute__('__dict__')
        __dict__[key] = value

    def __repr__(self):
        return f'\033[1;;{self.repr_color_code}m {self.title} | {self.price} ₽  \n'


if __name__ == "__main__":
    student = """{
        "title": "python",
        "price": 1,
        "location": {
                    "address": "город Москва, Лесная, 7",
                    "metro_stations": ["Белорусская"]
                    }
    }"""
    cor = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""
    st = json.loads(student)
    less_ad = Advert(st)
    print(less_ad.location.address)
    print(less_ad)

    c = json.loads(cor)
    corgi = Advert(c)
    print(corgi)
    print(corgi.class_)
