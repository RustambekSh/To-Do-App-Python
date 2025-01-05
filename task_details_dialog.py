# task_details_dialog.py

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QDateEdit, QComboBox, QLineEdit, QLabel, QPushButton, QTimeEdit
from PyQt5.QtCore import QDate, QTime
from styles import *

class TaskDetailsDialog(QDialog):
    def __init__(self, task_text="", due_date=QDate.currentDate(), priority="Medium", description="", tags="", timer=QTime(0, 0), parent=None):
        super().__init__(parent)
        self.setWindowTitle("Task Details")
        self.setGeometry(200, 200, 350, 350)
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR}; border-radius: 10px;")

        layout = QVBoxLayout()

        # Task Description
        self.description_input = QTextEdit()
        self.description_input.setPlainText(description)
        self.description_input.setStyleSheet(f"background-color: #3B4252; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px; border-radius: 5px;")
        layout.addWidget(QLabel("Description:"))
        layout.addWidget(self.description_input)

        # Due Date
        self.due_date_input = QDateEdit(due_date)
        self.due_date_input.setStyleSheet(f"background-color: #3B4252; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px; border-radius: 5px;")
        layout.addWidget(QLabel("Due Date:"))
        layout.addWidget(self.due_date_input)

        # Priority
        self.priority_input = QComboBox()
        self.priority_input.addItems(["High", "Medium", "Low"])
        self.priority_input.setCurrentText(priority)
        self.priority_input.setStyleSheet(f"background-color: #3B4252; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px; border-radius: 5px;")
        layout.addWidget(QLabel("Priority:"))
        layout.addWidget(self.priority_input)

        # Tags
        self.tags_input = QLineEdit(tags)
        self.tags_input.setPlaceholderText("Enter tags (e.g., Urgent, Important)")
        self.tags_input.setStyleSheet(f"background-color: #3B4252; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px; border-radius: 5px;")
        layout.addWidget(QLabel("Tags:"))
        layout.addWidget(self.tags_input)

        # Timer
        self.timer_input = QTimeEdit(timer)
        self.timer_input.setDisplayFormat("HH:mm")
        self.timer_input.setStyleSheet(f"background-color: #3B4252; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px; border-radius: 5px;")
        layout.addWidget(QLabel("Timer (HH:mm):"))
        layout.addWidget(self.timer_input)

        # Save Button
        save_button = QPushButton("Save")
        save_button.setStyleSheet(BUTTON_STYLE)
        save_button.clicked.connect(self.accept)
        layout.addWidget(save_button)

        self.setLayout(layout)

    # In the TaskDetailsDialog class
    def get_details(self):
        return {
            "description": self.description_input.toPlainText(),
            "due_date": self.due_date_input.date().toString("yyyy-MM-dd"),
            "priority": self.priority_input.currentText(),
            "tags": self.tags_input.text(),
            "timer": self.timer_input.time().toString("HH:mm"),  # Ensure timer is correctly formatted
        }