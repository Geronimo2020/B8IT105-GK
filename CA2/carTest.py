"""
Course/module: HDip / B8IT105 - Programming for Big Data
Student: Gerard Keaty
Student Id: 10544675
Lecturer: Darren Redmond
Task   : CA2 - Car Rental app
Unittesting
"""


import unittest

from car import Car, CarFleet, ElectricCar, PetrolCar, HybridCar

class TestCar(unittest.TestCase):


    def test_car_reg(self):
        self.car = Car()
        self.assertEqual('', self.car.getReg())
        self.car.setReg('01G488')
        self.assertEqual('01G488', self.car.getReg())
    
    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())
    
    
    def test_car_model(self):
        self.car = Car()
        self.assertEqual('', self.car.getModel())
        self.car.setModel('Testarossa')
        self.assertEqual('Testarossa', self.car.getModel())


    def test_car_rented(self):
        self.car = Car()
        self.assertEqual('', self.car.getRented())
        # rented here means it is available - see class and csv. 
        #In the csv I use available / unavailable. So a new car being set would
        # automatically be available i.e. 'yes'
        self.car.setRented('yes') 
        self.assertEqual('yes', self.car.getRented())

    
    def test_carFleet(self):
        car_fleet = CarFleet()
        self.assertEqual([], car_fleet.getPetrolCars())
        self.assertEqual([], car_fleet.getElectricCars())
        self.assertEqual([], car_fleet.getHybridCars())
        self.assertEqual([], car_fleet.getHybridCars())


if __name__ == '__main__':
    unittest.main()


