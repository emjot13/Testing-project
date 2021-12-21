from assertpy import *
from projekt.main import E_gradebook
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = E_gradebook()

    def test_assert_init_object_is_empty(self):
        assert_that(bool(self.temp.students)).is_false()

    def test_assert_adding_students_is_string(self):
        assert_that(self.temp.index).is_equal_to(0)