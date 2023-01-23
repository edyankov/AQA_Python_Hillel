import pytest

from datetime import datetime, timedelta


@pytest.fixture(scope="module", autouse=True)
def func_fixture():
    print("\nStart execution of the fixture for Package_2")
    yield
    print("\nFinish execution the fixture for Package_2")


sport_wear_brand = ["Nike", "Dope", "Adidas", "Reebok", "Puma", "NewBalance"]


@pytest.mark.param
@pytest.mark.parametrize('brand',
                         ["Nike", "Dope", "Adidas"])
def test_sport_wear_brand(brand):
    assert brand in sport_wear_brand


@pytest.mark.param
@pytest.mark.parametrize("input_value, expected_value",
                         [("5+6", 11), ("4*4", 16), ("49/7", 7)])
def test_result_of_operation(input_value, expected_value):
    print(f"\n{input_value} = {expected_value}")
    assert eval(input_value) == expected_value


data = [
    (datetime(2022, 12, 21), datetime(2022, 12, 20), timedelta(1)),
    (datetime(2022, 12, 20), datetime(2022, 12, 21), timedelta(-1)),
]


@pytest.mark.param
@pytest.mark.parametrize("dt1,dt2,expected",
                         data, ids=["forward", "backward"])
def test_distance_in_time(dt1, dt2, expected):
    diff = dt1 - dt2
    assert diff == expected
