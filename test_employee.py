import pytest
from employee import Employee

@pytest.fixture
def employee_test_object():
    """An employee that can be used in all tests."""
    employee_test_object = Employee('David', 'Everson', 48000)
    return employee_test_object

def test_give_default_raise(employee_test_object):
    """Test that the default raise is given properly."""
    employee_test_object.give_raise()
    assert employee_test_object.salary == 53000

def test_give_custom_raise(employee_test_object):
    """Test that the a custom raise is given properly."""
    employee_test_object.give_raise(17000)
    assert employee_test_object.salary == 65000
