import sys
from PySide6.QtCore import QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from bancodedados import autenticar_usuario
from contatos import Ui_Form as Ui_Tela_Contatos  # Renomeado para evitar conflito
from cadastro_proj import Ui_Tela_Cadastro  

class Ui_Tela_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Tela_Login")
        self.setFixedSize(800, 600)

        # Frame principal com gradiente moderno
        self.frame = QWidget(self)
        self.frame.setGeometry(0, 0, 800, 600)
        self.frame.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)

        # Título "Login" (caixa reduzida, fundo transparente)
        self.txt_Login = QLabel("Login", self.frame)
        self.txt_Login.setGeometry(100, 30, 75, 35)  # Reduzido de 121x31 para 75x35
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.txt_Login.setFont(font1)
        self.txt_Login.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)  # Fundo transparente

        # Campo Email (label reduzida)
        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setGeometry(100, 340, 35, 14)  # Reduzido de 121x16 para 35x14
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(100, 360, 551, 30)
        self.line_email.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)

        # Campo Senha (label reduzida)
        self.txt_senha = QLabel("Senha:", self.frame)
        self.txt_senha.setGeometry(100, 410, 39, 14)  # Reduzido de 121x16 para 39x14
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setGeometry(100, 430, 551, 30)
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)

        # Botão Entrar
        self.pushButton_Entrar = QPushButton("Entrar", self.frame)
        self.pushButton_Entrar.setGeometry(320, 490, 131, 41)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
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
                padding: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
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

        # Link Cadastre-se (caixa reduzida, letras em branco)
        self.link_cadastrar = QLabel("<a href='cadastro'>Cadastre-se</a>", self.frame)
        self.link_cadastrar.setGeometry(100, 70, 80, 14)  # Reduzido de 121x16 para 80x14
        font4 = QFont()
        font4.setPointSize(10)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.link_cadastrar.setOpenExternalLinks(False)

        # Imagem ajustada
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(295, 130, 200, 150))  # Reduzido de 341x231 para 300x200 e centralizado
        self.label.setPixmap(QPixmap("asc.png"))
        self.label.setScaledContents(True)

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tela_Login()
        self.setCentralWidget(self.ui)

        self.ui.pushButton_Entrar.clicked.connect(self.realizar_login)
        self.ui.link_cadastrar.linkActivated.connect(self.abrir_tela_cadastro)

    def realizar_login(self):
        email = self.ui.line_email.text().strip()
        senha = self.ui.line_senha.text()

        if not email or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        try:
            autenticado, usuario_id, nome_usuario = autenticar_usuario(email, senha)
            if autenticado:
                QMessageBox.information(self, "Sucesso", f"Bem-vindo, {nome_usuario}!")
                self.abrir_tela_contatos(usuario_id)
            else:
                QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Falha na autenticação: {e}")

    def abrir_tela_contatos(self, usuario_id):
        if not hasattr(self, 'tela_contatos') or not self.tela_contatos.isVisible():
            self.tela_contatos = QMainWindow()
            self.ui_contatos = Ui_Tela_Contatos(usuario_id)
            self.ui_contatos.setupUi(self.tela_contatos)
        self.hide()
        self.tela_contatos.show()
        self.ui_contatos.carregar_contatos()

    def abrir_tela_cadastro(self):
        if not hasattr(self, 'tela_cadastro') or not self.tela_cadastro.isVisible():
            self.tela_cadastro = QMainWindow()
            self.ui_cadastro = Ui_Tela_Cadastro()
            self.ui_cadastro.setupUi(self.tela_cadastro)
        self.hide()
        self.tela_cadastro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TelaLogin()
    main_window.show()
    sys.exit(app.exec())