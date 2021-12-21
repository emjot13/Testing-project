from assertpy import *
from projekt.main import E_gradebook
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = E_gradebook()

    def test_assert_init_object_is_empty(self):
        assert_that(bool(self.temp.students)).is_false() # checking if initial value of object is empty

    def test_assert_init_index_equals_0(self):
        assert_that(self.temp.index).is_equal_to(0)     # checking if starting index that will be incremented automatically is 0

    def test_correct_instance(self):
        assert_that(self.temp).is_instance_of(E_gradebook)

