from PyQt5 import QtCore, QtGui, QtWidgets
import json, random
#файл с вопросами
from PyQt5.QtWidgets import QWidget

f = open("questions.json", encoding="utf-8-sig")
phrases = json.load(f)
f.close()
#случайный порядок вопросов
random.shuffle(phrases)


class Ui_MainWindow(object):

    centralwidget: QWidget

    def setupUi(self, MainWindow):
        #список значений ответов на вопросы
        self.list_of_values = []
        #номер текущего вопроса
        self.n = 0
        MainWindow.setObjectName("MainWindow")
        #главное окно 800х650
        MainWindow.resize(800, 650)
        MainWindow.setStyleSheet("background-color:rgb(71, 71, 71);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # изначальные значения героев
        self.score = {"Винни-Пух": 50,
                 "Тигра": 50,
                 "Иа-Иа": 50,
                 "Кристофер Робин": 50,
                 "Крошка Ру": 50,
                 "Пятачок": 50,
                 "Кролик": 50
                 }
        # шрифт
        self.font = QtGui.QFont()
        self.font.setFamily("PT Mono")
        self.font.setPointSize(23)
        self.font.setBold(True)
        self.font.setItalic(False)
        self.font.setUnderline(False)
        self.font.setWeight(75)
        self.font.setStrikeOut(False)
        # запуск
        self.what_is_your_name()

    # метод запроса имени пользователя
    def what_is_your_name(self):
        #Строка ввода
        self.name=QtWidgets.QTextEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(50, 360, 700, 50))
        self.name.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                                "border-radius:10px")

        #!!! Выравнивание строки ввода(не выравнивает по вертикали)
        self.name.setAlignment(QtCore.Qt.AlignCenter)


        # Строка с вопросом
        self.ask = QtWidgets.QLabel(self.centralwidget)
        self.ask.setEnabled(True)
        self.ask.setGeometry(QtCore.QRect(50, 135, 700, 200))
        self.ask.setAutoFillBackground(False)
        self.ask.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.ask.setAlignment(QtCore.Qt.AlignCenter)
        self.ask.setObjectName("phrase")

        self.ask.setFont(self.font)
        self.ask.setText("Как вас зовут?")
        self.name.setFont(self.font)

        # кнопка "Начать!"
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(300, 435, 200, 150))
        self.start_button.setStyleSheet(" QPushButton {"
                                       "    background-color: rgb(239, 150, 9);"
                                       "border-radius:10px;"
                                       " }"
                                       " QPushButton:pressed {"
                                       "     background-color: rgb(225, 117, 0);"
                                       " }"
                                       )
        self.start_button.setFont(self.font)

        _translate = QtCore.QCoreApplication.translate
        self.start_button.setText(_translate("MainWindow", "Начать!"))
        self.start_button.clicked.connect(self.start_game)
        self.start_button.clicked.connect(self.deleter_1)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def deleter_1(self):
        self.start_button.deleteLater()
        self.name.deleteLater()
        self.ask.deleteLater()
    def deleter_2(self):
        self.next_button.close()
        self.back_button.close()
        self.agree.close()
        self.disagree.close()
        self.choose.close()
        self.tabWidget.close()
        self.phrase.close()
    def deleter_3(self):
        self.from_redactor.deleteLater()
        self.bye.deleteLater()
    def show_(self):
        self.next_button.show()
        self.back_button.show()
        self.agree.show()
        self.disagree.show()
        self.choose.show()
        self.tabWidget.show()
        self.phrase.show()
        self.tabWidget.setCurrentIndex(0)  # 0-Тест 1-Редактор




    def start_game(self):
        # Строка с фразами
        self.phrase = QtWidgets.QLabel(self.centralwidget)
        self.phrase.setEnabled(True)
        self.phrase.setGeometry(QtCore.QRect(50, 135, 700, 181))
        self.phrase.setAutoFillBackground(False)
        self.phrase.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                               "border-radius:10px")
        self.phrase.setAlignment(QtCore.Qt.AlignCenter)
        self.phrase.setObjectName("phrase")


        # кнопка "Дальше"
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(405, 460, 150, 111))

        self.next_button.setStyleSheet(" QPushButton {\n"
                                       "    background-color: rgb(239, 150, 9);\n"
                                       "border-radius:10px;\n"
                                       " }\n"
                                       "\n"
                                       " QPushButton:pressed {\n"
                                       "     background-color: rgb(225, 117, 0);\n"
                                       " }\n"

                                       "")
        self.next_button.setObjectName("next_button")

        # ползунок выбора
        self.choose = QtWidgets.QSlider(self.centralwidget)
        self.choose.setMinimum(-3)
        self.choose.setMaximum(3)
        self.choose.setValue(0)
        self.choose.setTickInterval(1)
        self.choose.setGeometry(QtCore.QRect(180, 360, 401, 41))
        self.choose.setStyleSheet("background-color:rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.choose.setOrientation(QtCore.Qt.Horizontal)
        self.choose.setObjectName("choose")

        # виджет "вкладки"
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 800, 51))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color:  rgb(239, 150, 9);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setCurrentIndex(0)  # 0-Тест 1-Редактор

        #окошко "Не согласен"
        self.disagree = QtWidgets.QLabel(self.centralwidget)
        self.disagree.setGeometry(QtCore.QRect(50, 400, 100, 60))
        self.disagree.setStyleSheet("background-color:  rgb(239, 150, 9);\n"
                                    "border-radius:10px;")
        self.disagree.setAlignment(QtCore.Qt.AlignCenter)
        self.disagree.setObjectName("disagree")
        # окошко "Согласен"
        self.agree = QtWidgets.QLabel(self.centralwidget)
        self.agree.setGeometry(QtCore.QRect(650, 400, 100, 60))
        self.agree.setStyleSheet("background-color : rgb(239, 150, 9);\n"
                                 "border-radius:10px;")
        self.agree.setAlignment(QtCore.Qt.AlignCenter)
        self.agree.setObjectName("agree")

        # кнопка "Назад"
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(245, 460, 150, 111))
        self.back_button.setStyleSheet(" QPushButton {"
                                       "    background-color: rgb(239, 150, 9);"
                                       "border-radius:10px;"
                                       " }"
                                       " QPushButton:pressed {"
                                       "     background-color: rgb(225, 117, 0);"
                                       " }"
                                       )
        self.back_button.setObjectName("back_button")

        # ставим в виджеты шрифты с соответствующими размерами
        self.font.setPointSize(17)
        self.phrase.setFont(self.font)

        self.font.setPointSize(30)
        self.back_button.setFont(self.font)
        self.next_button.setFont(self.font)

        self.font.setPointSize(13)
        self.tabWidget.setFont(self.font)

        self.agree.setFont(self.font)
        self.disagree.setFont(self.font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # показать все новые виджеты
        self.phrase.show()
        self.back_button.show()
        self.next_button.show()
        self.disagree.show()
        self.agree.show()
        self.choose.show()
        self.tabWidget.show()

    def retranslateUi(self, MainWindow):


        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_button.setText(_translate("MainWindow", "Дальше"))
        self.phrase.setText(_translate("MainWindow", phrases[0]["question"]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Тест"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Редактор"))
        self.disagree.setText(_translate("MainWindow", "Не согласен"))
        self.agree.setText(_translate("MainWindow", "Согласен"))
        self.back_button.setText(_translate("MainWindow", "Назад"))
        self.back_button.clicked.connect(self.back_fun)
        self.tabWidget.currentChanged.connect(self.tab_fun)
        self.next_button.clicked.connect(self.next_fun)


    def tab_fun(self):
        if self.tabWidget.currentIndex() == 1:
            if self.n == 32:
                self.redactor()
            else:
                self.return_()

    def pointer(self, vall, index):

        for i in range(len(phrases[index]["characters"])):
                hero = phrases[index]["characters"][i]
                self.score[hero] += vall * 3
        if len(self.list_of_values) - 1 >= index: # correcting the old value
                self.score[hero] -= self.list_of_values[index] * 3
                self.list_of_values[index] = vall
        else:
            self.list_of_values.append(vall)

    def finish(self):
        self.finish_list=[(value,key) for key,value in self.score.items()]
        self.finish_list.sort(reverse=True)
        if self.finish_list[0][0]==self.finish_list[1][0]:
            self.phrase.setText("У Вас одинаково выражены два или более психотипа, которые\nхарактерны для персонажей сказки «Винни-Пух». Возможно, что\nу Вас одинаковое соотношение всех имеющихся психотипов. \nВозможен также вариант, что Вы просто ответили на вопросы таким образом,\n что Вы оказались на грани результатов, \nхотя на самом деле у Вас есть определенный \nпсихотип среди имеющихся персонажей.\n Мы не можем с точностью ответить, \nприсущи Вам черты всех персонажей или \nВы просто случайно получили такой результат. \nСоответственно, мы не можем предоставить более \nдетальное описание Вашей личности. \nОднако Вы можете рассмотреть таблицу с результатами\n и определить, личность какого персонажа набрала \nнаибольшее количество процентов.")
            self.phrase.adjustSize()
            MainWindow.sizeHint()
        else:
            self.phrase.setText("Поздравляю!\nВы "+max(self.finish_list)[1])
        self.init_game()
        self.next_button.deleteLater()
        self.back_button.deleteLater()
        self.agree.deleteLater()
        self.disagree.deleteLater()
        self.choose.deleteLater()

    def init_game(self):
        pass


            
    def next_fun(self):
        self.pointer(self.choose.value(), self.n)
        self.n += 1
        self.phrase.setText(phrases[self.n]["question"])
        if len(self.list_of_values) - 1 >= self.n:
            self.choose.setValue(self.list_of_values[self.n])
        else:
            self.choose.setValue(0)
        if self.n == 32:
            self.finish()




    def back_fun(self):
        if self.n == 0:
            pass
        else:
            self.n -= 1
            self.phrase.setText(phrases[self.n]["question"])
            self.choose.setValue(self.list_of_values[self.n])


    def redactor(self):
        print("redactor")

    def return_(self):
        # Строка с фразами
        self.bye = QtWidgets.QLabel(self.centralwidget)
        self.bye.setEnabled(True)
        self.bye.setGeometry(QtCore.QRect(50, 135, 700, 181))
        self.bye.setAutoFillBackground(False)
        self.bye.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                               "border-radius:10px")
        self.bye.setAlignment(QtCore.Qt.AlignCenter)
        self.bye.setObjectName("bye")
        self.bye.setText("Редактор недоступен!\nПройдите тест!")


        self.deleter_2()
        self.from_redactor = QtWidgets.QPushButton(self.centralwidget)
        self.from_redactor.setGeometry(QtCore.QRect(300, 435, 200, 150))
        self.from_redactor.setStyleSheet(" QPushButton {"
                                       "    background-color: rgb(239, 150, 9);"
                                       "border-radius:10px;"
                                       " }"
                                       " QPushButton:pressed {"
                                       "     background-color: rgb(225, 117, 0);"
                                       " }"
                                       )
        self.from_redactor.setObjectName("back_button")
        self.font.setPointSize(30)
        self.from_redactor.setText("Вернуться!")
        self.bye.setFont(self.font)
        self.from_redactor.setFont(self.font)

        self.from_redactor.show()
        self.bye.show()
        self.from_redactor.clicked.connect(self.show_)
        self.from_redactor.clicked.connect(self.deleter_3)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
