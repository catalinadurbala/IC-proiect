from tasty.types import conversions
import dill as pickle
from tasty.types import *

def protocol(client, server):
    conversions.Paillier_Garbled_send(server.hrs, client.grs, 19, [1], False)
    client.grc = Garbled(val=client.rc, passive=True, signed=False, bitlen=35, dim=[1])
    client.r = client.grc - client.grs
    client.gt = Garbled(val=Unsigned(bitlen=19, dim=[1], signed=False, passive=True, empty=True), passive=True, signed=False, bitlen=19, dim=[1])
    client.gresult = client.r < client.gt
    client.result = Unsigned(val=client.gresult, passive=True, signed=False, bitlen=1, dim=[1])
