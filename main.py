import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        # 1 и 2 аргумент - позиция окна (0,0 в левом верхнем углу),
        # 3 и 4 аргумент - ширина и высота окна
        self.setGeometry(400, 200, 500, 400)
        self.setWindowTitle('Кто ты из Винни-Пуха?')
        self.setWindowIcon(QIcon("icon.jpg"))
        layout = QGridLayout()
        self.setLayout(layout)

        # 1, 2 цифры в addWidget - позиция по х, у
        # 3, 4 цифры - сколько строк и столбцов занимает виджет

        # Добавляет кнопки на верхнюю панель
        toolbar = QToolBar()
        test_toolbutton = QToolButton()
        test_toolbutton.setText("Тест")
        toolbar.addWidget(test_toolbutton)
        
        editor_toolbutton = QToolButton()
        editor_toolbutton.setText("Редактирование")
        toolbar.addWidget(editor_toolbutton)
        # сюда вставить функции кнопок: Тест активная,
        # Редактирование выводит экран с надписью:
        # "Редактирование недоступно, сначала пройдите тест"
        

        # Добавляет поле с текстом.
        label = QLabel("Тест для определения\n Вашего психотипа")
        # Подобрать цвет и шрифт всех виджетов похожим образом!
        label.setStyleSheet("background-color: yellow;")
        label.setFont(QFont("Times",18))
        label.setAlignment(Qt.AlignCenter)

        # Добавляет кнопку старта. Добавить действие - переход к тесту!
        start_button = QPushButton("Начать!")

        # Размеры таблицы рассчитываются автоматически
        # на основе максимального размера виджета
        # Подобрать коэффициенты!

        # 1 число - отступ слева, 2 число - отступ сверху,
        # 3 число - отступ справа, 4 число - отступ снизу
        layout.setContentsMargins(50, 0, 50, 0)
        #toolbar.setContentsMargins(0,0,0,50)
        layout.addWidget(toolbar, 0,2, 1,3)
        layout.addWidget(label, 3,5, 3,3)
        layout.addWidget(start_button, 6,4, 2,2)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
