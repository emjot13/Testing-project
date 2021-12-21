class E_gradebook:
    def __init__(self):
        self.students = []
        self.index = 0

    def string_error(self, string):
        if type(string) is not str:
            raise TypeError(f'Given value: "{string}" is not a string')

    def add_student(self, student):
        self.string_error(student)
        if len(student.split()) < 2:
            raise ValueError("Student must have a name and a surname")
        dic = {self.index: student, "annotations": {}, "average grades": {}}
        new_entry = [dic, {}]
        self.students.append(new_entry)
        self.index += 1






