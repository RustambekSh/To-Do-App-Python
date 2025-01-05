# main.py

import sys
from PyQt5.QtWidgets import QApplication
from todo_app import ToDoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Modern style
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())