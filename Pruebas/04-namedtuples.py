
from collections import namedtuple

Person = namedtuple("Person", "name lastname age salary")

person1 = Person("Diego", "Martin", 36, 19000.00 ) 

print(person1)