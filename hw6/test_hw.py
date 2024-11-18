
import unittest

from car import Car
from engine import Engine
from exceptions import CargoOverload, LowFuelError, NotEnoughFuel
from plane import Plane
from vehicle import Vehicle


class VehicleTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(fuel=40, fuel_consumption=1.0)

    def test_start_with_fuel(self) -> None:
        self.assertFalse(self.vehicle.is_started)
        self.vehicle.start()
        self.assertTrue(self.vehicle.is_started)

    def test_start_without_fuel(self) -> None:
        self.vehicle.fuel = 0.0
        self.assertRaises(LowFuelError, self.vehicle.start)

    def test_move(self):
        self.vehicle.move(24.0)
        self.assertEqual(self.vehicle.fuel, 16.0)
        self.assertRaises(NotEnoughFuel, lambda: self.vehicle.move(20.0))


class CarTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mercedes_benz_m178 = Engine(volume=3996, pistons=8)
        self.mercedes_benz_s580 = Car()

    def test_set_engine(self):
        self.assertIsNone(self.mercedes_benz_s580.engine)
        self.mercedes_benz_s580.set_engine(self.mercedes_benz_m178)
        self.assertEqual(self.mercedes_benz_s580.engine, self.mercedes_benz_m178)


class PlaneTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.plane = Plane(weight=25000.0, fuel=10000.0, fuel_consumption=5.0, max_cargo=12000.0)
        self.cargo_amount = 10000.0

    def test_cargo(self) -> None:
        self.assertEqual(self.plane.cargo, 0.0)
        self.assertRaises(CargoOverload, lambda: self.plane.load_cargo(100500.0))

        self.plane.load_cargo(self.cargo_amount)
        self.assertEqual(self.plane.cargo, self.cargo_amount)

        dropped_amount = self.plane.remove_all_cargo()
        self.assertEqual(self.plane.cargo, 0.0)
        self.assertEqual(dropped_amount, self.cargo_amount)


if __name__ == '__main__':
    unittest.main()
