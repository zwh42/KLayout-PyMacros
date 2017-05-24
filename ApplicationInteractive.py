import pya  #KLayout  Python interface package

import sys
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib")  ##Added other Python package, for KLayout v0.24, Python version is 3.4.2
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib\site-packages")

import numpy

current_application = pya.Application.instance()
main_window = current_application.main_window()

layout_view = main_window.current_view()

k = layout_view.each_object_selected() 

#print(help(layout_view))
#print(help(k))
#print(next(k))


pya.MessageBox.info("2333", "Hello!", pya.MessageBox.Ok) 
