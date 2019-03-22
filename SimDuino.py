import sys,os,serial,serial.tools.list_ports
from PyQt4.QtGui import *
from _thread import *

app = QApplication(sys.argv)

################################# Functions ###################################

################### Serial Monitor ######################

ser = None
exitflag = 0

def sendser():
    global ser
    ser.write(bytes(wle.text(),encoding='UTF-8'))


def sermon(ser):
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
        if asflag == 1:
            rtb.moveCursor(QTextCursor.End)
        else:
            pass



def SerialMonitor():
    global ser,exitflag
    exitflag = 0
    try:
        ser = serial.Serial(pcb.currentText(), int(br.currentText()))
    except:
        msg = QErrorMessage(sw)
        msg.setWindowTitle('Serial Monitor')
        if pcb.currentText() == '':
            msg.showMessage('No COM Found')
        else:
            msg.showMessage(pcb.currentText() + ' not found')
        msg.show()
        return
    start_new_thread(sermon,(ser,))
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
        ser.close()
        QCloseEvent.accept()


sw = SMWidget()
sw.setWindowTitle("Serial Monitor")
sw.resize(500, 405)

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
    start_new_thread(sermon, (ser,))

br.currentIndexChanged.connect(brchange)



############# Utilities #################
def diff(l,l1):
    j = []
    for i in l:
        if(i not in l1 ):
            j.append(i)
    return j


def atosl(l,e,n):
        if n<len(l) and n >= 0:
            t = l[n:]
            l = diff(l,t)
            l.append(e)
            for i in t:
                l.append(i)
        elif(n == len(l)):
            l.append(e)
        else:
            print("Out of range!")
        return l

global var

var = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def pin(pn,id):
    if(id == 0):
        func(id,lp0,cb0)
        if cb0.currentIndex() == 0:
            txt = ''
        elif cb0.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb0.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 1):
        func(id,lp1, cb1)
        if cb1.currentIndex() == 0:
            txt = ''
        elif cb1.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb1.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 2):
        func(id,lp2, cb2)
        if cb2.currentIndex() == 0:
            txt = ''
        elif cb2.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb2.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 3):
        func(id,lp3, cb3)
        if cb3.currentIndex() == 0:
            txt = ''
        elif cb3.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb3.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 4):
        func(id,lp4, cb4)
        if cb4.currentIndex() == 0:
            txt = ''
        elif cb4.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb4.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 5):
        func(id,lp5, cb5)
        if cb5.currentIndex() == 0:
            txt = ''
        elif cb5.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb5.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 6):
        func(id,lp6, cb6)
        if cb6.currentIndex() == 0:
            txt = ''
        elif cb6.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb6.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 7):
        func(id,lp7, cb7)
        if cb7.currentIndex() == 0:
            txt = ''
        elif cb7.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb7.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 8):
        func(id,lp8, cb8)
        if cb8.currentIndex() == 0:
            txt = ''
        elif cb8.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb8.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 9):
        func(id,lp9, cb9)
        if cb9.currentIndex() == 0:
            txt = ''
        elif cb9.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb9.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 10):
        func(id,lp10, cb10)
        if cb10.currentIndex() == 0:
            txt = ''
        elif cb10.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb10.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 11):
        func(id,lp11, cb11)
        if cb11.currentIndex() == 0:
            txt = ''
        elif cb11.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb11.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 12):
        func(id,lp12, cb12)
        if cb12.currentIndex() == 0:
            txt = ''
        elif cb12.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb12.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 13):
        func(id,lp13, cb13)
        if cb13.currentIndex() == 0:
            txt = ''
        elif cb13.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb13.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 14):
        func(id,lp14, cb14)
        if cb14.currentIndex() == 0:
            txt = ''
        elif cb14.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb14.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 15):
        func(id,lp15, cb15)
        if cb15.currentIndex() == 0:
            txt = ''
        elif cb15.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb15.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 16):
        func(id,lp16, cb16)
        if cb16.currentIndex() == 0:
            txt = ''
        elif cb16.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb16.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 17):
        func(id,lp17, cb17)
        if cb17.currentIndex() == 0:
            txt = ''
        elif cb17.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb17.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 18):
        func(id,lp18, cb18)
        if cb18.currentIndex() == 0:
            txt = ''
        elif cb18.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb18.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif(id == 19):
        func(id,lp19, cb19)
        if cb19.currentIndex() == 0:
            txt = ''
        elif cb19.currentIndex() == 1:
            txt = "pinMode(%s,INPUT);\n" % pn
        elif cb19.currentIndex() == 2:
            txt = "pinMode(%s,OUTPUT);\n" % pn
    elif id == 20:
        if pn == 'None':
            txt = ''
            srw.setCurrentIndex(0)
            srw.removeItem(2)
            srw.removeItem(1)
        else :
            txt = "Serial.begin(%s);\n" % pn
            srw.addItem("Read")
            srw.addItem("Print")

    f = open(inopath, 'r')
    d = f.readlines()
    f.close()
    f = d

    if var[id] == 0:
        j = 0
        for i in f:
            if i == '\n':
                var[id] = j
                d[j] = txt
                d = atosl(d, '\n', j + 1)
                break
            else:
                j += 1

        pt.setPlainText(''.join(d))
        f = open(inopath, 'w')
        f.writelines(d)
        f.close()

    else:
        d[var[id]] = txt
        pt.setPlainText(''.join(d))
        f = open(inopath, 'w')
        f.writelines(d)
        f.close()
        if txt == '':
            var[id] = 0


def func(id,a,b):
    a.clear()
    a.addItem("None")
    if b.currentIndex() == 1 :
        a.addItem("Digital Read")
        if id == 19 or id == 18 or id == 16 or id == 15 or id == 14 or id == 11 or id == 10 or id == 9 or id == 6 or id == 5 or id == 3:
            a.addItem("Analog Read")
    if b.currentIndex() == 2 :
        a.addItem("High")
        a.addItem("LOW")
        if id == 19 or id == 18 or id == 16 or id == 15 or id == 14 or id == 11 or id == 10 or id == 9 or id == 6 or id == 5 or id == 3 :
            a.addItem("PWM")








################################ Files ##########################################
inopath = os.path.abspath('Temp\\temp.ino')
ino = open(inopath,'w')
ino.writelines("void setup(){\n\n}\n\nvoid loop(){\n\n}")
ino.close()

################################## The GUI #####################################

mw = QMainWindow()
mw.setFixedSize(695,395)
l1 = QIcon("sd.png")
mw.setWindowIcon(l1)
mw.setWindowTitle("SimDuino")
tabs = QTabWidget(mw)
tabs.setFixedSize(695, 375)
tabs.move(0,20)

x = QWidget()
y = QWidget()
z = QWidget()

tabs.addTab(x,"Setup")
tabs.addTab(y,"Loop")
tabs.addTab(z,"LCD")

########## Basics ########

def new():
    pass

def save():
    global ino,sn,inopath

    if sn == 0:
        fn = QFileDialog.getSaveFileName(mw,'Save File','*.sdi',"*.sdi")
        a = open(fn,'w')
        a.write(fn)
        a.close()

        p = os.path.splitext(fn)[0]
        os.mkdir(p)
        ino = open(inopath,'r')
        temp = ino.readlines()
        inopath = p+'/'+os.path.basename(fn)[0]+'.ino'
        ino = open(inopath,'w')
        ino.writelines(temp)
        ino.close()
        sn = 1

    else:
        pass





na = QAction("New",mw)
na.setShortcut("CTRL+n")
sa = QAction("Save",mw)
sa.setShortcut("CTRL+S")

mb = QMenuBar(mw)
mb.resize(mw.width(),20)
fm = mb.addMenu('File')

fm.addActions([na,sa])

na.triggered.connect(new)

sn = 0
sa.triggered.connect(save)

########## Plain Text
ptl = QLabel(tabs)
ptl.setText("Code Flow")
pt = QTextBrowser(tabs)
pt.resize(280, 280)
pt.setPlainText(''.join(["void setup(){","\n","\n}\n\nvoid loop(){","\n","\n}"]))
ptl.move(500, 35)
pt.move(400, 60)

def tabchanged():
    if tabs.currentIndex() == 0 :
        mw.setFixedSize(695,395)
        tabs.setFixedSize(695, 375)
        ptl.move(500, 35)
        pt.move(400, 60)
        mb.resize(mw.width(), 20)
        pcb.move(555, 345)
        upb.move(630, 345)
        upf.move(400, 343)
    elif tabs.currentIndex() == 1 :
        mw.setFixedSize(795, 395)
        tabs.setFixedSize(795, 375)
        ptl.move(600, 35)
        pt.move(500, 60)
        mb.resize(mw.width(), 20)
        pcb.move(655, 345)
        upb.move(730, 345)
        upf.move(500, 343)

tabs.currentChanged.connect(tabchanged)

######## Ports & Upload
def ports():
    lst = []
    while 1:
        p = (list(serial.tools.list_ports.comports()))
        if not p:
            pcb.clear()
            lst.clear()
            pcb.setToolTip('There is no connected COM')
        else:
            for i in p:
                if i[0] in lst:
                    continue
                else:
                    lst.append(i[0])
                    pcb.addItem(i[0])
                    if pcb.currentText() == '':
                        pcb.setCurrentIndex(0)
                pcb.setToolTip(str(i[1]))

pcb = QComboBox(tabs)
pcb.resize(70,20)
pcb.move(555,345)

start_new_thread(ports,())


upb = QPushButton(tabs)
upb.setText("Upload")
upb.resize(50,21)
upb.move(630,345)

errflag = 2

def upload_th():
    global errflag
    os.chdir("C:\Program Files (x86)\Arduino")
    err = os.system("arduino_debug --port "+pcb.currentText()+ " --upload " + inopath)
    errflag = err
    print(err)
    exit_thread()

upf = QLabel(tabs)
upf.move(400, 343)
upf.resize(150,25)


def upload():
    msg = QErrorMessage(mw)
    msg.setWindowTitle('Upload')
    upf.setText('Uploading ..')

    if pcb.currentText() == '':
        msg.showMessage('No COM port Found')
        upf.setText('No COM port Found')
    else:
        start_new_thread(upload_th,())
        start_new_thread(erroruploading,())



def erroruploading():
    global errflag
    errflag = 2
    while errflag == 2:
        continue
    if errflag == 0:
        print('Done uploading')
        upf.setText('Done Uploading')
    elif errflag == 1:
        upf.setText('An error occurred!')
    exit_thread()


upb.clicked.connect(upload)

####### Tab Setup
arl = QLabel(x)
arl.setText("Arduino")
arl.move(10, 10)
ar = QComboBox(x)
ar.addItem("Uno")
ar.addItem("Mega")
ar.resize(90, 20)
ar.move(20, 30)
################################
sl = QLabel(x)
sl.setText("Serial")
sl.move(10, 60)
s = QComboBox(x)
s.addItem("None")
s.addItem("9600")
s.addItem("115200")
s.resize(90, 20)
s.move(20, 80)
########## Digital PINS #########
digl = QLabel(x)
digl.setText("Digital Pins")
digl.move(160, 10)

l0 = QLabel(x)
l0.setText("Pin 0")
l0.move(140, 40)
cb0 = QComboBox(x)
cb0.addItem("None")
cb0.addItem("Input")
cb0.addItem("Output")
cb0.resize(70, 16)
cb0.move(180, 40)
################################
l1 = QLabel(x)
l1.setText("Pin 1")
l1.move(140, 60)
cb1 = QComboBox(x)
cb1.addItem("None")
cb1.addItem("Input")
cb1.addItem("Output")
cb1.resize(70, 16)
cb1.move(180, 60)
################################
l2 = QLabel(x)
l2.setText("Pin 2")
l2.move(140, 80)
cb2 = QComboBox(x)
cb2.addItem("None")
cb2.addItem("Input")
cb2.addItem("Output")
cb2.resize(70, 16)
cb2.move(180, 80)
################################
l3 = QLabel(x)
l3.setText("Pin 3 ~")
l3.move(140, 100)
cb3 = QComboBox(x)
cb3.addItem("None")
cb3.addItem("Input")
cb3.addItem("Output")
cb3.resize(70, 16)
cb3.move(180, 100)
################################
l4 = QLabel(x)
l4.setText("Pin 4")
l4.move(140, 120)
cb4 = QComboBox(x)
cb4.addItem("None")
cb4.addItem("Input")
cb4.addItem("Output")
cb4.resize(70, 16)
cb4.move(180, 120)
################################
l5 = QLabel(x)
l5.setText("Pin 5 ~")
l5.move(140, 140)
cb5 = QComboBox(x)
cb5.addItem("None")
cb5.addItem("Input")
cb5.addItem("Output")
cb5.resize(70, 16)
cb5.move(180, 140)
################################
l6 = QLabel(x)
l6.setText("Pin 6 ~")
l6.move(140, 160)
cb6 = QComboBox(x)
cb6.addItem("None")
cb6.addItem("Input")
cb6.addItem("Output")
cb6.resize(70, 16)
cb6.move(180, 160)
################################
l7 = QLabel(x)
l7.setText("Pin 7")
l7.move(140, 180)
cb7 = QComboBox(x)
cb7.addItem("None")
cb7.addItem("Input")
cb7.addItem("Output")
cb7.resize(70, 16)
cb7.move(180, 180)
################################
l8 = QLabel(x)
l8.setText("Pin 8")
l8.move(140, 200)
cb8 = QComboBox(x)
cb8.addItem("None")
cb8.addItem("Input")
cb8.addItem("Output")
cb8.resize(70, 16)
cb8.move(180, 200)
################################
l9 = QLabel(x)
l9.setText("Pin 9 ~")
l9.move(140, 220)
cb9 = QComboBox(x)
cb9.addItem("None")
cb9.addItem("Input")
cb9.addItem("Output")
cb9.resize(70, 16)
cb9.move(180, 220)
################################
l10 = QLabel(x)
l10.setText("Pin 10~")
l10.move(140, 240)
cb10 = QComboBox(x)
cb10.addItem("None")
cb10.addItem("Input")
cb10.addItem("Output")
cb10.resize(70, 16)
cb10.move(180, 240)
################################
l11 = QLabel(x)
l11.setText("Pin 11~")
l11.move(140, 260)
cb11 = QComboBox(x)
cb11.addItem("None")
cb11.addItem("Input")
cb11.addItem("Output")
cb11.resize(70, 16)
cb11.move(180, 260)
################################
l12 = QLabel(x)
l12.setText("Pin 12")
l12.move(140, 280)
cb12 = QComboBox(x)
cb12.addItem("None")
cb12.addItem("Input")
cb12.addItem("Output")
cb12.resize(70, 16)
cb12.move(180, 280)
################################
l13 = QLabel(x)
l13.setText("Pin 13")
l13.move(140, 300)
cb13 = QComboBox(x)
cb13.addItem("None")
cb13.addItem("Input")
cb13.addItem("Output")
cb13.resize(70, 16)
cb13.move(180, 300)

################################

########## Analog PINS ###############
al = QLabel(x)
al.setText("Analog Pins")
al.move(290, 10)

l14 = QLabel(x)
l14.setText("Pin 0")
l14.move(270, 40)
cb14 = QComboBox(x)
cb14.addItem("None")
cb14.addItem("Input")
cb14.addItem("Output")
cb14.resize(70, 16)
cb14.move(310, 40)
################################
l15 = QLabel(x)
l15.setText("Pin 1")
l15.move(270, 60)
cb15 = QComboBox(x)
cb15.addItem("None")
cb15.addItem("Input")
cb15.addItem("Output")
cb15.resize(70, 16)
cb15.move(310, 60)
################################
l16 = QLabel(x)
l16.setText("Pin 2")
l16.move(270, 80)
cb16 = QComboBox(x)
cb16.addItem("None")
cb16.addItem("Input")
cb16.addItem("Output")
cb16.resize(70, 16)
cb16.move(310, 80)
################################
l17 = QLabel(x)
l17.setText("Pin 3")
l17.move(270, 100)
cb17 = QComboBox(x)
cb17.addItem("None")
cb17.addItem("Input")
cb17.addItem("Output")
cb17.resize(70, 16)
cb17.move(310, 100)
################################
l18 = QLabel(x)
l18.setText("Pin 4")
l18.move(270, 120)
cb18 = QComboBox(x)
cb18.addItem("None")
cb18.addItem("Input")
cb18.addItem("Output")
cb18.resize(70, 16)
cb18.move(310, 120)
################################
l19 = QLabel(x)
l19.setText("Pin 5")
l19.move(270, 140)
cb19 = QComboBox(x)
cb19.addItem("None")
cb19.addItem("Input")
cb19.addItem("Output")
cb19.resize(70, 16)
cb19.move(310, 140)


###################################################

### Digital pins
cb0 .currentIndexChanged.connect(lambda:pin('0',0))
cb1 .currentIndexChanged.connect(lambda:pin('1',1))
cb2 .currentIndexChanged.connect(lambda:pin('2',2))
cb3 .currentIndexChanged.connect(lambda:pin('3',3))
cb4 .currentIndexChanged.connect(lambda:pin('4',4))
cb5 .currentIndexChanged.connect(lambda:pin('5',5))
cb6 .currentIndexChanged.connect(lambda:pin('6',6))
cb7 .currentIndexChanged.connect(lambda:pin('7',7))
cb8 .currentIndexChanged.connect(lambda:pin('8',8))
cb9 .currentIndexChanged.connect(lambda:pin('9',9))
cb10.currentIndexChanged.connect(lambda:pin('10',10))
cb11.currentIndexChanged.connect(lambda:pin('11',11))
cb12.currentIndexChanged.connect(lambda:pin('12',12))
cb13.currentIndexChanged.connect(lambda:pin('13',13))
### Analog pins
cb14.currentIndexChanged.connect(lambda:pin('A0',14))
cb15.currentIndexChanged.connect(lambda:pin('A1',15))
cb16.currentIndexChanged.connect(lambda:pin('A2',16))
cb17.currentIndexChanged.connect(lambda:pin('A3',17))
cb18.currentIndexChanged.connect(lambda:pin('A4',18))
cb19.currentIndexChanged.connect(lambda:pin('A5',19))
### Serial
s.currentIndexChanged.connect(lambda:pin(s.currentText(),20))


####### Tab Loop

class pwm:
    p = 0
    pb = 0
    def __init__(self,y,px,py,pbx,pby):
        if (px == None) and (py == None) :
            self.pb = QPushButton(y)
            self.pb.setText("+")
            self.pb.resize(16,16)
            self.pb.move(pbx,pby)
        else :
            self.p = QLineEdit(y)
            self.pb = QPushButton(y)
            self.p.setText("0")
            self.p.resize(40, 16)
            self.p.move(px, py)
            self.pb.setText("+")
            self.pb.resize(16, 16)
            self.pb.move(pbx, pby)


# Delay
dll = QLabel(y)
dll.setText("Delay")
dll.move(10, 10)
dl = QLineEdit(y)
dl.resize(50, 23)
dl.move(20, 30)

sec = QComboBox(y)
sec.addItem("ms")
sec.addItem("s")
sec.resize(40, 23)
sec.move(80, 30)

db = QPushButton(y)
db.setText("Add Delay")
db.move(30,60)

# Serial Read/Write
srwl = QLabel(y)
srwl.setText("Serial")
srwl.move(10,90)
srw = QComboBox(y)
srw.addItem("None")
srw.resize(70,20)
srw.move(20,110)

sp = QLineEdit(y)
sp.resize(105,20)
sp.move(20,135)

srwb = QPushButton(y)
srwb.setText("Add")
srwb.resize(30,20)
srwb.move(95,110)


sm = QPushButton(y)
sm.setText("Serial Monitor")
sm.move(30,160)

sm.clicked.connect(SerialMonitor)

########## Digital PINS #########
digl = QLabel(y)
digl.setText("Digital Pins")
digl.move(160, 10)

l0 = QLabel(y)
l0.setText("Pin 0")
l0.move(140, 40)
lp0 = QComboBox(y)
lp0.addItem("None")
lp0.resize(70, 16)
lp0.move(180, 40)

b0 = pwm(y,None,None,255,40)

################################
l1 = QLabel(y)
l1.setText("Pin 1")
l1.move(140, 60)
lp1 = QComboBox(y)
lp1.addItem("None")
lp1.resize(70, 16)
lp1.move(180, 60)

b1 = pwm(y,None,None,255,60)

################################
l2 = QLabel(y)
l2.setText("Pin 2")
l2.move(140, 80)
lp2 = QComboBox(y)
lp2.addItem("None")
lp2.resize(70, 16)
lp2.move(180, 80)

b2 = pwm(y,None,None,255,80)

################################
l3 = QLabel(y)
l3.setText("Pin 3 ~")
l3.move(140, 100)
lp3 = QComboBox(y)
lp3.addItem("None")
lp3.resize(70, 16)
lp3.move(180, 100)

pwm0 = pwm(y,255,100,300,100)

################################
l4 = QLabel(y)
l4.setText("Pin 4")
l4.move(140, 120)
lp4 = QComboBox(y)
lp4.addItem("None")
lp4.resize(70, 16)
lp4.move(180, 120)

b4 = pwm(y,None,None,255,120)

################################
l5 = QLabel(y)
l5.setText("Pin 5 ~")
l5.move(140, 140)
lp5 = QComboBox(y)
lp5.addItem("None")
lp5.resize(70, 16)
lp5.move(180, 140)

pwm1 = pwm(y,255,140,300,140)

################################
l6 = QLabel(y)
l6.setText("Pin 6 ~")
l6.move(140, 160)
lp6 = QComboBox(y)
lp6.addItem("None")
lp6.resize(70, 16)
lp6.move(180, 160)

pwm2 = pwm(y,255,160,300,160)

################################
l7 = QLabel(y)
l7.setText("Pin 7")
l7.move(140, 180)
lp7 = QComboBox(y)
lp7.addItem("None")
lp7.resize(70, 16)
lp7.move(180, 180)

b7 = pwm(y,None,None,255,180)

################################
l8 = QLabel(y)
l8.setText("Pin 8")
l8.move(140, 200)
lp8 = QComboBox(y)
lp8.addItem("None")
lp8.resize(70, 16)
lp8.move(180, 200)

b8 = pwm(y,None,None,255,200)

################################
l9 = QLabel(y)
l9.setText("Pin 9 ~")
l9.move(140, 220)
lp9 = QComboBox(y)
lp9.addItem("None")
lp9.resize(70, 16)
lp9.move(180, 220)

pwm3 = pwm(y,255,220,300,220)

################################
l10 = QLabel(y)
l10.setText("Pin 10~")
l10.move(140, 240)
lp10 = QComboBox(y)
lp10.addItem("None")
lp10.resize(70, 16)
lp10.move(180, 240)

pwm4 = pwm(y,255,240,300,240)

################################
l11 = QLabel(y)
l11.setText("Pin 11~")
l11.move(140, 260)
lp11 = QComboBox(y)
lp11.addItem("None")
lp11.resize(70, 16)
lp11.move(180, 260)

pwm5 = pwm(y,255,260,300,260)

################################
l12 = QLabel(y)
l12.setText("Pin 12")
l12.move(140, 280)
lp12 = QComboBox(y)
lp12.addItem("None")
lp12.resize(70, 16)
lp12.move(180, 280)

b12 = pwm(y,None,None,255,280)

################################
l13 = QLabel(y)
l13.setText("Pin 13")
l13.move(140, 300)
lp13 = QComboBox(y)
lp13.addItem("None")
lp13.resize(70, 16)
lp13.move(180, 300)

b13 = pwm(y,None,None,255,300)

################################

########## Analog PINS ###############
al = QLabel(y)
al.setText("Analog Pins")
al.move(352, 10)

l14 = QLabel(y)
l14.setText("Pin 0")
l14.move(326, 40)
lp14 = QComboBox(y)
lp14.addItem("None")
lp14.resize(70, 16)
lp14.move(356, 40)

pwm6 = pwm(y,431,40,476,40)

################################
l15 = QLabel(y)
l15.setText("Pin 1")
l15.move(326, 60)
lp15 = QComboBox(y)
lp15.addItem("None")
lp15.resize(70, 16)
lp15.move(356, 60)

pwm7 = pwm(y,431,60,476,60)

################################
l16 = QLabel(y)
l16.setText("Pin 2")
l16.move(326, 80)
lp16 = QComboBox(y)
lp16.addItem("None")
lp16.resize(70, 16)
lp16.move(356, 80)

pwm8 = pwm(y,431,80,476,80)

################################
l17 = QLabel(y)
l17.setText("Pin 3")
l17.move(326, 100)
lp17 = QComboBox(y)
lp17.addItem("None")
lp17.resize(70, 16)
lp17.move(356, 100)

pwm9 = pwm(y,431,100,476,100)

################################
l18 = QLabel(y)
l18.setText("Pin 4")
l18.move(326, 120)
lp18 = QComboBox(y)
lp18.addItem("None")
lp18.resize(70, 16)
lp18.move(356, 120)

pwm10 = pwm(y,431,120,476,120)

################################
l19 = QLabel(y)
l19.setText("Pin 5")
l19.move(326, 140)
lp19 = QComboBox(y)
lp19.addItem("None")
lp19.resize(70, 16)
lp19.move(356, 140)

pwm11 = pwm(y,431,140,476,140)


################################### LCD Tab #########################

lcdl = QLabel(z)
lcdl.setText("Activate LCD")
lcdl.move(20, 20)


lcdchb = QCheckBox(z)
lcdchb.move(85, 20)




###################################################

# Digital pins
b0 .pb.clicked.connect(lambda:pinrw("0",30))
b1 .pb.clicked.connect(lambda:pinrw("1",31))
b2 .pb.clicked.connect(lambda:pinrw("2",32))

pwm0.pb.clicked.connect(lambda:pinrw("3",33))

b4 .pb.clicked.connect(lambda:pinrw("4",34))

pwm1.pb.clicked.connect(lambda:pinrw("5",35))
pwm2.pb.clicked.connect(lambda:pinrw("6",36))

b7 .pb.clicked.connect(lambda:pinrw("7",37))
b8 .pb.clicked.connect(lambda:pinrw("8",38))

pwm3.pb.clicked.connect(lambda:pinrw("9",39))
pwm4.pb.clicked.connect(lambda:pinrw("10",40))
pwm5.pb.clicked.connect(lambda:pinrw("11",41))

b12.pb.clicked.connect(lambda:pinrw("12",42))
b13.pb.clicked.connect(lambda:pinrw("13",43))

# Analog Pins
pwm6.pb.clicked.connect(lambda:pinrw("A0",44))
pwm7.pb.clicked.connect(lambda:pinrw("A1",45))
pwm8.pb.clicked.connect(lambda:pinrw("A2",46))
pwm9.pb.clicked.connect(lambda:pinrw("A3",47))
pwm10.pb.clicked.connect(lambda:pinrw("A4",48))
pwm11.pb.clicked.connect(lambda:pinrw("A5",49))

# Delay
db.clicked.connect(lambda:pinrw(dl.text(),50))

# Serial Read/Write
srwb.clicked.connect(lambda:pinrw(sp.text(),51))

# Serial Monitor



def pinrw(pn,id):
    if id == 30 :
        if lp0.currentText() == "None" :
            txt = ''
        elif lp0.currentText() == "Digital Read" :
            txt = "digitalRead(%s);\n" %pn
        elif lp0.currentText() == "Analog Read" :
            txt = "analogRead(%s);\n" %pn
        elif lp0.currentText() == "High" :
            txt = "digitalWrite(%s,HIGH);\n" %pn
        elif lp0.currentText() == "LOW" :
            txt = "digitalWrite(%s,LOW);\n" %pn
        elif lp0.currentText() == "PWM" :
            txt = "analogWrite(%s,%d);\n" %pn %int(pwm0.p.text())
    elif id == 31 :
        if lp1.currentText() == "None" :
            txt = ''
        elif lp1.currentText() == "Digital Read" :
            txt = "digitalRead(%s);\n" %pn
        elif lp1.currentText() == "Analog Read" :
            txt = "analogRead(%s);\n" %pn
        elif lp1.currentText() == "High" :
            txt = "digitalWrite(%s,HIGH);\n" %pn
        elif lp1.currentText() == "LOW" :
            txt = "digitalWrite(%s,LOW);\n" %pn
    elif id == 32 :
        if lp2.currentText() == "None" :
            txt = ''
        elif lp2.currentText() == "Digital Read" :
            txt = "digitalRead(%s);\n" %pn
        elif lp2.currentText() == "Analog Read" :
            txt = "analogRead(%s);\n" %pn
        elif lp2.currentText() == "High" :
            txt = "digitalWrite(%s,HIGH);\n" %pn
        elif lp2.currentText() == "LOW" :
            txt = "digitalWrite(%s,LOW);\n" %pn
    elif id == 33:
        if lp3.currentText() == "None":
            txt = ''
        elif lp3.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp3.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp3.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp3.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp3.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm0.p.text())
    elif id == 34:
        if lp4.currentText() == "None":
            txt = ''
        elif lp4.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp4.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp4.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp4.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
    elif id == 35:
        if lp5.currentText() == "None":
            txt = ''
        elif lp5.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp5.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp5.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp5.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp5.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm1.p.text())
    elif id == 36:
        if lp6.currentText() == "None":
            txt = ''
        elif lp6.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp6.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp6.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp6.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp6.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm2.p.text())
    elif id == 37:
        if lp7.currentText() == "None":
            txt = ''
        elif lp7.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp7.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp7.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp7.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
    elif id == 38:
        if lp8.currentText() == "None":
            txt = ''
        elif lp8.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp8.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp8.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp8.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
    elif id == 39:
        if lp9.currentText() == "None":
            txt = ''
        elif lp9.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp9.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp9.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp9.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp9.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm3.p.text())
    elif id == 40:
        if lp10.currentText() == "None":
            txt = ''
        elif lp10.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp10.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp10.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp10.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp10.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm4.p.text())
    elif id == 41:
        if lp11.currentText() == "None":
            txt = ''
        elif lp11.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp11.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp11.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp11.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp11.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm5.p.text())
    elif id == 42:
        if lp12.currentText() == "None":
            txt = ''
        elif lp12.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp12.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp12.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp12.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
    elif id == 43:
        if lp13.currentText() == "None":
            txt = ''
        elif lp13.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp13.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp13.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp13.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn

    elif id == 44:
        if lp14.currentText() == "None":
            txt = ''
        elif lp14.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp14.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp14.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp14.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp14.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm6.p.text())
    elif id == 45:
        if lp15.currentText() == "None":
            txt = ''
        elif lp15.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp15.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp15.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp15.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp15.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm7.p.text())
    elif id == 46:
        if lp16.currentText() == "None":
            txt = ''
        elif lp16.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp16.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp16.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp16.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp16.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm8.p.text())
    elif id == 47:
        if lp17.currentText() == "None":
            txt = ''
        elif lp17.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp17.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp17.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp17.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp17.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm9.p.text())
    elif id == 48:
        if lp18.currentText() == "None":
            txt = ''
        elif lp18.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp18.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp18.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp18.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp18.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm10.p.text())
    elif id == 49:
        if lp19.currentText() == "None":
            txt = ''
        elif lp19.currentText() == "Digital Read":
            txt = "digitalRead(%s);\n" % pn
        elif lp19.currentText() == "Analog Read":
            txt = "analogRead(%s);\n" % pn
        elif lp19.currentText() == "High":
            txt = "digitalWrite(%s,HIGH);\n" % pn
        elif lp19.currentText() == "LOW":
            txt = "digitalWrite(%s,LOW);\n" % pn
        elif lp19.currentText() == "PWM":
            txt = "analogWrite(%s,%d);\n" % pn % int(pwm11.p.text())
    elif id == 50 :
        if sec.currentText() == "ms" :
            txt = "delay(%d);\n" %int(dl.text())
        elif sec.currentText() == "s" :
            txt = "delay(%d);\n" %(int(dl.text())*1000)
    elif id == 51 :
        if srw.currentText() == "None" :
            txt = ''
        elif srw.currentText() == "Print" :
            txt = 'Serial.println("%s");\n' %pn
        elif srw.currentText() == "Read" :
            txt = "Serial.read();\n"



    f = open(inopath, 'r')
    d = f.readlines()
    f.close()
    f = []
    k = 0
    while (k < len(d)):
        if d[k] == "void loop(){\n":
            while (k < len(d)):
                f.append(d[k])
                d[k] = ''
                k += 1
        else:
            k += 1


    j = 0
    for i in f:
        if i == '\n':
            f[j] = txt
            f = atosl(f, '\n', j + 1)
            break
        else:
            j += 1

    d+=f
    pt.setPlainText(''.join(d))
    f = open(inopath, 'w')
    f.writelines(d)
    f.close()



mw.show()
sys.exit(app.exec_())

