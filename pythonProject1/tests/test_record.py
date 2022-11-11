import pytest

from lab3 import Record,CaloriesCalculator
Records = []


def test_record_good():
    Records.append(Record(amount=145, comment='Test_comment'))
    assert len(Records) == 1


@pytest.fixture()
def t_calories_calc1():
    calories_calc = CaloriesCalculator(1900)
    calories_calc.add_record(Record(amount=400, comment='Завтрак.'))
    calories_calc.add_record(Record(amount=800, comment='Обед.'))
    calories_calc.add_record(Record(amount=600, comment='Ужин.'))
    return calories_calc.get_calories_remained()

@pytest.fixture()
def t_calories_calc2():
    calories_calc = CaloriesCalculator(1900)
    calories_calc.add_record(Record(amount=400, comment='Завтрак.'))
    calories_calc.add_record(Record(amount=1900, comment='Обед.'))
    calories_calc.add_record(Record(amount=900, comment='Ужин.'))
    return calories_calc.get_calories_remained()


def test_calories_calc1(t_calories_calc1):
    assert t_calories_calc1 == 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 100 кКал'


def test_calories_calc2(t_calories_calc2):
    assert t_calories_calc2 == 'Хватит есть!'

@pytest.mark.parametrize("a, result", [(1000, 'Хватит есть!'),
                        (1500, 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 300 кКал'),
                        (2000, 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 800 кКал')])
def test_calories_variations(a, result):
    calories_calc=CaloriesCalculator(a)
    calories_calc.add_record(Record(amount=400, comment='Завтрак.'))
    calories_calc.add_record(Record(amount=800, comment='Обед.'))
    assert calories_calc.get_calories_remained() == result


