class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.score = []



    def fullname(self):
        return f"Fullname: {self.firstname} {self.lastname}"
    
    def add_score(self, new_score):
        return self.score.append(new_score)
    
    def total_score(self):
        return sum(self.score)

    def highest_score(self):
        return max(self.score)
        
    def lowest_score(self):
        return min(self.score)

   
    



joseph = Student("joseph","dre")
dorcas = Student("dorcas", "tanimu")
joseph.add_score(10)
dorcas.add_score(4)


print(joseph.fullname())
print(dorcas.fullname())
print(joseph.score)
print(dorcas.score)
print(joseph.total_score())
print(joseph.highest_score())
print(dorcas.highest_score())
print(joseph.lowest_score())
print(dorcas.lowest_score())
