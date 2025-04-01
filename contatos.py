import sys
from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QMainWindow, QWidget, QScrollArea, QVBoxLayout,
                               QLineEdit, QLabel, QHBoxLayout, QApplication)
from chat_simples import Ui_Tela_Chat_Simples
from dados_locais import obter_usuarios

class Ui_Form(object):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self.labels_chat = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 579)
        Form.setWindowTitle("Chat")
        Form.setWindowIcon(QIcon("chat_icon.png"))

        self.centralwidget = QWidget(Form)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        Form.setCentralWidget(self.centralwidget)

        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(40, 40, 50);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
            }
        """)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_widget)

        self.label_usuarios = QLabel("Usuários")
        font_title = QFont("Segoe UI", 14, QFont.Bold)
        self.label_usuarios.setFont(font_title)
        self.label_usuarios.setStyleSheet("color: rgb(220, 220, 255); background-color: transparent; padding: 5px;")
        self.scroll_layout.addWidget(self.label_usuarios)

        self.line_buscar = QLineEdit()
        self.line_buscar.setPlaceholderText("Buscar Usuários...")
        self.line_buscar.setStyleSheet("""
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
        self.scroll_layout.addWidget(self.line_buscar)

        self.main_layout.addWidget(self.scroll_area)

        self.usuarios = []
        self.labels_usuarios = []
        self.labels_chat = []
        self.lines = []

        self.line_buscar.textChanged.connect(self.filtrar_usuarios)
        self.carregar_usuarios()
        QMetaObject.connectSlotsByName(Form)

    def filtrar_usuarios(self):
        texto_busca = self.line_buscar.text().lower()
        for i, label in enumerate(self.labels_usuarios):
            visivel = texto_busca in label.text().lower()
            label.setVisible(visivel)
            if i < len(self.labels_chat):
                self.labels_chat[i].setVisible(visivel)
            if i < len(self.lines):
                self.lines[i].setVisible(visivel)
        self.scroll_widget.adjustSize()
        self.scroll_area.update()

    def carregar_usuarios(self):
        self.usuarios = obter_usuarios()
        for label in self.labels_usuarios:
            label.deleteLater()
        for line in self.lines:
            line.deleteLater()
        for label_chat in self.labels_chat:
            label_chat.deleteLater()

        self.labels_usuarios.clear()
        self.lines.clear()
        self.labels_chat.clear()

        for i, usuario in enumerate(self.usuarios):
            if usuario["id"] == self.usuario_id:
                continue

            nome = usuario.get("nome", "Sem Nome")
            usuario_layout = QHBoxLayout()
            usuario_layout.setAlignment(Qt.AlignLeft)
            usuario_layout.setSpacing(10)

            label = QLabel()
            label.setObjectName(f"label_usuario_{nome}_{i}")
            label.setText(f"{nome}")
            label.setStyleSheet("""
                color: rgb(255, 255, 255);
                background-color: transparent;
                font-family: Segoe UI;
                font-size: 12pt;
                padding: 5px;
            """)
            usuario_layout.addWidget(label)
            self.labels_usuarios.append(label)

            label_chat = QLabel()
            label_chat.setObjectName(f"label_chat_{i}")
            label_chat.setText("Chat")
            label_chat.setStyleSheet("""
                color: rgb(100, 150, 255);
                background-color: transparent;
                font-family: Segoe UI;
                font-size: 12pt;
            """)
            label_chat.mousePressEvent = lambda event, idx=i: self.abrir_chat(idx)
            usuario_layout.addWidget(label_chat)
            self.labels_chat.append(label_chat)

            self.scroll_layout.addLayout(usuario_layout)

            line = QWidget()
            line.setFixedHeight(1)
            line.setStyleSheet("background-color: rgb(80, 80, 100);")
            self.scroll_layout.addWidget(line)
            self.lines.append(line)

    def abrir_chat(self, i):
        usuario = self.usuarios[i]
        usuario_info = {"id": usuario["id"], "nome": usuario["nome"]}
        self.tela_chat = QMainWindow()
        self.ui_chat = Ui_Tela_Chat_Simples()
        self.ui_chat.setupUi(self.tela_chat, self.usuario_id, usuario_info, self)
        self.tela_chat.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Form(1)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())