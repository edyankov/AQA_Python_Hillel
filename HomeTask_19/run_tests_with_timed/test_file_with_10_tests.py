"""Bстановити, якщо не встановлений, плагін pytest-xdist; Створити 10 тестів, кожен з яких буде спочатку спати 2 секунди,
потім assert True, або pass. Поставити на ці тести мітку "timed". Запустити тести так, щоб вони пройшли значно швидше
ніж за 20 секунд. Команду запуску додати в текстовий файл в репозиторії домашки.
Поставити, якщо не встановлено, плагін pytest-html. Запустити тести з міткою "timed" так, щоб згенерувався html-репорт,
який можна переглянути в браузері. Команду запуску додати в текстовий файл з командами.
Бонус: розібратись і встановити Allure. Запустити ці ж тести так, щоб згенерувався xml файл з результатами.
На основі зненерованого xml, зробити репорт Allure, який можна переглянути в браузері."""

import pytest
import time

sleep_time = 2


@pytest.fixture
def sleep():
    time.sleep(sleep_time)


@pytest.mark.timed
def test_first(sleep):
    pass


@pytest.mark.timed
def test_second(sleep):
    pass


@pytest.mark.timed
def test_third(sleep):
    pass


@pytest.mark.skip
@pytest.mark.timed
def test_fourth(sleep):
    pass


@pytest.mark.timed
def test_fifth(sleep):
    pass


@pytest.mark.skip
@pytest.mark.timed
def test_sixth(sleep):
    pass


@pytest.mark.timed
def test_seventh(sleep):
    pass


@pytest.mark.skip
@pytest.mark.timed
def test_eighth(sleep):
    pass


@pytest.mark.timed
def test_ninth(sleep):
    pass


@pytest.mark.skip
@pytest.mark.timed
def test_tenth(sleep):
    pass
