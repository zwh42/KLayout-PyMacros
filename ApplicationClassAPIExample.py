import pya
import sys
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib")  ##Added other Python package, for KLayout v0.24, Python version is 3.4.2
sys.path.append(r"C:\Users\wzhao\AppData\Local\Continuum\Anaconda3\envs\py34\Lib\site-packages")
import numpy

current_application = pya.Application.instance()

data_path = current_application.application_data_path()
print("user-local storage path: " + data_path)

install_path = current_application.inst_path()
print("isntallation path: " + install_path)

is_editable = current_application.is_editable()
print("current application editable? " + str(is_editable))

klayout_path = current_application.klayout_path()
print("klayout path: " + str(klayout_path))

klayout_version = current_application.version()
print("klayout version: " + klayout_version)

main_window = current_application.main_window()
main_window.close_current_view()

#print(help(main_window.create_layout))
cell_view = main_window.create_layout("StarkIndustry", 1) #tech name, mode

current_view_index = main_window.current_view_index()
print("current view index: " + str(current_view_index))

global_grid = main_window.grid_micron()
print("global grid in micron : " + str(global_grid))

#help(main_window.load_layout)
cell_view1 = main_window.load_layout(r"C:\Localdata\temp\temp.oas", 1)

load_layout_options = pya.LoadLayoutOptions()
load_layout_options.cif_dbu=0.003

#help(pya.LoadLayoutOptions)  
cell_view2 = main_window.load_layout(r"C:\Localdata\temp\temp.oas", 1)

main_window.close_all()

main_window.create_view()
layout_view = main_window.current_view()

image = pya.Image(r"C:\Users\wzhao\Desktop\IronMan.png")
layout_view.insert_image(image)

marker = pya.Marker.new(layout_view)
marker.set(pya.DBox(-200, -300, -100, -200))

