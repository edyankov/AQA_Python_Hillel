import pytest


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("\nStart execution of the fixture for Package_1")
    yield
    print("\nFinish execution the fixture for Package_1")


class Test:

    @pytest.mark.from_class
    def test_first(self):
        print("\nFirst test is successfully")
        pass

    @pytest.mark.from_class
    def test_second(self):
        print("\nSecond test is successfully")
        pass

    @pytest.mark.from_class
    def test_third(self):
        print("\nThird test is successfully")
        pass

    @pytest.mark.from_class
    def test_fourth(self):
        print("\nFourth test is successfully")
        pass

    @pytest.mark.from_class
    def test_fifth(self):
        print("\nFifth test is successfully")
        pass
