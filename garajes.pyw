import sys, datos, informe
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QTableWidget, QHeaderView, QPushButton, QDateEdit

class Ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Generador de recibos")
        self.setWindowIcon(QIcon("iconos/icono.png"))
        self.setFixedSize(800, 480)

        self.tabla = QTableWidget(self)
        self.tabla.setRowCount(1)
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["Nombre","Garaje","Alquilver"])
        self.tabla.verticalHeader().hide()
        self.tabla.setGeometry(10,10,self.width()-20, 400)
        self.tabla.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tabla.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tabla.setColumnWidth(1, 200)
        self.tabla.setColumnWidth(2, 100)
        self.tabla.itemChanged.connect(self.edita)

        self.fecha = QDateEdit(self)
        self.fecha.setStyleSheet(datos.cssfecha)
        self.fecha.setAlignment(Qt.AlignHCenter)
        self.fecha.setDate(QDate.currentDate().addMonths(1))
        self.fecha.setDisplayFormat("MMMM yyyy")
        self.fecha.setGeometry(10, 420, 250, 50)

        self.boton = QPushButton(" IMPRIMIR", self)
        self.boton.setStyleSheet(datos.cssimpri)
        self.boton.setIcon(QIcon('iconos/impresion.png'))
        self.boton.setGeometry(541, 420, 250, 50)
        self.boton.clicked.connect(self.imprimir)        

        self.show()
        datos.cargar(self.tabla)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete and self.tabla.item(self.tabla.currentRow(),0):
            self.tabla.removeRow(self.tabla.currentRow())
            datos.grabar(self.tabla)
        else:
            super().keyPressEvent(event)

    def edita(self):
        self.tabla.sortItems(0, Qt.AscendingOrder)
        if self.tabla.item(self.tabla.rowCount()-1,0):
            self.tabla.insertRow(self.tabla.rowCount())
        datos.grabar(self.tabla)

    def imprimir(self):
        informe.generar(self.tabla,self.fecha.date().toString("MMMM yyyy"))
        self.close()


app = QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec_())
