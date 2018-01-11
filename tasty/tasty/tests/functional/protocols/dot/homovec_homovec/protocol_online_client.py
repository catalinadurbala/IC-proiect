from tasty.types import conversions
from tasty.types import *
from tasty import state
from tasty.cost_results import *

def protocol(client, server):
    conversions.Unsigned_Unsigned_receive(server.cr, client.cr, 42, [1], False)
    server.hr = server.hv.dot(server.hw)
    conversions.Paillier_Unsigned_receive(server.hr, client.r, 42, [1], False)

    if client.cr == client.r:
        client.output('SUCCESS')
    else:
        client.output('FAIL!')
