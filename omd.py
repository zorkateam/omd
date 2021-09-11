# Guido van Rossum <guido@python.org>
import random


def dec_step(decorated_function):
    def wrapper():
        choice = {'step2_no_umbrella':
                        """Сын спрашивает у папы - Пап, что такое альтернатива? Тот отвечает:
                        - Представь, что ты захотел поесть и пожарил себе яичницу, а ведь мог
                        ее не есть, завернуть яйца в марлю, обложить ватой и положить под лампой.
                        Через каких-то 2-3 недели у тебя появились бы 2 курочки и петушок. Ты бы
                        за ними ухаживал, растил, кормил и через полгодика у тебя бы уже был
                        инкубатор дома, везде бы бегали куры и петухи, через еще годик у тебя бы
                        уже была маленькая ферма, через 2 года большая птицефабрика, через 5 лет
                        ты самый большой импортер курятины во все страны мира. Но в один
                        прекрасный день происходит страшный ураган, наводнение, и всех твоих кур
                        нахер смывает.
                        - Папа, так в чем же альтернатива?
                        - 🦆 Утки! """,
                  'step2_umbrella': 'Слава утке я взяла зонт!'}

        rain_chance = random.random()
        print(f'Вероятность дождя: {100 * rain_chance:2.0f}%.')
        decorated_function()
        if rain_chance > 0.8:
            print('Начался ливень.')
            print(choice[decorated_function.__name__])
        else:
            print('Похоже, что в этом баре я все выпила, пора двигаться дальше.\n')
            step1()
    return wrapper


@dec_step
def step2_umbrella():
    print('Кажется дождь собирается.')


@dec_step
def step2_no_umbrella():
    print('Мне повезет! Надеюсь, дождя не будет.')


def step1():
    print(
        'Утка-маляр 🦆 решила зайти выпить в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()