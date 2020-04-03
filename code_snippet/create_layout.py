import pya
import sys
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib")  ##Added other Python package, for KLayout v0.24, Python version is 3.4.2
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib\site-packages")

sys.stderr = sys.stdout

import numpy

pya.Application.instance().main_window().close_all()
pya.Application.instance().main_window().create_view()

layout_view = pya.Application.instance().main_window().current_view()

main_window = pya.Application.instance().main_window()
layout = main_window.create_layout(1).layout()
layout.dbu = 0.001 #in micron

cell = layout.create_cell("TOP")

layer_index = layout.insert_layer(pya.LayerInfo(10, 0))
cell.shapes(layer_index).insert(pya.Box(0, 0, 1000, 2000))

layer_index2 = layout.insert_layer(pya.LayerInfo(10, 1))
cell.shapes(layer_index2).insert(pya.Box(-1000,-1000, 1000, 1000))


layout_view.select_cell(cell.cell_index(), 0)
layout_view.zoom_fit()


lib = pya.Library.library_by_name("Basic")
#print(pya.Library.library_names())

if not lib:
    raise("Unknown lib")

pcell_decl = lib.layout().pcell_declaration("TEXT")

parameter_dict = {
    "text" : "Hello, World!",
    "layer" : pya.LayerInfo(100, 200),
    "mag" : 2.5,
}

pv = []

print([p.name for p in pcell_decl.get_parameters()])


for p in pcell_decl.get_parameters():
    if p.name in parameter_dict:
        pv.append(parameter_dict[p.name])
    else:
        pv.append(p.default)

pcell_var = layout.add_pcell_variant(lib, pcell_decl.id(), pv)

t = pya.Trans(pya.Trans.R0, 0, 0)
pcell_inst = cell.insert(pya.CellInstArray(pcell_var, t))




output_options = SaveLayoutOptions()
output_options.dbu = 0.025
output_options.format = "OASIS"
output_options.scale_factor = 0.5


layout.write(r"C:\Localdata\temp\test6.gds", output_options)
print("write gds done")

