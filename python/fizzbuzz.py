for number in range(0, 101):
    fizz = number % 3
    buzz = number % 5
    if fizz == 0 and buzz == 0:
        print(f'{number} fizzbuzz')
    elif fizz == 0:
        print(f'{number} fizz')
    elif buzz == 0:
        print(f'{number} buzz')
    else:
        print(number)