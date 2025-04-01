import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QMainWindow, QWidget, QLabel, QLineEdit,
                               QPushButton, QScrollArea, QVBoxLayout, QHBoxLayout,
                               QMessageBox)
from PySide6.QtWebSockets import QWebSocket
from dados_locais import salvar_mensagem, obter_mensagens
import json

class Ui_Tela_Chat_Simples(object):
    def setupUi(self, tela_chat, usuario_id, usuario_info, tela_contatos):
        self.tela_chat = tela_chat
        self.usuario_id = usuario_id
        self.usuario_info = usuario_info
        self.tela_contatos = tela_contatos

        tela_chat.setObjectName("tela_chat_simples")
        tela_chat.resize(988, 579)
        tela_chat.setWindowTitle(f"Chat com {usuario_info.get('nome', 'Desconhecido')}")

        self.centralwidget = QWidget(tela_chat)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        tela_chat.setCentralWidget(self.centralwidget)

        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.txt_chat = QLabel(f"Chat com {usuario_info.get('nome', 'Desconhecido')}")
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_chat.setFont(font1)
        self.txt_chat.setStyleSheet("color: rgb(220, 220, 255); background-color: transparent;")
        self.txt_chat.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.txt_chat)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(40, 40, 50);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
            }
        """)
        self.main_layout.addWidget(self.scroll_area, stretch=1)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_area.setWidget(self.scroll_widget)

        self.input_layout = QHBoxLayout()
        self.line_mensagem = QLineEdit()
        self.line_mensagem.setMinimumHeight(40)
        self.line_mensagem.setPlaceholderText("Digite sua mensagem...")
        self.line_mensagem.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
        """)
        self.line_mensagem.returnPressed.connect(self.enviar_mensagem)
        self.input_layout.addWidget(self.line_mensagem, stretch=1)

        self.btn_enviar = QPushButton("Enviar")
        self.btn_enviar.setMinimumSize(100, 40)
        self.btn_enviar.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.btn_enviar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 8px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(120, 170, 255),
                    stop: 1 rgb(90, 120, 220)
                );
            }
        """)
        self.btn_enviar.clicked.connect(self.enviar_mensagem)
        self.input_layout.addWidget(self.btn_enviar)

        self.main_layout.addLayout(self.input_layout)

        self.btn_voltar = QPushButton("Voltar")
        self.btn_voltar.setMinimumSize(100, 40)
        self.btn_voltar.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.btn_voltar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 100, 100),
                    stop: 1 rgb(200, 70, 70)
                );
                border-radius: 8px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 120, 120),
                    stop: 1 rgb(220, 90, 90)
                );
            }
        """)
        self.btn_voltar.clicked.connect(lambda: tela_chat.close())
        self.main_layout.addWidget(self.btn_voltar, alignment=Qt.AlignRight)

        self.websocket = QWebSocket()
        self.websocket.connected.connect(self.on_connected)
        self.websocket.textMessageReceived.connect(self.on_message_received)
        self.websocket.error.connect(self.on_error)
        self.websocket.open(QUrl("ws://localhost:5000"))

        self.carregar_mensagens_iniciais()

    def on_connected(self):
        print("Conectado ao servidor WebSocket")

    def on_message_received(self, message):
        data = json.loads(message)
        if (data["remetente_id"] == self.usuario_info["id"] and data["destinatario_id"] == self.usuario_id) or \
           (data["remetente_id"] == self.usuario_id and data["destinatario_id"] == self.usuario_info["id"]):
            remetente = "Você" if data["remetente_id"] == self.usuario_id else self.usuario_info["nome"]
            mensagem_texto = f"{remetente}: {data['mensagem']}"
            mensagem = QLabel(mensagem_texto)
            mensagem.setFont(QFont("Segoe UI", 12))
            mensagem.setStyleSheet("""
                color: rgb(255, 255, 255);
                background-color: rgb(50, 50, 60);
                padding: 8px;
                border-radius: 5px;
            """)
            mensagem.setWordWrap(True)
            align = Qt.AlignRight if data["remetente_id"] == self.usuario_id else Qt.AlignLeft
            self.scroll_layout.addWidget(mensagem, alignment=align)
            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def on_error(self, error):
        print(f"Erro no WebSocket: {error}")

    def carregar_mensagens_iniciais(self):
        mensagens = obter_mensagens(self.usuario_id, self.usuario_info["id"])
        for msg in mensagens:
            remetente = "Você" if msg["remetente_id"] == self.usuario_id else self.usuario_info["nome"]
            mensagem_texto = f"{remetente}: {msg['mensagem']}"
            mensagem = QLabel(mensagem_texto)
            mensagem.setFont(QFont("Segoe UI", 12))
            mensagem.setStyleSheet("""
                color: rgb(255, 255, 255);
                background-color: rgb(50, 50, 60);
                padding: 8px;
                border-radius: 5px;
            """)
            mensagem.setWordWrap(True)
            align = Qt.AlignRight if msg["remetente_id"] == self.usuario_id else Qt.AlignLeft
            self.scroll_layout.addWidget(mensagem, alignment=align)

    def enviar_mensagem(self):
        texto = self.line_mensagem.text().strip()
        if not texto:
            return
        if salvar_mensagem(self.usuario_id, self.usuario_info["id"], texto):
            mensagem = {
                "remetente_id": self.usuario_id,
                "destinatario_id": self.usuario_info["id"],
                "mensagem": texto
            }
            self.websocket.sendTextMessage(json.dumps(mensagem))
            self.line_mensagem.clear()
        else:
            QMessageBox.warning(None, "Erro", "Erro ao enviar mensagem.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela_chat = QMainWindow()
    ui = Ui_Tela_Chat_Simples()
    usuario_exemplo = {"id": 2, "nome": "Maria"}
    ui.setupUi(tela_chat, 1, usuario_exemplo, None)
    tela_chat.show()
    sys.exit(app.exec())