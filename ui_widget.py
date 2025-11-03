# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QDoubleSpinBox, QFrame, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1296, 897)
        Widget.setMinimumSize(QSize(1280, 800))
        font = QFont()
        font.setFamilies([u"AlwynNewRounded-Regular"])
        font.setBold(False)
        Widget.setFont(font)
        Widget.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #d0d0d0;\n"
"}")
        self.selectFileButton = QPushButton(Widget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(820, 15, 130, 30))
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
"    background-color: #218838;   /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34;   /* Even darker when pressed */\n"
"}\n"
"")
        self.generateMeshButton = QPushButton(Widget)
        self.generateMeshButton.setObjectName(u"generateMeshButton")
        self.generateMeshButton.setGeometry(QRect(980, 15, 135, 30))
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
"    background-color: #218838;   /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34;   /* Even darker when pressed */\n"
"}\n"
"")
        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 55, 1241, 1))
        self.line.setStyleSheet(u"Line {\n"
"    background-color: #D3D3D3;  \n"
"    max-height: 1px;             /* Thickness of the line */\n"
"    border: none;                /* Remove default frame border */\n"
"}\n"
"")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.saveMeshButton = QPushButton(Widget)
        self.saveMeshButton.setObjectName(u"saveMeshButton")
        self.saveMeshButton.setGeometry(QRect(1130, 15, 130, 30))
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
"    background-color: #218838;   /* Darker green on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e7e34;   /* Even darker when pressed */\n"
"}\n"
"")
        self.frameTet = QFrame(Widget)
        self.frameTet.setObjectName(u"frameTet")
        self.frameTet.setGeometry(QRect(540, 80, 460, 621))
        self.frameTet.setStyleSheet(u"QFrame {\n"
"    background-color: #D3D3D3;\n"
"    border: 1px solid #d0d0d0;  /* Light gray border */\n"
"	border-radius: 15px;  \n"
"}\n"
"")
        self.frameTet.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTet.setFrameShadow(QFrame.Shadow.Raised)
        self.tetView = QVTKRenderWindowInteractor(self.frameTet)
        self.tetView.setObjectName(u"tetView")
        self.tetView.setGeometry(QRect(40, 40, 390, 450))
        self.tetView.setStyleSheet(u"QVTKRenderWindowInteractor {\n"
"    background-color: #D3D3D3;  \n"
"    border: 1px solid #121212;  /* Light gray border */\n"
"}\n"
"")
        self.tetMeshLabel = QLabel(self.frameTet)
        self.tetMeshLabel.setObjectName(u"tetMeshLabel")
        self.tetMeshLabel.setGeometry(QRect(10, 10, 121, 21))
        font3 = QFont()
        font3.setFamilies([u"Alwyn"])
        font3.setPointSize(11)
        self.tetMeshLabel.setFont(font3)
        self.tetMeshLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.tetNodesLabel = QLabel(self.frameTet)
        self.tetNodesLabel.setObjectName(u"tetNodesLabel")
        self.tetNodesLabel.setGeometry(QRect(10, 550, 121, 21))
        font4 = QFont()
        font4.setFamilies([u"AlwynNewRounded-Regular"])
        font4.setPointSize(10)
        self.tetNodesLabel.setFont(font4)
        self.tetNodesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.tetEdgesLabel = QLabel(self.frameTet)
        self.tetEdgesLabel.setObjectName(u"tetEdgesLabel")
        self.tetEdgesLabel.setGeometry(QRect(10, 565, 121, 21))
        self.tetEdgesLabel.setFont(font4)
        self.tetEdgesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.tetElementsLabel = QLabel(self.frameTet)
        self.tetElementsLabel.setObjectName(u"tetElementsLabel")
        self.tetElementsLabel.setGeometry(QRect(10, 580, 121, 21))
        self.tetElementsLabel.setFont(font4)
        self.tetElementsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.frameStl = QFrame(Widget)
        self.frameStl.setObjectName(u"frameStl")
        self.frameStl.setGeometry(QRect(40, 80, 460, 621))
        self.frameStl.setStyleSheet(u"QFrame {\n"
"    background-color: #E0F2CE;\n"
"    border: 1px solid #E0F2CE;  /* Light gray border */\n"
"	border-radius: 15px;  \n"
"}\n"
"")
        self.frameStl.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameStl.setFrameShadow(QFrame.Shadow.Raised)
        self.stlView = QVTKRenderWindowInteractor(self.frameStl)
        self.stlView.setObjectName(u"stlView")
        self.stlView.setGeometry(QRect(40, 40, 390, 450))
        self.stlView.setStyleSheet(u"QVTKRenderWindowInteractor {\n"
"    background-color: #D3D3D3;  \n"
"    border: 3px solid #121212;  /* Light gray border */\n"
"}\n"
"")
        self.surfaceMeshLabel = QLabel(self.frameStl)
        self.surfaceMeshLabel.setObjectName(u"surfaceMeshLabel")
        self.surfaceMeshLabel.setGeometry(QRect(10, 10, 121, 21))
        self.surfaceMeshLabel.setFont(font3)
        self.surfaceMeshLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.stlFileNameLabel = QLabel(self.frameStl)
        self.stlFileNameLabel.setObjectName(u"stlFileNameLabel")
        self.stlFileNameLabel.setGeometry(QRect(10, 550, 121, 21))
        self.stlFileNameLabel.setFont(font4)
        self.stlFileNameLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.stlPointsLabel = QLabel(self.frameStl)
        self.stlPointsLabel.setObjectName(u"stlPointsLabel")
        self.stlPointsLabel.setGeometry(QRect(10, 565, 121, 21))
        self.stlPointsLabel.setFont(font4)
        self.stlPointsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.stlVerticesLabel = QLabel(self.frameStl)
        self.stlVerticesLabel.setObjectName(u"stlVerticesLabel")
        self.stlVerticesLabel.setGeometry(QRect(10, 580, 121, 21))
        self.stlVerticesLabel.setFont(font4)
        self.stlVerticesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.appNameLabel = QLabel(Widget)
        self.appNameLabel.setObjectName(u"appNameLabel")
        self.appNameLabel.setGeometry(QRect(40, 10, 301, 40))
        font5 = QFont()
        font5.setFamilies([u"AlwynNewRounded-Regular"])
        font5.setPointSize(14)
        self.appNameLabel.setFont(font5)
        self.appNameLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}\n"
"")
        self.meshSettingsLabel = QLabel(Widget)
        self.meshSettingsLabel.setObjectName(u"meshSettingsLabel")
        self.meshSettingsLabel.setGeometry(QRect(1040, 75, 201, 21))
        self.meshSettingsLabel.setFont(font3)
        self.meshSettingsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.orderComboBox = QComboBox(Widget)
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.setObjectName(u"orderComboBox")
        self.orderComboBox.setGeometry(QRect(1040, 135, 210, 24))
        font6 = QFont()
        font6.setFamilies([u"AlwynNewRounded-Regular"])
        self.orderComboBox.setFont(font6)
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
        self.elementOrderLabel = QLabel(Widget)
        self.elementOrderLabel.setObjectName(u"elementOrderLabel")
        self.elementOrderLabel.setGeometry(QRect(1040, 110, 121, 21))
        self.elementOrderLabel.setFont(font4)
        self.elementOrderLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.elementOrdereExpLabel = QLabel(Widget)
        self.elementOrdereExpLabel.setObjectName(u"elementOrdereExpLabel")
        self.elementOrdereExpLabel.setGeometry(QRect(1040, 160, 121, 21))
        font7 = QFont()
        font7.setFamilies([u"AlwynNewRounded-Regular"])
        font7.setPointSize(8)
        self.elementOrdereExpLabel.setFont(font7)
        self.elementOrdereExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.mindihedralangleLabel = QLabel(Widget)
        self.mindihedralangleLabel.setObjectName(u"mindihedralangleLabel")
        self.mindihedralangleLabel.setGeometry(QRect(1040, 200, 121, 21))
        self.mindihedralangleLabel.setFont(font4)
        self.mindihedralangleLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.mindihedralSpinBox = QSpinBox(Widget)
        self.mindihedralSpinBox.setObjectName(u"mindihedralSpinBox")
        self.mindihedralSpinBox.setGeometry(QRect(1040, 225, 210, 24))
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
        self.mindihedralangleExpLabel = QLabel(Widget)
        self.mindihedralangleExpLabel.setObjectName(u"mindihedralangleExpLabel")
        self.mindihedralangleExpLabel.setGeometry(QRect(1040, 250, 121, 21))
        self.mindihedralangleExpLabel.setFont(font7)
        self.mindihedralangleExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.minRatioDoubleSpinBox = QDoubleSpinBox(Widget)
        self.minRatioDoubleSpinBox.setObjectName(u"minRatioDoubleSpinBox")
        self.minRatioDoubleSpinBox.setGeometry(QRect(1040, 315, 210, 24))
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
        self.minRatioLabel = QLabel(Widget)
        self.minRatioLabel.setObjectName(u"minRatioLabel")
        self.minRatioLabel.setGeometry(QRect(1040, 290, 121, 21))
        self.minRatioLabel.setFont(font4)
        self.minRatioLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.minRatioExpLabel = QLabel(Widget)
        self.minRatioExpLabel.setObjectName(u"minRatioExpLabel")
        self.minRatioExpLabel.setGeometry(QRect(1040, 340, 121, 21))
        self.minRatioExpLabel.setFont(font7)
        self.minRatioExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.maxVolumeLabel = QLabel(Widget)
        self.maxVolumeLabel.setObjectName(u"maxVolumeLabel")
        self.maxVolumeLabel.setGeometry(QRect(1040, 380, 121, 21))
        self.maxVolumeLabel.setFont(font4)
        self.maxVolumeLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.maxVolumeDoubleSpinBox = QDoubleSpinBox(Widget)
        self.maxVolumeDoubleSpinBox.setObjectName(u"maxVolumeDoubleSpinBox")
        self.maxVolumeDoubleSpinBox.setGeometry(QRect(1040, 405, 210, 24))
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
        self.maxVolumeExpLabel = QLabel(Widget)
        self.maxVolumeExpLabel.setObjectName(u"maxVolumeExpLabel")
        self.maxVolumeExpLabel.setGeometry(QRect(1040, 430, 121, 21))
        self.maxVolumeExpLabel.setFont(font7)
        self.maxVolumeExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.DisplaySettingsLabel = QLabel(Widget)
        self.DisplaySettingsLabel.setObjectName(u"DisplaySettingsLabel")
        self.DisplaySettingsLabel.setGeometry(QRect(1040, 580, 121, 21))
        self.DisplaySettingsLabel.setFont(font3)
        self.DisplaySettingsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.verboseCheckBox = QCheckBox(Widget)
        self.verboseCheckBox.setObjectName(u"verboseCheckBox")
        self.verboseCheckBox.setGeometry(QRect(1040, 460, 181, 20))
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
        self.verboseExpLabel = QLabel(Widget)
        self.verboseExpLabel.setObjectName(u"verboseExpLabel")
        self.verboseExpLabel.setGeometry(QRect(1040, 480, 121, 21))
        self.verboseExpLabel.setFont(font7)
        self.verboseExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.preserveSurfaceCheckBox = QCheckBox(Widget)
        self.preserveSurfaceCheckBox.setObjectName(u"preserveSurfaceCheckBox")
        self.preserveSurfaceCheckBox.setGeometry(QRect(1040, 520, 181, 20))
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
        self.preserveSurfaceExpLabel = QLabel(Widget)
        self.preserveSurfaceExpLabel.setObjectName(u"preserveSurfaceExpLabel")
        self.preserveSurfaceExpLabel.setGeometry(QRect(1040, 540, 121, 21))
        self.preserveSurfaceExpLabel.setFont(font7)
        self.preserveSurfaceExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.cameraViewLabel = QLabel(Widget)
        self.cameraViewLabel.setObjectName(u"cameraViewLabel")
        self.cameraViewLabel.setGeometry(QRect(1040, 610, 121, 21))
        self.cameraViewLabel.setFont(font4)
        self.cameraViewLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft| AlignVCenter';\n"
"}")
        self.cameraViewComboBox = QComboBox(Widget)
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.addItem("")
        self.cameraViewComboBox.setObjectName(u"cameraViewComboBox")
        self.cameraViewComboBox.setGeometry(QRect(1040, 635, 210, 24))
        self.cameraViewComboBox.setFont(font6)
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
        self.cameraViewlExpLabel = QLabel(Widget)
        self.cameraViewlExpLabel.setObjectName(u"cameraViewlExpLabel")
        self.cameraViewlExpLabel.setGeometry(QRect(1040, 660, 121, 21))
        self.cameraViewlExpLabel.setFont(font7)
        self.cameraViewlExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.normalsLengthLabelSpinBox = QDoubleSpinBox(Widget)
        self.normalsLengthLabelSpinBox.setObjectName(u"normalsLengthLabelSpinBox")
        self.normalsLengthLabelSpinBox.setGeometry(QRect(1040, 725, 210, 24))
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
        self.normalsLengthLabel = QLabel(Widget)
        self.normalsLengthLabel.setObjectName(u"normalsLengthLabel")
        self.normalsLengthLabel.setGeometry(QRect(1040, 700, 121, 21))
        self.normalsLengthLabel.setFont(font4)
        self.normalsLengthLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.normalsLengthExpLabel = QLabel(Widget)
        self.normalsLengthExpLabel.setObjectName(u"normalsLengthExpLabel")
        self.normalsLengthExpLabel.setGeometry(QRect(1040, 750, 121, 21))
        self.normalsLengthExpLabel.setFont(font7)
        self.normalsLengthExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.viewModeComboBox = QComboBox(Widget)
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.addItem("")
        self.viewModeComboBox.setObjectName(u"viewModeComboBox")
        self.viewModeComboBox.setGeometry(QRect(1040, 815, 210, 24))
        self.viewModeComboBox.setFont(font6)
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
        self.viewModelExpLabel = QLabel(Widget)
        self.viewModelExpLabel.setObjectName(u"viewModelExpLabel")
        self.viewModelExpLabel.setGeometry(QRect(1040, 840, 121, 21))
        self.viewModelExpLabel.setFont(font7)
        self.viewModelExpLabel.setStyleSheet(u"QLabel {\n"
"    color: #5f5f5f;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.viewModeLabel = QLabel(Widget)
        self.viewModeLabel.setObjectName(u"viewModeLabel")
        self.viewModeLabel.setGeometry(QRect(1040, 790, 121, 21))
        self.viewModeLabel.setFont(font4)
        self.viewModeLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft| AlignVCenter';\n"
"}")
        self.frameTet.raise_()
        self.frameStl.raise_()
        self.selectFileButton.raise_()
        self.generateMeshButton.raise_()
        self.line.raise_()
        self.saveMeshButton.raise_()
        self.appNameLabel.raise_()
        self.meshSettingsLabel.raise_()
        self.orderComboBox.raise_()
        self.elementOrderLabel.raise_()
        self.elementOrdereExpLabel.raise_()
        self.mindihedralangleLabel.raise_()
        self.mindihedralSpinBox.raise_()
        self.mindihedralangleExpLabel.raise_()
        self.minRatioDoubleSpinBox.raise_()
        self.minRatioLabel.raise_()
        self.minRatioExpLabel.raise_()
        self.maxVolumeLabel.raise_()
        self.maxVolumeDoubleSpinBox.raise_()
        self.maxVolumeExpLabel.raise_()
        self.DisplaySettingsLabel.raise_()
        self.verboseCheckBox.raise_()
        self.verboseExpLabel.raise_()
        self.preserveSurfaceCheckBox.raise_()
        self.preserveSurfaceExpLabel.raise_()
        self.cameraViewLabel.raise_()
        self.cameraViewComboBox.raise_()
        self.cameraViewlExpLabel.raise_()
        self.normalsLengthLabelSpinBox.raise_()
        self.normalsLengthLabel.raise_()
        self.normalsLengthExpLabel.raise_()
        self.viewModeComboBox.raise_()
        self.viewModelExpLabel.raise_()
        self.viewModeLabel.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Dialog", None))
        self.selectFileButton.setText(QCoreApplication.translate("Widget", u"Load File", None))
        self.generateMeshButton.setText(QCoreApplication.translate("Widget", u"Generate Mesh", None))
        self.saveMeshButton.setText(QCoreApplication.translate("Widget", u"Save File", None))
        self.tetMeshLabel.setText(QCoreApplication.translate("Widget", u"Tetrahedral Mesh", None))
        self.tetNodesLabel.setText(QCoreApplication.translate("Widget", u"Nodes:", None))
        self.tetEdgesLabel.setText(QCoreApplication.translate("Widget", u"Edges:", None))
        self.tetElementsLabel.setText(QCoreApplication.translate("Widget", u"Elements: ", None))
        self.surfaceMeshLabel.setText(QCoreApplication.translate("Widget", u"Surface Mesh", None))
        self.stlFileNameLabel.setText(QCoreApplication.translate("Widget", u"File Name: ", None))
        self.stlPointsLabel.setText(QCoreApplication.translate("Widget", u"Points: ", None))
        self.stlVerticesLabel.setText(QCoreApplication.translate("Widget", u"vertices: ", None))
        self.appNameLabel.setText(QCoreApplication.translate("Widget", u"Surf2Tetmesh", None))
        self.meshSettingsLabel.setText(QCoreApplication.translate("Widget", u"Mesh Generation Settings", None))
        self.orderComboBox.setItemText(0, QCoreApplication.translate("Widget", u"1. Linear", None))
        self.orderComboBox.setItemText(1, QCoreApplication.translate("Widget", u"2. Quadratic", None))

        self.elementOrderLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.elementOrdereExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.mindihedralangleLabel.setText(QCoreApplication.translate("Widget", u"Min Dihedral Angle", None))
        self.mindihedralangleExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.minRatioLabel.setText(QCoreApplication.translate("Widget", u"Min Ratio", None))
        self.minRatioExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.maxVolumeLabel.setText(QCoreApplication.translate("Widget", u"Max Volume", None))
        self.maxVolumeExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.DisplaySettingsLabel.setText(QCoreApplication.translate("Widget", u"Display Settings", None))
        self.verboseCheckBox.setText(QCoreApplication.translate("Widget", u"Verbose", None))
        self.verboseExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.preserveSurfaceCheckBox.setText(QCoreApplication.translate("Widget", u"Preserve Surface Feature", None))
        self.preserveSurfaceExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.cameraViewLabel.setText(QCoreApplication.translate("Widget", u"Perspective", None))
        self.cameraViewComboBox.setItemText(0, QCoreApplication.translate("Widget", u"3D", None))
        self.cameraViewComboBox.setItemText(1, QCoreApplication.translate("Widget", u"X", None))
        self.cameraViewComboBox.setItemText(2, QCoreApplication.translate("Widget", u"Y", None))
        self.cameraViewComboBox.setItemText(3, QCoreApplication.translate("Widget", u"Z", None))

        self.cameraViewlExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.normalsLengthLabel.setText(QCoreApplication.translate("Widget", u"Normals length", None))
        self.normalsLengthExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.viewModeComboBox.setItemText(0, QCoreApplication.translate("Widget", u"Surface", None))
        self.viewModeComboBox.setItemText(1, QCoreApplication.translate("Widget", u"Surface + Edges", None))
        self.viewModeComboBox.setItemText(2, QCoreApplication.translate("Widget", u"Wireframe", None))
        self.viewModeComboBox.setItemText(3, QCoreApplication.translate("Widget", u"Points", None))

        self.viewModelExpLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.viewModeLabel.setText(QCoreApplication.translate("Widget", u"View Mode", None))
    # retranslateUi

