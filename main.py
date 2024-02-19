class StudentsInMLOps:
    def __init__(self):
        self.total_students = 0
    
    def enrollStudents(self, count):
        self.total_students += count
    
    def dropStudents(self, count):
        self.total_students -= count
    
    def getTotalStrength(self):
        return self.total_students
    
    def getClassName(self):
        return self.__class__.__name__
