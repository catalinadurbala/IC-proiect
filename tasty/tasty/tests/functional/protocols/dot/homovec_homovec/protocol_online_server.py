from tasty.types import conversions
from tasty.types import *
from tasty import state
from tasty.cost_results import *

def protocol(client, server):
    server.v = UnsignedVec(bitlen=16, dim=1000, empty=True, signed=False).input(random=True)
    server.w = UnsignedVec(bitlen=16, dim=1000, empty=True, signed=False).input(random=True)
    server.cr = server.v.dot(server.w)
    conversions.Unsigned_Unsigned_send(server.cr, client.cr, 42, [1], False)
    server.hv = HomomorphicVec(val=server.v, signed=False, bitlen=16, dim=[1000])
    server.hw = HomomorphicVec(val=server.w, signed=False, bitlen=16, dim=[1000])
    server.hr = server.hv.dot(server.hw)
    conversions.Paillier_Unsigned_send(server.hr, client.r, 42, [1], False)
