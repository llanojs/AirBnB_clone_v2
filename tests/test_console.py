#!/usr/bin/python3
""" Test case for console """
import os
import sys
import pep8
import console
import MySQLdb
import unittest
from io import StringIO
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from unittest.mock import patch
from console import HBNBCommand
from models.review import Review
from models.amenity import Amenity
from models.__init__ import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


""" Test pep8 style validation """


class TestPep(unittest.TestCase):
    def test_pep(self):
        """ test base and test_base for pep8 conformance """
        p = pep8.StyleGuide(quiet=True)
        f1 = 'console.py'
        f2 = 'tests/test_console.py'
        res = p.check_files([f1, f2])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDoc(unittest.TestCase):
    """ check for documentation """

    def test_mod_doc(self):
        """ check for module documentation """
        self.assertTrue(len(console.__doc__) > 0)

    def test_cls_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_metd_doc(self):
        """ check for method documentation """
        for fn in dir(HBNBCommand):
            self.assertTrue(len(fn.__doc__) > 0)


class ConsoleTestClass(unittest.TestCase):
    """ Class to test case of input in console """

    def setUp(self):
        """ create instance global """
        self.obj = HBNBCommand()

    def tearDown(self):
        """ Clean all test case """
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     'environment = file')
    def test_create(self):
        """ Test Case to create a object from a class """

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('create')
            self.assertEqual('** class name missing **\n', _cmd.getvalue())

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('create Class')
            self.assertEqual('** class doesn\'t exist **\n',
                             _cmd.getvalue())

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('create State name="New_York"')
            self.assertTrue(len(_cmd.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('all State')
            self.assertTrue(len(_cmd.getvalue()) > 0)

    def test_exec_file(self):
        """ Check if file have permissions to execute """""
        # Check for read access
        is_read = os.access('console.py', os.R_OK)
        self.assertTrue(is_read)
        # Check for write access
        is_write = os.access('console.py', os.W_OK)
        self.assertTrue(is_write)
        # Check for execution access
        is_exec = os.access('console.py', os.X_OK)
        self.assertTrue(is_exec)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     'environment = db')
    def test_create_filestorage(self):
        """ Test Case to create a object from a class """

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('create')
            self.assertEqual('** class name missing **\n', _cmd.getvalue())

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('create Class')
            self.assertEqual('** class doesn\'t exist **\n',
                             _cmd.getvalue())

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('create State name="Texas"')
            self.assertTrue(len(_cmd.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as _cmd:
            self.obj.onecmd('all State')
            self.assertTrue(len(_cmd.getvalue()) > 0)


if __name__ == '__main__':
    unittest.main()
