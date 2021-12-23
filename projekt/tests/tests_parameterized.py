import unittest
from parameterized import parameterized, parameterized_class
from projekt.main import E_gradebook


class Tests_add_grade(unittest.TestCase):
    def setUp(self):
        self.temp = E_gradebook()
        self.temp.add_student("Kasia K")
        self.temp.add_subject(0, "matma")

    @parameterized.expand([
        (0, "matma", "spr", 3.55, 3.55),
        (0, "matma", "spr", 1.0, 1.0),
        (0, "matma", "spr", 5, 5),
        (0, "matma", "spr", 3.5, 3.5),
        (0, "matma", "spr", 1.5, 1.5),
        (0, "matma", "spr", 2.5, 2.5),
        (0, "matma", "spr", 4.5, 4.5),
        (0, "matma", "spr", 2, 2)
    ])
    def test_parameterized_add_grade(self, index, subject, description, grade, output):
        self.temp.add_grade(index, subject, description, grade)
        self.assertEqual(output, self.temp.students[0][1]["matma"]["spr"])

    @parameterized.expand([
        (1, "matma", "spr", 3.55),
        (-1, "matma", "spr", 1.0),
        (100, "matma", "spr", 5),
    ])

    def test_parameterized_non_existent_index(self, index, subject, description, grade):
        self.assertRaises(Exception, self.temp.add_grade, index, subject, description, grade)

    @parameterized.expand([
        (0, "MATMA", "spr", 3.55),
        (0, " matma", "spr", 1.0),
        (0, "matma ", "spr", 5),
        (0, "polski", "spr", 5),
    ])

    def test_parameterized_incorrect_subject_name(self, index, subject, description, grade):
        self.assertRaises(Exception, self.temp.add_grade, index, subject, description, grade)

    @parameterized.expand([
        (0, "matma", "spr", "3.55"),
        (0, "matma", "spr", {"grade": 1.0}),
        (0, "matma", "spr", [5]),
        (0, "matma", "spr", None),
        (0, "matma", "spr", True),

    ])

    def test_parameterized_incorrect_grade_data_type(self, index, subject, description, grade):
        self.assertRaises(Exception, self.temp.add_grade, index, subject, description, grade)

    @parameterized.expand([
        (0, "matma", "spr", 0.99),
        (0, "matma", "spr", 0.99999),
        (0, "matma", "spr", 6.01),
        (0, "matma", "spr", 6.0001),
        (0, "matma", "spr", 0),
        (0, "matma", "spr", -2),
        (0, "matma", "spr", -0.99),
        (0, "matma", "spr", -6.0001),
    ])

    def test_parameterized_incorrect_grade_value(self, index, subject, description, grade):
        self.assertRaises(Exception, self.temp.add_grade, index, subject, description, grade)

    
