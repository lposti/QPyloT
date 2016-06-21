#-------------------------------------------------
#
# Project created by QtCreator 2015-10-29T11:22:42
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = QPyLOT
TEMPLATE = app


SOURCES += main.cpp\
        qpylotwindow.cpp

HEADERS  += qpylotwindow.h

FORMS    += qpylotwindow.ui\
            plot1d_window.ui\
            start_window.ui

DISTFILES += \
    main.py

