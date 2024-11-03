#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function
and understand its purpose. Play with it in the Python console
to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to
test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function
for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
For each of these inputs, test with assertEqual that the function
returns the expected result.

The body of the test method should not be longer than 2 lines.
"""
from unittest.mock import Mock
import unittest
from parameterized import parameterized

access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test the access class"""

    @parameterized.expand([
        ({"nested_map": {"a": 1}, "path": ("a",)}, 1),
        ({"nested_map": {"a": {"b": 2}}, "path": ("a",)}, {'b': 2}),
        ({"nested_map": {"a": {"b": 2}}, "path": ("a", "b")}, 2),
    ])
    def test_access_nested_map(self, input, expected):
        """check if it matches the expected answer"""
        self.assertEqual(access_nested_map(input['nested_map'],
                                           input['path']), expected)
        

    @parameterized.expand([
        ({"nested_map": {}, "path": ("a",)}, KeyError),
        ({"nested_map": {"a": 1}, "path": ("a", "b")}, KeyError)
    ])
    def test_access_nested_map_exception(self, input, expected):
        """test if it raises an error when the wrong key is passed"""
        with self.assertRaises(KeyError) as ex:
            access_nested_map(input["nested_map"], input["path"])
            self.assertEqual(ex.exception, expected)
