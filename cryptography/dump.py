#!/usr/bin/env python3

# data. dump model
import os 
import io
import zlib
import numpy as np

code = io.BytesIO()
arr = np.random.rand(100,100)
np.save(code, arr)
compressed = zlib.compress(code.getvalue())

prt = np.load(io.BytesIO(zlib.decompress(compressed)))

print(prt)
