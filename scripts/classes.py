class Human(object):
    
    def __init__(self, name):
        self.firstName = name.split() [0]
        self.lastName = name.split() [1]

    def greet(self):
        print("Hello! My name is %s." % self.lastName)
    
    def sleep(self, length):
        print("Z" + ("z"*length))

    
class Canadian(Human):
    def __init__(self, name, city):
        super(Canadian, self).__init__(name)
        self.city = city

    def greet(self):
        print("Hello! My name is %s. How do you do?" % self.lastName + " I live in %s." % self.city)


bob = Canadian("Bob Bobert", "Vancouver")
bob.greet()