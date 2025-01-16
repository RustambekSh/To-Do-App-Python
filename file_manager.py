from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt
from styles import *

class FileManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle("File Manager")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR}; border-radius: 15px;")

        layout = QVBoxLayout()

        # Header
        header = QLabel("Saved Files")
        header.setStyleSheet(f"font-size: {HEADER_FONT_SIZE}px; font-weight: bold; color: {PRIMARY_COLOR};")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Text area to display saved files
        self.file_display = QTextEdit()
        self.file_display.setReadOnly(True)
        self.file_display.setStyleSheet(f"background-color: {CARD_COLOR}; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px; border-radius: 5px;")
        layout.addWidget(self.file_display)

        # Button to load files
        load_button = QPushButton("Load Files")
        load_button.setStyleSheet(SECONDARY_BUTTON_STYLE)
        load_button.clicked.connect(self.load_files)
        layout.addWidget(load_button)

        self.setLayout(layout)

    def load_files(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "r") as file:
                self.file_display.setText(file.read())

