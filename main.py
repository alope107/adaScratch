from oop_review.person import Person
from oop_review.student import Student
from oop_review.subscription import Subscription

auberon = Person(1994)
netflix = Subscription("Netflix", 20.00)
hbo = Subscription("HBO", 40.00)

auberon.subscribe(netflix)
auberon.subscribe(hbo)

xinting = Student(1993)
xinting.subscribe(netflix)
xinting.subscribe(hbo)

print(auberon.bill())
print(xinting.bill())