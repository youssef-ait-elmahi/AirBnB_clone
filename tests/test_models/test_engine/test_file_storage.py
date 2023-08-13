#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.storage = FileStorage()
        self.obj = BaseModel()

    def test_all(self):
        """
        Test retrieval of all objects.
        """
        self.storage.new(self.obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path) as f:
            saved_data = json.load(f)
            self.assertEqual(len(saved_data), 1)
            self.assertIn(self.obj, saved_data.values())

    def test_new(self):
        """
        Test adding a new object.
        """
        self.storage.new(self.obj)
        self.assertIn(self.obj, self.storage.all().values())

    def test_save(self):
        """
        Test saving to a file.
        """
        self.storage.new(self.obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path) as f:
            saved_data = json.load(f)
            self.assertIn(self.obj, saved_data.values())

    def test_reload(self):
        """
        Test reloading from a file.
        """
        self.storage.new(self.obj)
        self.storage.save()

        storage2 = FileStorage()
        storage2.reload()

        with open(storage2._FileStorage__file_path) as f:
            saved_data = json.load(f)
            self.assertIn(self.obj, saved_data.values())


if __name__ == '__main__':
    unittest.main()
