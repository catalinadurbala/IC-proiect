from tasty.types import conversions
from tasty.types.driver import IODriver
from tasty.types import *
driver = IODriver()

def protocol(client, server, params):
    server.gval = Garbled(bitlen=32, val=Unsigned(bitlen=32, dim=[1], signed=False, passive=True, empty=True), signed=False, dim=[1])
    client.gval = Garbled(bitlen=32, val=Unsigned(bitlen=32, dim=[1], signed=False, passive=True, empty=True), passive=True, signed=False, dim=[1])
    client.rval = Unsigned(bitlen=32, val=client.gval, passive=True, signed=False, dim=[1])
    server.gval2 = Garbled(bitlen=32, val=Unsigned(bitlen=32, dim=[1], signed=False, passive=True, empty=True), signed=False, dim=[1])
    conversions.Garbled_Garbled_send(server.gval2, client.gval2, 32, [1], False)
    client.rval2 = Unsigned(bitlen=32, val=client.gval2, passive=True, signed=False, dim=[1])
