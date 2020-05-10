# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:25:38 2020

@author: Gerard Keaty

CA3: Programming for Big Data
"""

#########################################
### Not sure how to demonstrate list comprehension unless I have 2 lists or more
### Therefore this calculator will ask for input of 2 set of numbers for simplicity
### in some cases

#### Also left the fibonacci generator in as an example of a generator
#### Honestly wasn't sure if that counted as one of the 10 operators
#### So I added an 11th operator just to be sure in case Fibonnaci 
#### does not count
######################################

    
print('')
print('*' * 30)
print('     CALCULATOR    ')
print('*' * 30)


# Definitions of calculations
class Calculator(object):

                   
    # 1: ADD two user of numbers
    def add(self,x,y):
        return map(lambda x,y:x+y, x,y)
    
    # 2: SUBTRACT two lists of numbers
    def subtract(self,x,y):
        return map(lambda x,y:x-y, x,y)
    
    # 3: SQUARE two user generated lists of numbers        
    def square(self,x):
        return map(lambda x: x*x, x)
    
    #4. Cube
    def cube(self, x):
        return map(lambda x: x*x*x, x)
       
    #5: Odd Numbers
    def odd(self, x):
       return filter(lambda x: x % 2, x)

    #6: EVEN Numbers
    def even(self, x):
       return filter(lambda x: x % 2 == 0, x)

    #7: Factorial!
    def factor(self, n):
        from functools import reduce
        return reduce(lambda x,y:x*y, list(range(1,n+1)))
    
    #8: SQUARE ROOT
    def squareRoot(self, x):
        return map(lambda x: x**0.5, x)

    #9: FIBONACCI
    def fibonacci(self, n):
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n): 
                return
            yield a
            a, b = b, a + b
            counter += 1
    
    #10: PERCENTAGE
    def percent(self, x, y): 
        return map(lambda x,y: (x/y) *100, x,y)
    
    #11: MAX
    def max(self, data):
        from functools import reduce
        return reduce(lambda a,b: a if (a>b) else b, list(data))

class Process():   
    def menu():
        print('')
        print('Choose one of the following 10 operations by entering the number:')
        print('1. ADD')
        print('2. SUBTRACT')
        print('3. SQUARE')
        print('4. CUBE')
        print('5. Find ODD NUMBERS in a range')
        print('6. Find EVEN NUMBERS in a range')
        print('7. FACTORIAL')
        print('8. SQUARE ROOT of a sequence of numbers')
        print('9. FIBONACCI')
        print('10. PERCENT')
        print('11. MAX')
        choice = int(input("Please enter your choice: "))
        
        # Add a list of no.s- with user input
        if choice == 1:
            a = []
            b = []
            print('\n1. Adding lists of numbers')
            print('Enter 2 lists of 4 numbers (list A and list B)')
            print('\n*Enter the 4 numbers in list A')
            countA = 1
            for item in range (4):
                a.append (int(input('Enter number '  +str(countA) + ' : ')))
                countA+=1
            print('\n*Enter the 4 numbers in list B')
            countB = 1
            for item in range (4):
                b.append (int(input('Enter number '  +str(countB) + ' : ')))
                countB+=1
            print('List A = ', a)    
            print('List B = ', b)
            c = Calculator()
            result = c.add(a,b)
            print('The two lists added = ', list(result))
        
        # Subtracting 
        elif choice == 2:
            a = []
            b = []
            print('\nSubtracting a lists of numbers')
            print('Enter 2 lists of 4 numbers (list A and list B)')
            print('\n*Enter the 4 numbers in list A')
            countA = 1
            for item in range (4):
                a.append (int(input('Enter number '  +str(countA) + ' : ')))
                countA+=1
            print('\n*Enter the 4 numbers in list B')
            countB = 1
            for item in range (4):
                b.append (int(input('Enter number '  +str(countB) + ' : ')))
                countB+=1
            print('List A = ', a)    
            print('List B = ', b)
            c = Calculator()
            result = c.subtract(a,b)
            print('List A minus List B is: ', list(result))   
        
        
        # 3: SQUARE numbers in a list
        elif choice == 3:
            numberList = []
            n = int(input("How many numbers would you like to Square?:  "))
            count = 1
            for item in range (0, n):
                number = int(input('Please enter number ' +str(count) + ' here:  '))
                numberList.append(number)
                count+=1
            c = Calculator()
            result = c.square(numberList)
            print("The squares are: ", list(result))

        # 4: CUBE two user generated lists of numbers, to display list comprehension
        if choice == 4:
            numberList = []
            n = int(input("How many numbers would you like to Cube?:  "))
            count = 1
            for item in range (0, n):
                number = int(input('Please enter number ' +str(count) + ' here:  '))
                numberList.append(number)
                count+=1
            print("The numbers you entered:", numberList)
            c = Calculator()
            result = c.cube(numberList)
            print("The cubes are: ", list(result))
       
        # 5: Find THE ODD NUMBERS in user generated range
        if choice == 5:
    
            numberList = []
            start = int(input("Please enter a start number:  "))
            end = int(input("Please enter an end number:  "))
            for item in range (start, end):
                numberList.append(item)
                c = Calculator()
            result = c.odd(numberList)
            print ("The odd numbers from " + str(start) +
                   " to " + str(end) + " are:\n", list(result))
       
        # 6: Find EVEN NUMBERS in user generated range    
        if choice == 6:
    
            numberList = []
            start = int(input("Please enter a start number:  "))
            end = int(input("Please enter an end number:  "))
            for item in range (start, end):
                numberList.append(item)
                c = Calculator()
            result = c.even(numberList)
            print ("The even numbers from " + str(start) +
                   " to " + str(end) + " are:\n", list(result))            
            
        # 7: FACTOR/PRODUCT/! from user generated range starting at 1    
        if choice == 7:
            print("We will calculate the factor for a number")
            value  = int(input("Enter a number greater than zero: "))
            if value < 1:
                value  = int(input("That number was too small. Please enter a number 1 or bigger: "))
            c = Calculator()
            result = c.factor(value)
            print("The factorial for " + str(value) + " is: ", 
                  (result))  
        
        # 8: SQUARE ROOT from user generated range           
        if choice == 8:
            print("We will calculate the square root of a range of consecutive numbers")
            start = int(input("Enter the start number for the range: "))
            end  = int(input("Enter the end number for the range: "))
            c = Calculator()
            result = c.squareRoot(range(1,end))
            print("\nThe square roots of the numbers " + str(start) + " to "
              + str(end) + ' are:\n', list(result))  
    
        # 9: A generator for creating the FIBONACCI numbers       
        if choice == 9:
            # 9: User input and calling the function get_fibonnaci ---->
            value = int(input("Enter a value for calculating Fibonnaci numbers: "))
            print("The Fibonacci numbers are as follows: ")  
            c = Calculator()
            f = c.fibonacci(value)
            for x in f:
                print(x, " ", end="") # 
            print()

        # 10: Calculating the PERCENT on one item in a list over corresponsing in other list
        if choice == 10:
            a = []
            b = []
            print('\nFnding Percentages from lists of numbers')
            print('Enter 2 lists of 4 numbers (list A and list B)')
            print('\n*Enter the 4 numbers in list A')
            countA = 1
            for item in range (4):
                a.append (int(input('Enter number '  +str(countA) + ' : ')))
                countA+=1
            print('\n*Enter the 4 numbers in list B')
            countB = 1
            for item in range (4):
                b.append (int(input('Enter number '  +str(countB) + ' : ')))
                countB+=1
            print('List A = ', a)    
            print('List B = ', b)
            c = Calculator()
            result = c.percent(a,b)
            print(str(a) + ' divided by ' + str(b) + ' as a percentage is ', list(result))
 
    # Finds the MAX number in list. VERY INTERESTING METHOD
        if choice == 11:
            numbersList = []
            print('\n*Enter 4 numbers')
            count = 1
            for item in range (4):
                numbersList.append (int(input('Enter number '  +str(count) + ' : ')))
                count+=1
            c = Calculator()
            result = c.max(numbersList)
            print ('These are the numbers you entered: ', numbersList )
            print("The Maximum number is: ", result)
    
    def run():
        go_again = ''
        while go_again != 'n':
            Process.menu()
            go_again = input('Would you like to do another calculation? (y/n) ')
        print('***** Thank you. The calculator will close now. *****')

if __name__ == '__main__':
    Process.run()