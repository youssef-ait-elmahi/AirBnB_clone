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
    """Test cases"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        """Remove test file after each test"""
        os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test retrieval of all objects"""
        self.storage.new(self.obj)

        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn(self.obj, all_objs.values())

    def test_new(self):
        """Test adding a new object"""
        self.storage.new(self.obj)
        self.assertIn(self.obj, self.storage.all().values())

    def test_save(self):
        """Test saving to a file"""
        self.storage.new(self.obj)
        self.storage.save()

        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))

        with open(self.storage._FileStorage__file_path) as f:
            saved_data = json.load(f)
            self.assertIn(self.obj.to_dict(), saved_data.values())

    def test_reload(self):
        """Test deserializing JSON file to objects"""
        self.storage.new(self.obj)
        self.storage.save()

        storage2 = FileStorage()
        storage2.reload()

        self.assertIn(self.obj, storage2.all().values())


if __name__ == '__main__':
    unittest.main()
