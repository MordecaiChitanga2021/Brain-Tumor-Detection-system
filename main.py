from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2
import imutils
import os
import datetime
import time
import shutil
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets


# splashscreen display
class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 500)
        self.setStyleSheet('''
                #title_label {
                    font-size: 50px;
                    color: skyblue;
                    font-family: Bauhaus 93, sans-serif;
                }
                #desc_label {
                    font-size: 20px;
                    color: skyblue;
                    font-family: Bauhaus 93, sans-serif;
                }
                #loading_label {
                    font-size: 30px;
                    color: skyblue;
                    font-family: Bauhaus 93, sans-serif;
                }
                QFrame {
                    background-image: url("SplashScreen.png");
                    border-top-left-radius: 50px;
                    
                }
                QProgressBar {
                    background-color: #ccc;
                    color: #c8c8c8;
                    border-style: none;
                    border-radius: 2px;
                    text-align: center;
                    font-size: 15px;
                }
                QProgressBar::chunk {
                    border-radius: 50px;
                    padding: 25px;

                    background-color: lightblue;
                }
        ''')
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.counter = 0
        self.n = 100
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        # layout to display splash screen frame
        layout = QVBoxLayout()
        self.setLayout(layout)
        # splash screen frame
        self.frame = QFrame()
        layout.addWidget(self.frame)
        # splash screen title
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName('title_label')
        self.title_label.resize(690, 120)
        self.title_label.move(0, 5)  # x, y
        self.title_label.setText('Brain Tumour')
        self.title_label.setAlignment(Qt.AlignCenter)
        # splash screen title description
        self.description_label = QLabel(self.frame)
        self.description_label.resize(690, 40)
        self.description_label.move(0, self.title_label.height())
        self.description_label.setObjectName('desc_label')
        self.description_label.setText('<b>Detection</b>')
        self.description_label.setAlignment(Qt.AlignCenter)
        # splash screen pogressbar
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, 180)  # self.description_label.y()+130
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        # splash screen loading label
        self.loading_label = QLabel(self.frame)
        self.loading_label.resize(self.width() - 10, 50)
        self.loading_label.move(0, self.progressBar.y() + 70)
        self.loading_label.setObjectName('loading_label')
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setText('Loading...')

    def loading(self):
        # set progressbar value
        self.progressBar.setValue(self.counter)
        # stop progress if counter
        # is greater than n and
        # display main window app
        if self.counter >= self.n:
            self.timer.stop()
            self.close()
            time.sleep(1)
            MainWindow.show()
        self.counter += 0.2
# end of splash screen display

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1121, 591))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 251, 281))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 251, 281))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 290, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(560, 10, 261, 281))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 290, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(840, 10, 261, 281))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(840, 290, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(380, 340, 301, 211))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setObjectName("label_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 430, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 341, 261))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(440, 30, 341, 261))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setObjectName("label_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 300, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(440, 300, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(8)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_5.clicked.connect(self.scan2) # type: ignore
        self.pushButton_4.clicked.connect(self.edgedetection) # type: ignore
        self.pushButton.clicked.connect(self.loadimage2) # type: ignore
        self.pushButton_3.clicked.connect(self.morphology) # type: ignore
        self.pushButton_2.clicked.connect(self.thresholding) # type: ignore
        self.pushButton_6.clicked.connect(self.loadimage) # type: ignore
        self.pushButton_7.clicked.connect(self.scan) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.filename = None
        self.tmp = None
    # Full scan view
    # setting photo to view in QDesigner
    def setPhoto2(self, image):
        self.tmp = image
        image = imutils.resize(image, width=220)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    # scanning uploaded mri
    def scan2(self, img):
        self.tmp = img
        img = copy2
        image = cv2.imread(img)
        dim = (300, 200)
        image = imutils.resize(image, width=200)
        # Convert image to GrayScale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)
        # Apply thresholding
        (T, thresh) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)
        (T, threshInv) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY_INV)
        # Morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        closed = cv2.erode(closed, None, iterations=14)
        closed = cv2.dilate(closed, None, iterations=13)


        img_blur = cv2.GaussianBlur(closed, (3,3), 0)



        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

        def auto_canny(image, sigma=0.33):
            import numpy as np
            # compute the median of the single channel pixel intensities
            v = np.median(image)

            # apply automatic Canny edge detection using the computed median
            lower = int(max(0, (1.0 - sigma) * v))
            upper = int(min(255, (1.0 + sigma) * v))
            edged = cv2.Canny(image, lower, upper)

            # return the edged image
            return edged

        canny = auto_canny(closed)


        # Apply contours
        # extracting regions of interest



        (cnts, _) = cv2.findContours(edges, cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)


        finalimage = cv2.drawContours(image, cnts, -1, (0, 0, 255), 2)

        image = QImage(finalimage, finalimage.shape[1], finalimage.shape[0], finalimage.strides[0],
                       QImage.Format_RGB888)
        self.label_5.setPixmap(QtGui.QPixmap.fromImage(image))

    def loadimage2(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        self.image = cv2.imread(self.filename)
        self.setPhoto2(self.image)
        global mydir
        mydir = os.path.join(os.getcwd(), 'uploaded_images' ,datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(mydir)
        #save to database
        global copy2
        copy2 = shutil.copy(self.filename, mydir)
        if copy2:
            print("files have been copied successfully")
            print(copy2)
        else:
            print("There is a problem with the shutil module")

    def thresholding(self, img):
        self.tmp = img
        img = copy2
        img = cv2.imread(img)
        img = imutils.resize(img, width=220)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, 0.7)

        (T, thresh) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)
        self.setthresholdingimage(thresh)
        print(thresh)
        return thresh

    def setthresholdingimage(self, image):
        self.tmp = image
        image = imutils.resize(image, width=220)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))

    def morphology(self, img):
        self.tmp =img
        img = copy2
        img = cv2.imread(img)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
        closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        closed = cv2.erode(closed, None, iterations=14)
        closed = cv2.dilate(closed, None, iterations=13)
        self.setmorphologyimage(closed)
        return closed

    def setmorphologyimage(self, image):
        self.tmp = image
        image = imutils.resize(image, width=220)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_3.setPixmap(QtGui.QPixmap.fromImage(image))

    def edgedetection(self, img, sigma=0.33):
        self.tmp = img
        img = copy2
        img = cv2.imread(img)
        v = np.median(img)
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(img, lower, upper)
        self.setedgedetection(edged)
        return edged

    def setedgedetection(self, image):
        self.tmp = image
        image = imutils.resize(image, width=220)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_4.setPixmap(QtGui.QPixmap.fromImage(image))

#Quick Scan
    def loadimage(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        print(self.filename)
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)

        mydir = os.path.join(os.getcwd(),'quickscans' ,datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(mydir)
        global copy
        copy = shutil.copy(self.filename, mydir)
        if copy:
            print("files have been copied successfully")
            print(copy)
        else:
            print("There is a problem with the shutil module")

    def setPhoto(self, image):
        self.tmp = image
        image = imutils.resize(image, width=220)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_6.setPixmap(QtGui.QPixmap.fromImage(image))

    def scan(self, img):
        self.tmp = img
        img = copy
        image = cv2.imread(img)
        dim = (300, 200)
        image = imutils.resize(image, width=220)
        # Convert image to GrayScale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)
        # Apply thresholding
        (T, thresh) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)
        (T, threshInv) = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY_INV)
        # Morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        closed = cv2.erode(closed, None, iterations=14)
        closed = cv2.dilate(closed, None, iterations=13)

        def auto_canny(image, sigma=0.33):
            import numpy as np
            # compute the median of the single channel pixel intensities
            v = np.median(image)

            # apply automatic Canny edge detection using the computed median
            lower = int(max(0, (1.0 - sigma) * v))
            upper = int(min(255, (1.0 + sigma) * v))
            edged = cv2.Canny(image, lower, upper)

            # return the edged image
            return edged

        canny = auto_canny(closed)
        # Apply contoursz
        # reshape the image to a 2D array of pixels and 3 color values (RGB)
        #kmeans algorithm
        Z = canny.reshape((-1,3))

        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 8
        ret, label,center = cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((canny.shape))

        (cnts, _) = cv2.findContours(res2, cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)
        finalimage = cv2.drawContours(image, cnts, -1, (0, 0, 255), 2)

        image = QImage(finalimage, finalimage.shape[1], finalimage.shape[0], finalimage.strides[0],
                       QImage.Format_RGB888)
        self.label_7.setPixmap(QtGui.QPixmap.fromImage(image))

        def regionofinterest(self, img):
             #image_path
            self.tmp = img
            img = copy
            #read image
            img_raw = cv2.imread(img)
            #select ROI function
            roi = cv2.selectROI(img_raw)
            #print rectangle points of selected roi
            print(roi)
            #Crop selected roi from raw image
            roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
            #show cropped image
            cv2.imshow("ROI", roi_cropped)
            cv2.imwrite("crop.jpeg", roi_cropped)
            #hold window
            cv2.waitKey(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "load"))
        self.label.setText(_translate("MainWindow", "Load Image"))
        self.label_2.setText(_translate("MainWindow", "Thresholding"))
        self.pushButton_2.setText(_translate("MainWindow", "thresholding"))
        self.label_3.setText(_translate("MainWindow", "Morphology"))
        self.pushButton_3.setText(_translate("MainWindow", "morphology"))
        self.label_4.setText(_translate("MainWindow", "Edge Detection"))
        self.pushButton_4.setText(_translate("MainWindow", "edges"))
        self.label_5.setText(_translate("MainWindow", "Results"))
        self.pushButton_5.setText(_translate("MainWindow", "scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Scan"))
        self.label_6.setText(_translate("MainWindow", "LOAD MRI IMAGE"))
        self.label_7.setText(_translate("MainWindow", "SCANNED MRI IMAGE"))
        self.pushButton_6.setText(_translate("MainWindow", "LOAD"))
        self.pushButton_7.setText(_translate("MainWindow", "SCAN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Quick Scan"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec_())
