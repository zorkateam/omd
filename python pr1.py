import abc
from abc import abstractmethod
import random


class AnimeMon(abc.ABC):
    @abstractmethod
    def inc_exp(self, value: int):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass


class EmojiMixin:
    poketypes = {'grass': '🌿',
                 'fire': '🔥',
                 'water': '🌊',
                 'electric': '⚡'}

    def __str__(self):
        str = super().__str__()
        return str.replace(self.poketype, self.poketypes[self.poketype])


class BasePokemon(AnimeMon):
    def __init__(self):
        self.__exp = 0

    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, value: int):
        self.__exp += value

    def inc_exp(self, value: int):
        self.exp = value


class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name: str, poketype: str):
        super().__init__()
        self.name = name
        self.poketype = poketype
        self.__exp = 0

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class Digimon(BasePokemon):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.__exp = 0

    def inc_exp(self, value: int):
        self.exp = value * 8

    def __str__(self):
        return f'{self.name}, exp={self.exp}'


def train(pokemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
print(bulbasaur)
train(bulbasaur)
print(bulbasaur.exp)
agumon = Digimon(name='Agumon')
train(agumon)
print(agumon)
