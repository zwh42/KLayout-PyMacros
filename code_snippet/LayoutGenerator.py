import pya
import sys
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib")  ##Added other Python package, for KLayout v0.24, Python version is 3.4.2
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib\site-packages")
sys.stderr = sys.stdout
import numpy

CELL_PATH = R"C:\Localdata\temp\saved_cell_1.oas"

main_window = pya.Application.instance().main_window()
main_window.close_all()
main_window.create_view()
layout_view = pya.Application.instance().main_window().current_view()

cell_view = main_window.load_layout(CELL_PATH, 1)
layout = cell_view.layout()

original_cell = layout.top_cells()[0]

top_cell = layout.create_cell("TOP")


top_cell.insert(pya.CellInstArray(original_cell.cell_index(), pya.Trans(1, True, 0, 0)))


print(top_cell)





