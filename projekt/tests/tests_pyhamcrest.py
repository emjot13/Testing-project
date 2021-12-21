from hamcrest import *
from projekt.main import E_gradebook
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = E_gradebook()
        self.one = E_gradebook()
        self.two = E_gradebook()
        self.three = E_gradebook()

    def test_is_any_instance(self):
        assert_that(self.temp, not_none())

    def test_is_correct_instance(self):
        assert_that(self.temp, instance_of(E_gradebook))

    def test_correct_instances_reproducibility(self):
        assert_that(all_of(instance_of(E_gradebook), self.one, self.two, self.three))


