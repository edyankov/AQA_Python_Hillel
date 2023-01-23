import pytest


@pytest.fixture(scope="function")
def func_fixture():
    print("\nStart of the fixture execution")
    yield
    print("\nFinish of the fixture execution")


@pytest.mark.pack
@pytest.mark.joint
def test_one(func_fixture):
    print("\nBody for test_one")
    pass


@pytest.mark.pack
@pytest.mark.joint
def test_two(func_fixture):
    print("\nBody for test_two")
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_tree(func_fixture):
    print("\nBody for test_tree")
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_four(func_fixture):
    print("\nBody for test_four")
    pass


@pytest.mark.pack
@pytest.mark.rest
def test_five(func_fixture):
    print("\nBody for test_five")
    pass
