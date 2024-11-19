"""Реализация ТС типа Самолёт."""

from exceptions import CargoOverload
from vehicle import Vehicle


class Plane(Vehicle):
    """ТС типа Самолёт."""

    def __init__(
            self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float
    ) -> None:
        """Инициализирует параметры самолёта."""
        super().__init__(weight, fuel, fuel_consumption)

        self.max_cargo = max_cargo
        """Максимальная масса, которую может перевозить самолёт."""

        self.__cargo = 0.0
        """Текущая масса груза."""

    @property
    def cargo(self) -> float:
        """Текущий вес груза в самоёлте, защита от записи."""
        return self.__cargo

    def load_cargo(self, amount: float) -> None:
        """Проверяет, что не возникнет перегруза и плюсует значение к массе текущего груза.

        :param amount: Масса груза, которую хотят загрузить

        :raise: CargoOverload
            Если превышена максимальная масса груза.
        """
        after_loading = amount + self.__cargo

        if after_loading > self.max_cargo:
            raise CargoOverload('Too much cargo')

        self.__cargo += after_loading

    def remove_all_cargo(self) -> float:
        """Обнуляет текущую загрузку и возвращает значение, которое было до обнуления."""
        last_value = self.__cargo
        self.__cargo = 0.0

        return last_value
