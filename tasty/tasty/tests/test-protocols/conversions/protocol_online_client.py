from tasty.types import conversions
from tasty.types.driver import IODriver
from tasty.types import *
driver = IODriver()

def protocol(client, server, params):
    client.val = Unsigned(bitlen=32, empty=True, signed=False, dim=[1]).input()
    client.gval = Garbled(bitlen=32, val=client.val, signed=False, dim=[1])
    client.rval = Unsigned(bitlen=32, val=client.gval, signed=False, dim=[1])

    if client.val == client.rval:
        client.output('client plain -> garbled -> plain: SUCCESS')
    else:
        client.output('client plain -> garbled -> plain: FAIL!')
    conversions.Garbled_Garbled_receive(server.gval2, client.gval2, 32, [1], False)
    client.rval2 = Unsigned(bitlen=32, val=client.gval2, signed=False, dim=[1])
    client.sval = Unsigned(bitlen=32, val=42, signed=False, dim=[1])

    if client.rval2 == client.sval:
        client.output('server plain -> garbled -> client plain: SUCCESS')
    else:
        client.output('server plain -> garbled -> client plain: SUCCESS')
