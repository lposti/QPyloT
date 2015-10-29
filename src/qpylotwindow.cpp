#include "qpylotwindow.h"
#include "ui_qpylotwindow.h"

QPyLOTWindow::QPyLOTWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::QPyLOTWindow)
{
    ui->setupUi(this);
}

QPyLOTWindow::~QPyLOTWindow()
{
    delete ui;
}
