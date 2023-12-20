#!/usr/bin/python3
"""This module contains the test cases for the class
    <City>
    """

from models.city import City
from models.base_model import BaseModel
import unittest
import datetime
import os


@unittest.skipIf(os.environ.get("HBNB_TYPE_STORAGE") == "db", "skip if it's for DBStorage")
class Test_City(unittest.TestCase):
    """This class contains several methods to the
    the class <City>
    """
    def test_class_name(self):
        """test if the class belongs to City"""
        c1 = City()
        self.assertEqual(type(c1), City)

    def test_subclass_name(self):
        """test if the subclass belongs to BaseModel"""
        c1 = City()
        self.assertTrue(issubclass(type(c1), BaseModel))

    def test_obj_attr(self):
        """test the class attribute of the object"""
        c1 = City()
        self.assertTrue(hasattr(c1, "name"))
        self.assertTrue(hasattr(c1, "state_id"))
        # self.assertEqual(c1.name, "")
        # self.assertEqual(c1.state_id, "")
        self.assertEqual(c1.__dict__.get("name"), None)
        self.assertEqual(c1.__dict__.get("state_id"), None)

    def test_unique_id(self):
        """test for unique id among instances"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_string_id(self):
        """test if the id is a string"""
        c1 = City()
        self.assertEqual(type(c1.id), str)
        c2 = City()
        self.assertEqual(type(c2.id), str)

    def test_created_at(self):
        """test the created_at attribute"""
        c1 = City()
        self.assertEqual(type(c1.created_at), datetime.datetime)
        self.assertNotEqual(c1.created_at, c1.updated_at)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)

    def test_updated_at(self):
        """test the updated_at attribute"""
        c1 = City()
        self.assertEqual(type(c1.updated_at), datetime.datetime)
        self.assertNotEqual(c1.created_at, c1.updated_at)
        c2 = City()
        self.assertLess(c1.updated_at, c2.updated_at)

    def test_str_method(self):
        """test the string implementation of the instance"""
        c1 = City()
        c1.id = "89"
        c1.name = "Yasmin"
        if c1.__dict__.get("_sa_instance_state"):
            del c1.__dict__["_sa_instance_state"]
        expected_out = "[City] (89) {}".format(c1.__dict__)
        self.assertEqual(str(c1), expected_out)

    def test_save(self):
        """test if the updated_at is truly updated"""
        c1 = City()
        temp_updated_at = c1.updated_at
        c1.save()
        self.assertLess(temp_updated_at, c1.updated_at)
        self.assertNotEqual(c1.updated_at, c1.created_at)
        temp_updated_at = c1.updated_at
        c1.save()
        self.assertLess(temp_updated_at, c1.updated_at)

    def test_to_dict(self):
        """test all the attribute stored in the dictionary"""
        c1 = City()
        obj_dict = c1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "City")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(c1.id, obj_dict["id"])

# ---------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """ test creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        c1 = City()
        c1_json = c1.to_dict()
        c2 = City(**c1_json)
        self.assertEqual(type(c2), City)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """ check that obj created with kwargs doesn't have class attribute
        """
        c1 = City()
        c1_json = c1.to_dict()
        c2 = City(**c1_json)
        self.assertNotIn("__class__", c2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """ check that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        c1 = City()
        c1_json = c1.to_dict()
        c2 = City(**c1_json)
        self.assertEqual(type(c2.id), str)
        self.assertEqual(type(c2.updated_at), datetime.datetime)
        self.assertEqual(type(c2.created_at), datetime.datetime)
        self.assertEqual(c1.id, c2.id)
        self.assertEqual(c1.created_at, c2.created_at)
        self.assertEqual(c1.updated_at, c2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """ check that obj created with kwargs has the same dictionary
            attribute as the obj created from
        """
        c1 = City()
        c1_json = c1.to_dict()
        c2 = City(**c1_json)
        self.assertEqual(c1.to_dict(), c2.to_dict())

        c3 = City()
        c3.name = "my name"
        c3.number = 98
        c3_json = c3.to_dict()
        c4 = City(**c3_json)
        self.assertEqual(c3.to_dict(), c4.to_dict())

    def test_two_object_to_dict_return(self):
        """ check that obj created with kwargs has the same dictionary
            retuned by to_dict method as the obj created from
        """
        c1 = City()
        c1_json = c1.to_dict()
        c2 = City(**c1_json)
        self.assertEqual(c2.to_dict(), c1_json)

    def test_two_objects_are_different(self):
        """ check that obj created with kwargs is a new object
        """
        c1 = City()
        c1_json = c1.to_dict()
        c2 = City(**c1_json)
        self.assertFalse(c1 is c2)


@unittest.skipIf(os.environ.get("HBNB_TYPE_STORAGE") != "db", "skip if it's for FileStorage")
class Test_City_sql(unittest.TestCase):
    """This test is for the City class which is mapped to
        the sql table with <cities>
    """
