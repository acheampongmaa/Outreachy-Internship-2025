''' This is the class representing students'''


class Students: 
    _id_counter =1


    def __init__(self, name, level, course, gpa):
        self.name = name
        self.level = level
        self.course = course
        self.gpa = gpa
        self.student_id = Students._id_counter
        Students._id_counter +=1
        

    def add_student(self):
        return f" New student {self.name} with student ID {self.student_id} has been added to records."
    
    def update_record(self):
        return f"Student with name {self.name} record has gpa {self.gpa} updated."
    
    def remove_student(self):
        return f"Student with name {self.name} and ID {self.student_id} has been removed."
    
    def to_dict(self):
        return {
            "student_id" : self.student_id,
            "name" : self.name,
            "level" : self.level ,
            "course" : self.course,
            "gpa" : self.gpa
         
        }



