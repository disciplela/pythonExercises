"""
# HW2 - Temp

## Description

For this assignment, modify the function "temp" to use `input` to prompt
the user for a temperature in Celsius that they would like to covert into
Farenheit.  Once you've obtained the Celsius value, convert it into Farenheit
and print to the screen the coversion.

### Example Usage

>>> python3 hw2_temp.py
What is the temperature you would like to convert (C)?
Temp (in C): 32
Temperature 32C is 89.6F

## Instructions

Replace/alter the contents in between the START and END comments below with
your code to fulfill the requirements for this assignment.

### Requirements
- You *must* use `input` to prompt the user for Temperature
- You *must* print out a statment to the console that has the value of the
    calculated temperature in Farenheit.
"""

def temp():
    # START: your code here
    print('What is the temperature you would like to convert (C)?')
    celsius = int(input('Temp (in C): '))

    fahrenheit = (celsius * 1.8) + 32 
    print( "Temperature" , celsius, "is",fahrenheit,"F")   
    # NOTE: you can remove the `pass` here if you want.  It's a null operation.
    pass
    # END: your code here

if __name__ == "__main__":
    temp()
