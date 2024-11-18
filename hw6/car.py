"""Реализация ТС типа Автомобиль."""

from engine import Engine
from vehicle import Vehicle


class Car(Vehicle):
    """ТС типа Автомобиль."""

    def __init__(
            self, weight: float = 1000, fuel: float = 40.0, fuel_consumption: float = 1.0
    ) -> None:
        """Инициализируется ззначениями по умолчанию, добавляет возможность установить движок."""
        super().__init__(weight, fuel, fuel_consumption)
        self.__engine = None

    @property
    def engine(self) -> Engine | None:
        """Какой движок установлен, защита от записи."""
        return self.__engine

    def set_engine(self, engine: Engine) -> None:
        """Ставит в авто указанный двигатель."""
        self.__engine = engine
