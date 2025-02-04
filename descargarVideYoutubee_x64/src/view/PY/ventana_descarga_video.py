# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_descarga_video.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_descargar_video_yt(object):
    def setupUi(self, descargar_video_yt):
        if not descargar_video_yt.objectName():
            descargar_video_yt.setObjectName(u"descargar_video_yt")
        descargar_video_yt.resize(400, 383)
        self.label = QLabel(descargar_video_yt)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 50, 241, 18))
        self.lineEdit = QLineEdit(descargar_video_yt)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(92, 120, 201, 32))
        self.pushButton = QPushButton(descargar_video_yt)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 200, 88, 34))
        self.pushButton_2 = QPushButton(descargar_video_yt)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 200, 88, 34))

        self.retranslateUi(descargar_video_yt)

        QMetaObject.connectSlotsByName(descargar_video_yt)
    # setupUi

    def retranslateUi(self, descargar_video_yt):
        descargar_video_yt.setWindowTitle(QCoreApplication.translate("descargar_video_yt", u"Form", None))
        self.label.setText(QCoreApplication.translate("descargar_video_yt", u"DESCARGAR VIDEOS DE YOUTUBE", None))
        self.pushButton.setText(QCoreApplication.translate("descargar_video_yt", u"DESCARGAR", None))
        self.pushButton_2.setText(QCoreApplication.translate("descargar_video_yt", u"CANCELAR", None))
    # retranslateUi

