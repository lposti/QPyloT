/********************************************************************************
** Form generated from reading UI file 'qpylotwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_QPYLOTWINDOW_H
#define UI_QPYLOTWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_QPyLOTWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QTabWidget *MaintabWidget;
    QWidget *Plot2Dtab;
    QGridLayout *gridLayout_2;
    QListWidget *Plot2DlistWidget;
    QSpacerItem *horizontalSpacer;
    QStackedWidget *Plot2DstackedWidget;
    QWidget *Plot2DDatapage;
    QGridLayout *gridLayout_3;
    QLabel *Filelabel;
    QSpacerItem *verticalSpacer;
    QLineEdit *Y1lineEdit;
    QFrame *line;
    QComboBox *Y1comboBox;
    QPushButton *Y1pushButton;
    QLabel *Columnlabel;
    QPushButton *X1pushButton;
    QLabel *Y1label;
    QComboBox *X1comboBox;
    QLabel *X1label;
    QPushButton *pushButton;
    QLineEdit *X1FilelineEdit;
    QPushButton *pushButton_2;
    QWidget *Plot2DAxespage;
    QGridLayout *gridLayout_4;
    QGridLayout *gridLayout_8;
    QSpinBox *YticsMinorspinBox;
    QDoubleSpinBox *YticsLengthdoubleSpinBox;
    QCheckBox *YticsRightcheckBox;
    QLabel *label_5;
    QSpinBox *XticsMinorspinBox;
    QLineEdit *YticslineEdit;
    QLabel *label_10;
    QLineEdit *XticslineEdit;
    QDoubleSpinBox *YticsMinorLengthdoubleSpinBox;
    QDoubleSpinBox *XticsLengthdoubleSpinBox;
    QCheckBox *YticsMinorcheckBox;
    QCheckBox *checkBox_4;
    QFrame *line_3;
    QCheckBox *XticsBottomcheckBox;
    QLabel *label_11;
    QLabel *label_6;
    QCheckBox *XticsTopcheckBox;
    QLabel *label_4;
    QLabel *label_8;
    QLabel *label_3;
    QLabel *label_7;
    QDoubleSpinBox *XticsMinorLengthdoubleSpinBox;
    QDoubleSpinBox *YticsOffsetdoubleSpinBox;
    QLabel *label_9;
    QCheckBox *XticsMinorcheckBox;
    QDoubleSpinBox *XticsOffsetdoubleSpinBox;
    QToolButton *YticsFonttoolButton;
    QLabel *label_12;
    QSpacerItem *verticalSpacer_3;
    QGridLayout *gridLayout_7;
    QDoubleSpinBox *YLabeloffsetdoubleSpinBox;
    QLabel *label_2;
    QLabel *Labelslabel;
    QLabel *label;
    QDoubleSpinBox *XLabeloffsetdoubleSpinBox;
    QLabel *YLabellabel;
    QLabel *XLabellabel;
    QLineEdit *YLabellineEdit;
    QLineEdit *XLabellineEdit;
    QLabel *Fontlabel;
    QToolButton *LabelFonttoolButton;
    QFrame *line_2;
    QWidget *page;
    QWidget *tab_2;
    QMenuBar *menuBar;
    QStatusBar *statusBar;
    QToolBar *mainToolBar;

    void setupUi(QMainWindow *QPyLOTWindow)
    {
        if (QPyLOTWindow->objectName().isEmpty())
            QPyLOTWindow->setObjectName(QStringLiteral("QPyLOTWindow"));
        centralWidget = new QWidget(QPyLOTWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        MaintabWidget = new QTabWidget(centralWidget);
        MaintabWidget->setObjectName(QStringLiteral("MaintabWidget"));
        Plot2Dtab = new QWidget();
        Plot2Dtab->setObjectName(QStringLiteral("Plot2Dtab"));
        gridLayout_2 = new QGridLayout(Plot2Dtab);
        gridLayout_2->setSpacing(6);
        gridLayout_2->setContentsMargins(11, 11, 11, 11);
        gridLayout_2->setObjectName(QStringLiteral("gridLayout_2"));
        Plot2DlistWidget = new QListWidget(Plot2Dtab);
        new QListWidgetItem(Plot2DlistWidget);
        new QListWidgetItem(Plot2DlistWidget);
        new QListWidgetItem(Plot2DlistWidget);
        new QListWidgetItem(Plot2DlistWidget);
        new QListWidgetItem(Plot2DlistWidget);
        Plot2DlistWidget->setObjectName(QStringLiteral("Plot2DlistWidget"));
        QSizePolicy sizePolicy(QSizePolicy::Ignored, QSizePolicy::Ignored);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(Plot2DlistWidget->sizePolicy().hasHeightForWidth());
        Plot2DlistWidget->setSizePolicy(sizePolicy);

        gridLayout_2->addWidget(Plot2DlistWidget, 0, 0, 1, 1);

        horizontalSpacer = new QSpacerItem(100, 1, QSizePolicy::Fixed, QSizePolicy::Minimum);

        gridLayout_2->addItem(horizontalSpacer, 1, 0, 1, 1);

        Plot2DstackedWidget = new QStackedWidget(Plot2Dtab);
        Plot2DstackedWidget->setObjectName(QStringLiteral("Plot2DstackedWidget"));
        Plot2DDatapage = new QWidget();
        Plot2DDatapage->setObjectName(QStringLiteral("Plot2DDatapage"));
        gridLayout_3 = new QGridLayout(Plot2DDatapage);
        gridLayout_3->setSpacing(6);
        gridLayout_3->setContentsMargins(11, 11, 11, 11);
        gridLayout_3->setObjectName(QStringLiteral("gridLayout_3"));
        Filelabel = new QLabel(Plot2DDatapage);
        Filelabel->setObjectName(QStringLiteral("Filelabel"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(Filelabel->sizePolicy().hasHeightForWidth());
        Filelabel->setSizePolicy(sizePolicy1);

        gridLayout_3->addWidget(Filelabel, 1, 1, 1, 2);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout_3->addItem(verticalSpacer, 5, 1, 1, 1);

        Y1lineEdit = new QLineEdit(Plot2DDatapage);
        Y1lineEdit->setObjectName(QStringLiteral("Y1lineEdit"));

        gridLayout_3->addWidget(Y1lineEdit, 3, 1, 1, 1);

        line = new QFrame(Plot2DDatapage);
        line->setObjectName(QStringLiteral("line"));
        line->setFrameShape(QFrame::HLine);
        line->setFrameShadow(QFrame::Sunken);

        gridLayout_3->addWidget(line, 4, 0, 1, 4);

        Y1comboBox = new QComboBox(Plot2DDatapage);
        Y1comboBox->setObjectName(QStringLiteral("Y1comboBox"));
        Y1comboBox->setEnabled(false);

        gridLayout_3->addWidget(Y1comboBox, 3, 3, 1, 1);

        Y1pushButton = new QPushButton(Plot2DDatapage);
        Y1pushButton->setObjectName(QStringLiteral("Y1pushButton"));

        gridLayout_3->addWidget(Y1pushButton, 3, 2, 1, 1);

        Columnlabel = new QLabel(Plot2DDatapage);
        Columnlabel->setObjectName(QStringLiteral("Columnlabel"));

        gridLayout_3->addWidget(Columnlabel, 1, 3, 1, 1);

        X1pushButton = new QPushButton(Plot2DDatapage);
        X1pushButton->setObjectName(QStringLiteral("X1pushButton"));

        gridLayout_3->addWidget(X1pushButton, 2, 2, 1, 1);

        Y1label = new QLabel(Plot2DDatapage);
        Y1label->setObjectName(QStringLiteral("Y1label"));

        gridLayout_3->addWidget(Y1label, 3, 0, 1, 1);

        X1comboBox = new QComboBox(Plot2DDatapage);
        X1comboBox->setObjectName(QStringLiteral("X1comboBox"));
        X1comboBox->setEnabled(false);

        gridLayout_3->addWidget(X1comboBox, 2, 3, 1, 1);

        X1label = new QLabel(Plot2DDatapage);
        X1label->setObjectName(QStringLiteral("X1label"));

        gridLayout_3->addWidget(X1label, 2, 0, 1, 1);

        pushButton = new QPushButton(Plot2DDatapage);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        gridLayout_3->addWidget(pushButton, 7, 1, 1, 1);

        X1FilelineEdit = new QLineEdit(Plot2DDatapage);
        X1FilelineEdit->setObjectName(QStringLiteral("X1FilelineEdit"));

        gridLayout_3->addWidget(X1FilelineEdit, 2, 1, 1, 1);

        pushButton_2 = new QPushButton(Plot2DDatapage);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));

        gridLayout_3->addWidget(pushButton_2, 6, 1, 1, 1);

        Plot2DstackedWidget->addWidget(Plot2DDatapage);
        Plot2DAxespage = new QWidget();
        Plot2DAxespage->setObjectName(QStringLiteral("Plot2DAxespage"));
        gridLayout_4 = new QGridLayout(Plot2DAxespage);
        gridLayout_4->setSpacing(6);
        gridLayout_4->setContentsMargins(11, 11, 11, 11);
        gridLayout_4->setObjectName(QStringLiteral("gridLayout_4"));
        gridLayout_8 = new QGridLayout();
        gridLayout_8->setSpacing(6);
        gridLayout_8->setObjectName(QStringLiteral("gridLayout_8"));
        YticsMinorspinBox = new QSpinBox(Plot2DAxespage);
        YticsMinorspinBox->setObjectName(QStringLiteral("YticsMinorspinBox"));
        YticsMinorspinBox->setEnabled(false);
        YticsMinorspinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        YticsMinorspinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_8->addWidget(YticsMinorspinBox, 5, 2, 1, 1);

        YticsLengthdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        YticsLengthdoubleSpinBox->setObjectName(QStringLiteral("YticsLengthdoubleSpinBox"));
        YticsLengthdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        YticsLengthdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);
        YticsLengthdoubleSpinBox->setValue(5);

        gridLayout_8->addWidget(YticsLengthdoubleSpinBox, 4, 4, 1, 1);

        YticsRightcheckBox = new QCheckBox(Plot2DAxespage);
        YticsRightcheckBox->setObjectName(QStringLiteral("YticsRightcheckBox"));
        YticsRightcheckBox->setChecked(true);

        gridLayout_8->addWidget(YticsRightcheckBox, 4, 5, 1, 1);

        label_5 = new QLabel(Plot2DAxespage);
        label_5->setObjectName(QStringLiteral("label_5"));
        QSizePolicy sizePolicy2(QSizePolicy::Maximum, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy2);

        gridLayout_8->addWidget(label_5, 3, 1, 1, 1);

        XticsMinorspinBox = new QSpinBox(Plot2DAxespage);
        XticsMinorspinBox->setObjectName(QStringLiteral("XticsMinorspinBox"));
        XticsMinorspinBox->setEnabled(false);
        XticsMinorspinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        XticsMinorspinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_8->addWidget(XticsMinorspinBox, 2, 2, 1, 1);

        YticslineEdit = new QLineEdit(Plot2DAxespage);
        YticslineEdit->setObjectName(QStringLiteral("YticslineEdit"));

        gridLayout_8->addWidget(YticslineEdit, 4, 1, 1, 2);

        label_10 = new QLabel(Plot2DAxespage);
        label_10->setObjectName(QStringLiteral("label_10"));

        gridLayout_8->addWidget(label_10, 6, 1, 1, 1);

        XticslineEdit = new QLineEdit(Plot2DAxespage);
        XticslineEdit->setObjectName(QStringLiteral("XticslineEdit"));

        gridLayout_8->addWidget(XticslineEdit, 1, 1, 1, 2);

        YticsMinorLengthdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        YticsMinorLengthdoubleSpinBox->setObjectName(QStringLiteral("YticsMinorLengthdoubleSpinBox"));
        YticsMinorLengthdoubleSpinBox->setEnabled(false);
        YticsMinorLengthdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        YticsMinorLengthdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_8->addWidget(YticsMinorLengthdoubleSpinBox, 5, 4, 1, 1);

        XticsLengthdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        XticsLengthdoubleSpinBox->setObjectName(QStringLiteral("XticsLengthdoubleSpinBox"));
        XticsLengthdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        XticsLengthdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);
        XticsLengthdoubleSpinBox->setValue(5);

        gridLayout_8->addWidget(XticsLengthdoubleSpinBox, 1, 4, 1, 1);

        YticsMinorcheckBox = new QCheckBox(Plot2DAxespage);
        YticsMinorcheckBox->setObjectName(QStringLiteral("YticsMinorcheckBox"));

        gridLayout_8->addWidget(YticsMinorcheckBox, 5, 1, 1, 1);

        checkBox_4 = new QCheckBox(Plot2DAxespage);
        checkBox_4->setObjectName(QStringLiteral("checkBox_4"));
        checkBox_4->setChecked(true);

        gridLayout_8->addWidget(checkBox_4, 4, 6, 1, 1);

        line_3 = new QFrame(Plot2DAxespage);
        line_3->setObjectName(QStringLiteral("line_3"));
        line_3->setFrameShape(QFrame::HLine);
        line_3->setFrameShadow(QFrame::Sunken);

        gridLayout_8->addWidget(line_3, 0, 1, 1, 6);

        XticsBottomcheckBox = new QCheckBox(Plot2DAxespage);
        XticsBottomcheckBox->setObjectName(QStringLiteral("XticsBottomcheckBox"));
        XticsBottomcheckBox->setChecked(true);

        gridLayout_8->addWidget(XticsBottomcheckBox, 1, 6, 1, 1);

        label_11 = new QLabel(Plot2DAxespage);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setEnabled(false);

        gridLayout_8->addWidget(label_11, 5, 3, 1, 1);

        label_6 = new QLabel(Plot2DAxespage);
        label_6->setObjectName(QStringLiteral("label_6"));
        sizePolicy2.setHeightForWidth(label_6->sizePolicy().hasHeightForWidth());
        label_6->setSizePolicy(sizePolicy2);

        gridLayout_8->addWidget(label_6, 1, 3, 1, 1);

        XticsTopcheckBox = new QCheckBox(Plot2DAxespage);
        XticsTopcheckBox->setObjectName(QStringLiteral("XticsTopcheckBox"));
        XticsTopcheckBox->setChecked(true);

        gridLayout_8->addWidget(XticsTopcheckBox, 1, 5, 1, 1);

        label_4 = new QLabel(Plot2DAxespage);
        label_4->setObjectName(QStringLiteral("label_4"));
        sizePolicy2.setHeightForWidth(label_4->sizePolicy().hasHeightForWidth());
        label_4->setSizePolicy(sizePolicy2);

        gridLayout_8->addWidget(label_4, 1, 0, 1, 1);

        label_8 = new QLabel(Plot2DAxespage);
        label_8->setObjectName(QStringLiteral("label_8"));

        gridLayout_8->addWidget(label_8, 4, 0, 1, 1);

        label_3 = new QLabel(Plot2DAxespage);
        label_3->setObjectName(QStringLiteral("label_3"));

        gridLayout_8->addWidget(label_3, 0, 0, 1, 1);

        label_7 = new QLabel(Plot2DAxespage);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setEnabled(false);

        gridLayout_8->addWidget(label_7, 2, 3, 1, 1);

        XticsMinorLengthdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        XticsMinorLengthdoubleSpinBox->setObjectName(QStringLiteral("XticsMinorLengthdoubleSpinBox"));
        XticsMinorLengthdoubleSpinBox->setEnabled(false);
        XticsMinorLengthdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        XticsMinorLengthdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_8->addWidget(XticsMinorLengthdoubleSpinBox, 2, 4, 1, 1);

        YticsOffsetdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        YticsOffsetdoubleSpinBox->setObjectName(QStringLiteral("YticsOffsetdoubleSpinBox"));
        YticsOffsetdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        YticsOffsetdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_8->addWidget(YticsOffsetdoubleSpinBox, 6, 2, 1, 1);

        label_9 = new QLabel(Plot2DAxespage);
        label_9->setObjectName(QStringLiteral("label_9"));

        gridLayout_8->addWidget(label_9, 4, 3, 1, 1);

        XticsMinorcheckBox = new QCheckBox(Plot2DAxespage);
        XticsMinorcheckBox->setObjectName(QStringLiteral("XticsMinorcheckBox"));

        gridLayout_8->addWidget(XticsMinorcheckBox, 2, 1, 1, 1);

        XticsOffsetdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        XticsOffsetdoubleSpinBox->setObjectName(QStringLiteral("XticsOffsetdoubleSpinBox"));
        XticsOffsetdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        XticsOffsetdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_8->addWidget(XticsOffsetdoubleSpinBox, 3, 2, 1, 1);

        YticsFonttoolButton = new QToolButton(Plot2DAxespage);
        YticsFonttoolButton->setObjectName(QStringLiteral("YticsFonttoolButton"));

        gridLayout_8->addWidget(YticsFonttoolButton, 7, 1, 1, 1);

        label_12 = new QLabel(Plot2DAxespage);
        label_12->setObjectName(QStringLiteral("label_12"));

        gridLayout_8->addWidget(label_12, 7, 0, 1, 1);


        gridLayout_4->addLayout(gridLayout_8, 6, 0, 1, 1);

        verticalSpacer_3 = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Fixed);

        gridLayout_4->addItem(verticalSpacer_3, 5, 0, 1, 1);

        gridLayout_7 = new QGridLayout();
        gridLayout_7->setSpacing(6);
        gridLayout_7->setObjectName(QStringLiteral("gridLayout_7"));
        YLabeloffsetdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        YLabeloffsetdoubleSpinBox->setObjectName(QStringLiteral("YLabeloffsetdoubleSpinBox"));
        YLabeloffsetdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        YLabeloffsetdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_7->addWidget(YLabeloffsetdoubleSpinBox, 2, 3, 1, 1);

        label_2 = new QLabel(Plot2DAxespage);
        label_2->setObjectName(QStringLiteral("label_2"));

        gridLayout_7->addWidget(label_2, 2, 2, 1, 1);

        Labelslabel = new QLabel(Plot2DAxespage);
        Labelslabel->setObjectName(QStringLiteral("Labelslabel"));

        gridLayout_7->addWidget(Labelslabel, 0, 0, 1, 1);

        label = new QLabel(Plot2DAxespage);
        label->setObjectName(QStringLiteral("label"));
        sizePolicy2.setHeightForWidth(label->sizePolicy().hasHeightForWidth());
        label->setSizePolicy(sizePolicy2);

        gridLayout_7->addWidget(label, 1, 2, 1, 1);

        XLabeloffsetdoubleSpinBox = new QDoubleSpinBox(Plot2DAxespage);
        XLabeloffsetdoubleSpinBox->setObjectName(QStringLiteral("XLabeloffsetdoubleSpinBox"));
        QSizePolicy sizePolicy3(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(XLabeloffsetdoubleSpinBox->sizePolicy().hasHeightForWidth());
        XLabeloffsetdoubleSpinBox->setSizePolicy(sizePolicy3);
        XLabeloffsetdoubleSpinBox->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        XLabeloffsetdoubleSpinBox->setButtonSymbols(QAbstractSpinBox::NoButtons);

        gridLayout_7->addWidget(XLabeloffsetdoubleSpinBox, 1, 3, 1, 1);

        YLabellabel = new QLabel(Plot2DAxespage);
        YLabellabel->setObjectName(QStringLiteral("YLabellabel"));

        gridLayout_7->addWidget(YLabellabel, 2, 0, 1, 1);

        XLabellabel = new QLabel(Plot2DAxespage);
        XLabellabel->setObjectName(QStringLiteral("XLabellabel"));

        gridLayout_7->addWidget(XLabellabel, 1, 0, 1, 1);

        YLabellineEdit = new QLineEdit(Plot2DAxespage);
        YLabellineEdit->setObjectName(QStringLiteral("YLabellineEdit"));

        gridLayout_7->addWidget(YLabellineEdit, 2, 1, 1, 1);

        XLabellineEdit = new QLineEdit(Plot2DAxespage);
        XLabellineEdit->setObjectName(QStringLiteral("XLabellineEdit"));

        gridLayout_7->addWidget(XLabellineEdit, 1, 1, 1, 1);

        Fontlabel = new QLabel(Plot2DAxespage);
        Fontlabel->setObjectName(QStringLiteral("Fontlabel"));
        sizePolicy2.setHeightForWidth(Fontlabel->sizePolicy().hasHeightForWidth());
        Fontlabel->setSizePolicy(sizePolicy2);

        gridLayout_7->addWidget(Fontlabel, 3, 0, 1, 1);

        LabelFonttoolButton = new QToolButton(Plot2DAxespage);
        LabelFonttoolButton->setObjectName(QStringLiteral("LabelFonttoolButton"));

        gridLayout_7->addWidget(LabelFonttoolButton, 3, 1, 1, 1);

        line_2 = new QFrame(Plot2DAxespage);
        line_2->setObjectName(QStringLiteral("line_2"));
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);

        gridLayout_7->addWidget(line_2, 0, 1, 1, 3);


        gridLayout_4->addLayout(gridLayout_7, 4, 0, 1, 1);

        Plot2DstackedWidget->addWidget(Plot2DAxespage);
        page = new QWidget();
        page->setObjectName(QStringLiteral("page"));
        Plot2DstackedWidget->addWidget(page);

        gridLayout_2->addWidget(Plot2DstackedWidget, 0, 1, 1, 1);

        MaintabWidget->addTab(Plot2Dtab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QStringLiteral("tab_2"));
        MaintabWidget->addTab(tab_2, QString());

        gridLayout->addWidget(MaintabWidget, 0, 0, 1, 1);

        QPyLOTWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(QPyLOTWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 714, 22));
        QPyLOTWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(QPyLOTWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        QPyLOTWindow->setStatusBar(statusBar);
        mainToolBar = new QToolBar(QPyLOTWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        QPyLOTWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);

        retranslateUi(QPyLOTWindow);

        Plot2DstackedWidget->setCurrentIndex(2);


        QMetaObject::connectSlotsByName(QPyLOTWindow);
    } // setupUi

    void retranslateUi(QMainWindow *QPyLOTWindow)
    {
        QPyLOTWindow->setWindowTitle(QApplication::translate("QPyLOTWindow", "QPyLOT", 0));

        const bool __sortingEnabled = Plot2DlistWidget->isSortingEnabled();
        Plot2DlistWidget->setSortingEnabled(false);
        QListWidgetItem *___qlistwidgetitem = Plot2DlistWidget->item(0);
        ___qlistwidgetitem->setText(QApplication::translate("QPyLOTWindow", "Data", 0));
        QListWidgetItem *___qlistwidgetitem1 = Plot2DlistWidget->item(1);
        ___qlistwidgetitem1->setText(QApplication::translate("QPyLOTWindow", "Axes", 0));
        QListWidgetItem *___qlistwidgetitem2 = Plot2DlistWidget->item(2);
        ___qlistwidgetitem2->setText(QApplication::translate("QPyLOTWindow", "Markers", 0));
        QListWidgetItem *___qlistwidgetitem3 = Plot2DlistWidget->item(3);
        ___qlistwidgetitem3->setText(QApplication::translate("QPyLOTWindow", "Legend", 0));
        QListWidgetItem *___qlistwidgetitem4 = Plot2DlistWidget->item(4);
        ___qlistwidgetitem4->setText(QApplication::translate("QPyLOTWindow", "Text", 0));
        Plot2DlistWidget->setSortingEnabled(__sortingEnabled);

        Filelabel->setText(QApplication::translate("QPyLOTWindow", "File (ASCII or FITS table)", 0));
        Y1pushButton->setText(QApplication::translate("QPyLOTWindow", "Open", 0));
        Columnlabel->setText(QApplication::translate("QPyLOTWindow", "Column", 0));
        X1pushButton->setText(QApplication::translate("QPyLOTWindow", "Open", 0));
        Y1label->setText(QApplication::translate("QPyLOTWindow", "Y", 0));
        X1label->setText(QApplication::translate("QPyLOTWindow", "X  ", 0));
        pushButton->setText(QApplication::translate("QPyLOTWindow", "PushButton", 0));
        pushButton_2->setText(QApplication::translate("QPyLOTWindow", "PushButton", 0));
        YticsRightcheckBox->setText(QApplication::translate("QPyLOTWindow", "Left", 0));
        label_5->setText(QApplication::translate("QPyLOTWindow", "Label offset", 0));
        label_10->setText(QApplication::translate("QPyLOTWindow", "Label offset", 0));
        YticsMinorcheckBox->setText(QApplication::translate("QPyLOTWindow", "Minor tics", 0));
        checkBox_4->setText(QApplication::translate("QPyLOTWindow", "Right", 0));
        XticsBottomcheckBox->setText(QApplication::translate("QPyLOTWindow", "Bottom", 0));
        label_11->setText(QApplication::translate("QPyLOTWindow", "Length", 0));
        label_6->setText(QApplication::translate("QPyLOTWindow", "Length", 0));
        XticsTopcheckBox->setText(QApplication::translate("QPyLOTWindow", "Top", 0));
        label_4->setText(QApplication::translate("QPyLOTWindow", "  X tics:", 0));
        label_8->setText(QApplication::translate("QPyLOTWindow", "  Y tics:", 0));
        label_3->setText(QApplication::translate("QPyLOTWindow", "TICS      ", 0));
        label_7->setText(QApplication::translate("QPyLOTWindow", "Length", 0));
        label_9->setText(QApplication::translate("QPyLOTWindow", "Length", 0));
        XticsMinorcheckBox->setText(QApplication::translate("QPyLOTWindow", " Minor tics", 0));
        YticsFonttoolButton->setText(QApplication::translate("QPyLOTWindow", "Helvetica, 12 pt", 0));
        label_12->setText(QApplication::translate("QPyLOTWindow", "  Font", 0));
        label_2->setText(QApplication::translate("QPyLOTWindow", "Offset", 0));
        Labelslabel->setText(QApplication::translate("QPyLOTWindow", "LABELS", 0));
        label->setText(QApplication::translate("QPyLOTWindow", "Offset", 0));
        YLabellabel->setText(QApplication::translate("QPyLOTWindow", "  Y label:", 0));
        XLabellabel->setText(QApplication::translate("QPyLOTWindow", "  X label:", 0));
        Fontlabel->setText(QApplication::translate("QPyLOTWindow", "  Font:", 0));
        LabelFonttoolButton->setText(QApplication::translate("QPyLOTWindow", "Helvetica, 12 pt", 0));
        MaintabWidget->setTabText(MaintabWidget->indexOf(Plot2Dtab), QApplication::translate("QPyLOTWindow", "2D Plot", 0));
        MaintabWidget->setTabText(MaintabWidget->indexOf(tab_2), QApplication::translate("QPyLOTWindow", "Tab 2", 0));
    } // retranslateUi

};

namespace Ui {
    class QPyLOTWindow: public Ui_QPyLOTWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_QPYLOTWINDOW_H
