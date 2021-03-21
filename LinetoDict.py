import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

answers = {"title": "", "Date": "", "Product": "", "Serial Num": ""}



class Template(QWidget):

    def __init__(self):
        super().__init__()
        self.projectDetailsUI()

    def projectDetailsUI(self):
        layout = QGridLayout(self)
        self.title = QLineEdit()
        self.title.setFixedWidth(300)


        self.date = QLineEdit()
        self.date.setFixedWidth(120)


        self.product = QLineEdit()
        self.product.setFixedWidth(300)


        self.serialNum = QLineEdit()
        self.serialNum.setFixedWidth(300)



        font = QFont()
        title = QLabel("Project Details")
        title.setFont(font)
        layout.addWidget(title, 0, 0)

        layout.addWidget(QLabel("Title"), 1, 0)
        layout.addWidget(self.title, 1, 2)

        layout.addWidget(QLabel("Date (dd/mm/yy)"), 2, 0)
        layout.addWidget(self.date, 2, 2)

        layout.addWidget(QLabel("Name"), 3, 0)
        layout.addWidget(self.product, 3, 2)

        layout.addWidget(QLabel("Serial Number (if available)"), 4, 0)
        layout.addWidget(self.serialNum, 4, 2)

        self.title.editingFinished.connect(self.set_answers)
        self.date.editingFinished.connect(self.set_answers)
        self.product.editingFinished.connect(self.set_answers)
        self.serialNum.editingFinished.connect(self.set_answers)




    def set_answers(self):
        answers['title'] = self.title.text()
        answers['Date'] = self.date.text()
        answers['Product'] = self.product.text()
        answers['Serial Num'] = self.serialNum.text()
        print(answers)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Template()
    window.show()
    sys.exit(app.exec_())