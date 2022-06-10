from plates import is_valid

def test_is_vaild_true():
    assert is_valid("Hello") == True
    assert is_valid("LINK")  == True
    assert is_valid("Goal")  == True
    assert is_valid("CS50")  == True

def test_is_valid_false():
    assert is_valid("My name is Alie") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("OUTATIME") == False
