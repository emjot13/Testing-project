from hamcrest import *
from projekt.main import E_gradebook
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = E_gradebook()
        self.one = E_gradebook()
        self.two = E_gradebook()
        self.three = E_gradebook()
        self.one.add_student("Kasia K")
        self.one.add_subject(0, "matma")



    def test_is_any_instance(self):
        assert_that(self.temp, not_none())

    def test_is_correct_instance(self):
        assert_that(self.temp, instance_of(E_gradebook))

    def test_correct_instances_reproducibility(self):
        assert_that(all_of(instance_of(E_gradebook), self.one, self.two, self.three))

    def test_assert_init_index_is_int(self):
        assert_that(self.temp.index, instance_of(int))

    def test_increased_index_after_adding_student(self):
        before = self.temp.index
        self.temp.add_student("Kasia K")
        after = self.temp.index
        assert_that(after - before), equal_to(1)

    def test_increased_index_after_adding_10_students(self):
        for x in range(10):
            self.temp.add_student("Kasia K")
        before = self.temp.index
        self.temp.add_student("Kasia K")
        after = self.temp.index
        assert_that(after - before), equal_to(1)

    def test_increased_index_after_adding_100_students(self):
        for x in range(100):
            self.temp.add_student("Kasia K")
        before = self.temp.index
        self.temp.add_student("Kasia K")
        after = self.temp.index
        assert_that(after - before), equal_to(1)

    def test_increased_index_after_adding_1000_students(self):
        for x in range(1000):
            self.temp.add_student("Kasia K")
        before = self.temp.index
        self.temp.add_student("Kasia K")
        after = self.temp.index
        assert_that(after - before), equal_to(1)

    def test_add_student_successful(self):
        assert_that(bool(self.one.students), is_(True))

    def test_add_student_successful2(self):
        assert_that(bool(self.one.students)), equal_to(1)

    def test_add_student_basic_info_is_dict(self):
        assert_that(self.one.students[0][0], instance_of(dict))

    def test_added_correct_value(self):
        assert_that(self.one.students[0][0], has_value("Kasia K"))

    def test_add_student_additional_info_is_dict(self):
        assert_that(self.one.students[0][1], instance_of(dict))


    def test_add_student_has_annotation_key(self):
        assert_that(self.one.students[0][0], has_key("annotations"))


    def test_add_student_has_average_grades_key(self):
        assert_that(self.one.students[0][0], has_key("average grades"))

    def test_add_annotation_is_dict(self):
        assert_that(self.one.students[0][0]["annotations"], instance_of(dict))

    def test_add_student_average_grades_is_dict(self):
        assert_that(self.one.students[0][0]["average grades"], instance_of(dict))

    def test_add_student_annotations_dict_is_empty(self):
        assert_that(bool(self.one.students[0][0]["annotations"]), is_(False))


    def test_add_student_average_grades_dict_is_empty(self):
        assert_that(bool(self.one.students[0][0]["average grades"]), is_(False))

    def test_add_subject_added(self):
        assert_that(bool(self.one.students[0][1]), is_(True))

    def test_add_subject_added_correct_subject_name(self):
        assert_that(self.one.students[0][1], has_key("matma"))

    def test_add_subject_subject_value_is_dict(self):
        assert_that(self.one.students[0][1], instance_of(dict))

    def test_add_subject_subject_value_is_empty_dict(self):
        assert_that(bool(self.one.students[0][1]["matma"]), is_(False))

    def test_add_subject_returns_correctly(self):
        assert_that(self.one.students, equal_to([[{0: 'Kasia K', 'annotations': {}, 'average grades': {}}, {'matma': {}}]]))

    def test_add_subject_returns_correctly_for_5_students(self):
        for k in range(4):
            self.one.add_student("Kasia K")
        for k in range(5):
            self.one.add_subject(k, "matma")
        assert_that(self.one.students, equal_to([[{0: 'Kasia K', 'annotations': {}, 'average grades': {}}, {'matma': {}}], [{1: 'Kasia K', 'annotations': {}, 'average grades': {}}, {'matma': {}}], [{2: 'Kasia K', 'annotations': {}, 'average grades': {}}, {'matma': {}}], [{3: 'Kasia K', 'annotations': {}, 'average grades': {}}, {'matma': {}}], [{4: 'Kasia K', 'annotations': {}, 'average grades': {}}, {'matma': {}}]]))

    def test_delete_is_dict_after_deleting_only_subject(self):
        self.one.delete_subject(0, "matma")
        assert_that(self.one.students[0][1], instance_of(dict))

    def test_delete_is_empty_dict_after_deleting_only_subject(self):
        self.one.delete_subject(0, "matma")
        assert_that(bool(self.one.students[0][1]), is_(False))

    def test_successfully_deletes_5_subjects(self):
        for x in range(1, 5):
            self.one.add_subject(0, "matma" + str(x))
        for x in range(0, 5):
            if x == 0:
                self.one.delete_subject(0, "matma")
            else:
                self.one.delete_subject(0, "matma" + str(x))
        assert_that(bool(self.one.students[0][1]), is_(False))

    def test_successfully_deletes_10_subjects(self):
        for x in range(1, 10):
            self.one.add_subject(0, "matma" + str(x))
        for x in range(0, 10):
            if x == 0:
                self.one.delete_subject(0, "matma")
            else:
                self.one.delete_subject(0, "matma" + str(x))
        assert_that(bool(self.one.students[0][1]), is_(False))

    def test_delete_subject_return_correctly(self):
        self.one.delete_subject(0, "matma")
        assert_that(self.one.students, equal_to([[{0: 'Kasia K', 'annotations': {}, 'average grades': {}}, {}]]))


