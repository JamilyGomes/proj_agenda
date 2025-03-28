# Importação das bibliotecas do PySide6 para criação da interface gráfica
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow
from add_cntt import Ui_tela_add_contato  # Importando a tela de adição de contato
from PySide6.QtCore import QSortFilterProxyModel, QStringListModel
from editarcntt import Ui_Form as Ui_EditarContato  # Importando a tela de edição de contato

# Definição da classe principal da interface
class Ui_Form(object):
    
    def setupUi(self, Form):
        """ Configura a interface da tela principal com os elementos básicos """
        
        if not Form.objectName():  # Verifica se o nome do objeto não foi definido
            Form.setObjectName(u"Form")
        
        # Redimensiona a janela principal
        Form.resize(988, 579)
        
        # Criação do frame principal onde os contatos serão exibidos
        self.frame_principal_cntt = QFrame(Form)
        self.frame_principal_cntt.setObjectName(u"frame_principal_cntt")
        self.frame_principal_cntt.setGeometry(QRect(170, 80, 651, 401))  # Define o tamanho e posição do frame
        self.frame_principal_cntt.setStyleSheet(u"background-color: rgb(255, 255, 255);")  # Estilo do frame (cor de fundo)
        
        # Label que exibe o título "Contatos"
        self.label_Cntt = QLabel(self.frame_principal_cntt)
        self.label_Cntt.setObjectName(u"label_Cntt")
        self.label_Cntt.setGeometry(QRect(30, 20, 71, 16))  # Posição e tamanho
        self.label_Cntt.setStyleSheet(u"font: 700 12pt \"Segoe Print\";")  # Estilo do texto
        
        # Campo de texto para buscar contatos
        self.line_buscar_cntt = QLineEdit(self.frame_principal_cntt)
        self.line_buscar_cntt.setObjectName(u"line_buscar_cntt")
        self.line_buscar_cntt.setGeometry(QRect(30, 40, 181, 22))  # Posição e tamanho
        self.line_buscar_cntt.setPlaceholderText("Buscar Contatos...")  # Texto de placeholder
        
        # Lista de contatos (aqui apenas com exemplos fixos)
        self.list_cntt = QListView(self.frame_principal_cntt)
        self.list_cntt.setObjectName(u"list_cntt")
        self.list_cntt.setGeometry(QRect(30, 80, 591, 291))  # Posição e tamanho
        
        # Lista de contatos (aqui temos apenas exemplos estáticos)
        self.contatos = ["Abgail", "Bento", "João", "Maria"]
        y_positions = [90, 130, 170, 210]  # Posições verticais onde os contatos serão exibidos
        self.labels_contatos = []  # Lista de labels para exibir o nome dos contatos
        self.labels_editar = []  # Lista de labels para exibir ícones de editar
        self.lines = []  # Lista de linhas de separação abaixo de cada contato
        
        # Criação dos widgets para cada contato
        for i, nome in enumerate(self.contatos):
            
            # Criação do label para o nome do contato
            label = QLabel(self.frame_principal_cntt)
            label.setObjectName(f"label_{nome}")
            label.setGeometry(QRect(40, y_positions[i], 50, 16))  # Posição e tamanho
            label.setText(nome)  # Definindo o nome do contato no label
            self.labels_contatos.append(label)  # Adiciona à lista de labels

            # Criação da linha de separação abaixo do nome do contato
            line = QFrame(self.frame_principal_cntt)
            line.setObjectName(f"line_{nome}")
            line.setGeometry(QRect(40, y_positions[i] + 18, 550, 1))  # Posição e tamanho
            line.setStyleSheet("background-color: black;")  # Estilo da linha (cor)
            self.lines.append(line)  # Adiciona à lista de linhas

            # Criação do ícone de editar para cada contato
            label_editar = QLabel(self.frame_principal_cntt)
            label_editar.setObjectName(f"label_editar{i+1}")
            label_editar.setGeometry(QRect(590, y_positions[i], 20, 20))  # Posição e tamanho
            label_editar.setPixmap(QPixmap(u"yy.png"))  # Ícone de editar
            label_editar.setScaledContents(True)  # Ajusta a escala da imagem
            self.labels_editar.append(label_editar)  # Adiciona à lista de ícones de editar
        
        # Ícone de adicionar novo contato
        self.label_add = QLabel(self.frame_principal_cntt)
        self.label_add.setObjectName(u"label_add")
        self.label_add.setGeometry(QRect(580, 40, 31, 31))  # Posição e tamanho
        self.label_add.setPixmap(QPixmap(u"xx.png"))  # Ícone de adicionar
        self.label_add.setScaledContents(True)  # Ajusta a escala da imagem
        self.label_add.mousePressEvent = self.adicionar_contato  # Conecta o evento de clique ao método de adicionar contato
        
        # Conecta a função de busca ao evento de texto alterado no campo de busca
        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)

        # Função para traduzir o texto da interface
        self.retranslateUi(Form)
        
        # Conecta o evento de clique nos ícones de editar aos métodos de edição de contatos
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, i=i: self.editar_contato(i)

    def retranslateUi(self, Form):
        """ Função para definir o título da janela e o texto do rótulo """
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", u"Contatos", None))

    def filtrar_contatos(self):
        """ Função para filtrar os contatos com base no texto inserido na busca """
        texto_busca = self.line_buscar_cntt.text().lower()  # Obtém o texto da busca e converte para minúsculas
        
        y_offset = 90  # Posição inicial para exibir os contatos filtrados
        
        # Para cada contato, verifica se o nome contém o texto da busca
        for i, label in enumerate(self.labels_contatos):
            nome_contato = label.text().lower()  # Obtém o nome do contato em minúsculas
            
            if texto_busca in nome_contato:  # Se o nome do contato contém o texto da busca
                # Torna os elementos visíveis
                self.labels_contatos[i].setVisible(True)
                self.lines[i].setVisible(True)
                self.labels_editar[i].setVisible(True)

                # Reposiciona os elementos de acordo com a busca
                self.labels_contatos[i].move(40, y_offset)
                self.lines[i].move(40, y_offset + 18)
                self.labels_editar[i].move(590, y_offset)

                y_offset += 40  # Atualiza a posição y para o próximo contato
            else:
                # Caso contrário, oculta os elementos
                self.labels_contatos[i].setVisible(False)
                self.lines[i].setVisible(False)
                self.labels_editar[i].setVisible(False)

    def editar_contato(self, i):
        """ Função chamada para editar um contato quando o ícone de edição é clicado """
        contato = self.contatos[i]  # Obtém o nome do contato
        print(f"Editando contato: {contato}")
        
        # Exemplo de informações do contato (aqui são valores fixos, mas deveriam vir de um banco de dados ou variável)
        contato_info = {
            "nome": contato,
            "contato": "(11) 99999-9999",  
            "email": "exemplo@email.com",
            "rede_social": "@exemplo",
            "notas": "Notas do contato"
        }
        
        # Criação da janela de edição de contato
        self.tela_editar_contato = QMainWindow()
        self.ui_editar_contato = Ui_EditarContato()
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info)  # Passa as informações do contato
        self.tela_editar_contato.show()  # Exibe a janela de edição

    def adicionar_contato(self, event):
        """ Função chamada para adicionar um novo contato quando o ícone de adicionar é clicado """
        # Criação da janela de adicionar contato
        self.tela_add_contato = QMainWindow()
        self.ui_add_contato = Ui_tela_add_contato()
        self.ui_add_contato.setupUi(self.tela_add_contato, self.tela_add_contato)  # Passa a tela para a função de adicionar
        self.tela_add_contato.show()  # Exibe a janela de adicionar
        event.accept()  # Aceita o evento

# Código principal para inicializar e executar a aplicação
if __name__ == "__main__":
    app = QApplication([])  # Criação da aplicação Qt
    MainWindow = QMainWindow()  # Criação da janela principal
    ui = Ui_Form()  # Criação da instância da interface
    ui.setupUi(MainWindow)  # Configura a interface gráfica na janela principal
    MainWindow.show()  # Exibe a janela principal
    app.exec()  # Inicia o loop de eventos da aplicação

