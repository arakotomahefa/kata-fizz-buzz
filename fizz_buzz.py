def buzz_fizz(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return ("FizzBuzz")
        return ("Fizz")
    elif number % 5 == 0:
        return ("Buzz")
    return (number)


