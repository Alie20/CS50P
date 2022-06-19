from um import count


def test_count_value1():
    assert count("um?") == 1
    assert count("Um, thanks for the album.,") == 1

def test_count_value2():
    assert count("um do you want um help") == 2
    assert count("um hello mom um") == 2

def test_count_value():
        assert count("um um um um") == 4
        assert count("um yummy yummy um um") == 3

def test_count_value0():
    assert count ("Yummy Yummy mum") == 0
    assert count ("Mummy can you help me") == 0