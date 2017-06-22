# from twisted.internet import protocol, reactor
# 
# class Echo(protocol.Protocol):
#     
#     def dataReceived(self, data):
#         self.transport.write(data)
#         
# class EchoFactory(protocol.Factory):
#     def buildProtocol(self, addr):
#         return Echo()
#     
# reactor.listenTCP(8000, EchoFactory())#@UndefinedVariable
# print("Try to listen")
# reactor.run()#@UndefinedVariable


# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    print("\nServer waiting for response")
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        if data == ("Here is my timestamp").encode():
            data_decoded = data.decode()
            print('\nClient said: {}'.format(data_decoded))
            server_response = ("I recieve  your timestamp, and you have passed").encode()
            
            self.transport.write(server_response)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(7000,factory)#@UndefinedVariable
    reactor.run()#@UndefinedVariable

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()









