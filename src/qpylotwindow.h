#ifndef QPYLOTWINDOW_H
#define QPYLOTWINDOW_H

#include <QMainWindow>

namespace Ui {
class QPyLOTWindow;
}

class QPyLOTWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit QPyLOTWindow(QWidget *parent = 0);
    ~QPyLOTWindow();

private:
    Ui::QPyLOTWindow *ui;
};

#endif // QPYLOTWINDOW_H
