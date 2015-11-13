#include "qpylotwindow.h"
#include "ui_qpylotwindow.h"
#include <QtGui>

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

void QPyLOTWindow::on_pushButton_2_clicked()
{
    QColor color;
    color = QColorDialog::getColor(Qt::green, this, "Select Color", QColorDialog::DontUseNativeDialog);
/*
       if (color.isValid()) {
           colorLabel->setText(color.name());
           colorLabel->setPalette(QPalette(color));
           colorLabel->setAutoFillBackground(true);
       }
*/
}

void QPyLOTWindow::on_pushButton_clicked()
{
    bool ok;
    QFont font = QFontDialog::getFont(
                    &ok, QFont("Helvetica [Cronyx]", 10), this);
    if (ok) {
        // the user clicked OK and font is set to the font the user selected
    } else {
        // the user canceled the dialog; font is set to the initial
        // value, in this case Helvetica [Cronyx], 10
    }
}
