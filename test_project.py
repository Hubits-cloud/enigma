import pytest
from project import get_plugboard, get_reflector, get_rotor_left,get_rotor_middle, get_rotor_right, get_key, get_rings

def main():
    ...

def test_plugboard():
    assert get_plugboard("AB CD EF") == ["AB", "CD", "EF"]
    assert get_plugboard("CD EF TZ") == ["CD", "EF", "TZ"]
    assert get_plugboard("ZT EX PU") == ["ZT", "EX", "PU"]
    with pytest.raises(SystemExit):
        assert get_plugboard("AA BB CC")

def test_reflector():
    with pytest.raises(SystemExit):
        assert get_reflector("D")
        assert get_reflector("AB")
        assert get_reflector("12")
        assert get_reflector(1231)

def test_rotor_left():
    with pytest.raises(SystemExit):
        assert get_rotor_left("7")
        assert get_rotor_left("none")
        assert get_rotor_left(12)
        assert get_rotor_left("#")

def test_rotor_midlle():
    with pytest.raises(SystemExit):
        assert get_rotor_middle("7")
        assert get_rotor_middle("none")
        assert get_rotor_middle(12)
        assert get_rotor_middle("#")

def test_rotor_right():
    with pytest.raises(SystemExit):
        assert get_rotor_right("7")
        assert get_rotor_right("none")
        assert get_rotor_right(12)
        assert get_rotor_right("#")

def test_keys():
    assert get_key("ABC") == "ABC"
    assert get_key("CAT") == "CAT"
    assert get_key("TTT") == "TTT"
    with pytest.raises(SystemExit):
        assert get_key("123")
        assert get_key("AAAA")
        assert get_key("AB1")

def test_rings():
    assert get_rings("1 1 1") == (1, 1, 1)
    assert get_rings("26 26 26") == (26, 26, 26) 
    assert get_rings("1 26 22") == (1, 26, 22)
    with pytest.raises(SystemExit):
        assert get_rings("abc")
        assert get_rings("1 26 c")
if __name__ == "__main__":
    main()