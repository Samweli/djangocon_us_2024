from qgis.core import *
from qgis.gui import QgsMapCanvas
from qgis.PyQt.QtWidgets import QFrame, QGridLayout, QMainWindow

application = QgsApplication([], False)


QgsApplication.setPrefixPath('/usr', True)
QgsApplication.initQgis()

main_window = QMainWindow()
main_window.setWindowTitle(
    "Python with QGIS example | "
    "DjangoCon US 2024"
)
frame = QFrame()
main_window.setCentralWidget(frame)
layout = QGridLayout(frame)

map_canvas = QgsMapCanvas()
layout.addWidget(map_canvas)

raster_file_uri = 'https://github.com/qgis/QGIS-Sample-Data/' \
                  'blob/master/qgis_sample_data/raster/' \
                  'SR_50M_alaska_nad.tif?raw=true'

raster_layer = QgsRasterLayer(raster_file_uri, 'test_layer')

QgsProject.instance().addMapLayer(raster_layer)
map_canvas.setLayers([raster_layer])
map_canvas.setExtent(raster_layer.extent())

main_window.show()
application.exec_()
