def prime_checker(number):
    is_prime = False
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = True
                break
            else:
                is_prime = False
        
    if result:
        print(f'Not a prime number')
    else:
        print(f'Is a prime number')

n = int(input('Check this number: '))

prime_checker(number = n)