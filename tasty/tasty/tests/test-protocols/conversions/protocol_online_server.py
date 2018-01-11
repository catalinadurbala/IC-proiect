from tasty.types import conversions
from tasty.types.driver import IODriver
from tasty.types import *
driver = IODriver()

def protocol(client, server, params):
    server.val = Unsigned(bitlen=32, empty=True, signed=False, dim=[1]).input()
    server.gval = Garbled(bitlen=32, val=server.val, signed=False, dim=[1])
    server.rval = Unsigned(bitlen=32, val=server.gval, signed=False, dim=[1])

    if server.val == server.rval:
        server.output('server plain -> garbled -> plain: SUCCESS')
    else:
        server.output('server plain -> garbled -> plain: FAIL!')
    client.gval = Garbled(bitlen=32, val=Unsigned(bitlen=32, dim=[1], signed=False, passive=True, empty=True), passive=True, signed=False, dim=[1])
    server.gval2 = Garbled(bitlen=32, val=server.val, signed=False, dim=[1])
    conversions.Garbled_Garbled_send(server.gval2, client.gval2, 32, [1], False)
