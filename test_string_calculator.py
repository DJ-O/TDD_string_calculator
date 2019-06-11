from string_calculator import add 
import pytest 

def test_add_empty_string() :
    result = add("")
    assert result == 0

def test_add_single_number() :
    result = add("1")
    assert result == 1 

def test_add_two_numbers() :
    result = add("1,2")
    assert result == 3

def test_new_line() : 
    result = add("1\n2,3")
    assert result == 6

def test_other_delimiter() :
    result = add("//;\n1;2")
    assert result == 3 

def test_negatives() : 
    with pytest.raises(Exception):
        assert add(-1)