from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QPushButton, QMainWindow, QWidget)

class Ui_Form(object):
    def setupUi(self, Form, contato_info=None):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(644, 759)
        
        self.frame_editarcntt = QFrame(Form)
        self.frame_editarcntt.setObjectName("frame_editarcntt")
        self.frame_editarcntt.setGeometry(QRect(30, 60, 561, 611))
        self.frame_editarcntt.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.label_Nome = QLabel("Nome:", self.frame_editarcntt)
        self.label_Nome.setGeometry(QRect(20, 60, 47, 13))
        
        self.label_Contato = QLabel("Contato:", self.frame_editarcntt)
        self.label_Contato.setGeometry(QRect(20, 120, 47, 13))
        
        self.label_Email = QLabel("Email:", self.frame_editarcntt)
        self.label_Email.setGeometry(QRect(20, 190, 47, 13))
        
        self.label_Rede_Social = QLabel("Perfil de Rede Social:", self.frame_editarcntt)
        self.label_Rede_Social.setGeometry(QRect(20, 310, 150, 16))
        
        self.label_Notas = QLabel("Notas:", self.frame_editarcntt)
        self.label_Notas.setGeometry(QRect(20, 370, 47, 13))
        
        self.label_DataNasc = QLabel("Data de Nascimento:", self.frame_editarcntt)
        self.label_DataNasc.setGeometry(QRect(20, 250, 150, 16))
        
        self.data_Nasc = QDateEdit(self.frame_editarcntt)
        self.data_Nasc.setGeometry(QRect(20, 270, 110, 22))
        
        self.lineEdit_nome = QLineEdit(self.frame_editarcntt)
        self.lineEdit_nome.setGeometry(QRect(20, 80, 521, 20))
        
        self.lineEdit_Cntt = QLineEdit(self.frame_editarcntt)
        self.lineEdit_Cntt.setGeometry(QRect(20, 140, 521, 20))
        self.lineEdit_Cntt.setInputMask("(99) 99999-9999")  # Adicionando a máscara de entrada para o campo de telefone
        
        self.lineEdit_Email = QLineEdit(self.frame_editarcntt)
        self.lineEdit_Email.setGeometry(QRect(20, 210, 521, 20))
        
        self.lineEdit_RedeSocial = QLineEdit(self.frame_editarcntt)
        self.lineEdit_RedeSocial.setGeometry(QRect(20, 330, 521, 20))
        
        self.lineEdit_Notas = QLineEdit(self.frame_editarcntt)
        self.lineEdit_Notas.setGeometry(QRect(20, 390, 521, 141))
        
        self.pushButton_voltar = QPushButton("Voltar", self.frame_editarcntt)
        self.pushButton_voltar.setGeometry(QRect(470, 20, 75, 23))
        self.pushButton_voltar.setStyleSheet("background-color: rgb(0, 0, 255); color: rgb(255, 255, 255);")
        self.pushButton_voltar.clicked.connect(Form.close)
        
        self.pushButton_Salvar = QPushButton("Salvar", self.frame_editarcntt)
        self.pushButton_Salvar.setGeometry(QRect(470, 570, 75, 23))
        self.pushButton_Salvar.setStyleSheet("background-color: rgb(0, 0, 255); color: rgb(255, 255, 255);")
        
        if contato_info:
            self.lineEdit_nome.setText(contato_info.get("nome", ""))
            self.lineEdit_Cntt.setText(contato_info.get("contato", ""))
            self.lineEdit_Email.setText(contato_info.get("email", ""))
            self.lineEdit_RedeSocial.setText(contato_info.get("rede_social", ""))
            self.lineEdit_Notas.setText(contato_info.get("notas", ""))
        
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Editar Contato"))

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_Form()
    contato_exemplo = {
        "nome": "João Silva",
        "contato": "(11) 99999-9999",  # Exemplo com a máscara
        "email": "joao@email.com",
        "rede_social": "@joaosilva",
        "notas": "Amigo de infância"
    }
    ui.setupUi(MainWindow, contato_exemplo)
    MainWindow.show()
    app.exec()
