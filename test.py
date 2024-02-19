from main import StudentsInMLOps

def test_enrollStudents():
    students = StudentsInMLOps()
    students.enrollStudents(5)
    assert students.getTotalStrength() == 5

def test_dropStudents():
    students = StudentsInMLOps()
    students.enrollStudents(10)
    students.dropStudents(3)
    assert students.getTotalStrength() == 7

def test_getClassName():
    students = StudentsInMLOps()
    assert students.getClassName() == "StudentsInMLOps"
