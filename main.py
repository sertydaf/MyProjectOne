import sys
import io
import sqlite3

from res_rc import *
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
    <width>984</width>
    <height>607</height>
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
      <x>0</x>
      <y>330</y>
      <width>331</width>
      <height>61</height>
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
      <x>340</x>
      <y>110</y>
      <width>301</width>
      <height>121</height>
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
background-color: rgb(185, 185, 185);
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
      <x>0</x>
      <y>-10</y>
      <width>981</width>
      <height>121</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
font: 75 14pt &quot;MS Shell Dlg 2&quot;;
border-radius: 10px;
border: 2px solid rgba(0, 0, 0, 230);
border-color:  rgb(0, 0, 0);
border-image: url(:/pictures/Название игры.png)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>110</y>
      <width>331</width>
      <height>71</height>
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
background-color: rgb(185, 185, 185);
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
      <x>650</x>
      <y>110</y>
      <width>331</width>
      <height>71</height>
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
      <x>640</x>
      <y>390</y>
      <width>341</width>
      <height>171</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image: url(:/pictures/Прогресс.png)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>330</y>
      <width>331</width>
      <height>61</height>
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
     <string>               Прогресс: 0/100</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>650</x>
      <y>190</y>
      <width>321</width>
      <height>131</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/Цель.png)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>240</y>
      <width>301</width>
      <height>321</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/Копать.png)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>190</y>
      <width>321</width>
      <height>131</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image: url(:/pictures/Магазин.png)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>400</y>
      <width>331</width>
      <height>161</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image: url(:/pictures/Баланс.png)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <zorder>pushButton</zorder>
   <zorder>label_10</zorder>
   <zorder>pushButton_2</zorder>
   <zorder>label_2</zorder>
   <zorder>label_3</zorder>
   <zorder>label</zorder>
   <zorder>label_5</zorder>
   <zorder>label_4</zorder>
   <zorder>label_6</zorder>
   <zorder>label_7</zorder>
   <zorder>label_8</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>984</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
"""

template1 = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Shop</class>
 <widget class="QMainWindow" name="Shop">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>770</width>
    <height>533</height>
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
      <y>80</y>
      <width>381</width>
      <height>61</height>
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
      <y>150</y>
      <width>381</width>
      <height>61</height>
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
      <y>220</y>
      <width>381</width>
      <height>61</height>
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
      <y>290</y>
      <width>381</width>
      <height>61</height>
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
      <height>61</height>
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
      <y>430</y>
      <width>381</width>
      <height>61</height>
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
      <y>80</y>
      <width>181</width>
      <height>61</height>
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
      <y>150</y>
      <width>181</width>
      <height>61</height>
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
      <y>220</y>
      <width>181</width>
      <height>61</height>
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
      <y>290</y>
      <width>181</width>
      <height>61</height>
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
      <height>61</height>
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
      <y>430</y>
      <width>181</width>
      <height>61</height>
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
      <y>80</y>
      <width>181</width>
      <height>61</height>
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
      <y>150</y>
      <width>181</width>
      <height>61</height>
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
      <y>220</y>
      <width>181</width>
      <height>61</height>
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
      <y>290</y>
      <width>181</width>
      <height>61</height>
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
      <height>61</height>
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
      <y>430</y>
      <width>181</width>
      <height>61</height>
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
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>761</width>
      <height>71</height>
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
     <string>                                                      Магазин</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>770</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


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
        self.progress = 0
        self.cel = 100
        self.upgrade_kol1 = 0
        self.upgrade_kol2 = 0
        self.upgrade_kol3 = 0
        self.upgrade_kol4 = 0
        self.upgrade_kol5 = 0
        self.upgrade_kol6 = 0
        self.upgrade_cost1 = 0
        self.upgrade_cost2 = 0
        self.upgrade_cost3 = 0
        self.upgrade_cost4 = 0
        self.upgrade_cost5 = 0
        self.upgrade_cost6 = 0


    def Sql(self):
        self.con = sqlite3.connect("MyProgectOne.sqlite")
        cur = self.con.cursor()
        self.result = cur.execute("""SELECT * FROM name""").fetchall()

    def initUI(self):
        self.pushButton.clicked.connect(self.Balance)
        self.pushButton_2.clicked.connect(self.open_shop)
        self.pushButton.clicked.connect(self.Progress)
        self.pushButton.clicked.connect(self.Cel)

    def Balance(self):
        self.money += 1
        self.label.setText('    Баланс: ' + str(self.money))

    def Progress(self):
        self.progress += 1
        if self.progress != self.cel:
            self.label_5.setText('               Прогресс: ' + str(self.progress) + '/' + str(self.cel))
        else:
            self.money *= 2
            self.cel *= 2
            self.label_5.setText('               Прогресс: ' + str(self.progress) + '/' + str(self.cel))

    def Cel(self):
        self.label_2.setText('Цель: нажать на кнопку "Копать" ' + str(self.cel) + ' раз')

    def open_shop(self):
        self.app1 = Shop()
        self.app1.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
