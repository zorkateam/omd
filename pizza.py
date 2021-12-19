import click
import random
from typing import Callable


def log(func: Callable) -> Callable:
    """Декоратор, который выводит комментарий и время выполнения для функции"""
    def wrapped(*args):
        pattern = {'bake': '🍪 Приготовили за ',
                   'delivery_pizza': '🛴 Доставили за ',
                   'pickup': '🏠 Забрали за '}
        min_time = 1
        max_time = 10
        time = random.randint(min_time, max_time)
        if func.__name__ in pattern:
            print(f'{pattern[func.__name__]}{time}c!')

        return func(*args)
    return wrapped


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
    pizzas = {'Margherita': {'logo': '🧀', 'recipe': ['tomato sauce', 'mozzarella', 'tomatoes']},
              'Pepperoni': {'logo': '🍕', 'recipe': ['tomato sauce', 'mozzarella', 'pepperoni']},
              'Hawaiian': {'logo': '🍍', 'recipe': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}}
    sizes = ['L', 'XL']

    def __init__(self, name: str, size='L'):
        self.name = name
        if size in Pizza.sizes:
            self.size = size
        else:
            print('Задан неверный размер!')

    def dict(self):
        """Печатаем описание пиццы"""
        print(Pizza.pizzas[self.name])

    def __eq__(self, other):
        """Проверяем на равенство две пиццы"""
        if isinstance(other, Pizza):
            return self.name == other.name and self.size == other.size
        return False


@log
def bake(pizza):
    """Готовит пиццу"""


@log
def delivery_pizza(pizza):
    """Доставляет пиццу"""


@log
def pickup(pizza):
    """Самовывоз"""


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    hot_pizza = Pizza(pizza)
    bake(hot_pizza)
    if delivery:
        delivery_pizza(hot_pizza)
    else:
        pickup(hot_pizza)


@cli.command()
def menu():
    """Выыодит меню"""
    print('Menu:')
    for i, item in enumerate(Pizza.pizzas):
        pizza = Pizza.pizzas[item]
        print(f"{i} - {item} {pizza['logo']} : {', '.join([word for word in pizza['recipe']])}")


if __name__ == '__main__':
    cli()
