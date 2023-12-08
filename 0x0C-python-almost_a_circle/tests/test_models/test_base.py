#!/usr/bin/python3
"""
    This is a unittest file for class Base
"""
import unittest
import inspect
from models.base import Base


class TestBase(unittest.TestCase):


    def test_base_is_class(self):
        self.assertTrue(inspect.isclass(Base))

    def test_base_is_not_none(self):
        b = Base()
        self.assertIsNotNone(b)

    def test_base_is_instance(self):
        b = Base()
        self.assertTrue(isinstance(b, Base))

    def test_base_is_type(self):
        b = Base()
        self.assertTrue(type(b) is Base)

    def test_create_instance_without_passing_id(self):
        obj_b = Base()
        self.assertIsNotNone(obj_b.id)

    def test_create_instance_with_passing_id(self):
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_create_instance_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_create_instance_incremental_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_create_instance_nb_objects(self):
        obj_id = Base()
        self.assertEqual(obj_id.id, Base._Base__nb_objects)


if __name__ == "__main__":
    unittest.main()
