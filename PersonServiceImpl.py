# utf-8

__author__ = "txx"

from py.thrift.generated import ttypes

class PersonServiceImpl:
    def getPersonByUsername(self,username):
        print("got client param:" + username)
        person = ttypes.Person()
        person.username = username
        person.married = False
        person.age = 12
        return person

    def savePerson(self,person):
        print("got client param:")
        print(person.married)
        print(person.username)
        print(person.age)