# from twisted.internet import reactor, protocol
# 
# class EchoClient(protocol.Protocol):
#     def connectionMade(self):
#         self.transport.write(("Hello, world!").encode())
# 
#     def dataReceived(self, data):
#         print ("Server said:", data.decode())
#         self.transport.loseConnection()
# 
# class EchoFactory(protocol.ClientFactory):
#     def buildProtocol(self, addr):
#         return EchoClient()
#  
#     def clientConnectionFailed(self, connector, reason):
#         print ("Connection failed.")
#         reactor.stop()#@UndefinedVariable
#         
#     def clientConnectionLost(self, connector, reason):
#         print ("Connection lost.")
#         reactor.stop()#@UndefinedVariable
# 
# reactor.connectTCP("localhost", 8000, EchoFactory())#@UndefinedVariable
# reactor.run()#@UndefinedVariable



# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


"""
An example client. Run simpleserv.py first before running this.
"""
from __future__ import print_function

from twisted.internet import reactor, protocol


# a client protocol

class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    
    def connectionMade(self):
        self.transport.write(("Here is my timestamp").encode())
        print('\nHere is my timestamp')
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print("\nServer said:", data.decode())
        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print("\nconnection lost")
        
        


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("\nConnection failed - goodbye!")
        reactor.stop()#@UndefinedVariable
    
    def clientConnectionLost(self, connector, reason):
        print("\nConnection lost - goodbye!")
        reactor.stop()#@UndefinedVariable


# this connects the protocol to a server running on port 8000
def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 7000, f)#@UndefinedVariable
    reactor.run()#@UndefinedVariable

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()