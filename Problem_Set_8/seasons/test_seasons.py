import pytest
from seasons import diff ,check ,convert
def test_valueerror():
    with pytest.raises(SystemExit):
        check('January 1, 1999')

def test_days():
    assert diff("1999-01-01") == 525600   and convert(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert diff("1998-01-01") == 1051200   and convert(1051200) == "One million, fifty-one thousand, two hundred minutes"
