import unittest
from click.testing import CliRunner
from pizza import order, menu
import itertools


class TestPizza(unittest.TestCase):

    def test_menu(self):
        """
        Тестируем функцию "menu", которая печатает меню нашего ресторана
        :return:
        """
        runner = CliRunner()
        result = runner.invoke(menu)
        assert result.exit_code == 0
        assert result.output in """Menu:
0 - margherita 🧀 : tomato sauce, mozzarella, tomatoes
1 - pepperoni 🍕 : tomato sauce, mozzarella, pepperoni
2 - hawaiian 🍍 : tomato sauce, mozzarella, chicken, pineapples
"""

    def test_order(self):
        """
        Тестируем функцию "order", которая оформляет заказ и производит доставку пиццы
        :return:
        """
        pizza_menu = ['pepperoni', 'margherita', 'hawaiian']
        options = [['--delivery', '--'],
                   ['pepperoni', 'margherita', 'hawaiian', 'cheese', '']]
        runner = CliRunner()
        for delivery, pizza_type in itertools.product(*options, repeat=1):
            result = runner.invoke(order, [delivery, pizza_type])
            assert result.exit_code == 0
            if pizza_type in pizza_menu:
                assert '🍪 Приготовили за ' in result.output
                if delivery == '--delivery':
                    assert '🛴 Доставили за ' in result.output
                else:
                    assert '🏠 Забрали за ' in result.output
            else:
                assert 'Пицца находится в стации разработки, обратитесь попозже.' in result.output


if __name__ == '__main__':
    unittest.main()
