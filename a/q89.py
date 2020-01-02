# a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class person(object):
    def gender(self):
        return "unknow"

class male(person):
    def gender(self):
        return "male"

class female(person):
    def gender(self):
        return "female"


a = male()
b = female()

print(a.gender())
print(b.gender())


      
