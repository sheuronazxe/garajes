import csv,os
from PyQt5.QtWidgets import QTableWidgetItem

archivo = 'datos/datos.csv'
cssfecha = "font-size: 18px;"
cssimpri = "font: bold 20px; color: #35a;"

try:
    os.mkdir('datos')
except:
    pass

def grabar(tabla):
    with open(archivo, 'w', newline='') as stream:
        writer = csv.writer(stream)
        i = 0
        while tabla.item(i,0):
            nombre = tabla.item(i,0).text()
            garaje = tabla.item(i,1).text() if tabla.item(i,1) else ''
            alquiler = tabla.item(i,2).text() if tabla.item(i,2) else ''
            writer.writerow([nombre, garaje, alquiler])
            i += 1

def cargar(tabla):
    try:
        with open(archivo, newline='') as stream:
            i = 0
            for rowdata in csv.reader(stream):
                tabla.insertRow(i)
                tabla.setItem(i, 0, QTableWidgetItem(rowdata[0]))
                tabla.setItem(i, 1, QTableWidgetItem(rowdata[1]))
                tabla.setItem(i, 2, QTableWidgetItem(rowdata[2]))
                i += 1
    except:
        pass