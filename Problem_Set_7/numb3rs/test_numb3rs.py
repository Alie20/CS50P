from numb3rs import validate

def test_true_validate():
    assert validate(r"14.21.12.14")== True
    assert validate(r"1.2.1.2") == True
    assert validate(r"148.12.145.2") == True
    assert validate(r"157.201.0.1") == True

def test_false_validate():
    assert validate("1.1.1.")== False
    assert validate("1.1.1.256")== False
    assert validate("1.1..")== False
    assert validate("1.")== False
    assert validate("290.125.11.22")== False
