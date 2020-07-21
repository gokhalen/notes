#   https://stackoverflow.com/a/33533514/13560598

# here, the method within class Point accepts arguments of type class Point
# to declare the type use 'Point' instead of just Point (which is the usual case)
# this is supposed to go away in Python 4
class Point(object):
    def distance(p1:'Point',p2:'Point'):
        return 
