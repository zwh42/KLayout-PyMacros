import pya


class ImageToLayout(pya.QDialog):
    def __init__(self, parent = None):
        super(ImageToLayout, self).__init__()
        self.setWindowTitle("Image to Layout")
        
        
        self.window_width = 800
        self.window_height = 600 
        
        self.resize(self.window_width, self.window_height)
        
        self.layout = pya.QGridLayout(self)
        
        self.input_text = pya.QLineEdit(self)
        self.input_text.setAcceptDrops(True)
        self.input_text.setFont(pya.QFont('Times', 15))
        
        self.input_text.setText("select image:")
        
        self.file_dialog = pya.QFileDialog(self)
        self.file_dialog.setFont(pya.QFont('Times', 10))
        
        self.select_file_button = pya.QPushButton("select image", self)
        self.select_file_button.setFont(pya.QFont('Times', 15, pya.QFont.Bold))
        self.select_file_button.clicked(self.select_file_button_clicked)
        
        self.convert_button = pya.QPushButton("convert to OASIS file", self)
        self.convert_button.setFont(pya.QFont('Times', 15, pya.QFont.Bold))
        self.convert_button.clicked(self.covert_buttion_clicked)
        
        self.raw_image_label = pya.QLabel()
        
        self.raw_image_info_label = pya.QLabel("image size:")
        self.raw_image_info_label.setVisible(False)
        
        
        
        self.threshold_text = pya.QLineEdit(self)
        self.threshold_text.setAcceptDrops(True)
        self.threshold_text.setFont(pya.QFont('Times', 15))        
        self.threshold_text.setText("set threshold: 0 - 255")
        
        self.dbu_text = pya.QLineEdit(self)
        self.dbu_text.setAcceptDrops(True)
        self.dbu_text.setFont(pya.QFont('Times', 15))        
        self.dbu_text.setText("set DBU: ")        
        
        self.inverse_checkbox = pya.QCheckBox("inverse", self)
        self.inverse_checkbox.setFont(pya.QFont('Times', 15))
        
        
        self.progress_bar = pya.QProgressBar(self)
         
        
        self.layout.addWidget(self.input_text, 0, 0)        
        self.layout.addWidget(self.select_file_button, 0, 1)
        self.layout.addWidget(self.raw_image_label, 1, 0, 3, 1)
        
        self.layout.addWidget(self.threshold_text, 1, 1)
        self.layout.addWidget(self.inverse_checkbox, 2, 1)
        self.layout.addWidget(self.dbu_text, 3, 1)
        
        self.layout.addWidget(self.raw_image_info_label, 4, 0)
        
        self.layout.addWidget(self.progress_bar, 5, 0)
        self.layout.addWidget(self.convert_button, 5, 1)
        
        self.setLayout(self.layout)
        

    def select_file_button_clicked(self, checked):
        """ Event handler: button clicked """
        image_path = pya.QFileDialog.getOpenFileName(self)
        self.input_text.setText(image_path)
        
        #print("path = {}".format(absolute_path))
        #pixmap = QPixmap(image_path)
        #pixmap = pixmap.scaled(320, 320, Qt_AspectRatioMode.KeepAspectRatio)
        #self.raw_image_label.setPixmap(pixmap)
        
        with open(image_path, "rb") as f:
            content = f.read()
            
        self.raw_image = pya.QImage()
        self.raw_image.loadFromData(content)
        self.raw_image = self.raw_image.convertToFormat(pya.QImage.Format.Format_Grayscale8)        
        

        
        self.image_array = [[0] * self.raw_image.height() for _ in range(self.raw_image.width())]
        print("init empty array size: {} x {}".format(len(self.image_array), len(self.image_array[0])))
        
        total_pixel_count = self.raw_image.width() * self.raw_image.height() 
        count = 0
        for x in range(self.raw_image.width()):
            for y in range(self.raw_image.height()):
                pixel_value = self.raw_image.pixel(x, y)
                pixel_color = pya.QColor(pixel_value)
                #pixel_rgb = (pixel_color.red, pixel_color.green, pixel_color.blue)
                pixel_gray = int(pixel_color.red * 0.299 + pixel_color.green * 0.587 + pixel_color.blue * 0.114)
                #print(x, y, pixel_gray)
                self.image_array[x][y] = pixel_gray
                count += 1
            
            self.progress_bar.setValue(int(count/total_pixel_count))
                
        
        pixmap = pya.QPixmap.fromImage(self.raw_image)
        pixmap = pixmap.scaled(480, 480, pya.Qt.AspectRatioMode.KeepAspectRatio)
        self.raw_image_label.setPixmap(pixmap)      
        self.raw_image_label.show()
        
        self.raw_image_info_label.setText("raw image size: {} x {}".format(self.raw_image.width(), self.raw_image.height()))
        self.raw_image_info_label.setVisible(True)
        
        self.progress_bar.setVisible(False)
        

    
    def covert_buttion_clicked(self, checked):
        image_path = self.input_text.text
        print("image path: ", image_path)
        

        
        main_window = pya.Application.instance().main_window()
        
        #print(dir(main_window))
        #current_view = main_window.current_view()
        #print(type(current_view))
        #if not current_view:
            
        main_window.create_view()
        current_view = main_window.current_view()
            #raise Exception("no view availbe!")
            
        #cell_view = current_view.active_cellview()
        
        cell_view_id = current_view.create_layout(True)
        current_view.set_active_cellview_index(cell_view_id)
        cell_view = current_view.cellview(cell_view_id)
        
        
        if not cell_view.is_valid():
            raise Exception("cell view is not available")
            
        
        layout_layers = [
            pya.LayerInfo.new( 0, 0),
            #pya.LayerInfo.new( 1, 0),
            #pya.LayerInfo.new( 2, 0),
            #pya.LayerInfo.new( 3, 0),            
        ]
        
        layers = []
        
    
        for item in layout_layers:
            print(item)
            layer = cell_view.layout().insert_layer(item)
            lp = pya.LayerPropertiesNode()
            lp.source_layer = item.layer
            lp.source_datatype = item.datatype
            
            current_view.init_layer_properties(lp)
            current_view.insert_layer(current_view.end_layers(), lp)
        
            layers.append(layer) 
        
        
        current_view.update_content()
 
        dbu = 1
        try:
            dbu = float(self.dbu_text.text)
        except ValueError:            
            error_message_box = pya.QMessageBox(self)
            error_message_box.setText("Please set dbu to a number!")
            return
        
        image = pya.Image(image_path)
        print("image: {}, width = {}, height = {}".format(image_path, image.width(), image.height()))
        
        current_view.transaction( "Image channels to RGB" )
        trans = pya.ICplxTrans.from_dtrans(pya.DCplxTrans.new(1 / dbu) * image.trans * pya.DCplxTrans.new(dbu))
        
        # The dimension of one pixel 
        pixel_width = image.pixel_width / dbu
        pixel_height = image.pixel_height / dbu
        print("pixel width: {} pixel height: {}".format(pixel_width, pixel_height))
        
        
        cell_view.layout().create_cell("TOP")
        cell_view.cell_name = "TOP"
        #print("cell::", type(cell_view.cell), cell_view.cell)
        
      
        
        
        try:
            threshold = int(self.threshold_text.text)
        except ValueError:            
            error_message_box = pya.QMessageBox(self)
            error_message_box.setText("Please set the threshold to a number (0 ~ 255)!")
            return
        
        print("threshold", threshold)
        
        for layer in layers: 
  
            shapes = cell_view.cell.shapes(layer)

            image_width = self.raw_image.width()
            image_height = self.raw_image.height()
            for x in range(image_width):
                for y in range(image_height):
                    d = self.image_array[x][image_height - 1 - y]                    
                    if (not self.inverse_checkbox.isChecked() and d > threshold) or (self.inverse_checkbox.isChecked() and d < threshold):                    
                        p1 = pya.DPoint(x * pixel_width, y * pixel_height)
                        p2 = pya.DPoint((x + 1) * pixel_width, (y + 1) * pixel_height)
                        #print("draw: box: {}, {}".format(x, y))
                        dbox = pya.DBox.new(p1, p2)
                        box = pya.Box.from_dbox(dbox)
                        poly = pya.Polygon.new(box)
                        shapes.insert(poly.transformed_cplx(trans)) 
        
        print("drawing done")

        current_view.commit()

dialog = ImageToLayout(pya.Application.instance().main_window())
dialog.show()