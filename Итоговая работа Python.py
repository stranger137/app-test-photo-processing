import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)

window = QWidget()
# 1 и 2 аргумент - позиция окна (0,0 в левом верхнем углу),
# 3 и 4 аргумент - ширина и высота окна
window.setGeometry(400, 200, 500, 400)
window.setWindowTitle('Кто ты из Винни-Пуха?')
window.setWindowIcon(QIcon("icon.jpg"))
layout = QGridLayout()
window.setLayout(layout)

# 1, 2 цифры в addWidget - позиция по х, у
# 3, 4 цифры - сколько строк и столбцов занимает виджет

# Добавляет кнопки на верхнюю панель
toolbar = QToolBar()
test_toolbutton = QToolButton()
test_toolbutton.setText("Тест")
editor_toolbutton = QToolButton()
editor_toolbutton.setText("Редактирование")
# сюда вставить функции кнопок: Тест активная,
# Редактирование выводит экран с надписью:
# "Редактирование недоступно, сначала пройдите тест"
toolbar.addWidget(test_toolbutton)
toolbar.addWidget(editor_toolbutton)

# Добавляет поле с текстом.
label = QLabel("Тест для определения\n Вашего психотипа")

# Подобрать цвет и шрифт всех виджетов похожим образом!
label.setStyleSheet("background-color: yellow;")
label.setFont(QFont("Times",18))
label.setAlignment(Qt.AlignCenter)

# Добавляет кнопку старта. Добавить действие - переход к тесту!
# Добавить кнопку в layout посередине! Разобраться с layout
#(текущие проблемы с выводом из-за того, что не все лежит в layout)
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

window.show()


sys.exit(app.exec_())
