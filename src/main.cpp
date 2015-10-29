#include "qpylotwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QPyLOTWindow w;
    w.show();

    return a.exec();
}
