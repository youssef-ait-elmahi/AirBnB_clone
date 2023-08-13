#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTestCase(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test environment."""
        del self.storage

    def test_all(self):
        """Test the all() method of FileStorage."""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """Test the new() method of FileStorage."""
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(obj_key, self.storage.all())

    def test_save_reload(self):
        """Test the save() and reload() methods of FileStorage."""
        obj = BaseModel()
        obj.name = "My_First_Model"
        obj.my_number = 89
        obj.save()

        # Reload the storage
        new_storage = FileStorage()
        new_storage.reload()

        obj_key = "{}.{}".format(
            obj.__class__.__name__, obj.id
        )
        self.assertIn(obj_key, new_storage.all())

        reloaded_obj = new_storage.all()[obj_key]
        self.assertEqual(reloaded_obj.name, obj.name)
        self.assertEqual(reloaded_obj.my_number, obj.my_number)


if __name__ == '__main__':
    unittest.main()
