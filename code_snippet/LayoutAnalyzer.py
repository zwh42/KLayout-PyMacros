import pya
import sys
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib")  ##Added other Python package, for KLayout v0.24, Python version is 3.4.2
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib\site-packages")

sys.stderr = sys.stdout

import numpy


def iterative_child_cell(cell):
    print(cell.name)
    for child_cell in cell.each_child_cell():
        print(child_cell)
        iterative_child_cell(child_cell)   

main_window = pya.Application.instance().main_window()
main_window.close_all()
main_window.create_view()
layout_view = pya.Application.instance().main_window().current_view()

cell_view = main_window.load_layout(r"C:\Localdata\temp\3h.oas", 1)
layout = cell_view.layout()

print("file: " + cell_view.filename())
print("path: ")
#print(dir(cell_view))
print(cell_view.cell_name, cell_view.name(), cell_view.technology)

#print(dir(layout))
print(layout.each_cell_top_down())

for cell in layout.each_top_cell():
    pass
    #print(cell)
    

for cell in layout.top_cells():
    print("top cell name: " + cell.name)
    iterative_child_cell(cell)
    
    


    