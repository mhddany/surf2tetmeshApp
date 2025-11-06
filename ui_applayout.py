# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applayout.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1280, 800)
        Widget.setStyleSheet(u"background-color: #ffffff;\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_widget = QWidget(Widget)
        self.top_widget.setObjectName(u"top_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_widget.sizePolicy().hasHeightForWidth())
        self.top_widget.setSizePolicy(sizePolicy)
        self.top_widget.setMinimumSize(QSize(0, 60))
        self.top_widget.setStyleSheet(u"background-color: #ffffff;   \n"
"border-bottom: 1px solid #d3d3d3;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.top_widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.appNameLabel = QLabel(self.top_widget)
        self.appNameLabel.setObjectName(u"appNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(6)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.appNameLabel.sizePolicy().hasHeightForWidth())
        self.appNameLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"AlwynNewRounded-Regular"])
        font.setPointSize(14)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.appNameLabel)

        self.selectFileButton = QPushButton(self.top_widget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.selectFileButton.sizePolicy().hasHeightForWidth())
        self.selectFileButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"AlwynNewRounded-Regular"])
        font1.setBold(True)
        self.selectFileButton.setFont(font1)
        self.selectFileButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #648047;   /* Green */\n"
"    color: white;                /* White text */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 5px 10px;           /* Nice spacing */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #475932;   /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #303d22;   /* Even darker when pressed */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.selectFileButton)

        self.generateMeshButton = QPushButton(self.top_widget)
        self.generateMeshButton.setObjectName(u"generateMeshButton")
        sizePolicy2.setHeightForWidth(self.generateMeshButton.sizePolicy().hasHeightForWidth())
        self.generateMeshButton.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Leelawadee UI"])
        font2.setBold(True)
        self.generateMeshButton.setFont(font2)
        self.generateMeshButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #648047;   /* Green */\n"
"    color: white;                /* White text */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 5px 10px;           /* Nice spacing */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #475932;   /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #303d22;   /* Even darker when pressed */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.generateMeshButton)

        self.saveMeshButton = QPushButton(self.top_widget)
        self.saveMeshButton.setObjectName(u"saveMeshButton")
        sizePolicy2.setHeightForWidth(self.saveMeshButton.sizePolicy().hasHeightForWidth())
        self.saveMeshButton.setSizePolicy(sizePolicy2)
        self.saveMeshButton.setFont(font2)
        self.saveMeshButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #648047;   /* Green */\n"
"    color: white;                /* White text */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 5px 10px;           /* Nice spacing */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #475932;   /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #303d22;   /* Even darker when pressed */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.saveMeshButton)


        self.verticalLayout.addWidget(self.top_widget)

        self.bottom_widget = QWidget(Widget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.viewer_surface_widget = QWidget(self.bottom_widget)
        self.viewer_surface_widget.setObjectName(u"viewer_surface_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(4)
        sizePolicy3.setHeightForWidth(self.viewer_surface_widget.sizePolicy().hasHeightForWidth())
        self.viewer_surface_widget.setSizePolicy(sizePolicy3)
        self.viewer_surface_widget.setStyleSheet(u"background-color: #E0F2CE;\n"
"border-radius: 15px;")
        self.verticalLayout_2 = QVBoxLayout(self.viewer_surface_widget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, -1)
        self.surfaceMeshLabel = QLabel(self.viewer_surface_widget)
        self.surfaceMeshLabel.setObjectName(u"surfaceMeshLabel")
        font3 = QFont()
        font3.setFamilies([u"Alwyn"])
        font3.setPointSize(11)
        self.surfaceMeshLabel.setFont(font3)
        self.surfaceMeshLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_2.addWidget(self.surfaceMeshLabel)

        self.stlView = QVTKRenderWindowInteractor(self.viewer_surface_widget)
        self.stlView.setObjectName(u"stlView")
        self.stlView.setStyleSheet(u"QVTKRenderWindowInteractor {\n"
"    background-color: #D3D3D3;  \n"
"    border: 3px solid #121212;  /* Light gray border */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.stlView)

        self.stlFileNameLabel = QLabel(self.viewer_surface_widget)
        self.stlFileNameLabel.setObjectName(u"stlFileNameLabel")
        font4 = QFont()
        font4.setFamilies([u"AlwynNewRounded-Regular"])
        font4.setPointSize(10)
        self.stlFileNameLabel.setFont(font4)
        self.stlFileNameLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_2.addWidget(self.stlFileNameLabel)

        self.stlPointsLabel = QLabel(self.viewer_surface_widget)
        self.stlPointsLabel.setObjectName(u"stlPointsLabel")
        self.stlPointsLabel.setFont(font4)
        self.stlPointsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_2.addWidget(self.stlPointsLabel)

        self.stlVerticesLabel = QLabel(self.viewer_surface_widget)
        self.stlVerticesLabel.setObjectName(u"stlVerticesLabel")
        self.stlVerticesLabel.setFont(font4)
        self.stlVerticesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_2.addWidget(self.stlVerticesLabel)


        self.horizontalLayout_2.addWidget(self.viewer_surface_widget)

        self.viewer_tetra_widget = QWidget(self.bottom_widget)
        self.viewer_tetra_widget.setObjectName(u"viewer_tetra_widget")
        sizePolicy3.setHeightForWidth(self.viewer_tetra_widget.sizePolicy().hasHeightForWidth())
        self.viewer_tetra_widget.setSizePolicy(sizePolicy3)
        self.viewer_tetra_widget.setStyleSheet(u"background-color: #D3D3D3;\n"
"border-radius: 15px;")
        self.verticalLayout_3 = QVBoxLayout(self.viewer_tetra_widget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.tetMeshLabel = QLabel(self.viewer_tetra_widget)
        self.tetMeshLabel.setObjectName(u"tetMeshLabel")
        self.tetMeshLabel.setFont(font3)
        self.tetMeshLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_3.addWidget(self.tetMeshLabel)

        self.tetView = QVTKRenderWindowInteractor(self.viewer_tetra_widget)
        self.tetView.setObjectName(u"tetView")
        self.tetView.setStyleSheet(u"QVTKRenderWindowInteractor {\n"
"    background-color: #D3D3D3;  \n"
"    border: 1px solid #121212;  /* Light gray border */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.tetView)

        self.tetNodesLabel = QLabel(self.viewer_tetra_widget)
        self.tetNodesLabel.setObjectName(u"tetNodesLabel")
        self.tetNodesLabel.setFont(font4)
        self.tetNodesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_3.addWidget(self.tetNodesLabel)

        self.tetEdgesLabel = QLabel(self.viewer_tetra_widget)
        self.tetEdgesLabel.setObjectName(u"tetEdgesLabel")
        self.tetEdgesLabel.setFont(font4)
        self.tetEdgesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_3.addWidget(self.tetEdgesLabel)

        self.tetElementsLabel = QLabel(self.viewer_tetra_widget)
        self.tetElementsLabel.setObjectName(u"tetElementsLabel")
        self.tetElementsLabel.setFont(font4)
        self.tetElementsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_3.addWidget(self.tetElementsLabel)


        self.horizontalLayout_2.addWidget(self.viewer_tetra_widget)

        self.settings_widget = QWidget(self.bottom_widget)
        self.settings_widget.setObjectName(u"settings_widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(4)
        sizePolicy4.setHeightForWidth(self.settings_widget.sizePolicy().hasHeightForWidth())
        self.settings_widget.setSizePolicy(sizePolicy4)
        self.verticalLayout_4 = QVBoxLayout(self.settings_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.rightScrollArea = QScrollArea(self.settings_widget)
        self.rightScrollArea.setObjectName(u"rightScrollArea")
        self.rightScrollArea.setStyleSheet(u"/* === VERTICAL SCROLLBAR === */\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: #ffffff;\n"
"	width: 14px;\n"
"	margin: 10px 0 10px 0;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"/* Handle (draggable bar) */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: #d3d3d3;\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {	\n"
"	background-color: #E0F2CE;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #d2e3c1;\n"
"}\n"
"\n"
"/* Top button */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: #d3d3d3;\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: #E0F2CE;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: #d2e3c1;\n"
"}\n"
"\n"
"/* Bottom button */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	ba"
                        "ckground-color: #d3d3d3;\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: #E0F2CE;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: #d2e3c1;\n"
"}\n"
"\n"
"/* Remove default arrows and pages */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"/* === HORIZONTAL SCROLLBAR === */\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #ffffff;\n"
"	height: 14px;\n"
"	margin: 0 15px 0 15px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"/* Handle (draggable bar) */\n"
"QScrollBar::handle:horizontal {	\n"
"	background-color: #d3d3d3;\n"
"	min-width: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {	\n"
"	background-color: #E0F2CE;"
                        "\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: #d2e3c1;\n"
"}\n"
"\n"
"/* Left button */\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"	background-color: #d3d3d3;\n"
"	width: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {	\n"
"	background-color: #E0F2CE;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {	\n"
"	background-color: #d2e3c1;\n"
"}\n"
"\n"
"/* Right button */\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"	background-color: #d3d3d3;\n"
"	width: 15px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {	\n"
"	background-color: #E0F2CE;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {	\n"
"	background-color: #d2e3c1;\n"
"}\n"
"\n"
"/* Remove default arrows and pages *"
                        "/\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"	background: none;\n"
"}\n"
"")
        self.rightScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 226, 874))
        self.horizontalLayout_3 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.display_setting_groupbox = QGroupBox(self.widget)
        self.display_setting_groupbox.setObjectName(u"display_setting_groupbox")
        font5 = QFont()
        font5.setFamilies([u"AlwynNewRounded-Regular"])
        self.display_setting_groupbox.setFont(font5)
        self.display_setting_groupbox.setStyleSheet(u"QGroupBox {\n"
"    color: black;        /* text color */\n"
"    font-size: 15px;     /* font size */\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.display_setting_groupbox)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 10, 5, 10)
        self.cameraViewLabel = QLabel(self.display_setting_groupbox)
        self.cameraViewLabel.setObjectName(u"cameraViewLabel")
        self.cameraViewLabel.setFont(font4)
        self.cameraViewLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft| AlignVCenter';\n"
"}")

        self.verticalLayout_6.addWidget(self.cameraViewLabel)

        self.cameraViewComboBox = QComboBox(self.display_setting_groupbox)
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.setObjectName(u"cameraViewComboBox")
        self.cameraViewComboBox.setFont(font5)
        self.cameraViewComboBox.setStyleSheet(u"/* === Base ComboBox Appearance === */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;     /* White background */\n"
"    color: #000000;                /* Black text */\n"
"    border: 1px solid #A0A0A0;    /* Thin gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"    padding: 2px 6px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* === Hover and Focus States === */\n"
"QComboBox:hover {\n"
"    border: 1px solid #648047;     /* Blue highlight when hovered */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #648047;     /* Darker blue when focused */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* === Drop-down Arrow Area === */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0; /* Divider line */\n"
"    background-color: #F5F5F5;      /* Slight gray background */\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
""
                        "/* === Drop-down Arrow Icon (keep default) === */\n"
"QComboBox::down-arrow {\n"
"    image: none; /* Use system default arrow */\n"
"}\n"
"\n"
"/* === Popup List (the dropdown menu) === */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #E0F2CE;    /* White background for dropdown list */\n"
"    color: #000000;               /* Black text */\n"
"    border: 1px solid #A0A0A0;   /* Thin border around dropdown */\n"
"    selection-background-color: #D0E7FF; /* Light blue highlight */\n"
"    selection-color: #000000;     /* Black text when selected */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.cameraViewComboBox)

        self.cameraViewlExpLabel = QLabel(self.display_setting_groupbox)
        self.cameraViewlExpLabel.setObjectName(u"cameraViewlExpLabel")
        font6 = QFont()
        font6.setFamilies([u"AlwynNewRounded-Regular"])
        font6.setPointSize(8)
        self.cameraViewlExpLabel.setFont(font6)
        self.cameraViewlExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.cameraViewlExpLabel.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.cameraViewlExpLabel)

        self.normalsLengthLabel = QLabel(self.display_setting_groupbox)
        self.normalsLengthLabel.setObjectName(u"normalsLengthLabel")
        self.normalsLengthLabel.setFont(font4)
        self.normalsLengthLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_6.addWidget(self.normalsLengthLabel)

        self.normalsLengthLabelSpinBox = QDoubleSpinBox(self.display_setting_groupbox)
        self.normalsLengthLabelSpinBox.setObjectName(u"normalsLengthLabelSpinBox")
        self.normalsLengthLabelSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #FFFFFF;   /* White background */\n"
"    color: #000000;              /* Black text */\n"
"    border: 1px solid #A0A0A0;  /* Thin gray border */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 2px 6px;            /* Space inside box */\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* Optional: style the up/down arrows */\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;   /* up button */\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0;\n"
"    border-radius: 0;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-position: bottom right; /* down button */\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.normalsLengthLabelSpinBox)

        self.normalsLengthExpLabel = QLabel(self.display_setting_groupbox)
        self.normalsLengthExpLabel.setObjectName(u"normalsLengthExpLabel")
        self.normalsLengthExpLabel.setFont(font6)
        self.normalsLengthExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.normalsLengthExpLabel.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.normalsLengthExpLabel)

        self.viewModeLabel = QLabel(self.display_setting_groupbox)
        self.viewModeLabel.setObjectName(u"viewModeLabel")
        self.viewModeLabel.setFont(font4)
        self.viewModeLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft| AlignVCenter';\n"
"}")

        self.verticalLayout_6.addWidget(self.viewModeLabel)

        self.viewModeComboBox = QComboBox(self.display_setting_groupbox)
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.setObjectName(u"viewModeComboBox")
        self.viewModeComboBox.setFont(font5)
        self.viewModeComboBox.setStyleSheet(u"/* === Base ComboBox Appearance === */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;     /* White background */\n"
"    color: #000000;                /* Black text */\n"
"    border: 1px solid #A0A0A0;    /* Thin gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"    padding: 2px 6px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* === Hover and Focus States === */\n"
"QComboBox:hover {\n"
"    border: 1px solid #648047;     /* Blue highlight when hovered */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #648047;     /* Darker blue when focused */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* === Drop-down Arrow Area === */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0; /* Divider line */\n"
"    background-color: #F5F5F5;      /* Slight gray background */\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
""
                        "/* === Drop-down Arrow Icon (keep default) === */\n"
"QComboBox::down-arrow {\n"
"    image: none; /* Use system default arrow */\n"
"}\n"
"\n"
"/* === Popup List (the dropdown menu) === */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #E0F2CE;    /* White background for dropdown list */\n"
"    color: #000000;               /* Black text */\n"
"    border: 1px solid #A0A0A0;   /* Thin border around dropdown */\n"
"    selection-background-color: #D0E7FF; /* Light blue highlight */\n"
"    selection-color: #000000;     /* Black text when selected */\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.viewModeComboBox)

        self.viewModelExpLabel = QLabel(self.display_setting_groupbox)
        self.viewModelExpLabel.setObjectName(u"viewModelExpLabel")
        self.viewModelExpLabel.setFont(font6)
        self.viewModelExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.viewModelExpLabel.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.viewModelExpLabel)

        self.line = QFrame(self.display_setting_groupbox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)


        self.verticalLayout_5.addWidget(self.display_setting_groupbox)

        self.tetgen_setting_groupbox = QGroupBox(self.widget)
        self.tetgen_setting_groupbox.setObjectName(u"tetgen_setting_groupbox")
        self.tetgen_setting_groupbox.setFont(font5)
        self.tetgen_setting_groupbox.setStyleSheet(u"QGroupBox {\n"
"    color: black;        /* text color */\n"
"    font-size: 15px;     /* font size */\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.tetgen_setting_groupbox)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 10, 5, 10)
        self.elementOrderLabel = QLabel(self.tetgen_setting_groupbox)
        self.elementOrderLabel.setObjectName(u"elementOrderLabel")
        self.elementOrderLabel.setFont(font4)
        self.elementOrderLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_7.addWidget(self.elementOrderLabel)

        self.orderComboBox = QComboBox(self.tetgen_setting_groupbox)
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.setObjectName(u"orderComboBox")
        self.orderComboBox.setFont(font5)
        self.orderComboBox.setStyleSheet(u"/* === Base ComboBox Appearance === */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;     /* White background */\n"
"    color: #000000;                /* Black text */\n"
"    border: 1px solid #A0A0A0;    /* Thin gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"    padding: 2px 6px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* === Hover and Focus States === */\n"
"QComboBox:hover {\n"
"    border: 1px solid #648047;     /* Blue highlight when hovered */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #648047;     /* Darker blue when focused */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* === Drop-down Arrow Area === */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0; /* Divider line */\n"
"    background-color: #F5F5F5;      /* Slight gray background */\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
""
                        "/* === Drop-down Arrow Icon (keep default) === */\n"
"QComboBox::down-arrow {\n"
"    image: none; /* Use system default arrow */\n"
"}\n"
"\n"
"/* === Popup List (the dropdown menu) === */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #E0F2CE;    /* White background for dropdown list */\n"
"    color: #000000;               /* Black text */\n"
"    border: 1px solid #A0A0A0;   /* Thin border around dropdown */\n"
"    selection-background-color: #D0E7FF; /* Light blue highlight */\n"
"    selection-color: #000000;     /* Black text when selected */\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.orderComboBox)

        self.elementOrdereExpLabel = QLabel(self.tetgen_setting_groupbox)
        self.elementOrdereExpLabel.setObjectName(u"elementOrdereExpLabel")
        self.elementOrdereExpLabel.setFont(font6)
        self.elementOrdereExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.elementOrdereExpLabel.setMidLineWidth(0)
        self.elementOrdereExpLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.elementOrdereExpLabel)

        self.mindihedralangleLabel = QLabel(self.tetgen_setting_groupbox)
        self.mindihedralangleLabel.setObjectName(u"mindihedralangleLabel")
        self.mindihedralangleLabel.setFont(font4)
        self.mindihedralangleLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_7.addWidget(self.mindihedralangleLabel)

        self.mindihedralSpinBox = QSpinBox(self.tetgen_setting_groupbox)
        self.mindihedralSpinBox.setObjectName(u"mindihedralSpinBox")
        self.mindihedralSpinBox.setStyleSheet(u"QSpinBox {\n"
"    background-color: #FFFFFF;   /* White background */\n"
"    color: #000000;              /* Black text */\n"
"    border: 1px solid #A0A0A0;  /* Thin gray border */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 2px 6px;            /* Space inside box */\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* Optional: style the up/down arrows */\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;   /* up button */\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0;\n"
"    border-radius: 0;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    subcontrol-position: bottom right; /* down button */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.mindihedralSpinBox)

        self.mindihedralangleExpLabel = QLabel(self.tetgen_setting_groupbox)
        self.mindihedralangleExpLabel.setObjectName(u"mindihedralangleExpLabel")
        self.mindihedralangleExpLabel.setFont(font6)
        self.mindihedralangleExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.mindihedralangleExpLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.mindihedralangleExpLabel)

        self.minRatioLabel = QLabel(self.tetgen_setting_groupbox)
        self.minRatioLabel.setObjectName(u"minRatioLabel")
        self.minRatioLabel.setFont(font4)
        self.minRatioLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_7.addWidget(self.minRatioLabel)

        self.minRatioDoubleSpinBox = QDoubleSpinBox(self.tetgen_setting_groupbox)
        self.minRatioDoubleSpinBox.setObjectName(u"minRatioDoubleSpinBox")
        self.minRatioDoubleSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #FFFFFF;   /* White background */\n"
"    color: #000000;              /* Black text */\n"
"    border: 1px solid #A0A0A0;  /* Thin gray border */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 2px 6px;            /* Space inside box */\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* Optional: style the up/down arrows */\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;   /* up button */\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0;\n"
"    border-radius: 0;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-position: bottom right; /* down button */\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.minRatioDoubleSpinBox)

        self.minRatioExpLabel = QLabel(self.tetgen_setting_groupbox)
        self.minRatioExpLabel.setObjectName(u"minRatioExpLabel")
        self.minRatioExpLabel.setFont(font6)
        self.minRatioExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.minRatioExpLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.minRatioExpLabel)

        self.maxVolumeLabel = QLabel(self.tetgen_setting_groupbox)
        self.maxVolumeLabel.setObjectName(u"maxVolumeLabel")
        self.maxVolumeLabel.setFont(font4)
        self.maxVolumeLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")

        self.verticalLayout_7.addWidget(self.maxVolumeLabel)

        self.maxVolumeDoubleSpinBox = QDoubleSpinBox(self.tetgen_setting_groupbox)
        self.maxVolumeDoubleSpinBox.setObjectName(u"maxVolumeDoubleSpinBox")
        self.maxVolumeDoubleSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"    background-color: #FFFFFF;   /* White background */\n"
"    color: #000000;              /* Black text */\n"
"    border: 1px solid #A0A0A0;  /* Thin gray border */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 2px 6px;            /* Space inside box */\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* Optional: style the up/down arrows */\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;   /* up button */\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0;\n"
"    border-radius: 0;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-position: bottom right; /* down button */\n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow, QDoubleSpinBox::down-arrow {\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.maxVolumeDoubleSpinBox)

        self.maxVolumeExpLabel = QLabel(self.tetgen_setting_groupbox)
        self.maxVolumeExpLabel.setObjectName(u"maxVolumeExpLabel")
        self.maxVolumeExpLabel.setFont(font6)
        self.maxVolumeExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.maxVolumeExpLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.maxVolumeExpLabel)

        self.verboseCheckBox = QCheckBox(self.tetgen_setting_groupbox)
        self.verboseCheckBox.setObjectName(u"verboseCheckBox")
        self.verboseCheckBox.setFont(font4)
        self.verboseCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color: #000000;                /* Text color */\n"
"    spacing: 8px;                  /* Space between box and label */\n"
"	border: 0px solid #A0A0A0;    \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;                   /* Box width */\n"
"    height: 16px;                  /* Box height */\n"
"    border: 1px solid #A0A0A0;    /* Thin gray border */\n"
"    border-radius: 2px;            /* Rounded corners */\n"
"    background-color: #FFFFFF;     /* White background */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #648047;     /* Green when checked */\n"
"    border: 1px solid #648047;\n"
"}\n"
"")
        self.verboseCheckBox.setChecked(True)

        self.verticalLayout_7.addWidget(self.verboseCheckBox)

        self.verboseExpLabel = QLabel(self.tetgen_setting_groupbox)
        self.verboseExpLabel.setObjectName(u"verboseExpLabel")
        self.verboseExpLabel.setFont(font6)
        self.verboseExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.verboseExpLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.verboseExpLabel)

        self.preserveSurfaceCheckBox = QCheckBox(self.tetgen_setting_groupbox)
        self.preserveSurfaceCheckBox.setObjectName(u"preserveSurfaceCheckBox")
        self.preserveSurfaceCheckBox.setFont(font4)
        self.preserveSurfaceCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color: #000000;                /* Text color */\n"
"    spacing: 8px;                  /* Space between box and label */\n"
"	border: 0px solid #A0A0A0;    \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 16px;                   /* Box width */\n"
"    height: 16px;                  /* Box height */\n"
"    border: 1px solid #A0A0A0;    /* Thin gray border */\n"
"    border-radius: 2px;            /* Rounded corners */\n"
"    background-color: #FFFFFF;     /* White background */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #648047;     /* Green when checked */\n"
"    border: 1px solid #648047;\n"
"}\n"
"")
        self.preserveSurfaceCheckBox.setChecked(True)

        self.verticalLayout_7.addWidget(self.preserveSurfaceCheckBox)

        self.preserveSurfaceExpLabel = QLabel(self.tetgen_setting_groupbox)
        self.preserveSurfaceExpLabel.setObjectName(u"preserveSurfaceExpLabel")
        self.preserveSurfaceExpLabel.setFont(font6)
        self.preserveSurfaceExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignTop';\n"
"}")
        self.preserveSurfaceExpLabel.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.preserveSurfaceExpLabel)


        self.verticalLayout_5.addWidget(self.tetgen_setting_groupbox)


        self.horizontalLayout_3.addWidget(self.widget)

        self.rightScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.rightScrollArea)


        self.horizontalLayout_2.addWidget(self.settings_widget)


        self.verticalLayout.addWidget(self.bottom_widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.appNameLabel.setText(QCoreApplication.translate("Widget", u" Surf2Tetmesh", None))
        self.selectFileButton.setText(QCoreApplication.translate("Widget", u"Load File", None))
        self.generateMeshButton.setText(QCoreApplication.translate("Widget", u"Generate Mesh", None))
        self.saveMeshButton.setText(QCoreApplication.translate("Widget", u"Save File", None))
        self.surfaceMeshLabel.setText(QCoreApplication.translate("Widget", u"Surface Mesh", None))
        self.stlFileNameLabel.setText(QCoreApplication.translate("Widget", u"File Name: ", None))
        self.stlPointsLabel.setText(QCoreApplication.translate("Widget", u"Points: ", None))
        self.stlVerticesLabel.setText(QCoreApplication.translate("Widget", u"vertices: ", None))
        self.tetMeshLabel.setText(QCoreApplication.translate("Widget", u"Tetrahedral Mesh", None))
        self.tetNodesLabel.setText(QCoreApplication.translate("Widget", u"Nodes:", None))
        self.tetEdgesLabel.setText(QCoreApplication.translate("Widget", u"Edges:", None))
        self.tetElementsLabel.setText(QCoreApplication.translate("Widget", u"Elements: ", None))
        self.display_setting_groupbox.setTitle(QCoreApplication.translate("Widget", u"Display Settings", None))
        self.cameraViewLabel.setText(QCoreApplication.translate("Widget", u"Perspective", None))
        self.cameraViewComboBox.setItemText(0, QCoreApplication.translate("Widget", u"3D", None))
        self.cameraViewComboBox.setItemText(1, QCoreApplication.translate("Widget", u"X", None))
        self.cameraViewComboBox.setItemText(2, QCoreApplication.translate("Widget", u"Y", None))
        self.cameraViewComboBox.setItemText(3, QCoreApplication.translate("Widget", u"Z", None))

        self.cameraViewlExpLabel.setText(QCoreApplication.translate("Widget", u"Choose the view angle", None))
        self.normalsLengthLabel.setText(QCoreApplication.translate("Widget", u"Normals length", None))
        self.normalsLengthExpLabel.setText(QCoreApplication.translate("Widget", u"Adjust the length of surface normals; set to 0 to hide them.", None))
        self.viewModeLabel.setText(QCoreApplication.translate("Widget", u"View Mode", None))
        self.viewModeComboBox.setItemText(0, QCoreApplication.translate("Widget", u"Surface", None))
        self.viewModeComboBox.setItemText(1, QCoreApplication.translate("Widget", u"Surface + Edges", None))
        self.viewModeComboBox.setItemText(2, QCoreApplication.translate("Widget", u"Wireframe", None))
        self.viewModeComboBox.setItemText(3, QCoreApplication.translate("Widget", u"Points", None))

        self.viewModelExpLabel.setText(QCoreApplication.translate("Widget", u"Select how the mesh is displayed", None))
        self.tetgen_setting_groupbox.setTitle(QCoreApplication.translate("Widget", u"Meshing Settings", None))
        self.elementOrderLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.orderComboBox.setItemText(0, QCoreApplication.translate("Widget", u"1. Linear", None))
        self.orderComboBox.setItemText(1, QCoreApplication.translate("Widget", u"2. Quadratic", None))

        self.elementOrdereExpLabel.setText(QCoreApplication.translate("Widget", u"Choose 1 for linear tetrahedra or 2 for quadratic tetrahedra.", None))
        self.mindihedralangleLabel.setText(QCoreApplication.translate("Widget", u"Min Dihedral Angle", None))
        self.mindihedralangleExpLabel.setText(QCoreApplication.translate("Widget", u"Minimum allowed angle between tetrahedron faces (\u00b0). ", None))
        self.minRatioLabel.setText(QCoreApplication.translate("Widget", u"Min Ratio", None))
        self.minRatioExpLabel.setText(QCoreApplication.translate("Widget", u"Minimum quality ratio of tetrahedra; higher values improve mesh quality.", None))
        self.maxVolumeLabel.setText(QCoreApplication.translate("Widget", u"Max Volume", None))
        self.maxVolumeExpLabel.setText(QCoreApplication.translate("Widget", u"Maximum volume of each tetrahedron; smaller values create finer meshes.", None))
        self.verboseCheckBox.setText(QCoreApplication.translate("Widget", u"Verbose", None))
        self.verboseExpLabel.setText(QCoreApplication.translate("Widget", u"Show detailed output of mesh generation.", None))
        self.preserveSurfaceCheckBox.setText(QCoreApplication.translate("Widget", u"Preserve Surface Feature", None))
        self.preserveSurfaceExpLabel.setText(QCoreApplication.translate("Widget", u"Keep sharp edges and corners from the input surface.", None))
    # retranslateUi

