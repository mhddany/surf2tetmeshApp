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
        Widget.resize(955, 731)
        Widget.setStyleSheet(u"QWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #d0d0d0;\n"
"}")
        self.mindihedralSpinBox = QSpinBox(Widget)
        self.mindihedralSpinBox.setObjectName(u"mindihedralSpinBox")
        self.mindihedralSpinBox.setGeometry(QRect(220, 550, 241, 24))
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
        self.minRatioDoubleSpinBox = QDoubleSpinBox(Widget)
        self.minRatioDoubleSpinBox.setObjectName(u"minRatioDoubleSpinBox")
        self.minRatioDoubleSpinBox.setGeometry(QRect(220, 580, 241, 24))
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
        self.selectFileButton = QPushButton(Widget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(620, 15, 81, 30))
        font = QFont()
        font.setFamilies([u"Leelawadee UI"])
        font.setBold(True)
        self.selectFileButton.setFont(font)
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
        self.generateMeshButton.setGeometry(QRect(720, 15, 121, 30))
        self.generateMeshButton.setFont(font)
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
        self.line.setGeometry(QRect(20, 55, 921, 1))
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
        self.saveMeshButton.setGeometry(QRect(862, 15, 81, 30))
        self.saveMeshButton.setFont(font)
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
        self.frameTet.setGeometry(QRect(520, 80, 420, 400))
        self.frameTet.setStyleSheet(u"QFrame {\n"
"    background-color: #D3D3D3;\n"
"    border: 1px solid #d0d0d0;  /* Light gray border */\n"
"}\n"
"")
        self.frameTet.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTet.setFrameShadow(QFrame.Shadow.Raised)
        self.tetView = QVTKRenderWindowInteractor(self.frameTet)
        self.tetView.setObjectName(u"tetView")
        self.tetView.setGeometry(QRect(20, 40, 381, 281))
        self.tetView.setStyleSheet(u"QVTKRenderWindowInteractor {\n"
"    background-color: #D3D3D3;  \n"
"    border: 1px solid #121212;  /* Light gray border */\n"
"}\n"
"")
        self.tetMeshLabel = QLabel(self.frameTet)
        self.tetMeshLabel.setObjectName(u"tetMeshLabel")
        self.tetMeshLabel.setGeometry(QRect(10, 10, 121, 21))
        font1 = QFont()
        font1.setFamilies([u"Alwyn"])
        font1.setPointSize(11)
        self.tetMeshLabel.setFont(font1)
        self.tetMeshLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.tetNodesLabel = QLabel(self.frameTet)
        self.tetNodesLabel.setObjectName(u"tetNodesLabel")
        self.tetNodesLabel.setGeometry(QRect(10, 330, 121, 21))
        font2 = QFont()
        font2.setFamilies([u"AlwynNewRounded-Regular"])
        font2.setPointSize(10)
        self.tetNodesLabel.setFont(font2)
        self.tetNodesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.tetEdgesLabel = QLabel(self.frameTet)
        self.tetEdgesLabel.setObjectName(u"tetEdgesLabel")
        self.tetEdgesLabel.setGeometry(QRect(10, 345, 121, 21))
        self.tetEdgesLabel.setFont(font2)
        self.tetEdgesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.tetElementsLabel = QLabel(self.frameTet)
        self.tetElementsLabel.setObjectName(u"tetElementsLabel")
        self.tetElementsLabel.setGeometry(QRect(10, 360, 121, 21))
        self.tetElementsLabel.setFont(font2)
        self.tetElementsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.frameStl = QFrame(Widget)
        self.frameStl.setObjectName(u"frameStl")
        self.frameStl.setGeometry(QRect(40, 80, 420, 400))
        self.frameStl.setStyleSheet(u"QFrame {\n"
"    background-color: #E0F2CE;\n"
"    border: 1px solid #d0d0d0;  /* Light gray border */\n"
"}\n"
"")
        self.frameStl.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameStl.setFrameShadow(QFrame.Shadow.Raised)
        self.stlView = QVTKRenderWindowInteractor(self.frameStl)
        self.stlView.setObjectName(u"stlView")
        self.stlView.setGeometry(QRect(20, 40, 381, 281))
        self.stlView.setStyleSheet(u"QVTKRenderWindowInteractor {\n"
"    background-color: #D3D3D3;  \n"
"    border: 3px solid #121212;  /* Light gray border */\n"
"}\n"
"")
        self.surfaceMeshLabel = QLabel(self.frameStl)
        self.surfaceMeshLabel.setObjectName(u"surfaceMeshLabel")
        self.surfaceMeshLabel.setGeometry(QRect(10, 10, 121, 21))
        self.surfaceMeshLabel.setFont(font1)
        self.surfaceMeshLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.stlFileNameLabel = QLabel(self.frameStl)
        self.stlFileNameLabel.setObjectName(u"stlFileNameLabel")
        self.stlFileNameLabel.setGeometry(QRect(10, 330, 121, 21))
        self.stlFileNameLabel.setFont(font2)
        self.stlFileNameLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.stlPointsLabel = QLabel(self.frameStl)
        self.stlPointsLabel.setObjectName(u"stlPointsLabel")
        self.stlPointsLabel.setGeometry(QRect(10, 345, 121, 21))
        self.stlPointsLabel.setFont(font2)
        self.stlPointsLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.stlVerticesLabel = QLabel(self.frameStl)
        self.stlVerticesLabel.setObjectName(u"stlVerticesLabel")
        self.stlVerticesLabel.setGeometry(QRect(10, 360, 121, 21))
        self.stlVerticesLabel.setFont(font2)
        self.stlVerticesLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 500, 921, 1))
        self.line_2.setStyleSheet(u"Line {\n"
"    background-color: #D3D3D3;  \n"
"    max-height: 1px;             /* Thickness of the line */\n"
"    border: none;                /* Remove default frame border */\n"
"}\n"
"")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.appNameLabel = QLabel(Widget)
        self.appNameLabel.setObjectName(u"appNameLabel")
        self.appNameLabel.setGeometry(QRect(20, 10, 301, 40))
        font3 = QFont()
        font3.setFamilies([u"AlwynNewRounded-Regular"])
        font3.setPointSize(14)
        self.appNameLabel.setFont(font3)
        self.appNameLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}\n"
"")
        self.elementOrderLabel = QLabel(Widget)
        self.elementOrderLabel.setObjectName(u"elementOrderLabel")
        self.elementOrderLabel.setGeometry(QRect(80, 520, 121, 21))
        self.elementOrderLabel.setFont(font2)
        self.elementOrderLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}")
        self.mindihedralangleLabel = QLabel(Widget)
        self.mindihedralangleLabel.setObjectName(u"mindihedralangleLabel")
        self.mindihedralangleLabel.setGeometry(QRect(80, 550, 121, 21))
        self.mindihedralangleLabel.setFont(font2)
        self.mindihedralangleLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}")
        self.minRatioLabel = QLabel(Widget)
        self.minRatioLabel.setObjectName(u"minRatioLabel")
        self.minRatioLabel.setGeometry(QRect(80, 580, 121, 21))
        self.minRatioLabel.setFont(font2)
        self.minRatioLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}")
        self.maxVolumeLabel = QLabel(Widget)
        self.maxVolumeLabel.setObjectName(u"maxVolumeLabel")
        self.maxVolumeLabel.setGeometry(QRect(80, 610, 121, 21))
        self.maxVolumeLabel.setFont(font2)
        self.maxVolumeLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignRight | AlignVCenter';\n"
"}")
        self.displayModeLabel = QLabel(Widget)
        self.displayModeLabel.setObjectName(u"displayModeLabel")
        self.displayModeLabel.setGeometry(QRect(540, 580, 121, 21))
        self.displayModeLabel.setFont(font2)
        self.displayModeLabel.setStyleSheet(u"QLabel {\n"
"    color: #000000;                  /* Black text */\n"
"    background: transparent;         /* No background */\n"
"    border: none;                    /* No border */\n"
"	qproperty-alignment: 'AlignLeft | AlignVCenter';\n"
"}")
        self.orderComboBox = QComboBox(Widget)
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.setObjectName(u"orderComboBox")
        self.orderComboBox.setGeometry(QRect(220, 520, 241, 24))
        self.orderComboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #FFFFFF;   /* White background */\n"
"    color: #000000;              /* Black text */\n"
"    border: 1px solid #A0A0A0;  /* Thin gray border */\n"
"    border-radius: 2px;          /* Rounded corners */\n"
"    padding: 2px 6px;            /* Space inside box */\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"/* Keep default arrow without removing it */\n"
"QComboBox#orderComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #A0A0A0;\n"
"    border-radius: 0;\n"
"}\n"
"")
        self.maxVolumeDoubleSpinBox = QDoubleSpinBox(Widget)
        self.maxVolumeDoubleSpinBox.setObjectName(u"maxVolumeDoubleSpinBox")
        self.maxVolumeDoubleSpinBox.setGeometry(QRect(220, 610, 241, 24))
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
        self.preserveSurfaceCheckBox = QCheckBox(Widget)
        self.preserveSurfaceCheckBox.setObjectName(u"preserveSurfaceCheckBox")
        self.preserveSurfaceCheckBox.setGeometry(QRect(520, 550, 181, 20))
        self.preserveSurfaceCheckBox.setFont(font2)
        self.preserveSurfaceCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color: #000000;                /* Text color */\n"
"    spacing: 4px;                  /* Space between box and label */\n"
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
"    background-color: #28a745;     /* Green when checked */\n"
"    border: 1px solid #28a745;\n"
"}\n"
"")
        self.verboseCheckBox = QCheckBox(Widget)
        self.verboseCheckBox.setObjectName(u"verboseCheckBox")
        self.verboseCheckBox.setGeometry(QRect(520, 520, 181, 20))
        self.verboseCheckBox.setFont(font2)
        self.verboseCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color: #000000;                /* Text color */\n"
"    spacing: 4px;                  /* Space between box and label */\n"
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
"    background-color: #28a745;     /* Green when checked */\n"
"    border: 1px solid #28a745;\n"
"}\n"
"")
        self.frameTet.raise_()
        self.frameStl.raise_()
        self.mindihedralSpinBox.raise_()
        self.minRatioDoubleSpinBox.raise_()
        self.selectFileButton.raise_()
        self.generateMeshButton.raise_()
        self.line.raise_()
        self.saveMeshButton.raise_()
        self.line_2.raise_()
        self.appNameLabel.raise_()
        self.elementOrderLabel.raise_()
        self.mindihedralangleLabel.raise_()
        self.minRatioLabel.raise_()
        self.maxVolumeLabel.raise_()
        self.displayModeLabel.raise_()
        self.orderComboBox.raise_()
        self.maxVolumeDoubleSpinBox.raise_()
        self.preserveSurfaceCheckBox.raise_()
        self.verboseCheckBox.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Dialog", None))
        self.selectFileButton.setText(QCoreApplication.translate("Widget", u"Select File", None))
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
        self.elementOrderLabel.setText(QCoreApplication.translate("Widget", u"Element Order", None))
        self.mindihedralangleLabel.setText(QCoreApplication.translate("Widget", u"Min Dihedral Angle", None))
        self.minRatioLabel.setText(QCoreApplication.translate("Widget", u"Min Ratio", None))
        self.maxVolumeLabel.setText(QCoreApplication.translate("Widget", u"Max Volume", None))
        self.displayModeLabel.setText(QCoreApplication.translate("Widget", u"Display Mode", None))
        self.orderComboBox.setItemText(0, QCoreApplication.translate("Widget", u"1. Linear", None))
        self.orderComboBox.setItemText(1, QCoreApplication.translate("Widget", u"2. Quadratic", None))

        self.preserveSurfaceCheckBox.setText(QCoreApplication.translate("Widget", u"Preserve Surface Feature", None))
        self.verboseCheckBox.setText(QCoreApplication.translate("Widget", u"Verbose", None))
    # retranslateUi

