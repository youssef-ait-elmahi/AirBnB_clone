#!/usr/bin/python3

"""Unittests for AirBnB clone User model."""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):

    def setUp(self):
        """Initialize instance of User for testing"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_inheritance(self):
        """Test that User inherits from BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test default User attribute values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict(self):
        """Test conversion of User to dictionary"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["first_name"], "John")
        self.assertEqual(user_dict["last_name"], "Doe")

    def test_save(self):
        """Test saving user updates storage"""
        old_created_at = self.user.created_at
        self.user.save()
        self.assertNotEqual(old_created_at, self.user.created_at)
        self.assertIn(
            "User." + self.user.id,
            FileStorage._FileStorage__objects
            )


if __name__ == "__main__":
    unittest.main()
