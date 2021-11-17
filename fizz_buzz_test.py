from fizz_buzz import return_fizz,return_buzz

# "Fizz" if %3
# "buzz" if %5
# "FizzBuzz" if %3 && %5
# sinon le meme nombre si no match

def test_should_return_fizz():
    divisible_by_3 = 15
    actual = return_fizz(divisible_by_3)
    expected = "Fizz"
    assert actual == expected

def test_should_return_buzz():
    divisible_by_5 = 20
    actual = return_buzz(divisible_by_5)
    expected = "Buzz"
    assert actual == expected