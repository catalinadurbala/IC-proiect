from tasty.types import conversions
import dill as pickle
from tasty.types import *

def protocol(client, server):
    conversions.UnsignedVec_UnsignedVec_receive(client.X, server.Y, 7, [16], False)
    conversions.PaillierVec_PaillierVec_receive(client.hminustwox, server.hminustwox, 22, [16], True)
    conversions.Paillier_Paillier_receive(client.hxsq, server.hxsq, 18, [1], False)
    server.ysq = server.Y.dot(server.Y)
    server.hysq = Homomorphic(val=server.ysq, signed=False, bitlen=18, dim=[1])
    server.hminustwoxy = server.hminustwox.dot(server.Y)
    server.d = server.hxsq + server.hysq
    server.rs = Unsigned(bitlen=19, empty=True, signed=False, dim=[1]).input(random=True)
    server.hrs = Homomorphic(val=server.rs, signed=False, bitlen=19, dim=[1])
    server.dprime = server.d + server.hrs
    conversions.Paillier_Paillier_send(server.dprime, client.dprime, 35, [1], True)
    conversions.Paillier_Unsigned_send(server.dprime, client.rc, 35, [1], True)
    conversions.Paillier_Garbled_send(server.hrs, client.grs, 19, [1], False)
    client.grc = Garbled(val=client.rc, passive=True, signed=False, bitlen=35, dim=[1])
    client.gt = Garbled(val=Unsigned(bitlen=19, dim=[1], signed=False, passive=True, empty=True), passive=True, signed=False, bitlen=19, dim=[1])
    server.output('SUCCESS')
