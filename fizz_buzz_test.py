from fizz_buzz import return_fizz

# "Fizz" if %3
# "buzz" if %5
# "FizzBuzz" if %3 %5
# sinon le meme nombre si no match

def test_should_return_fizz():
    divisible_by_3 = 15
    actual = return_fizz(divisible_by_3)
    expected = "Fizz"
    assert actual == expected