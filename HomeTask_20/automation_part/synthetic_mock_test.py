"""5. Згадати про Mock. Написати будь який синтетичний юніт-тест, в якому буде щось замокане."""

import unittest
from unittest.mock import Mock


class TestMock(unittest.TestCase):
    def test_mock_object(self):
        mock_obj = Mock()
        mock_obj.get_name.return_value = 'John'
        name = mock_obj.get_name()
        self.assertEqual(name, 'John')
        mock_obj.get_name.assert_called_once()
