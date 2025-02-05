from functools import partial
from qgis.core import *
from qgis.gui import QgsMapCanvas, QgsSlider

from qgis.PyQt.QtWidgets import QFrame, QGridLayout, QMainWindow, QPushButton, QHBoxLayout
from qgis.PyQt.QtCore import QDateTime, QDate, QTime, Qt


def slider_value_changed(map_canvas, dates, value):
    """ Handles the application slider value update

    :param map_canvas: QGIS map canvas instance
    :type map_canvas: QgsMapCanvas

    :param date: Date that is to be set into the map canvas
    :type date: QDateTime
    """
    get_date(map_canvas, dates[value])


def get_date(map_canvas, date):
    """ Refreshes the passed QGIS map canvas with the date
    :param map_canvas: QGIS map canvas instance
    :type map_canvas: QgsMapCanvas

    :param date: Date that is to be set into the map canvas
    :type date: QDateTime

    """
    # The map canvas temporal range uses QgsDateTimeRange instance
    # as a type for the datetime properties.
    time = QgsDateTimeRange(
        date,
        date
    )
    map_canvas.setTemporalRange(time)
    map_canvas.refresh()


def set_date_widgets(
        map_canvas,
        main_window,
        frame,
        layout
):
    """
    Initializes slider and date buttons widgets that will
    be used in the navigation of the temporal layer.

    :param map_canvas: QGIS map canvas instance
    :type map_canvas: QgsMapCanvas

    :param main_window: Main application window
    :type main_window: QMainWindow

    :param frame: Frame that will hold all widgets
    :type frame: QFrame


    :param layout: Main window layout
    :type layout: QLayout
    """

    date_one = QPushButton('2024-09-23 00:00:00')
    date_two = QPushButton('2024-09-23 03:00:00')
    date_three = QPushButton('2024-09-23 06:00:00')
    date_four = QPushButton('2024-09-23 09:00:00')
    date_five = QPushButton('2024-09-23 12:00:00')
    date_six = QPushButton('2024-09-23 15:00:00')

    # Setting the datetimes based on the available temporal data from
    # the used layer, at the time of writing this the layer had the below temporal
    # date time values available. These might need to be changed by looking
    # at the temporal layer capabilities.

    date_time_one = QDateTime(QDate(2024, 9, 23), QTime(0, 00, 00))
    date_time_two = QDateTime(QDate(2024, 9, 23), QTime(3, 00, 00))
    date_time_three = QDateTime(QDate(2024, 9, 23), QTime(6, 00, 00))
    date_time_four = QDateTime(QDate(2024, 9, 23), QTime(9, 00, 00))
    date_time_five = QDateTime(QDate(2024, 9, 23), QTime(12, 00, 00))
    date_time_six = QDateTime(QDate(2024, 9, 23), QTime(15, 00, 00))


    animate_date_one = partial(get_date, map_canvas, date_time_one)
    date_one.clicked.connect(animate_date_one)

    animate_date_two = partial(get_date, map_canvas, date_time_two)
    date_two.clicked.connect(animate_date_two)

    animate_date_three = partial(get_date, map_canvas, date_time_three)
    date_three.clicked.connect(animate_date_three)

    animate_date_four = partial(get_date, map_canvas, date_time_four)
    date_four.clicked.connect(animate_date_four)

    animate_date_five = partial(get_date, map_canvas, date_time_five)
    date_five.clicked.connect(animate_date_five)

    animate_date_six = partial(get_date, map_canvas, date_time_six)
    date_six.clicked.connect(animate_date_six)


    dates = [
        date_time_one,
        date_time_two,
        date_time_three,
        date_time_four,
        date_time_five,
        date_time_six
    ]

    slider = QgsSlider(Qt.Orientation.Horizontal, main_window)
    value_changed = partial(slider_value_changed, map_canvas, dates)
    slider.valueChanged.connect(value_changed)
    slider.setMinimum(0)
    slider.setMaximum(5)
    slider.setSingleStep(1)
    slider.setTickPosition(QgsSlider.TickPosition.TicksBothSides)
    slider.setTracking(True)

    h_layout = QHBoxLayout(frame)
    h_layout.addWidget(date_one)
    h_layout.addWidget(date_two)
    h_layout.addWidget(date_three)
    h_layout.addWidget(date_four)
    h_layout.addWidget(date_five)
    h_layout.addWidget(date_six)

    layout.addLayout(h_layout, 1, 0)
    layout.addWidget(slider)


def run():
    """ Main application function """
    application = QgsApplication([], False)

    # The prefix path varies depending on the method of installation
    # used to install QGIS and the OS in use.
    # If conda package manager was used to install QGIS then the
    # prefix path should be location of the qgis package.
    # Otherwise the prefix path should be the location of where
    # QGIS application has been installed.
    QgsApplication.setPrefixPath('/usr', True)
    QgsApplication.initQgis()

    main_window = QMainWindow()
    main_window.setWindowTitle(
        "Python with QGIS animation example | "
        "Django US 2024"
    )
    frame = QFrame()
    main_window.setCentralWidget(frame)
    layout = QGridLayout(frame)

    map_canvas = QgsMapCanvas()
    layout.addWidget(map_canvas)


    # Initiliazing a QGIS raster layer from that is served via WMS,
    # the raster layer uri is required to have a string of parameters and
    # values as found on its capabilities properties.
    #
    raster_layer = QgsRasterLayer(
        'crs=EPSG:4326&dpiMode=7&format=image/png&layers=GDPS.ETA_TT&'
        'referenceTimeDimensionExtent=2024-09-22T00:00:00Z/2024-09-23T00:00:00Z/PT12H&'
        'styles&temporalSource=provider&'
        'timeDimensionExtent=2024-09-23T00:00:00Z/2024-10-03T00:00:00Z/PT3H&'
        'type=wmst&url=https://geo.weather.gc.ca/geomet?layers%3DGDPS.ETA_TT',
        'air',
        'wms'
    )

    QgsProject.instance().addMapLayer(raster_layer)

    map_canvas.setLayers([raster_layer])
    map_canvas.setExtent(raster_layer.extent())

    set_date_widgets(
        map_canvas,
        main_window,
        frame,
        layout
    )

    main_window.show()
    application.exec_()


run()
