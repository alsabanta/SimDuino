import sys,os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from _thread import *
import serial

app = QApplication(sys.argv)


ser = None
exitflag = 0

def sendser():
    global ser
    ser.write(bytes(wle.text(),encoding='UTF-8'))


def x(ser):
    global exitflag
    while True:
        if exitflag == 1:
            exit_thread()
        t = list(str(ser.readline()))
        t[0],t[1],t[len(t)-1] = '','',''
        m = 0
        for l in t:
            if l == '\\' and (t[m+1] == 'r' or t[m+1] == 'n'):
                t[m],t[m+1] = '',''
                m += 1
            else:
                m += 1

        rtb.append(''.join(t))
        print(''.join(t))
        if asflag == 1 :
            rtb.moveCursor(QTextCursor.End)
        else:
            pass



def SerialMonitor():
    global ser,exitflag
    exitflag = 0
    try:
        ser = serial.Serial('com15', 9600)
    except:
        msg = QErrorMessage(sw)
        msg.setWindowTitle('Serial Monitor')
        msg.showMessage('COM15 not found')
        msg.show()
        return
    start_new_thread(x,(ser,))
    sw.show()


def autoscroll():
    global asflag
    if chb.checkState() == 0:
        asflag = 0
    else:
        asflag = 1




class SMWidget(QWidget):
    global ser

    def __init__(self):
        QWidget.__init__(self)

    def closeEvent(self, QCloseEvent):
        global exitflag
        exitflag = 1
        rtb.clear()
        print("############################I Closed###########################################")
        ser.close()
        QCloseEvent.accept()




sw = SMWidget()
sw.setWindowTitle("Serial Monitor")
sw.resize(500, 405)

#sw.destroyed.connect(closeit)

wle = QLineEdit(sw)
wle.resize(450, 20)
wle.move(5, 5)

sb = QPushButton(sw)
sb.setText("Send")
sb.resize(40, 20)
sb.move(455, 5)

sb.clicked.connect(sendser)

rtb = QTextBrowser(sw)
rtb.resize(490, 350)
rtb.move(5, 30)

asflag = 0
chb = QCheckBox(sw)
chb.setText("Auto scroll")
chb.move(5,385)
chb.clicked.connect(autoscroll)


brl = QLabel(sw)
brl.setText('Buad Rate')
brl.move(380,385)
br = QComboBox(sw)
br.addItem('9600')
br.addItem('115200')
br.resize(60,15)
br.move(435,385)

def brchange():
    global ser,exitflag
    exitflag = 1
    ser.close()
    exitflag = 0
    ser = serial.Serial('com15', int(br.currentText()))
    start_new_thread(x, (ser,))

br.currentIndexChanged.connect(brchange)


def k():
    print("Hi !!")


w = QWidget()
w.resize(200,200)
b = QPushButton(w)
b.setText("Fuck")
b.clicked.connect(SerialMonitor)

b2 = QPushButton(w)
b2.setText("Hi !")
b2.move(0,30)
b2.clicked.connect(k)
w.show()
app.exec_()


