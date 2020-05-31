# -*- coding: utf-8 -*-
"""
Course/module: HDip / B8IT105 - Programming for Big Data
Student: Gerard Keaty
Student Id: 10544675
Lecturer: Darren Redmond
Task   : CA2 - Car Rental app

"""

from car import ElectricCar, PetrolCar, HybridCar, DieselCar, CarFleet, Number 



europcar = CarFleet()

europcar.readFleet()
europcar.checkCarsInStock()
europcar.mainMenu()
europcar.getPetrolCars()
europcar.changeStatus()

europcar.write_to_csv()

    

