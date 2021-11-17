from fizz_buzz import buzz_fizz

def test_should_return_fizz():
    divisible_by_3 = 9
    actual = buzz_fizz(divisible_by_3)
    expected = "Fizz"
    assert actual == expected

def test_should_return_buzz():
    divisible_by_5 = 20
    actual = buzz_fizz(divisible_by_5)
    expected = "Buzz"
    assert actual == expected

def test_should_return_fizzbuzz():
    divisible_by_3_5 = 15
    actual = buzz_fizz(divisible_by_3_5)
    expected = "FizzBuzz"
    assert actual == expected

def test_should_return_number():
    number_no_match = 22
    actual = buzz_fizz(number_no_match)
    expected = 22
    assert actual == expected