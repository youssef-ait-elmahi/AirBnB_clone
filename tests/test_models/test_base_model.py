#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_attributes(self):
        """Test if the BaseModel instance
        has the required attributes."""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_id_generation(self):
        """Test if the ID is generated
        correctly for each BaseModel instance."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """Test if the `created_at` attribute
        is set as an instance of datetime."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        """Test if the `updated_at` attribute
        is updated correctly when calling `save()`."""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test if the `to_dict()` method
        returns the expected dictionary representation."""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89

        model_dict = model.to_dict()

        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str(self):
        """Test if the `__str__()` method
        returns the expected string representation."""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89

        expected_output = "[BaseModel] ({model.id})"
        expected_output += " {}".format(model.__dict__)
        # expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)


if __name__ == '__main__':
    unittest.main()
