from bank import value


def test_value_0():
    assert value("Hello") == 0
    assert value("Hello mr") ==0
    assert value("Hello Alie") ==0

def test_value_20():
    assert value("Help") == 20
    assert value("Hi") == 20
    assert value("How are you") == 20

def test_value_100():
    assert value("me") == 100
    assert value("good morning") ==100
    assert value("yes sir") == 100
