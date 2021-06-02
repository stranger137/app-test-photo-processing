from PIL import Image
from PyQt5.Qt import Qt
import io
from PyQt5.QtCore import QBuffer
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import json, random, ast
import photo_processing
from matplot import pic_maker
from photo_processing import flip, brightness, my_filter, crop, rotate, contrast, sharpness, temperature, write
from PyQt5.QtWidgets import QWidget, QScrollArea

# файл с вопросами
f = open("questions.json", encoding="utf-8-sig")
phrases = json.load(f)
f.close()
# случайный порядок вопросов
random.shuffle(phrases)
#для перевода значений слайдера в %
values = {-3: -10,
          -2: -7,
          -1: -3,
          0: 0,
          1: 3,
          2: 7,
          3: 10}
 # итоговые фразы
f = open("descriptions.txt", encoding="utf-8")
contents = f.read()
descriptions = ast.literal_eval(contents)
f.close()


class Ui_MainWindow(QScrollArea):
    centralwidget: QWidget

    def setupUi(self, MainWindow):
        # список значений ответов на вопросы
        self.list_of_values = []
        # номер текущего вопроса
        self.n = 0
        MainWindow.setObjectName("MainWindow")
        # главное окно 800х650
        MainWindow.resize(800, 650)
        # цвет главного окна
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
        # Строка ввода
        self.name = QtWidgets.QTextEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(50, 360, 700, 50))
        self.name.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                                "border-radius:10px")

        # !!! Выравнивание строки ввода(не выравнивает по вертикали)
        self.name.setAlignment(QtCore.Qt.AlignCenter)

        # Строка с вопросом
        self.ask = QtWidgets.QLabel(self.centralwidget)
        # доступна для событий
        self.ask.setEnabled(True)
        # размер 700х200; положение (50,135)
        self.ask.setGeometry(QtCore.QRect(50, 135, 700, 200))
        self.ask.setAutoFillBackground(False)
        # добавляем цвет и закругленность краев
        self.ask.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                               "border-radius:10px")
        self.ask.setAlignment(QtCore.Qt.AlignCenter)
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
        self.start_button.clicked.connect(self.get_name)
        self.start_button.clicked.connect(self.deleter_1)
        self.start_button.clicked.connect(self.start_game)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# удаляем виджеты на 1 "слайде"
    def get_name(self):
        self.username = self.name.toPlainText()
    def deleter_1(self):
        self.start_button.deleteLater()
        self.name.deleteLater()
        self.ask.deleteLater()

    # скрываем виджеты на 2 "слайде"

    def deleter_2(self):
        self.next_button.close()
        self.back_button.close()
        self.agree.close()
        self.disagree.close()
        self.choose.close()
        self.tabWidget.close()
        self.phrase.close()

    # удаляем виджеты на заблокированном редакторе

    def deleter_3(self):
        self.from_redactor.deleteLater()
        self.bye.deleteLater()

    # показываем виджеты на 2 "слайде"
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
        self.choose.setGeometry(QtCore.QRect(200, 360, 400, 41))
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
        # окошко "Не согласен"
        self.disagree = QtWidgets.QLabel(self.centralwidget)
        self.disagree.setGeometry(QtCore.QRect(50, 360, 100, 30))
        self.disagree.setStyleSheet("background-color:  rgb(239, 150, 9);\n"
                                    "border-radius:10px;")
        self.disagree.setAlignment(QtCore.Qt.AlignCenter)
        self.disagree.setObjectName("disagree")
        # окошко "Согласен"
        self.agree = QtWidgets.QLabel(self.centralwidget)
        self.agree.setGeometry(QtCore.QRect(650, 360, 100, 30))
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
        # если значение таба изменилось
        # если мы зашли в редактор
        if self.tabWidget.currentIndex() == 1:
            # если тест закончен
            if self.n == 32:
                # включается редактор
                self.editor()
            else:
                # окошко "Вернитесь обратно"
                self.return_()

    def pointer(self, vall, index):
        # функция начисления баллов, запоминания выбранных значений
        for i in range(len(phrases[index]["characters"])):
            hero = phrases[index]["characters"][i]
            self.score[hero] += values[vall]
        if len(self.list_of_values) - 1 >= index:  # correcting the old value
            self.score[hero] -= values[self.list_of_values[index]]
            self.list_of_values[index] = vall
        else:
            self.list_of_values.append(vall)

    def finish(self):
        # вывод результата
        # сортировка баллов
        self.finish_list = [(value, key) for key, value in self.score.items()]
        self.finish_list.sort(reverse=True)
        # если нет 1 персонажа с наибольшим баллом, то ставим результат "Смешанный тип"
        if self.finish_list[0][0] == self.finish_list[1][0]:
            self.phrase.setText(descriptions["Смешанный тип"])
        # если есть 1 персонаж с наибольшим баллом, то ставим соответствующий результат
        else:
            self.phrase.setText("Поздравляю!\nВы " + max(self.finish_list)[1] + descriptions[max(self.finish_list)[1]])
        # лэйбл для гистограммы
        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setEnabled(True)
        self.pic.setGeometry(QtCore.QRect(175, 450, 500, 300))
        self.pic.setAutoFillBackground(False)
        self.pic.setStyleSheet("background-color: rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.phrase.setAlignment(QtCore.Qt.AlignCenter)
        # создаем гистограмму
        pic_maker(self.finish_list)
        print(self.finish_list)
        # ставим в лэйбл гистограмму
        self.graphic = QPixmap('photos/graphic.png')
        self.pic.setPixmap(self.graphic)
        self.pic.setScaledContents(True)
        self.pic.show()
        # положение обьектов в зависимости от текста персонажа
        if self.finish_list[0][0] == self.finish_list[1][0]:
            self.pic.move(125, 400)
            MainWindow.setGeometry(500, 100, 800, 750)
        elif self.finish_list[0][1] == 'Винни-Пух':
            self.phrase.move(150, 100)
            self.phrase.move(15, 100)
            MainWindow.setGeometry(500, 100, 800, 775)
        elif self.finish_list[0][1] == 'Кристофер Робин':
            self.phrase.move(80, 100)
            MainWindow.setGeometry(500, 100, 800, 775)
            self.pic.move(150, 450)
        elif self.finish_list[0][1] == 'Пятачок':
            self.phrase.move(65, 100)
            MainWindow.setGeometry(500, 100, 800, 775)
            self.pic.move(120, 420)
        else:
            self.phrase.move(65, 100)
            MainWindow.setGeometry(500, 100, 800, 775)
            self.pic.move(160, 460)
        self.phrase.adjustSize()
        # удаляем лишнее
        self.next_button.deleteLater()
        self.back_button.deleteLater()
        self.agree.deleteLater()
        self.disagree.deleteLater()
        self.choose.deleteLater()




        # реализация функции на кнопке "Дальше"

    def next_fun(self):
        # начисление баллов
        self.pointer(self.choose.value(), self.n)
        # номер вопроса изменяется на следующий
        self.n += 1
        # ставим слудующую фразу в лэйбл
        self.phrase.setText(phrases[self.n]["question"])
        # если мы тут уже были
        if len(self.list_of_values) - 1 >= self.n:
            self.choose.setValue(self.list_of_values[self.n])
        else:
            # если мы на этом вопросе впервые, значение слайдера на 0
            self.choose.setValue(0)
            # если мы были на последнем вопросе
        if self.n == 32:
            self.finish()

    def back_fun(self):
        # нельзя вернуться назад на первом вопросе
        if self.n == 0:
            pass
        else:
            # уменьшаем номер вопроса
            self.n -= 1
            # ставим старый вопрос
            self.phrase.setText(phrases[self.n]["question"])
            # ставим предыдущее значение слайдера
            self.choose.setValue(self.list_of_values[self.n])


    def saver(self):
        # список функций в редакторе
        d = {1: photo_processing.flip,
             2: photo_processing.brightness,
             3: photo_processing.my_filter,
             4: photo_processing.contrast,
             5: photo_processing.sharpness,
             6: photo_processing.temperature}
        # если мы на отражении, мы должны изменять текущую картинку
        if self.num == 1:
            self.image_on_the_screen = Image.open(self.current_image_path)
            self.image_on_the_screen = d[self.num](self.image_on_the_screen, self.coef)
            self.image_on_the_screen.save(self.current_image_path)
            self.phrase.setPixmap(QPixmap(self.current_image_path))
            # если в фильтрах мы на 0 позиции (начальное фото)
        elif self.num == 3 and self.coef == 0:
            self.image_on_the_screen = Image.open(self.finish_image_path)
            self.image_on_the_screen.save(self.current_image_path)
            self.phrase.setPixmap(QPixmap(self.current_image_path))
            # в остальных случаях
        else:
            # открываем фото,которое было при входе в текущий режим редактора
            self.image_on_the_screen = Image.open(self.finish_image_path)
            # изменяем фото текущим редактором
            self.image_on_the_screen = d[self.num](self.image_on_the_screen, self.coef)
            self.image_on_the_screen.save(self.current_image_path)
            self.phrase.setPixmap(QPixmap(self.current_image_path))
    def editor(self):
        self.pic.deleteLater()
        MainWindow.setGeometry(500, 100, 800, 650)

        self.tabWidget.deleteLater()
        # если смешанный тип
        if self.finish_list[0][0] == self.finish_list[1][0]:
            # выбираем фотографию
            self.image_on_the_screen = Image.open('photos/all.png')
            self.current_image_path ='photos/all1.png'
            self.finish_image_path = 'photos/all2.png'
            # ставим подпись на нужное место
            self.image_on_the_screen = write(self.image_on_the_screen,
                                             self.username + ", у вас смешанный психотип!", (20, 530))

        else:
            # выбираем фотографию в зависимости от персонажа
            self.current_image_path ='photos/'+self.finish_list[0][1]+'1.png'
            self.finish_image_path = 'photos/'+self.finish_list[0][1]+'2.png'
            self.image_on_the_screen = Image.open('photos/'+self.finish_list[0][1]+'.png')
            # выбираем для каждого персонажа положение подписи
            if self.finish_list[0][1] == 'Винни-Пух':
                self.image_on_the_screen = write(self.image_on_the_screen,
                                                 self.username + ", Вы " + max(self.finish_list)[1] + "!", (650, 530))
            elif self.finish_list[0][1] == 'Иа-Иа':
                self.image_on_the_screen = write(self.image_on_the_screen, self.username + ", Вы " +
                                                 max(self.finish_list)[1] + "!", (650, 750))
            elif self.finish_list[0][1] == 'Кристофер Робин':
                self.image_on_the_screen = write(self.image_on_the_screen,
                                                 self.username + ", Вы " + max(self.finish_list)[1] + "!", (50, 675))
            elif self.finish_list[0][1] == 'Тигра':
                self.image_on_the_screen = write(self.image_on_the_screen,
                                                 self.username + ", Вы " + max(self.finish_list)[1] + "!", (50, 100))
            elif self.finish_list[0][1] == 'Кролик':
                self.image_on_the_screen = write(self.image_on_the_screen,
                                                 self.username + ", Вы " + max(self.finish_list)[1] + "!", (50, 675))
            elif self.finish_list[0][1] == 'Крошка Ру':
                self.image_on_the_screen = write(self.image_on_the_screen,
                                                 self.username + ", Вы " + max(self.finish_list)[1] + "!", (50, 670))
            else:
                self.image_on_the_screen = write(self.image_on_the_screen,
                                                 self.username + ",\n\n    Вы " + max(self.finish_list)[1] + "!", (650,
                                                                                                                   200))

        self.image_on_the_screen.save(self.current_image_path)
        self.image_on_the_screen.save(self.finish_image_path)
        self.pixmap = QPixmap(self.current_image_path)
        self.phrase.setPixmap(self.pixmap)
        self.phrase.setGeometry(50, 75, 700, 350)
        self.phrase.setScaledContents(True)
        # виджет "вкладки"
        self.tab_in_editor = QtWidgets.QTabWidget(self.centralwidget)
        self.font.setPointSize(13)
        self.tab_in_editor.setFont(self.font)
        self.tab_in_editor.setGeometry(QtCore.QRect(0, 10, 800, 51))
        self.tab_in_editor.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tab_in_editor.setAutoFillBackground(False)
        self.tab_in_editor.setStyleSheet("background-color:  rgb(239, 150, 9);")
        self.tab_in_editor.setObjectName("tab_in_editor")



        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_in_editor.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_in_editor.addTab(self.tab_2, "")

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab")
        self.tab_in_editor.addTab(self.tab3, "")

        self.tab6 = QtWidgets.QWidget()
        self.tab6.setObjectName("tab4")
        self.tab_in_editor.addTab(self.tab6, "")

        self.tab7 = QtWidgets.QWidget()
        self.tab7.setObjectName("tab7")
        self.tab_in_editor.addTab(self.tab7, "")

        self.tab8 = QtWidgets.QWidget()
        self.tab8.setObjectName("tab8")
        self.tab_in_editor.addTab(self.tab8, "")
        self.tab9 = QtWidgets.QWidget()
        self.tab9.setObjectName("tab9")
        self.tab_in_editor.addTab(self.tab9, "")

        _translate = QtCore.QCoreApplication.translate
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab), _translate("MainWindow", "Отразить"))
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab_2), _translate("MainWindow", "Яркость"))
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab3), _translate("MainWindow", "Фильтры"))
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab6), _translate("MainWindow", "Контраст"))
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab7), _translate("MainWindow", "Четкость"))
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab8), _translate("MainWindow", "Температура"))
        self.tab_in_editor.setTabText(self.tab_in_editor.indexOf(self.tab9), _translate("MainWindow", "Сохранить"))

        self.tab_in_editor.show()
        self.red_click = QtWidgets.QPushButton(self.centralwidget)
        self.tab_in_editor.currentChanged.connect(self.tabs)
        self.flipQt()

    def tabs(self):
        if self.tab_in_editor.currentIndex() == 0:
            self.flipQt()
        elif self.tab_in_editor.currentIndex() == 1:
            self.brightnessQt()
        elif self.tab_in_editor.currentIndex() == 2:
            self.filterQt()
        elif self.tab_in_editor.currentIndex() == 3:
            self.contrastQt()
        elif self.tab_in_editor.currentIndex() == 4:
            self.sharpnessQt()
        elif self.tab_in_editor.currentIndex() == 5:
            self.temperatureQt()
        elif self.tab_in_editor.currentIndex() == 6:
            self.saveQt()

    def flipQt(self):
        self.image_on_the_screen.save(self.finish_image_path)
        self.num = 1
        self.coef=0
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QPushButton(self.centralwidget)
        self.red_click.setGeometry(QtCore.QRect(300, 500, 200, 100))
        self.red_click.setStyleSheet(" QPushButton {"
                                         "    background-color: rgb(239, 150, 9);"
                                         "border-radius:10px;"
                                         " }"
                                         " QPushButton:pressed {"
                                         "     background-color: rgb(225, 117, 0);"
                                         " }")
        self.font.setPointSize(25)
        self.red_click.setFont(self.font)
        self.red_click.setText("Отразить!")
        self.red_click.show()
        self.red_click.clicked.connect(self.saver)

    def brightnessQt(self):
        self.image_on_the_screen.save(self.finish_image_path)
        self.num = 2
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QSlider(self.centralwidget)
        self.red_click.setMinimum(0)
        self.red_click.setMaximum(200)
        self.red_click.setValue(100)
        self.red_click.setTickInterval(10)
        self.red_click.setGeometry(QtCore.QRect(100, 500, 600, 41))
        self.red_click.setStyleSheet("background-color:rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.red_click.setOrientation(QtCore.Qt.Horizontal)
        self.red_click.show()
        self.red_click.valueChanged.connect(self.valuer)
        self.red_click.valueChanged.connect(self.saver)

    def valuer(self):
        self.coef=self.red_click.value()



    def filterQt(self):
        self.image_on_the_screen.save(self.finish_image_path)
        self.num = 3
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QSlider(self.centralwidget)
        self.red_click.setMinimum(0)
        self.red_click.setMaximum(8)
        self.red_click.setValue(0)
        self.red_click.setTickInterval(1)
        self.red_click.setGeometry(QtCore.QRect(100, 500, 600, 41))
        self.red_click.setStyleSheet("background-color:rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.red_click.setOrientation(QtCore.Qt.Horizontal)
        self.red_click.show()
        self.coef=self.red_click.value()

        self.red_click.valueChanged.connect(self.valuer)
        self.red_click.valueChanged.connect(self.saver)



    def contrastQt(self):
        self.image_on_the_screen.save(self.finish_image_path)

        self.num = 4
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QSlider(self.centralwidget)
        self.red_click.setMinimum(0)
        self.red_click.setMaximum(200)
        self.red_click.setValue(100)
        self.red_click.setTickInterval(1)
        self.red_click.setGeometry(QtCore.QRect(100, 500, 600, 41))
        self.red_click.setStyleSheet("background-color:rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.red_click.setOrientation(QtCore.Qt.Horizontal)
        self.red_click.show()
        self.coef=self.red_click.value()

        self.red_click.valueChanged.connect(self.valuer)
        self.red_click.valueChanged.connect(self.saver)


    def sharpnessQt(self):
        self.image_on_the_screen.save(self.finish_image_path)

        self.num = 5
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QSlider(self.centralwidget)
        self.red_click.setMinimum(0)
        self.red_click.setMaximum(200)
        self.red_click.setValue(100)
        self.red_click.setTickInterval(1)
        self.red_click.setGeometry(QtCore.QRect(100, 500, 600, 41))
        self.red_click.setStyleSheet("background-color:rgb(239, 150, 9);\n"
                                  "border-radius:10px")
        self.red_click.setOrientation(QtCore.Qt.Horizontal)
        self.red_click.show()

        self.red_click.valueChanged.connect(self.valuer)

        self.red_click.valueChanged.connect(self.saver)


    def temperatureQt(self):
        self.image_on_the_screen.save(self.finish_image_path)

        self.num = 6
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QSlider(self.centralwidget)
        self.red_click.setMinimum(0)
        self.red_click.setMaximum(18)
        self.red_click.setValue(11)
        self.red_click.setTickInterval(1)
        self.red_click.setGeometry(QtCore.QRect(100, 500, 600, 41))
        self.red_click.setStyleSheet("background-color:rgb(239, 150, 9);\n"
                                    "border-radius:10px")
        self.red_click.setOrientation(QtCore.Qt.Horizontal)
        self.red_click.show()
        self.red_click.valueChanged.connect(self.valuer)

        self.red_click.valueChanged.connect(self.saver)



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
    def saveQt(self):
        self.red_click.deleteLater()
        self.red_click = QtWidgets.QPushButton(self.centralwidget)
        self.red_click.setGeometry(QtCore.QRect(300, 500, 200, 100))
        self.red_click.setStyleSheet(" QPushButton {"
                                         "    background-color: rgb(239, 150, 9);"
                                         "border-radius:10px;"
                                         " }"
                                         " QPushButton:pressed {"
                                         "     background-color: rgb(225, 117, 0);"
                                         " }"
                                         )
        self.font.setPointSize(25)
        self.red_click.setFont(self.font)
        self.red_click.setText("Сохранить!")
        self.red_click.clicked.connect(self.save_this_photo)
        self.red_click.show()
    def save_this_photo(self):
        self.image_on_the_screen.save('results/'+self.username + '.png')
        self.path = QtWidgets.QLabel(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(300, 450, 200, 40))
        self.path.setStyleSheet("background-color : rgb(239, 150, 9);\n"
                                 "border-radius:10px;")
        self.path.setAlignment(QtCore.Qt.AlignCenter)
        self.font.setPointSize(10)
        self.path.setFont(self.font)
        self.path.setText('Название файла: '+self.username + '.png')
        self.path.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())