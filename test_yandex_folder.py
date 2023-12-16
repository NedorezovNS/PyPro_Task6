import unittest
from unittest import TestCase

from modules.yandex_folder import ya_folder_create


class TestYandexFolder(TestCase):
    def test_ya_folder_create(self):
        result = ya_folder_create('Folder_for_test')
        self.assertIn(result, (201, 409))


if __name__ == '__main__':
    unittest.main()