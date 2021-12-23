from assertpy import *
from projekt.main import E_gradebook
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = E_gradebook()
        self.temp1 = E_gradebook()
        self.temp1.add_student("Kasia K")
        self.temp2 = E_gradebook()
        self.temp2.add_student("Kasia K")
        self.temp2.add_subject(0, "matma")

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

    def test_add_student_returns_correctly(self):
        self.temp.add_student("Kasia K")
        assert_that(self.temp.students).is_equal_to([[{0: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}]])

    def test_add_student_returns_correctly_for_5_students(self):
        for x in range(5):
            self.temp.add_student("Kasia K")
        assert_that(self.temp.students).is_equal_to([[{0: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{1: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{2: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{3: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{4: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}]])

    def test_add_student_returns_correctly_for_10_students(self):
        for x in range(10):
            self.temp.add_student("Kasia K")
        assert_that(self.temp.students).is_equal_to([[{0: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{1: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{2: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{3: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{4: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{5: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{6: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{7: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{8: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}], [{9: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}]])



    def test_delete_student_index_is_none(self):
        assert_that(self.temp1.delete_student).raises(TypeError).when_called_with(None)

    def test_delete_student_index_is_str(self):
        assert_that(self.temp1.delete_student).raises(TypeError).when_called_with("10")

    def test_delete_student_index_is_dict(self):
        assert_that(self.temp1.delete_student).raises(TypeError).when_called_with({0: 0})

    def test_delete_student_index_is_list(self):
        assert_that(self.temp1.delete_student).raises(TypeError).when_called_with([0])

    def test_delete_student_index_is_float(self):
        assert_that(self.temp1.delete_student).raises(TypeError).when_called_with(0.0)

    def test_delete_student_no_student_with_given_index(self):
        assert_that(self.temp1.delete_student).raises(ValueError).when_called_with(1)

    def test_delete_student_no_student_with_negative_index(self):
        assert_that(self.temp1.delete_student).raises(ValueError).when_called_with(-1)

    def test_delete_student_successful(self):
        self.temp1.delete_student(0)
        assert_that(bool(self.temp1.students)).is_false() # checking if value of object is empty after deleting the only student

    def test_delete_5_students_succesful(self):
        for x in range(4):
            self.temp1.add_student("Kasia K")
        for x in range(5):
            self.temp1.delete_student(x)
        assert_that(bool(self.temp1.students)).is_false()

    def test_delete_15_students_succesful(self):
        for x in range(14):
            self.temp1.add_student("Kasia K")
        for x in range(15):
            self.temp1.delete_student(x)
        assert_that(bool(self.temp1.students)).is_false()

    def test_delete_150_students_succesful(self):
        for x in range(149):
            self.temp1.add_student("Kasia K")
        for x in range(150):
            self.temp1.delete_student(x)
        assert_that(bool(self.temp1.students)).is_false()

    def test_students_is_list_after_deleting(self):
        self.temp1.delete_student(0)
        assert_that(self.temp1.students).is_instance_of(list)

    def test_assert_edit_student_name_is_none(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with(None)

    def test_assert_edit_student_name_is_int(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with(10)

    def test_assert_edit_student_name_is_dict(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with({"student": "Anna"})

    def test_assert_edit_student_name_is_list(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with(["Kasia"])



    def test_assert_edit_student_index_is_none(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with(None)

    def test_assert_edit_student_index_is_str(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with("10")

    def test_assert_edit_student_index_is_dict(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with({2: "two"})

    def test_assert_edit_student_index_is_tuple(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with((0, 0))

    def test_assert_edit_student_index_is_float(self):
        assert_that(self.temp1.edit_student).raises(TypeError).when_called_with(0.0)


    def test_assert_edit_student_successful(self):
        self.temp1.edit_student(0, "Kasia KKK")
        assert_that(self.temp1.students[0][0][0]).is_equal_to("Kasia KKK")

    def test_edit_5_students_succesful(self):
        for x in range(4):
            self.temp1.add_student("Kasia K")
        for x in range(5):
            self.temp1.edit_student(x, "Kasia KKK")
            assert_that(self.temp1.students[x][0][x]).is_equal_to("Kasia KKK")

    def test_edit_15_students_succesful(self):
        for x in range(14):
            self.temp1.add_student("Kasia K")
        for x in range(15):
            self.temp1.edit_student(x, "Kasia KKK")
            assert_that(self.temp1.students[x][0][x]).is_equal_to("Kasia KKK")

    def test_edit_150_students_succesful(self):
        for x in range(149):
            self.temp1.add_student("Kasia K")
        for x in range(150):
            self.temp1.edit_student(x, "Kasia KKK")
            assert_that(self.temp1.students[x][0][x]).is_equal_to("Kasia KKK")

    def test_edit_student_returns_correct_students_value_1(self):
        self.temp1.edit_student(0, "Kasia KKK")
        assert_that(self.temp1.students).is_equal_to([[{0: 'Kasia KKK', 'annotations': {}, 'average grades': {}}, {}]])

    def test_edit_student_returns_correct_students_value_2(self):
        self.temp1.edit_student(0, "Kasia KKKKKK")
        assert_that(self.temp1.students).is_equal_to([[{0: 'Kasia KKKKKK', 'annotations': {}, 'average grades': {}}, {}]])

    def test_edit_student_no_student_with_given_index(self):
        assert_that(self.temp1.edit_student).raises(ValueError).when_called_with(1, "Kasia K")

    def test_edit_student_no_student_with_negative_index(self):
        assert_that(self.temp1.edit_student).raises(ValueError).when_called_with(-1, "Kasia K")

    def test_assert_edit_student_has_full_name(self):
        assert_that(self.temp1.edit_student).raises(ValueError).when_called_with(0, "Kasia")

    def test_assert_edit_student_has_full_name_space_before(self):
        assert_that(self.temp1.edit_student).raises(ValueError).when_called_with(0, " Kasia")

    def test_assert_edit_student_has_full_name_space_after(self):
        assert_that(self.temp1.edit_student).raises(ValueError).when_called_with(0, "Kasia ")


    def test_assert_subject_average_index_is_float(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(0.0, "matma")

    def test_assert_subject_average_index_is_none(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(None, "matma")

    def test_assert_subject_average_index_is_str(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with("0", "matma")

    def test_assert_subject_average_index_is_bool(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(True, "matma")

    def test_assert_subject_average_index_is_list(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with([0], "matma")

    def test_assert_subject_average_subject_is_float(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(0, 0.0)

    def test_assert_subject_average_subject_is_none(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(0, None)

    def test_assert_subject_average_subject_is_int(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(0, 0)

    def test_assert_subject_average_subject_is_bool(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(0, False)

    def test_assert_subject_average_subject_is_list(self):
        assert_that(self.temp2.subject_average).raises(TypeError).when_called_with(0, ["matma"])

    def test_assert_subject_average_non_existent_index(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(1, "matma")

    def test_assert_subject_average_non_existent_index1(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(-1, "matma")

    def test_assert_subject_average_non_existent_index2(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(100, "matma")

    def test_assert_subject_average_non_existent_subject(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(0, "polski")

    def test_assert_subject_average_non_existent_subject1(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(0, "MATMA")

    def test_assert_subject_average_non_existent_subject2(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(0, " matma")

    def test_assert_subject_average_non_existent_subject3(self):
        assert_that(self.temp2.subject_average).raises(ValueError).when_called_with(0, "matma ")


    def test_assert_subject_average_no_grades(self):
        assert_that(self.temp2.subject_average).raises(Exception).when_called_with(0, "matma")  #exception as there are no grades so we would have to divide by zero


    def test_assert_subject_average(self):
        self.temp2.add_grade(0, "matma", "spr", 5)
        self.temp2.add_grade(0, "matma", "spr1", 4)
        self.temp2.subject_average(0, "matma")
        assert_that(self.temp2.students[0][0]["average grades"]["average matma grade"]).is_equal_to(4.5)

    def test_assert_overall_average_index_is_float(self):
        assert_that(self.temp2.overall_average).raises(TypeError).when_called_with(0.0)

    def test_assert_overall_average_index_is_none(self):
        assert_that(self.temp2.overall_average).raises(TypeError).when_called_with(None)

    def test_assert_overall_average_index_is_str(self):
        assert_that(self.temp2.overall_average).raises(TypeError).when_called_with("0")

    def test_assert_overall_average_index_is_bool(self):
        assert_that(self.temp2.overall_average).raises(TypeError).when_called_with(True)

    def test_assert_overall_average_index_is_list(self):
        assert_that(self.temp2.overall_average).raises(TypeError).when_called_with([0])


    def test_assert_overall_average_non_existent_index(self):
        assert_that(self.temp2.overall_average).raises(ValueError).when_called_with(1)

    def test_assert_overall_average_non_existent_index1(self):
        assert_that(self.temp2.overall_average).raises(ValueError).when_called_with(-1)

    def test_assert_overall_average_non_existent_index2(self):
        assert_that(self.temp2.overall_average).raises(ValueError).when_called_with(100)

    def test_assert_overall_average_no_grades(self):
        self.temp2.delete_subject(0, "matma")
        assert_that(self.temp2.overall_average).raises(Exception).when_called_with(0, "matma")


    def test_assert_overall_average(self):
        self.temp2.add_subject(0, "polski")
        self.temp2.add_grade(0, "polski", "spr", 4)
        self.temp2.add_grade(0, "matma", "spr", 3)
        self.temp2.add_grade(0, "matma", "spr1", 1)
        self.temp2.overall_average(0)
        assert_that(self.temp2.students[0][0]["overall average"]).is_equal_to(3.0)

    def test_assert_add_annotation_index_is_float(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0.0, "zachowanie", "bdb")

    def test_assert_add_annotation_index_is_none(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(None, "zachowanie", "bdb")

    def test_assert_add_annotation_index_is_str(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with("0", "zachowanie", "bdb")

    def test_assert_add_annotation_index_is_bool(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(True, "zachowanie", "bdb")

    def test_assert_add_annotation_index_is_list(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with([0], "zachowanie", "bdb")

    def test_assert_add_annotation_category_is_float(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, 0.0, "bdb")

    def test_assert_add_annotation_category_is_none(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, None, "bdb")

    def test_assert_add_annotation_category_is_int(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, 0, "bdb")

    def test_assert_add_annotation_category_is_bool(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, False, "bdb")

    def test_assert_add_annotation_category_is_list(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, ["matma"], "bdb")

    def test_assert_add_annotation_content_is_float(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, "zachowanie", 0.0)

    def test_assert_add_annotation_content_is_none(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, "zachowanie", None)

    def test_assert_add_annotation_content_is_int(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, "zachowanie", 0)

    def test_assert_add_annotation_content_is_bool(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, "zachowanie", True)

    def test_assert_add_annotation_content_is_list(self):
        assert_that(self.temp2.add_annotation).raises(TypeError).when_called_with(0, "zachowanie", ["bdb"])





