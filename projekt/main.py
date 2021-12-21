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





