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

private slots:
    void on_pushButton_2_clicked();

    void on_pushButton_clicked();

private:
    Ui::QPyLOTWindow *ui;
};

#endif // QPYLOTWINDOW_H
