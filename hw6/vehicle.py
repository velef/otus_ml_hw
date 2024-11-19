"""Реализация базового класса Vehicle."""

from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    """Предоставляет функционал, общий для объектов типа ```Транспортное средство```."""

    def __init__(self, weight: float = 1000.0, fuel: float = 40.0, fuel_consumption: float = 1.0):
        """Инициализация параметров ТС.

        :param weight: Масса ТС.
        :param fuel: Колличество топлив.
        :param fuel_consumption: Расход топлива.
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

        self.__is_started: bool = False

    @property
    def is_started(self) -> bool:
        """Запущено ли ТС, защита от записи."""
        return self.__is_started

    def start(self):
        """Обновляет состояние started если уровень топлива больше нуля и ТС не запущено.

        :raise: LowFuelError
            Когда нет топлива.
        """
        if not self.__is_started:

            if self.fuel <= 0:
                raise LowFuelError('No fuel')

            self.__is_started = True

    def move(self, distance: float) -> None:
        """Обновляет счётчик топлива на значение, оставщееся после проезда указанной дистанции.

        :param distance: Расстояние, которое нужно проехать.

        :raise: NotEnoughFuel
            Если топлива не хватит на указанную дистанцию.
        """
        requirement_fuel = self.fuel_consumption * distance

        if requirement_fuel > self.fuel:
            raise NotEnoughFuel(f'Not enough fuel for {distance} km.')

        self.fuel -= requirement_fuel
