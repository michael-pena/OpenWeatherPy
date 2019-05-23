# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weathergui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys, requests, json

'''
TO DO:
1. add all weather conditions
2. add weather in "Dallas" label
3. add humidty label
4. add pressure label
5. fix the Temperature label to only 2 decimal points
'''


class Ui_OpenWeatherPy(object):
    def setupUi(self, OpenWeatherPy):
        OpenWeatherPy.setObjectName("OpenWeatherPy")
        OpenWeatherPy.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OpenWeatherPy)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 460, 87, 29))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(250, 460, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.label_cityname = QtWidgets.QLabel(self.centralwidget)
        self.label_cityname.setGeometry(QtCore.QRect(150, 470, 91, 20))
        self.label_cityname.setObjectName("label_cityname")
        self.label_currentWeather = QtWidgets.QLabel(self.centralwidget)
        self.label_currentWeather.setGeometry(QtCore.QRect(230, 50, 331, 71))
        self.label_currentWeather.setObjectName("label_currentWeather")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(350, 380, 91, 41))
        self.label_temp.setObjectName("label_temp")
        self.label_picture = QtWidgets.QLabel(self.centralwidget)
        self.label_picture.setGeometry(QtCore.QRect(300, 200, 200, 200))
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        OpenWeatherPy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OpenWeatherPy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        OpenWeatherPy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OpenWeatherPy)
        self.statusbar.setObjectName("statusbar")
        OpenWeatherPy.setStatusBar(self.statusbar)

        self.retranslateUi(OpenWeatherPy)
        QtCore.QMetaObject.connectSlotsByName(OpenWeatherPy)

    def retranslateUi(self, OpenWeatherPy):
        _translate = QtCore.QCoreApplication.translate
        OpenWeatherPy.setWindowTitle(_translate("OpenWeatherPy", "MainWindow"))
        self.pushButton.setText(_translate("OpenWeatherPy", "Go"))
        self.label_cityname.setText(_translate("OpenWeatherPy", "Enter city name"))
        self.label_currentWeather.setText(_translate("OpenWeatherPy", "<html><head/><body><p><span style=\" font-size:28pt;\">Current Weather</span></p></body></html>"))
        self.label_temp.setText("O F")
        self.pushButton.clicked.connect(self.enter_clicked)

    def enter_clicked(self):
        api_key = "3355e77c86c8f6c976c8b75ddbc56722"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = self.textEdit.toPlainText()

        print(city_name)

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)

        # json method of response object
        # convert json format data into
        # python format data
        x = response.json()

        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
        if x["cod"] != "404":

            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]


            #converts to fahrenheit
            temp = str(current_temperature)
            temp_kelvin = format(temp)
            temp_kelvin = float(temp_kelvin)
            temp_far = temp_kelvin * (9/5) - 459.67
            temp_far = round(temp_far,2)


            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
            current_humidiy = y["humidity"]

            # store the value of "weather"
            # key in variable z
            z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]

            # print following values
            print("\n"+str(x)+"\n")

            print(" Temperature (in fahrenheit) = " +
                            str(temp_far) +
                  "F\n atmospheric pressure (in hPa unit) = " +
                            str(current_pressure) +
                  "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                  "\n description = " +
                            str(weather_description))

            self.label_temp.setText(str(temp_far) + " F")


        else:
            print(" City Not Found ")

        if "cloud" in weather_description:
            self.label_picture.setPixmap(QPixmap('weatherimages/cloudy.png'))
        if "clear" in weather_description:
            self.label_picture.setPixmap(QPixmap('weatherimages/sunny.png'))
        if "rain" in weather_description:
            self.label_picture.setPixmap(QPixmap('weatherimages/rain.png'))
        if "snow" in weather_description:
            self.label_picture.setPixmap(QPixmap('weatherimages/rain.png'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenWeatherPy = QtWidgets.QMainWindow()
    ui = Ui_OpenWeatherPy()
    ui.setupUi(OpenWeatherPy)
    OpenWeatherPy.show()
    sys.exit(app.exec_())
