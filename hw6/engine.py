"""Реализация сущности Engine."""

from dataclasses import dataclass


@dataclass
class Engine:
    """Двигатель транспортного средства."""

    volume: float
    """Объем двигателя (см^3)."""

    pistons: int
    """Количество цилиндров (шт)."""
