import click
import random
from typing import Callable


def log(pattern: str) -> Callable:
    """Декоратор, который выводит комментарий и время выполнения для функции
    pattern: Шаблон вывода времени, должен содержать "{}"
    """
    def outer_wrapper(func: Callable) -> Callable:
        def wrapped(*args):
            min_time = 1
            max_time = 10
            time = random.randint(min_time, max_time)
            if pattern:
                print(pattern.format(time))
            return func(*args)
        return wrapped
    return outer_wrapper


class Pizza:
    """
    Класс Пицца

    Поля класса:
    pizza_dict: Dict - словарь с описанием всех пицц, изображениями и рецептами
    sizes: List - Список возможных размеров

    Поля объектов:
    name: String - Название пиццы
    size: String - Размер пиццы

    Методы:
    dict: Печатает описание пиццы
    __eq__: Проверяет на равенство два объекта типа Пицца
    """
    pizzas = {'margherita': {'logo': '🧀', 'recipe': ['tomato sauce', 'mozzarella', 'tomatoes']},
              'pepperoni': {'logo': '🍕', 'recipe': ['tomato sauce', 'mozzarella', 'pepperoni']},
              'hawaiian': {'logo': '🍍', 'recipe': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}}
    sizes = ['L', 'XL']

    def dict(self):
        """Печатаем описание пиццы"""
        print(Pizza.pizzas[self.name])

    def __eq__(self, other):
        """Проверяем на равенство две пиццы"""
        if isinstance(other, Pizza):
            return self.name == other.name and self.size == other.size
        return False


class Pepperoni(Pizza):
    def __init__(self, name: str, size='L'):
        super().__init__()
        self.name = name
        if self.name in Pizza.pizzas:
            self.recipe = Pizza.pizzas[self.name]
        else:
            print('Пицца находится в стации разработки, обратитесь попозже.')
        if size in Pizza.sizes:
            self.size = size
        else:
            print('Задан неверный размер!')


class Margherita(Pizza):
    def __init__(self, name: str, size='L'):
        super().__init__()
        self.name = name
        if self.name in Pizza.pizzas:
            self.recipe = Pizza.pizzas[self.name]
        else:
            print('Пицца находится в стации разработки, обратитесь попозже.')
        if size in Pizza.sizes:
            self.size = size
        else:
            print('Задан неверный размер!')


class Hawaiian(Pizza):
    def __init__(self, name: str, size='L'):
        super().__init__()
        self.name = name
        if self.name in Pizza.pizzas:
            self.recipe = Pizza.pizzas[self.name]
        else:
            print('Пицца находится в стации разработки, обратитесь попозже.')
        if size in Pizza.sizes:
            self.size = size
        else:
            print('Задан неверный размер!')


@log('🍪 Приготовили за {}c!')
def bake(pizza: Pizza):
    """Готовит пиццу"""


@log('🛴 Доставили за {}c!')
def delivery_pizza(pizza: Pizza):
    """Доставляет пиццу"""


@log('🏠 Забрали за {}c!')
def pickup(pizza: Pizza):
    """Самовывоз"""


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza_menu = {'margherita': Margherita,
                  'pepperoni': Pepperoni,
                  'hawaiian': Hawaiian}
    if pizza in pizza_menu:
        hot_pizza = pizza_menu[pizza](pizza)
        bake(hot_pizza)
        if delivery:
            delivery_pizza(hot_pizza)
        else:
            pickup(hot_pizza)
    else:
        print('Пицца находится в стации разработки, обратитесь попозже.')


@cli.command()
def menu():
    """Выводит меню"""
    print('Menu:')
    for i, item in enumerate(Pizza.pizzas):
        pizza = Pizza.pizzas[item]
        print(f"{i} - {item} {pizza['logo']} : {', '.join([word for word in pizza['recipe']])}")


if __name__ == '__main__':
    cli()
