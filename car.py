# -*- coding: utf-8 -*-
"""
Course/module: HDip / B8IT105 - Programming for Big Data
Student: Gerard Keaty
Student Id: 10544675
Lecturer: Darren Redmond
Task   : CA2 - Car Rental app

"""

# Darren I created different car attributes than those in the lecture- to match with the 
# 5 fields I created in my scv file - reg no., make, model, type and availability(rented/not rented) 


## I spent most of my time getting the app to populate from a csv file containing the 
# itemised fleet of cars
# And it writes back to the csv the fleet items and the updated status
class Car(object):
    
    def __init__(self):
        self.__reg = ''
        self.__make = ''
        self.__model = ''
        self.__rented = ''

    def getReg(self):
        return self.__reg

    def getMake(self):
        return self.__make


    def getModel(self):
        return self.__model

    def getRented(self):
        return self.__rented    

    def setReg(self, reg):
        self.__reg = reg


    def setMake(self, make):
        self.__make = make

    def setModel(self, model):
        self.__model = model
    
    def setRented(self, rented):
        self.__rented = rented


class ElectricCar():
    
    def __init__(self):
        self.__electric.cars = []
        

class PetrolCar():
    
    def __init__(self):
        self.__petrol.cars = []


    
class HybridCar():
    def __init__(self):
        self.__hybrid.cars = []


class DieselCar():
    def __init__(self):
        self.__diesel.cars = []
        
        
        
# Creating a class for the user inputted amount of cars to rent
#I know this is not brilliant code. If I had another week I would finesse. 
# My fault -  this number will be used to decide how many times to pop a car 
# from a list withon a function in another class
# 
class Number():
    def __init__(self):
        self.number.cars = 0


class CarFleet(object):
    # Initiating lists for the 3 types of cars
    # I also felt I needed to initiate a permamnet number cars
    # owned by Europacar for each type. I understand that in a more dynamic 
    # version that permanent number can change and would be fed by the changes 
    # while using the app
    
    def __init__(self):
        self.__petrol_cars = []
        self.__electric_cars = []
        self.__hybrid_cars = []
        self.__diesel_cars = []
        self.__unavailable_cars = []
        self.__number = 0

        for i in range(len(self.__petrol_cars)):
            self.__petrol_cars.append(PetrolCar())
        for i in range(len(self.__electric_cars)):
            self.__electric_cars.append(ElectricCar())
        for i in range(len(self.__hybrid_cars)):
            self.__hybrid_cars.append(HybridCar())
        for i in range(len(self.__diesel_cars)):
            self.__diesel_cars.append(DieselCar())

    # The next 3 functions are used to get the fixed number of cars of each
    # type which is set up in the constructor
 
    
    def getPetrolCars(self):
        return self.__petrol_cars
    
    def getElectricCars(self):
        return self.__electric_cars
    
    def getHybridCars(self):
        return self.__hybrid_cars
    
    def getDieselCars(self):
        return self.__diesel_cars
    
    def getUnavailableCars(self):
        return self.__unavailable_cars
    
    def getNumber(self):
        return self.__number
  
    # reading in all the  details from the csv file
    def readFleet(self):
        file = open('fleet.csv').readlines()
        for line in file:
            info = line.strip().split(',')
            cat = info[3]
            available = info[4]            
            
            if available == 'yes':
                
                if cat == 'Petrol':
                    self.__petrol_cars.append(line.strip().split(','))
                elif cat == 'Electric':
                   self.__electric_cars.append(line.strip().split(','))
                elif cat == 'Hybrid':
                   self.__hybrid_cars.append(line.strip().split(','))
                else:
                   self.__diesel_cars.append(line.strip().split(','))

            elif available == 'no':
                self.__unavailable_cars.append(line.strip().split(','))

    def checkCarsInStock(self):
        print()
        print('**** Welcome to Europcar Car Rentals ****')
        print()
        print('The current number of available cars')
        print('Petrol: ' + str(len(self.getPetrolCars())))
        print('Electric: ' + str(len(self.getElectricCars())))
        print('Hybrid: ' + str(len(self.getHybridCars())))
        print('Diesel: ' + str(len(self.getDieselCars())))
        print('*' * 10)
        # code to test if this works. commented out
        # y  = self.getUnavailableCars()
        # print(y)

    # pop out cars from the individual car category lists according to the number of
    # cars the user wants to rent using self.number value
    def rent(self, type):
        if type.upper() == 'P':

       
       # iterate this with the cars in stock in each category
       # to make sure the user is not requesting too many
       # unfortunately found no elegant way to terminate and return to the menu
           if self.number > len(self.__petrol_cars):
               # warning message in case of not enough stock
               print('!' * 12)
               print('There are not enough Petrol Cars in stock')
               print('You will be reverted to the menu again')
               print('!' * 12)
        # pop out a car from the list a number of times based on the amount the
        # user wanted
           else:
               for i in range(int(self.number)):
                   self.__unavailable_cars.append(self.__petrol_cars.pop())
    
        elif type.upper()  == 'E':
            
            if self.number > len(self.__electric_cars):
               
               print('!' * 12)
               print('There are not enough Electric cars in stock')
               print('You will be reverted to the menu again')
               print('!' * 12)

            else:
                for i in range(int(self.number)):
                    self.__unavailable_cars.append(self.__electric_cars.pop())
                    
                    
        elif type.upper() == 'H':
            
            if self.number > len(self.__hybrid_cars):
               
               print('!' * 12)
               print('There are not enough Electric cars in stock')
               print('You will be reverted to the menu again')
               print('!' * 12)
            
            else:
                for i in range(int(self.number)):
                    self.__unavailable_cars.append(self.__hybrid_cars.pop())
        
        
        elif type.upper() == 'D':
            
            if self.number > len(self.__diesel_cars):
               
               print('!' * 12)
               print('There are not enough Electric cars in stock')
               print('You will be reverted to the menu again')
               print('!' * 12)
            
            else:            
                for i in range(int(self.number)):
                    self.__unavailable_cars.append(self.__diesel_cars.pop())
    
    def returnCar(self, type,car):
        if type.upper() == 'P':
            self.__petrol_cars.append(car)
        elif type.upper() == 'E':
            self.__electric_cars.append(car)
        elif type.upper() == 'H':
            self.__hybrid_cars.append(car)
        elif type.upper() == 'D':
            self.__diesel_cars.append(car)


    def mainMenu(self):
        print()
        print('*' * 10)
        rentedCar = None
        answer = input('Which of the following would you like to do' + 
                       '\n' + '1: RENT a car (press 1)' +
                       '\n' + '2: RETURN a car (press 2)' +
                       '\n' + '3: QUIT (press any other key)' +
                       '\n' + '> ')

        # a rented car will be popped a number of times based on thos value
        self.number = int(input('How many cars? ' ))
        

        
        while answer == '1' or answer == '2':
            if answer == '1':

                type = input('What type of car would you like to rent' +  
                             '\n' + '- P for petrol' +
                             '\n' + '- E for electric' +
                             '\n' + '- H for Hybrid'+
                             '\n' + '- D for Diesel'+
                             '\n' + '> ')

                rentedCar = self.rent(type)
            elif answer == '2':
                type = input('What type car would you like to return?' +
                             '\n' + '- P for petrol' +
                             '\n' + '- E for electric' +
                             '\n' + '- H for Hybrid'+
                             '\n' + '- D for Diesel'+
                             '\n' + '> ')
                self.returnCar(type, rentedCar)
            print()
            self.checkCarsInStock()
            answer = input('Which of the following would you like to do' + 
                           '\n' + '1: RENT a car (press 1)' +
                           '\n' + '2: RETURN a car (press 2)' +
                           '\n' + '3: QUIT (press any key)' +
                           '\n' + '> ')
    
    # From the list of unavailable cars i.e. those rented out I 
    # want to change the status from 'yes' to 'no'
    # before writing it back to the csv
    def changeStatus(self):      
        unavailable = self.getUnavailableCars()
        for x in unavailable:
            x[4] = 'no'
  
    
    # Rewriting the csv with all the cars
    # the only change is those cars with newly rented status
    # working on changing status of those returned cars but propbably don't have enough
    # time
    def write_to_csv(self):

        import csv
        with open('fleet.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Registration','Make', 'Model', 'Type', 'Available'])
     
            petrol = self.getPetrolCars()
            for p in petrol:
                writer.writerow(p)
            
            electric = self.getElectricCars()
            for e in electric:
                writer.writerow(e)
            
            hybrid = self.getHybridCars()
            for h in hybrid:
                writer.writerow(h)
            
            diesel = self.getDieselCars()
            for d in diesel:
                writer.writerow(d)
       
            unavailable = self.getUnavailableCars()
            for u in unavailable:
                writer.writerow(u)
                    
                    

   
    
    

    
    
    
    
    
    
    
    
    
