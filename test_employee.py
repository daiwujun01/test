import pytest
from employee import Employee

@pytest.fixture
def my_salary():
    """define a person's default salary"""
    my_salary = Employee("David", "Hou", "4000")
    return my_salary

def test_give_default_raise(my_salary):
    """test wether the default value is 5000"""
    my_salary.get_raise()
    assert my_salary.salary == 9000

def test_give_custom_raise(my_salary):
    """test wether the get_raise funcs well"""
    my_salary.get_raise(10000)
    assert my_salary.salary == 14000
