from PySide2.QtWidgets import QApplication, QMessageBox,QFileDialog,QMenu,QAction
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWebEngineWidgets import *
import test1
import requests
import json
from PySide2.QtCore import Signal,QObject
from threading import Thread
import sys
# from threading import Thread
# from time import sleep
import chardet
import os
class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('d:\code\qt\http.ui')
        # self.ui.comboBox.currentIndexChanged.connect(handleSelectionChange)
        #定义按钮按下时函数
        pushButton1 = self.ui.pushButton
        pushButton4 = self.ui.pushButton_4
        pushButton1.clicked.connect(self.test)
        pushButton4.clicked.connect(self.deltext)
        pushButton2 = self.ui.pushButton_2
        pushButton3 = self.ui.pushButton_3
        pushButton2.clicked.connect(self.additem)
        pushButton3.clicked.connect(self.delitem)
        pushButton5 = self.ui.pushButton_5
        pushButton5.clicked.connect(self.open)
        pushButton6 = self.ui.pushButton_6
        pushButton6.clicked.connect(self.save)
        text = self.ui.textEdit_2
        self.ui.lineEdit.setPlaceholderText('请在这里输入URL')
        his = self.ui.actionhis.triggered.connect(self.his)
        his = self.ui.actionhis.setShortcut('Ctrl+S')
        #新增关于按钮
        web = self.ui.menuBar().addAction(u"打开浏览器").triggered.connect(self.webgo)
        about = self.ui.menuBar().addAction(u"关于").triggered.connect(self.about)
       
        
    def test(self):
        combox1 = self.ui.comboBox
        get = combox1.currentText()
        url = self.ui.lineEdit.text()
        
        text = self.ui.textEdit_2
        table = self.ui.tableWidget
        a = 0 
        jsonlist1 = []
        jsonlist2 = []
        ##获取数据转成list打印
        for a in range(table.rowCount()):
            # table.item(a,a).text()
            # print(table.item(a,0).text())
            # print(table.item(a,1).text())
            jsonlist1.append(table.item(a,0).text())
            jsonlist2.append(table.item(a,1).text())
        #list转dict    
        # print(jsonlist1,jsonlist2)
        jsonlist= zip(jsonlist1,jsonlist2)
        data = dict(jsonlist)
        try:
            if combox1.currentText() == "get":
                req = requests.get(url,params=data)
                self.ui.textEdit_2.setText(str(req)+str(req.text)+str(req.content))
               
            else:
                combox1.currentText() == "post"
                req = requests.post(url,data=data)
                self.ui.textEdit_2.setText(str(req)+str(req.text)+str(req.content))
        except:
            self.ui.textEdit_2.setText("链接输入有误")

    def deltext(self):
        text = self.ui.textEdit_2
        text.clear()
        
    def additem(self):
        tablelite = self.ui.tableWidget.insertRow(0)
        a = 20
        return a
    def delitem(self):
        
        method = self.ui.tableWidget
        if method.currentRow() > -1:
            method.removeRow(method.currentRow())
            # print (method.currentRow())
        else:
            # print()
            method.removeRow(0)
    def open(self):
        text = self.ui.textEdit_2
        
        dialog = QFileDialog()
        # 设置文件过滤器，这里是任何文件，包括目录噢
        dialog.setFileMode(QFileDialog.AnyFile)
        # 设置显示文件的模式，这里是详细模式
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            # self.text.setText(fileNames[0])
            # print(fileNames[0])
            #自动读取编码避免文件异常
            f = open(fileNames[0],'rb')
            textdata=f.read()
            result = chardet.detect(textdata)
            # print(result["encoding"])
            b = (textdata.decode(result["encoding"]))
            f.close()
            text.setText(b)
    def save(self):
        # QFileDialog.getOpenFileName()    #获取一个打开文件的文件名
        # QFileDialog.getOpenFileNames()   #获取多个打开文件的文件名
        # QFileDialog.getOpenFileUrl()     #获取一个打开文件的统一资源定位符
        # QFileDialog.getOpenFileUrls()    #获取多个打开文件的统一资源定位符
        # QFileDialog.getSaveFileName()    #获取保存的文件名
        # QFileDialog.getSaveFileUrl()     #获取保存的url
        # ##保存文件
        dialog = QFileDialog()
        fileNames = dialog.getSaveFileName(None,'选择一个txt文件','./','ALL(*.*);;Images(*.png *.jpg);;txt文件(*.txt)','txt文件(*.txt)')
        print(fileNames[0])
       
        f = open(fileNames[0],'w')
        my_text=self.ui.textEdit_2.toPlainText()
        f.write(my_text)
        f.close()
    def about(self):
        # View.createWindow(self)
        msgBox = QMessageBox()

        msgBox.about(None, u'关于', u'BY Zore Lu')
       
        # QMessageBox().addButton(("Connect"))
        #新建窗口
    def his(self):
        test1.newindow.Window(self)

    def webgo(self):
        webView.createWindow(self)
        


#浏览器函数
class webView():
    def __init__(self,parent = None):
        super().__init__(parent)
        self.load(("https://www.baidu.com"))
        self.setWindowTitle("New Page")
        self.show()

    # 简单重载了下createWindow函数，实现鼠标点击链接在新窗口打开
    def createWindow(self):
        self.newView = webView()
        self.newView.resize(900,600)
        return self.newView



if __name__ =="__main__":     
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    sys.exit(app.exec_())
    