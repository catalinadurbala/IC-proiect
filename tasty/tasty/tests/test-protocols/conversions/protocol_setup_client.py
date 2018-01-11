from tasty.types import conversions
from tasty.types.driver import IODriver
from tasty.types import *
driver = IODriver()

def protocol(client, server, params):
    client.gval = Garbled(bitlen=32, val=Unsigned(bitlen=32, dim=[1], signed=False, passive=True, empty=True), signed=False, dim=[1])
    client.rval = Unsigned(bitlen=32, val=client.gval, signed=False, dim=[1])
    conversions.Garbled_Garbled_receive(server.gval2, client.gval2, 32, [1], False)
    client.rval2 = Unsigned(bitlen=32, val=client.gval2, signed=False, dim=[1])
