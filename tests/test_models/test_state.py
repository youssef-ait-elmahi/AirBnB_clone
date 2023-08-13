#!/usr/bin/python3
"""
Unit tests for the State class.
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_attributes(self):
        """Test if the State instance has the required attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
