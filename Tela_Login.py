import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                               QPushButton, QWidget, QMessageBox, QVBoxLayout,
                               QHBoxLayout)

from dados_locais import autenticar_usuario
from contatos import Ui_Form

class Ui_Tela_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Tela_Login")
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)

        self.frame = QWidget(self)
        self.frame.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
            border-radius: 10px;
        """)
        self.main_layout.addWidget(self.frame, stretch=1)

        self.frame_layout = QVBoxLayout(self.frame)
        self.frame_layout.setContentsMargins(40, 40, 40, 40)
        self.frame_layout.setSpacing(20)
        self.frame_layout.setAlignment(Qt.AlignCenter)

        self.txt_Login = QLabel("Bem-vindo!", self.frame)
        font1 = QFont("Segoe UI", 20, QFont.Bold)
        self.txt_Login.setFont(font1)
        self.txt_Login.setStyleSheet("color: rgb(220, 220, 255); background-color: transparent;")
        self.txt_Login.setAlignment(Qt.AlignCenter)
        self.frame_layout.addWidget(self.txt_Login)

        self.email_layout = QHBoxLayout()
        self.txt_email = QLabel("Email:", self.frame)
        font2 = QFont("Segoe UI", 12)
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.email_layout.addWidget(self.txt_email)

        self.line_email = QLineEdit(self.frame)
        self.line_email.setMinimumHeight(30)
        self.line_email.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.email_layout.addWidget(self.line_email, stretch=1)
        self.frame_layout.addLayout(self.email_layout)

        self.senha_layout = QHBoxLayout()
        self.txt_senha = QLabel("Senha:", self.frame)
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet("color: rgb(200, 200, 200);")
        self.senha_layout.addWidget(self.txt_senha)

        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setMinimumHeight(30)
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.senha_layout.addWidget(self.line_senha, stretch=1)
        self.frame_layout.addLayout(self.senha_layout)

        self.pushButton_Entrar = QPushButton("Entrar", self.frame)
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(120, 170, 255),
                    stop: 1 rgb(90, 120, 220)
                );
            }
            QPushButton:pressed {
                background: rgb(50, 80, 180);
            }
        """)
        self.pushButton_Entrar.setCursor(Qt.PointingHandCursor)
        self.pushButton_Entrar.setMinimumSize(100, 40)
        self.frame_layout.addWidget(self.pushButton_Entrar, alignment=Qt.AlignHCenter)

        self.link_cadastrar = QPushButton("Cadastre-se", self.frame)
        font4 = QFont("Segoe UI", 10)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 220, 100);
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                color: rgb(255, 200, 80);
                text-decoration: underline;
            }
        """)
        self.link_cadastrar.setCursor(Qt.PointingHandCursor)
        self.link_cadastrar.setMinimumSize(100, 20)
        self.frame_layout.addWidget(self.link_cadastrar, alignment=Qt.AlignHCenter)

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tela_Login()
        self.setCentralWidget(self.ui)
        self.ui.pushButton_Entrar.clicked.connect(self.realizar_login)
        self.ui.link_cadastrar.clicked.connect(self.abrir_tela_cadastro)
        self.setMinimumSize(400, 300)
        self.resize(800, 600)

    def realizar_login(self):
        email = self.ui.line_email.text().strip()
        senha = self.ui.line_senha.text().strip()

        try:
            autenticado, usuario_id, nome_usuario = autenticar_usuario(email, senha)
        except Exception as e:
            QMessageBox.warning(self, "Erro", f"Erro ao autenticar: {str(e)}")
            return

        if autenticado:
            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {nome_usuario}!")
            self.abrir_tela_contatos(usuario_id)
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")

    def abrir_tela_contatos(self, usuario_id):
        self.tela_contatos = QMainWindow()
        self.ui_contatos = Ui_Form(usuario_id)
        self.ui_contatos.setupUi(self.tela_contatos)
        self.tela_contatos.show()

    def abrir_tela_cadastro(self):
        from cadastro_proj import Ui_Tela_Cadastro
        self.tela_cadastro = QMainWindow()
        self.ui_cadastro = Ui_Tela_Cadastro()
        self.ui_cadastro.setupUi(self.tela_cadastro)
        self.tela_cadastro.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TelaLogin()
    main_window.show()
    sys.exit(app.exec())