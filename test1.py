from PySide2.QtWidgets import QApplication, QMessageBox,QFileDialog,QMenu,QAction,QTabWidget
from PySide2.QtUiTools import QUiLoader
import sys
from suds.client import Client
import time
import xmltodict
import json
try:
# client = Client("http://172.16.11.15:8891/pacsServices/services/pacsServices?wsdl",proxy={'http':'http://rejion.ticp.net:24142'})     
    client = Client("http://172.16.11.15:8891/pacsServices/services/pacsServices?wsdl") 

except:
    client = Client("http://172.16.11.15:8891/pacsServices/services/pacsServices?wsdl",proxy={'http':'http://rejion.ticp.net:24142'})
class newindow():
    def __init__(self):     
        self.ui1 = QUiLoader().load('d:\code\qt\http2.ui')
        self.ui1.show()
        pushButton1 = self.ui1.pushButton
        pushButton1.clicked.connect(self.checkhis)
        pushButton2 = self.ui1.pushButton_2
        pushButton2.clicked.connect(self.closewin)
        pushButton3 = self.ui1.pushButton_3
        pushButton3.clicked.connect(self.back)
        label2 = self.ui1.label_2
        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label2.setOpenExternalLinks(True)
        label2.setText("<a href='https://www.94linux.top'>关于本人</a>")
        label2.setToolTip('这是一个超级链接')
    def Window(self):
        self.newView = newindow()
        return self.newView
        
    def checkhis(self):
        combox1 = self.ui1.comboBox
        hisnum = combox1.currentIndex() + 1
        textbro = self.ui1.textBrowser
        # print(hisnum)
        reqid = self.ui1.lineEdit.text()
        xmlstr = ('''<?xml version="1.0" encoding="UTF-8"?> <sqdinfo> <PatientSource>%s</PatientSource> <RequestID>%s</RequestID> </sqdinfo>''' % (hisnum,reqid))
        result =  client.service.querySQDByXml(xmlstr)
        ###格式化输出
        jsdata=json.dumps(dict(xmltodict.parse(result)) ,ensure_ascii=False)
        cdata=json.loads(jsdata)
        try:
            #住院病人提取
 
            textda = "姓名:" + cdata['sqdinfo']['name'] + "\n" + "住院号/门诊号:"+ cdata['sqdinfo']['patientid'] +  "\n" + "开单科室:" + cdata['sqdinfo']['studydept'] + "\n" + "执行科室编号:" + cdata['sqdinfo']['zxkscode'] + "\n"
            textbro.setText(textda)

        except:
            textbro.setText(result)

#关闭窗体
    def closewin(self):
        self.ui1.close()

#退费功能
    def back(self):
        textbro = self.ui1.textBrowser
        reqid = self.ui1.lineEdit.text()
        combox1 = self.ui1.comboBox
        hisnum = combox1.currentIndex() + 1
        xmlstr = ('''<?xml version="1.0" encoding="UTF-8"?> <sqdInfo> <PatientSource>%s</PatientSource> <RequestID>%s</RequestID> <jczt>-1</jczt> </sqdInfo>''' % (hisnum,reqid))
        result =  client.service.changeSQDState(xmlstr)
        textbro.setText(result)