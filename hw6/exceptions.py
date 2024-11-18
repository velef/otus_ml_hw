"""Модуль содержит кастомные исключения, используемые в домашнем задании."""


class LowFuelError(Exception):
    """Вызывается, когда топливо в ТС на нуле."""


class NotEnoughFuel(Exception):
    """Вызывается, когда топлива в ТС не хватит для преодоления указанной дистанции."""


class CargoOverload(Exception):
    """Вызывается, если количество загруженного в ТС груза превышает лимит."""
