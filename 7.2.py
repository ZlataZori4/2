"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Outfit(ABC):

    def __init__(self, param):
        self.param = float(param)

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

    @abstractmethod
    def abstract(self):
        return 'Тпрр'


class Coat(Outfit):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Пумпурумпум'


class Costume(Outfit):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass


coat = Coat(2)
costume = Costume(3)
print(coat.consumption())
print(coat.abstract())
print(costume.consumption())
print(costume.abstract())
print(property(coat.consumption(), costume.consumption()))