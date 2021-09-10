from PyQt5.QtWidgets import QApplication , QMainWindow
import sys

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.altura = 600
        self.largura = 800
        self.titulo = 'Teste de inteface Gráfica'
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda , self.topo , self.altura , self.largura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicaçao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicaçao.exec_())