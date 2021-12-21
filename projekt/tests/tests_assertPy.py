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

    def test_assert_student_is_none(self):
        assert_that(self.temp.add_student).raises(TypeError).when_called_with(None)

    def test_assert_student_is_int(self):
        assert_that(self.temp.add_student).raises(TypeError).when_called_with(10)

    def test_assert_student_is_dict(self):
        assert_that(self.temp.add_student).raises(TypeError).when_called_with({"student": "Anna"})

    def test_assert_student_is_list(self):
        assert_that(self.temp.add_student).raises(TypeError).when_called_with(["Kasia"])

    def test_assert_student_has_full_name(self):
        assert_that(self.temp.add_student).raises(ValueError).when_called_with("Kasia")

    def test_assert_student_has_full_name_space_before(self):
        assert_that(self.temp.add_student).raises(ValueError).when_called_with(" Kasia")

    def test_assert_student_has_full_name_space_after(self):
        assert_that(self.temp.add_student).raises(ValueError).when_called_with("Kasia ")