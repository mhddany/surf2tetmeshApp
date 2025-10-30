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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QPushButton,
    QSizePolicy, QWidget)

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(979, 610)
        self.selectFileButton = QPushButton(Widget)
        self.selectFileButton.setObjectName(u"selectFileButton")
        self.selectFileButton.setGeometry(QRect(40, 460, 79, 31))
        self.generateMeshButton = QPushButton(Widget)
        self.generateMeshButton.setObjectName(u"generateMeshButton")
        self.generateMeshButton.setGeometry(QRect(500, 460, 79, 31))
        self.stlView = QVTKRenderWindowInteractor(Widget)
        self.stlView.setObjectName(u"stlView")
        self.stlView.setGeometry(QRect(40, 40, 400, 400))       
        self.tetView = QVTKRenderWindowInteractor(Widget)
        self.tetView.setObjectName(u"tetView")
        self.tetView.setGeometry(QRect(500, 40, 400, 400))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Dialog", None))
        self.selectFileButton.setText(QCoreApplication.translate("Widget", u"Select File", None))
        self.generateMeshButton.setText(QCoreApplication.translate("Widget", u"Mesh", None))
    # retranslateUi

