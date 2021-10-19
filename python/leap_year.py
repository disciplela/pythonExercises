print(f"LEAP YEAR CALCULATOR")

year = int(input(f"Which year would you like to check?"))

firstCondition = year % 4
secondCondition = year % 100
thirdCondition = year % 400


if (firstCondition == 0):
    if (secondCondition == 0):
        if(thirdCondition == 0):
            print(f'Leap year')
        else:
            print(f'Not a leap year')
    else:
        print(f'leap year')
else:
    print(f'Not a leap year')

    


