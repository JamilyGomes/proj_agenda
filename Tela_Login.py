from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox
 
class Ui_Tela_Login(object):
    def setupUi(self, Tela_Login):
        if not Tela_Login.objectName():
            Tela_Login.setObjectName(u"Tela_Login")
        Tela_Login.resize(800, 600)

        # Central Widget
        self.centralwidget = QWidget(Tela_Login)
        self.centralwidget.setObjectName(u"centralwidget")

        # Frame para a tela
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(0, 0, 800, 600)  # Ajustado para o tamanho da janela
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Título "Login"
        self.txt_Login = QLabel(self.frame)
        self.txt_Login.setObjectName(u"txt_Login")
        self.txt_Login.setGeometry(100, 30, 121, 31)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_Login.setFont(font1)

        # Campo de E-mail
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(100, 340, 121, 16)
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_email.setFont(font2)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(100, 360, 551, 22)

        # Campo de Senha
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(100, 400, 121, 16)
        self.txt_senha.setFont(font2)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(100, 420, 551, 22)
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)

        # Botão de Login
        self.pushButton_Entrar = QPushButton(self.frame)
        self.pushButton_Entrar.setObjectName(u"pushButton_Entrar")
        self.pushButton_Entrar.setGeometry(320, 480, 131, 51)
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")
        self.pushButton_Entrar.clicked.connect(self.realizar_login)  # Conectar ao método de login

        # Link para Cadastro
        self.link_cadastrar = QLabel(self.frame)
        self.link_cadastrar.setObjectName(u"link_cadastrar")
        self.link_cadastrar.setGeometry(80, 70, 121, 16)
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(True)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.link_cadastrar.setText("Cadastre-se")
        self.link_cadastrar.mousePressEvent = self.abrir_tela_cadastro  # Link clicável

        # Exibindo a imagem corretamente
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(215, 20, 341, 331))
        self.label.setPixmap(QPixmap("asc.png"))  # Alterar para o caminho correto
        self.label.setScaledContents(True)  # Permitindo que a imagem se ajuste ao tamanho do QLabel
        self.label.raise_()  # Garante que a imagem fique no topo da camada visual

        Tela_Login.setCentralWidget(self.centralwidget)
        self.retranslateUi(Tela_Login)
        QMetaObject.connectSlotsByName(Tela_Login)

    def retranslateUi(self, Tela_Login):
        Tela_Login.setWindowTitle(QCoreApplication.translate("Tela_Login", u"Login de Usuário", None))
        self.txt_Login.setText(QCoreApplication.translate("Tela_Login", u"Login", None))
        self.txt_email.setText(QCoreApplication.translate("Tela_Login", u"Email:", None))
        self.txt_senha.setText(QCoreApplication.translate("Tela_Login", u"Senha:", None))
        self.pushButton_Entrar.setText(QCoreApplication.translate("Tela_Login", u"Entrar", None))

    def abrir_tela_cadastro(self, event):
        from cadastro_proj import Ui_Tela_Cadastro  # Importe a tela de cadastro
        self.window = QMainWindow()  # Crie uma nova janela
        self.ui = Ui_Tela_Cadastro()  # Instancie a tela de cadastro
        self.ui.setupUi(self.window)  # Configure a tela de cadastro
        self.window.show()  # Exiba

    def realizar_login(self):
        # Função para realizar o login
        email = self.line_email.text()
        senha = self.line_senha.text()

        # Verificação simples (alterar conforme sua lógica de validação)
        if email == "betta@example.com" and senha == "123":
            self.close_window()  # Fechar a janela de login
            self.open_contact_screen()  # Chama a função para abrir a tela de contatos
        else:
            QMessageBox.warning(None, "Erro", "Email ou senha incorretos. Tente novamente.")

    def close_window(self):
        # Verifique se a janela principal foi passada para a classe
        if hasattr(self, 'window'):
            self.window.close()  # Fechar a janela principal
        else:
            print("Erro: A janela principal não foi inicializada corretamente.")

    def open_contact_screen(self):
        # Esta função abre a tela de contatos (a segunda tela que você forneceu)
        from contatos import Ui_Form  # Importe a tela de contatos
        self.window = QMainWindow()  # Crie uma nova janela
        self.ui = Ui_Form()  # Instancie a tela de contatos
        self.ui.setupUi(self.window)  # Configure a tela de contatos
        self.window.show()  # Exiba a tela de contatos

if __name__ == "__main__":
    app = QApplication([])  # Criação da aplicação
    MainWindow = QMainWindow()  # Criação da janela principal
    ui = Ui_Tela_Login()  # Instancia a tela de login
    ui.setupUi(MainWindow)  # Configura a interface de login
    MainWindow.show()  # Exibe a janela principal
    app.exec()  # Inicia o loop de eventos da aplicação
