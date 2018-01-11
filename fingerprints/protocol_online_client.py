from tasty.types import conversions
import dill as pickle
from tasty.types import *

def protocol(client, server):
    client.X = UnsignedVec(bitlen=7, dim=16, empty=True, signed=False).input(random=True)
    conversions.UnsignedVec_UnsignedVec_send(client.X, server.Y, 7, [16], False)
    client.minustwox = SignedVec(dim=16, bitlen=10, signed=True)

    for i in range(16):
        client.minustwox[i] = Signed(bitlen=3, val=-2, signed=True, dim=[1]) * client.X[i]

    client.givinguponlife = Unsigned(val=524288, signed=False, bitlen=20, dim=[1])
    client.minustwoxmod2n = SignedVec(dim=16, bitlen=22, signed=True)

    for i in range(16):
        client.minustwoxmod2n[i] = client.givinguponlife + client.minustwox[i]

    client.xsq = client.X.dot(client.X)
    client.hxsq = Homomorphic(val=client.xsq, signed=False, bitlen=18, dim=[1])
    client.hminustwox = HomomorphicVec(val=client.minustwoxmod2n, signed=True, bitlen=22, dim=[16])
    conversions.PaillierVec_PaillierVec_send(client.hminustwox, server.hminustwox, 22, [16], True)
    conversions.Paillier_Paillier_send(client.hxsq, server.hxsq, 18, [1], False)
    conversions.Paillier_Paillier_receive(server.dprime, client.dprime, 35, [1], True)
    conversions.Paillier_Unsigned_receive(server.dprime, client.rc, 35, [1], True)
    conversions.Paillier_Garbled_receive(server.hrs, client.grs, 19, [1], False)
    client.grc = Garbled(val=client.rc, signed=False, bitlen=35, dim=[1])
    client.r = client.grc - client.grs
    client.t = Unsigned(bitlen=19, val=5, signed=False, dim=[1])
    client.gt = Garbled(val=client.t, signed=False, bitlen=19, dim=[1])
    client.gresult = client.r < client.gt
    client.result = Unsigned(val=client.gresult, signed=False, bitlen=1, dim=[1])
    client.result.output(desc='same fingerprints? ')
    client.output('SUCCESS')
