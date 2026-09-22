class School:
    def __init__(self):
        self.names_grades = {}
        self.added_bool = []
        
    def add_student(self, name, grade):
        if name in self.names_grades:
            self.added_bool.append(False)
        else:
            self.added_bool.append(True)
            self.names_grades[name] = grade
            self.names_grades = dict(sorted(self.names_grades.items(), key = lambda item:(item[1], item[0])))

    def roster(self):
        return list(self.names_grades)

    def grade(self, grade_number):
        studen_grade =[name for name, grade in self.names_grades.items() if grade == grade_number]
        return studen_grade

    def added(self):
        return self.added_bool