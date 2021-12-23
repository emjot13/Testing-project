from projekt.main import E_gradebook


class Tests:
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()