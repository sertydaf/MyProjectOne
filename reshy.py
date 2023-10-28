import sys
import io

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QLCDNumber

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Menu</class>
 <widget class="QMainWindow" name="Menu">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>749</width>
    <height>354</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(255, 255, 255);</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>110</y>
      <width>211</width>
      <height>91</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>    Баланс: 0</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>210</y>
      <width>211</width>
      <height>101</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(175, 255, 125);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Копать</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>0</y>
      <width>731</width>
      <height>101</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>                              Игра &quot;Копатель онлайн&quot; </string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>171</width>
      <height>201</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(175, 255, 125);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Магазин</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>110</y>
      <width>331</width>
      <height>91</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 10pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Цель: нажать на кнопку &quot;Копать&quot; 100 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>210</y>
      <width>331</width>
      <height>101</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Прогресс: 0/100</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>749</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""


template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Shop</class>
 <widget class="QMainWindow" name="Shop">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>572</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton_5">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>381</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(158, 158, 158);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Улучшить количество работника(ов)</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_6">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>90</y>
      <width>381</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(158, 158, 158);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Улучшить скорость работника(ов)</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_7">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>180</y>
      <width>381</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(158, 158, 158);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Улучшить умения работника(ов)</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_8">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>270</y>
      <width>381</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(158, 158, 158);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Улучшить оборудование работника(ов)</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_9">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>360</y>
      <width>381</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(158, 158, 158);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Улучшить условия для работы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_10">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>450</y>
      <width>381</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
}

QPushButton:hover {
background-color: rgb(158, 158, 158);
color: black;
border-radius: 10px;
border-color:  rgb(0, 0, 0)
}</string>
    </property>
    <property name="text">
     <string>Купить &quot;super&quot; работника</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>0</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Куплено: 0 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>90</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Куплено: 0 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>180</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Куплено: 0 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_12">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>270</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Куплено: 0 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_13">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>360</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Куплено: 0 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_14">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>450</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)</string>
    </property>
    <property name="text">
     <string>Куплено: 0 раз</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>0</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
</string>
    </property>
    <property name="text">
     <string>Стоимость: 0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>90</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
</string>
    </property>
    <property name="text">
     <string>Стоимость: 0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>180</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
</string>
    </property>
    <property name="text">
     <string>Стоимость: 0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_15">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>270</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
</string>
    </property>
    <property name="text">
     <string>Стоимость: 0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_16">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>360</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
</string>
    </property>
    <property name="text">
     <string>Стоимость: 0</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_17">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>450</y>
      <width>181</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0)
</string>
    </property>
    <property name="text">
     <string>Стоимость: 0</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>"""



class Shop(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template1)
        uic.loadUi(f, self)


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()
        self.money = 0

    def initUI(self):
        self.pushButton.clicked.connect(self.eva)
        self.pushButton_2.clicked.connect(self.open_shop)

    def eva(self):
        self.money += 1
        self.label.setText('Баланс: ' + str(self.money))

    def open_shop(self):
        self.app1 = Shop()
        self.app1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
