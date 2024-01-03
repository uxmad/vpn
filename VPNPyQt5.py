import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class AuthWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Authorization')
        self.setGeometry(100, 100, 600, 450)
        self.setStyleSheet("background-color: #000434;")

        layout = QVBoxLayout()

        label_login = QLabel('Login Proxy', self)
        label_login.setStyleSheet("color: #FFFFFF; font-family: Mazzard; font-size: 20px; qproperty-alignment: AlignCenter;")

        label_enter_key = QLabel('Enter key:', self)
        label_enter_key.setStyleSheet("color: #FFFFFF; font-family: Mazzard; font-size: 15px; qproperty-alignment: AlignCenter;")

        self.input_code = QLineEdit(self)
        self.input_code.setStyleSheet("border-radius: 10px; font-size: 20px; color: white;border: 1px solid #ffffff;")
        self.input_code.setFixedSize(600, 60)

        btn_submit = QPushButton('Submit', self)
        btn_submit.setStyleSheet("border-radius: 10px; background-color: #4CAF50; color: #FFFFFF; width: 60px; height: 40px; color: #ffffff;text-align: center; text-decoration: none; font-size: 16px; margin: 4px 2px;")
        btn_submit.clicked.connect(self.authenticate)

        layout.addWidget(label_login)
        layout.addWidget(label_enter_key)
        layout.addWidget(self.input_code)
        layout.addWidget(btn_submit)

        self.setLayout(layout)

    def authenticate(self):
        code = self.input_code.text()
        response = requests.get(f'https://yourapi.ru/api.php?key=&validateuser={code}')

        if response.text.strip() == "true":
            self.close()
            server_window.show()


class ServerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 450, 600)
        self.setWindowTitle('VPN LIST')
        self.setStyleSheet("background-color: #000434;")
        self.server_label = QPushButton('Server List ', self)
        self.server_label.setGeometry(10, 10, 430, 60)
        self.server_label.setStyleSheet('background-color: #0d1744; color: white; border-radius: 3px; font-family: Mazzard; font-size: 20px; padding :15px;')

        
        self.server_buttons = {
            'USA': QPushButton('USA', self),
            'Canada': QPushButton('Canada', self),
            'United Kingdom': QPushButton('United Kingdom', self),
            'Germany': QPushButton('Germany', self),
            'Japan': QPushButton('Japan', self),
        }

        v_layout = QVBoxLayout()

        for server, button in self.server_buttons.items():
            button.setStyleSheet('background-color: #4CAF50; color: white; border-radius: 10px; font-size: 18px; font-family: Mazzard;')
            button.setFixedSize(430, 60)
            button.clicked.connect(lambda _, server=server: self.connect_to_server(server))
            v_layout.addWidget(button)

        self.setLayout(v_layout)

    def connect_to_server(self, server):
        # Здесь вы можете добавить логику подключения к серверу
        # Например, вы можете использовать библиотеку для сетевого взаимодействия.

        # Предположим, что подключение прошло успешно
        print(f'Successfully connected to {server}')

        # Обновим текст надписи серверов
        self.server_label.setText(f'Conected to: {server}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    auth_window = AuthWindow()
    server_window = ServerWindow()

    auth_window.show()

    sys.exit(app.exec_())
