import pya  #KLayout  Python interface package

import sys
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib")  ##Added other Python package, for KLayout v0.24, Python version is 3.4.2
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib\site-packages")

import numpy

layout = pya.Layout()
layout.dbu = 0.01

top = layout.create_cell("TOP")
layer = layout.layer(1, 0)

top.shapes(layer).insert(pya.Box(0, 0, 1000, 2000))

layout.write(r"C:\Localdata\temp\test.gds")
print("write gds done")