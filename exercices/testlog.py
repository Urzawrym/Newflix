"""from collections import namedtuple

listionary = [{u'city': u'paris', u'id': u'1', u'name': u'paul'},
              {u'city': u'madrid', u'id': u'2', u'name': u'paul'},
              {u'city': u'berlin', u'id': u'3', u'name': u'tom'},
              {u'city': u'madrid', u'id': u'4', u'name': u'tom'}]


Profile = namedtuple('Profile', ['city', 'id', 'name'])
listionary = [Profile(*d) for d in listionary]

if listionary.city == "paul" and ele.city = "madrid"
    print ("yes")"""

"""people = [
{'name': "Tom", 'age': 10},
{'name': "Mark", 'age': 5},
{'name': "Pam", 'age': 7}
]

userdict = list(filter(lambda person: person['name'] == 'Pam', people))

print (userdict)"""

import operator, functools

l=[{'value': 'apple', 'blah': 2},
 {'value': 'banana', 'blah': 3} ,
 {'value': 'cars', 'blah': 4}]


print(list(map(operator.itemgetter('value'), l)))

