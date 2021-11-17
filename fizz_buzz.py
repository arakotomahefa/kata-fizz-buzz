def buzz_fizz(number):
    if divisible_by_3:
        if divisible_by_5(number):
            return ("FizzBuzz")
        return ("Fizz")
    elif divisible_by_5(number):
        return ("Buzz")
    return (number)

def divisible_by_5(number):
    number % 5 == 0

def divisible_by_3(number):
    number % 3 == 0


