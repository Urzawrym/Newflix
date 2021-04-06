import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.Qt import QStandardItemModel, QStandardItem



class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('World Country Diagram')
        self.resize(500, 700)

        treeView = QTreeView()
        treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()


        # America
        america = QStandardItem('America')

        california = QStandardItem('California')
        america.appendRow(california)

        oakland = QStandardItem('Oakland')
        sanfrancisco = QStandardItem('San Francisco')
        sanjose = QStandardItem('San Jose')

        california.appendRow(oakland)
        california.appendRow(sanfrancisco)
        california.appendRow(sanjose)


        texas = QStandardItem('Texas')
        america.appendRow(texas)

        austin = QStandardItem('Austin')
        houston = QStandardItem('Houston')
        dallas = QStandardItem('dallas')
        testo = QStandardItem("testo")
        testo2 = QStandardItem("testo2")
        testo3 = QStandardItem("testo3")
        item = (testo,testo2,testo3)
        texas.appendRow(austin)
        texas.appendRow(houston)
        texas.appendRow(dallas)
        texas.appendRow(item)

        # Canada
        canada = QStandardItem('Canada')

        alberta = QStandardItem('Alberta')
        bc = QStandardItem('British Columbia')
        ontario = QStandardItem('Ontario')
        canada.appendRows([alberta, bc, ontario])


        rootNode.appendRow(america)
        rootNode.appendRow(canada)

        treeView.setModel(treeModel)
        treeView.expandAll()
        treeView.doubleClicked.connect(self.getValue)

        self.setCentralWidget(treeView)

    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())


app = QApplication(sys.argv)

demo = AppDemo()
demo.show()

sys.exit(app.exec_())