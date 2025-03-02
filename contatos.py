from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow
from add_cntt import Ui_tela_add_contato
from PySide6.QtCore import QSortFilterProxyModel, QStringListModel, Qt

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(988, 579)

        # Frame principal
        self.frame_principal_cntt = QFrame(Form)
        self.frame_principal_cntt.setObjectName(u"frame_principal_cntt")
        self.frame_principal_cntt.setGeometry(QRect(170, 80, 651, 401))
        self.frame_principal_cntt.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        # Título "Contatos"
        self.label_Cntt = QLabel(self.frame_principal_cntt)
        self.label_Cntt.setObjectName(u"label_Cntt")
        self.label_Cntt.setGeometry(QRect(30, 20, 71, 16))
        self.label_Cntt.setStyleSheet(u"font: 700 12pt \"Segoe Print\"; color: black;")

        # Campo de busca
        self.line_buscar_cntt = QLineEdit(self.frame_principal_cntt)
        self.line_buscar_cntt.setObjectName(u"line_buscar_cntt")
        self.line_buscar_cntt.setGeometry(QRect(30, 40, 181, 22))
        self.line_buscar_cntt.setPlaceholderText("Buscar Contatos...")

        # Lista de contatos
        self.list_cntt = QListView(self.frame_principal_cntt)
        self.list_cntt.setObjectName(u"list_cntt")
        self.list_cntt.setGeometry(QRect(30, 80, 591, 291))

        # Lista de contatos
        self.contatos = ["Abgail", "Bento", "João", "Maria"]

        self.model = QStringListModel(self.contatos)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setFilterKeyColumn(0)
        self.proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.sort(0, Qt.AscendingOrder)  # Ordena os contatos

        self.list_cntt.setModel(self.proxy_model)

        self.line_buscar_cntt.textChanged.connect(self.proxy_model.setFilterFixedString)

        # Ícone de adicionar contato
        self.label_add = QLabel(self.frame_principal_cntt)
        self.label_add.setObjectName(u"label_add")
        self.label_add.setGeometry(QRect(580, 40, 31, 31))
        self.label_add.setPixmap(QPixmap(u"xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.mousePressEvent = self.adicionar_contato

        # Criando os ícones de edição e as linhas abaixo dos contatos
        y_positions = [90, 130, 170, 210]
        self.labels_editar = []
        self.lines = []

        for i, nome in enumerate(self.contatos):
            label_editar = QLabel(self.frame_principal_cntt)
            label_editar.setObjectName(f"label_editar{i+1}")
            label_editar.setGeometry(QRect(590, y_positions[i], 20, 20))
            label_editar.setPixmap(QPixmap(u"yy.png"))  # Ícone preto
            label_editar.setScaledContents(True)
            label_editar.mousePressEvent = lambda event, index=i: self.editar_contato(index)
            self.labels_editar.append(label_editar)

            # Adicionando linha abaixo do contato
            line = QFrame(self.frame_principal_cntt)
            line.setGeometry(QRect(30, y_positions[i] + 25, 580, 1))
            line.setStyleSheet("background-color: black;")
            self.lines.append(line)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", u"Contatos", None))

    def editar_contato(self, index):
        contato = self.contatos[index]
        print(f"Editando contato: {contato}")

    def adicionar_contato(self, event):
        self.tela_add_contato = QMainWindow()
        self.ui_add_contato = Ui_tela_add_contato()
        self.ui_add_contato.setupUi(self.tela_add_contato, self.tela_add_contato)
        self.tela_add_contato.show()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()
