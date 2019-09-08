
__author__ = 'txx'

from thrift import Thrift
from py.thrift.generated import PersonService
from PersonServiceImpl import  PersonServiceImpl
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer


try:
    personServiceHandler = PersonServiceImpl()
    processor = PersonService.Processor(personServiceHandler)

    serverSocket = TSocket.TServerSocket(host="127.0.0.1",port=8899)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TSimpleServer(processor,serverSocket,transportFactory,protocolFactory)
    server.serve()
except Thrift.TException as ex:
    print("%s" % ex.message)