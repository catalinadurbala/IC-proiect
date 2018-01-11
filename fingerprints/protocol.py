# -*- coding: utf-8 -*
import dill as pickle
from tasty.types import *

def protocol(client, server):
    M = 16
    L = 7
    N = 19
    # distance threshold
    Tsq = 5

    # client input
    client.X = UnsignedVec(bitlen=L, dim=M).input(random=True)
    
    # server input
    server.Y = UnsignedVec(bitlen=L, dim=M).input(random=True)
    #server.Y <<= client.X
    
    # Step 1
    client.minustwox = SignedVec(dim=M)
    for i in range(M):
        client.minustwox[i] = (-2) * client.X[i]
    client.givinguponlife = Unsigned(val=2**N)
    client.minustwoxmod2n = SignedVec(dim=M)
    
    for i in range(M):
        client.minustwoxmod2n[i] = client.givinguponlife + client.minustwox[i] 
    client.xsq = client.X.dot(client.X)
    
    client.hxsq = Homomorphic(val=client.xsq)
    client.hminustwox = HomomorphicVec(val=client.minustwoxmod2n)

    server.hminustwox <<= client.hminustwox
    server.hxsq <<= client.hxsq
    
    # Step 2 (a)
    server.ysq = server.Y.dot(server.Y)
    server.hysq = Homomorphic(val=server.ysq)
    server.hminustwoxy = server.hminustwox.dot(server.Y)
    server.d = server.hxsq + server.hysq
    server.d += server.hminustwoxy
    
    server.rs = Unsigned(bitlen=N).input(random=True)
    server.hrs = Homomorphic(val=server.rs)
    server.dprime = server.d + server.hrs
    client.dprime <<= server.dprime
    
    # Step 2 (b)
    client.rc <<= Unsigned(val=server.dprime)
    
    # Step 2 (c)
    client.grs <<= Garbled(val=server.hrs)
    client.grc = Garbled(val=client.rc)
    client.r = client.grc - client.grs
    client.t = Unsigned(bitlen=N, val=Tsq)
    client.gt = Garbled(val=client.t)
    client.gresult = client.r < client.gt
    client.result = Unsigned(val=client.gresult)
    client.result.output(desc="same fingerprints? ")
    
    client.output("SUCCESS")
    server.output("SUCCESS")