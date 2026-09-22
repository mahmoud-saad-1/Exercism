PLANTS_ENCODING = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets"
}

STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

class Garden:
    def __init__(self, diagram, students=STUDENTS):
        # 1. No list conversion needed; keep them as strings!
        lines = diagram.splitlines()
        
        # 2. Extract the plant groupings using your clever unpacking trick
        plants_to_student = [
            [*lines[0][i:i+2], *lines[1][i:i+2]]
            for i in range(0, len(lines[0]), 2)
        ]
        
        # 3. Sort the students and map them instantly in a one-liner dictionary
        self.student_map = dict(zip(sorted(students), plants_to_student))

    def plants(self, student):
        # Look up the student's 4-letter list and translate them
        return [PLANTS_ENCODING[p] for p in self.student_map[student]]