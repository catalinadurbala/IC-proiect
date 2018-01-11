from tasty.types import conversions
from tasty.types import *
from tasty.types.driver import IODriver
import dill as pickle
__params__ = {'K': 12, 'N': 52, 'M': 42}
driver = IODriver({'K': 12, 'N': 52, 'M': 42})

def protocol(c, s, p):
    c.gbot = Garbled(val=Unsigned(bitlen=6, dim=[1], signed=False, passive=True, empty=True), passive=True, signed=False, bitlen=6, dim=[1])
    conversions.PaillierVec_GarbledVec_send(s.hD, c.gD, 69, [42], True, force_bitlen=50, force_signed=False)
    (c.gDmin_val, c.gDmin_ix) = c.gD.min_value_index()
    conversions.Unsigned_Garbled_send(s.tau, c.gtau, 50, [1], False)
    c.gcmp = c.gDmin_val < c.gtau
    c.gout = c.gcmp.mux(c.gbot, c.gDmin_ix)
    c.out = Unsigned(val=c.gout, passive=True, signed=False, bitlen=6, dim=[1])
