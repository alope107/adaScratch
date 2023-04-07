from oop_review.person import Person

class Student(Person):
    def bill(self):
        return super().bill() * .8