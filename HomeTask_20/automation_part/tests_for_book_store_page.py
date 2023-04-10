"""4. Відповідно до п.3 створити тести:
а. отримати список книг конкретного видавництва
(No Starch Press, O'Reilly Media), переконатись що кількість вірна. Тест має бути параметризований.
б. Перевірити що для книги якогось конкретного автора, завантажилось зображення. Тест параметризувати.
Внести на перевірку як мінімум двох авторів.
в. Створти тест на пошук
г. Створтити тест на сортування по видавництву"""

import pytest
import requests
from page_object_book_store_page import BookStorePage


PUBLISHER_NAMES = ["O'Reilly Media", 'No Starch Press']
AUTHOR_NAMES = [
    'Kyle Simpson',
    'Richard E. Silverman',
    'Eric Elliott'
]


class TestBookStore:

    @pytest.mark.parametrize('publisher', PUBLISHER_NAMES)
    def test_can_filter_books_by_publisher(self, chrome, publisher):
        page = BookStorePage(chrome)
        book_list = page.get_book_list_by_publisher(publisher)
        assert len(book_list) == len(page.get_book_titles_by_search(publisher))

    @pytest.mark.parametrize('author', AUTHOR_NAMES)
    def test_can_display_book_image(self, chrome, author):
        page = BookStorePage(chrome)
        img_url = page.get_book_picture_by_author(author)
        assert requests.get(img_url).status_code == 200

    def test_can_search_for_books(self, chrome):
        page = BookStorePage(chrome)
        book_list = page.get_book_titles_by_search("java")
        assert len(book_list) > 0

    def test_can_sort_books_by_publisher(self, chrome):
        page = BookStorePage(chrome)
        result = page.sort_data_by_asc("Publisher")
        assert "-sort-asc" in result.get_attribute("class")

    def test_can_access_login_page(self, chrome):
        page = BookStorePage(chrome)
        result = page.clicked_login_button()
        assert 'login' in result
