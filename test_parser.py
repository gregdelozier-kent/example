# we want parser.py to parse numeric strings 
# and return the float number that the string represents. 

# given that I have a string that contains a floating point number
# when I call parse(s) with the string
# then the function returns the value of the floating point number

from parser import parse

def test_parse_single_digits():
    assert parse("") == None
    assert parse("q") == None
    assert parse(":") == None
    assert parse("0") == 0
    assert parse("9") == 9


def test_parse_multiple_digits():
    assert parse("123") == 123
    assert parse("54321") == 54321
    assert parse("9753124680") == 9753124680
    assert parse("543 21") == None


def test_parse_negative_integers():
    assert parse("-123") == -123
    assert parse("-54321") == -54321
    assert parse("-9753124680") == -9753124680
    assert parse("54321-") == None
    assert parse("9753-124680") == None


def test_parse_floating_point_numbers():
    assert parse(".23") == 0.23
    assert parse("1.23") == 1.23
    assert parse("54.321") == 54.321
    assert parse("1.23.") == None
    assert parse("..123") == None
    assert parse(".12.3") == None

if __name__ == "__main__":
   test_parse_single_digits()