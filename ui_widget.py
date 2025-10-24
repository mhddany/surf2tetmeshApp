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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(523, 456)
        self.selectFileButton = QPushButton(Widget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(430, 40, 79, 31))
        self.generateMeshButton = QPushButton(Widget)
        self.generateMeshButton.setObjectName(u"generateMeshButton")
        self.generateMeshButton.setGeometry(QRect(430, 80, 79, 31))
        self.plotTab = QTabWidget(Widget)
        self.plotTab.setObjectName(u"plotTab")
        self.plotTab.setGeometry(QRect(20, 20, 391, 411))
        self.stlTab = QWidget()
        self.stlTab.setObjectName(u"stlTab")
        self.stlView = QVTKRenderWindowInteractor(self.stlTab)
        self.stlView.setObjectName(u"stlView")
        self.stlView.setGeometry(QRect(10, 10, 371, 361))
        self.plotTab.addTab(self.stlTab, "")
        self.tetTab = QWidget()
        self.tetTab.setObjectName(u"tetTab")
        self.tetView = QGraphicsView(self.tetTab)
        self.tetView.setObjectName(u"tetView")
        self.tetView.setGeometry(QRect(10, 10, 371, 361))
        self.plotTab.addTab(self.tetTab, "")

        self.retranslateUi(Widget)

        self.plotTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Dialog", None))
        self.selectFileButton.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.generateMeshButton.setText(QCoreApplication.translate("Widget", u"Mesh", None))
        self.plotTab.setTabText(self.plotTab.indexOf(self.stlTab), QCoreApplication.translate("Widget", u"Surface Mesh", None))
        self.plotTab.setTabText(self.plotTab.indexOf(self.tetTab), QCoreApplication.translate("Widget", u"Volumetric Mesh", None))
    # retranslateUi

