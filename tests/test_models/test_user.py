#!/usr/bin/python3
"""Module to test the user class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser Class
    """
    def test_create_user(self):
        """Test when create a user
        """
        my_model = User()
        dict_copy = my_model.to_dict()
        self.assertEqual(dict_copy['__class__'], 'User')
