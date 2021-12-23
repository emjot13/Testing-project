from projekt.main import E_gradebook


class Tests_add_subject:
    """
    >>> obj = E_gradebook()
    >>> obj.add_student("Kasia K")              # tests for incorrect index values
    >>> obj.add_subject("0", "matma")           # string
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_subject([0], "matma")           # list
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_subject(0.0, "matma")           # float
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_subject(None, "matma")          # none
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_subject(True, "matma")          # bool
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_subject({0:0}, "matma")          # dict
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_subject(0, 0)                    # tests for incorrect subject name values int
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0" is not a string
    >>> obj.add_subject(0, ["matma"])            # list
    Traceback (most recent call last):
    ...
    TypeError: Given value: "['matma']" is not a string
    >>> obj.add_subject(0, 0.0)                  # float
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0.0" is not a string
    >>> obj.add_subject(0, None)                 # none
    Traceback (most recent call last):
    ...
    TypeError: Given value: "None" is not a string
    >>> obj.add_subject(0, False)                # bool
    Traceback (most recent call last):
    ...
    TypeError: Given value: "False" is not a string
    >>> obj.add_subject(0, {"subject":"matma"}) # dict
    Traceback (most recent call last):
    ...
    TypeError: Given value: "{'subject': 'matma'}" is not a string
    >>> obj.add_subject(1, "matma")             #tests for non-existent index value
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.add_subject(-1, "matma")
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.add_subject(100, "matma")
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    """

class Tests_delete_subject:
    """
    >>> obj = E_gradebook()
    >>> obj.add_student("Kasia K")              # tests for incorrect index values
    >>> obj.add_subject("0", "matma")           # string
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.delete_subject([0], "matma")           # list
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.delete_subject(0.0, "matma")           # float
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.delete_subject(None, "matma")          # none
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.delete_subject(True, "matma")          # bool
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.delete_subject({0:0}, "matma")          # dict
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.delete_subject(0, 0)                    # tests for incorrect subject name values int
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0" is not a string
    >>> obj.delete_subject(0, ["matma"])            # list
    Traceback (most recent call last):
    ...
    TypeError: Given value: "['matma']" is not a string
    >>> obj.delete_subject(0, 0.0)                  # float
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0.0" is not a string
    >>> obj.delete_subject(0, None)                 # none
    Traceback (most recent call last):
    ...
    TypeError: Given value: "None" is not a string
    >>> obj.delete_subject(0, False)                # bool
    Traceback (most recent call last):
    ...
    TypeError: Given value: "False" is not a string
    >>> obj.delete_subject(0, {"subject":"matma"}) # dict
    Traceback (most recent call last):
    ...
    TypeError: Given value: "{'subject': 'matma'}" is not a string
    >>> obj.delete_subject(1, "matma")             #tests for non-existent index value
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.delete_subject(-1, "matma")
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.delete_subject(100, "matma")
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.delete_subject(0, "MATMA")             #tests for non-existent subject name value
    Traceback (most recent call last):
    ...
    ValueError: Student with this index does not attend given subject
    >>> obj.delete_subject(0, "matma ")
    Traceback (most recent call last):
    ...
    ValueError: Student with this index does not attend given subject
    >>> obj.delete_subject(0, " matma")
    Traceback (most recent call last):
    ...
    ValueError: Student with this index does not attend given subject
    """

class Tests_edit_subject:
    """
    >>> obj = E_gradebook()
    >>> obj.add_student("Kasia K")
    >>> obj.add_subject(0, "matma")
    >>> obj.edit_subject("0", "matma", "polski")      # tests for incorrect index values
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.edit_subject([0], "matma", "polski")           # list
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.edit_subject(0.0, "matma", "polski")           # float
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.edit_subject(None, "matma", "polski")          # none
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.edit_subject(True, "matma", "polski")          # bool
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.edit_subject({0:0}, "matma", "polski")          # dict
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.edit_subject(0, 0,"polski")                    # tests for incorrect subject name values int
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0" is not a string
    >>> obj.edit_subject(0, ["matma"], "polski")            # list
    Traceback (most recent call last):
    ...
    TypeError: Given value: "['matma']" is not a string
    >>> obj.edit_subject(0, 0.0, "polski")                  # float
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0.0" is not a string
    >>> obj.edit_subject(0, None, "polski")                 # none
    Traceback (most recent call last):
    ...
    TypeError: Given value: "None" is not a string
    >>> obj.edit_subject(0, False, "polski")                # bool
    Traceback (most recent call last):
    ...
    TypeError: Given value: "False" is not a string
    >>> obj.edit_subject(0, {"subject":"matma"}, "polski") # dict
    Traceback (most recent call last):
    ...
    TypeError: Given value: "{'subject': 'matma'}" is not a string
    >>> obj.edit_subject(0, "matma", 0)                    # tests for incorrect updated subject name values int
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0" is not a string
    >>> obj.edit_subject(0, "matma", ["polski"])            # list
    Traceback (most recent call last):
    ...
    TypeError: Given value: "['polski']" is not a string
    >>> obj.edit_subject(0, "matma", 0.0)                  # float
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0.0" is not a string
    >>> obj.edit_subject(0, "matma", None)                 # none
    Traceback (most recent call last):
    ...
    TypeError: Given value: "None" is not a string
    >>> obj.edit_subject(0, "matma", False)                # bool
    Traceback (most recent call last):
    ...
    TypeError: Given value: "False" is not a string
    >>> obj.edit_subject(0, "matma", {"subject":"polski"}) # dict
    Traceback (most recent call last):
    ...
    TypeError: Given value: "{'subject': 'polski'}" is not a string
    >>> obj.edit_subject(1, "matma", "polski")             #tests for non-existent index value
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.edit_subject(-1, "matma", "polski")
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.edit_subject(100, "matma", "polski")
    Traceback (most recent call last):
    ...
    ValueError: Student with given index has not been found
    >>> obj.edit_subject(0, "MATMA", "polski")             #tests for non-existent subject name value
    Traceback (most recent call last):
    ...
    ValueError: Student with this index does not attend given subject
    >>> obj.edit_subject(0, "matma ", "polski")
    Traceback (most recent call last):
    ...
    ValueError: Student with this index does not attend given subject
    >>> obj.edit_subject(0, " matma", "polski")
    Traceback (most recent call last):
    ...
    ValueError: Student with this index does not attend given subject
    """

class Tests_add_grade:
    """
    >>> obj = E_gradebook()
    >>> obj.add_student("Kasia K")
    >>> obj.add_subject(0, "matma")
    >>> obj.add_grade("0", "matma", "spr", 5)      # tests for incorrect index values
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_grade([0], "matma", "spr", 5)           # list
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_grade(0.0, "matma", "spr", 5)           # float
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_grade(None, "matma", "spr", 5)          # none
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_grade(True, "matma", "spr", 5)          # bool
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_grade({0:0}, "matma", "spr", 5)          # dict
    Traceback (most recent call last):
    ...
    TypeError: Index must be an integer
    >>> obj.add_grade(0, 0,"spr", 5)                    # tests for incorrect subject name values int
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0" is not a string
    >>> obj.add_grade(0, ["matma"], "spr", 5)            # list
    Traceback (most recent call last):
    ...
    TypeError: Given value: "['matma']" is not a string
    >>> obj.add_grade(0, 0.0, "spr", 5)                  # float
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0.0" is not a string
    >>> obj.add_grade(0, None, "spr", 5)                 # none
    Traceback (most recent call last):
    ...
    TypeError: Given value: "None" is not a string
    >>> obj.add_grade(0, False, "spr", 5)                # bool
    Traceback (most recent call last):
    ...
    TypeError: Given value: "False" is not a string
    >>> obj.add_grade(0, {"subject":"matma"}, "spr", 5) # dict
    Traceback (most recent call last):
    ...
    TypeError: Given value: "{'subject': 'matma'}" is not a string
    >>> obj.add_grade(0, "matma", 0, 5)                    # tests for incorrect description
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0" is not a string
    >>> obj.add_grade(0, "matma", ["spr"], 5)            # list
    Traceback (most recent call last):
    ...
    TypeError: Given value: "['spr']" is not a string
    >>> obj.add_grade(0, "matma", 0.0, 5)                  # float
    Traceback (most recent call last):
    ...
    TypeError: Given value: "0.0" is not a string
    >>> obj.add_grade(0, "matma", None, 5)                 # none
    Traceback (most recent call last):
    ...
    TypeError: Given value: "None" is not a string
    >>> obj.add_grade(0, "matma", False, 5)                # bool
    Traceback (most recent call last):
    ...
    TypeError: Given value: "False" is not a string
    >>> obj.add_grade(0, "matma", {"subject":"polski"}, 5) # dict
    Traceback (most recent call last):
    ...
    TypeError: Given value: "{'subject': 'polski'}" is not a string

    """





if __name__ == "__main__":
    import doctest
    doctest.testmod()