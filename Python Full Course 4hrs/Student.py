class Student:
    def __init__(self, name, major, gpa, IsProbation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.IsProbation = IsProbation

    def on_honor_role(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
