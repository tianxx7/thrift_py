# utf-8

__author__ = "txx"

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from py.thrift.generated import PersonService
from py.thrift.generated import ttypes

try:
    tSocket = TSocket.TSocket('localhost',8899)
    tSocket.setTimeout(600)
    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)

    client = PersonService.Client(protocol)

    transport.open()
    person = client.getPersonByUsername("张三")
    print(person.username)
    print(person.age)
    print(person.married)

    print("----------------")

    newPerson = ttypes.Person()
    newPerson.username = "张力"
    newPerson.married = False
    newPerson.age = 34

    client.savePerson(newPerson)


except Thrift.TException as tx:
    print('%s' % tx.message)