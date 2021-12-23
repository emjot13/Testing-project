class E_gradebook:
    def __init__(self):
        self.students = []
        self.index = 0

    def string_error(self, string):
        if type(string) is not str:
            raise TypeError(f'Given value: "{string}" is not a string')

    def index_error(self, index):
        if type(index) is not int:
            raise TypeError("Index must be an integer")

    def add_student(self, student):
        self.string_error(student)
        if len(student.split()) < 2:
            raise ValueError("Student must have a name and a surname")
        dic = {self.index: student, "annotations": {}, "average grades": {}}
        new_entry = [dic, {}]
        self.students.append(new_entry)
        self.index += 1

    def delete_student(self, index):
        self.index_error(index)
        is_index = False
        for item in self.students:
            if index in item[0].keys():
                self.students.remove(item)
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")


    def edit_student(self, index, new_value):
        self.string_error(new_value)
        self.index_error(index)
        is_index = False
        for item in self.students:
            if index in item[0].keys():
                item[0][index] = new_value
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")
        if len(new_value.split()) < 2:
            raise ValueError("Student must have a name and a surname")


    def add_subject(self, index, subject_name):
        self.index_error(index)
        self.string_error(subject_name)
        is_index = False
        for item in self.students:
            if index in item[0].keys():
                item[1][subject_name] = {}
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")

    def delete_subject(self, index, subject_name):
        self.index_error(index)
        self.string_error(subject_name)
        is_index, is_subject = False, False
        for item in self.students:
            if index in item[0].keys():
                if subject_name in item[1].keys():
                    is_subject = True
                    del item[1][subject_name]
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")
        if not is_subject:
            raise ValueError("Student with this index does not attend given subject")

    def edit_subject(self, index, subject_name, new_subject_name):
        self.index_error(index)
        self.string_error(subject_name)
        self.string_error(new_subject_name)
        is_index, is_subject = False, False
        for item in self.students:
            if index in item[0].keys():
                if subject_name in item[1].keys():
                    is_subject = True
                    item[1][new_subject_name] = item[1].pop(subject_name)
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")
        if not is_subject:
            raise ValueError("Student with this index does not attend given subject")

    def add_grade(self, index, subject_name, description, grade):
        self.index_error(index)
        self.string_error(description)
        self.string_error(subject_name)
        is_index, is_subject = False, False
        if type(grade) not in [int, float]:
            raise TypeError("Given grade must be a number")
        if not 1 <= grade <= 6:
            raise ValueError("Given grade must be between 1 and 6")
        for item in self.students:
            if index in item[0].keys():
                is_index = True
                if subject_name in item[1].keys():
                    is_subject = True
                    item[1][subject_name][description] = grade
        if not is_index:
            raise ValueError("Student with given index has not been found")
        if not is_subject:
            raise ValueError("Student with this index does not attend given subject")


    def edit_grade(self, index, subject_name, description, grade):
        self.index_error(index)
        self.string_error(subject_name)
        self.string_error(description)
        if type(grade) not in [int, float]:
            raise TypeError("Given grade must be a number")
        if not 1 <= grade <= 6:
            raise ValueError("Given grade must be between 1 and 6")
        is_index, is_subject, is_description = False, False, False
        for item in self.students:
            if index in item[0].keys():
                if subject_name in item[1].keys():
                    is_subject = True
                    if description in item[1][subject_name].keys():
                        is_description = True
                        item[1][subject_name][description] = grade
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")
        if not is_subject:
            raise ValueError("Student with this index does not attend given subject")
        if not is_description:
            raise ValueError("This student does not have a grade with such description")

    def subject_average(self, index, subject_name):
        self.index_error(index)
        self.string_error(subject_name)
        is_index, is_subject = False, False
        for item in self.students:
            if index in item[0].keys():
                if subject_name in item[1].keys():
                    is_subject = True
                    if len(item[1][subject_name]) == 0:
                        raise Exception("There are none grades from this subject")
                    item[0]["average grades"][f"average {subject_name} grade"] = round(
                        sum(item[1][subject_name].values()) / len(item[1][subject_name]), 2)
                is_index = True
        if not is_index:
            raise ValueError("Student with given index has not been found")
        if not is_subject:
            raise ValueError("Student with this index does not attend given subject")