def fizz_buzz(number):
    if divisible_by_3(number) and divisible_by_5(number):
        return "FizzBuzz"
    if divisible_by_3(number):
        return "Fizz"
    if divisible_by_5(number):
        return "Buzz"
    else :
        return str(number)

def divisible_by_5(number):
    return number % 5 == 0

def divisible_by_3(number):
    return number % 3 == 0


