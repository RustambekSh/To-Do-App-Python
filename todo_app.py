import json
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QCheckBox,
    QMessageBox, QLabel, QProgressBar, QGroupBox
)
from PyQt5.QtCore import Qt
from task_details_dialog import TaskDetailsDialog
from file_manager import FileManager
from styles import *

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
       
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR}; border-radius: 15px;")

        layout = QVBoxLayout()

        header = QLabel("My To-Do List")
        header.setStyleSheet(f"font-size: {HEADER_FONT_SIZE}px; font-weight: bold; color: {PRIMARY_COLOR};")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.setStyleSheet(INPUT_STYLE)
        input_layout.addWidget(self.task_input)

        self.add_button = QPushButton("➕ Add Task", self)
        self.add_button.setStyleSheet(BUTTON_STYLE)
        self.add_button.clicked.connect(self.add_task)
        input_layout.addWidget(self.add_button)

        layout.addLayout(input_layout)

        self.task_sections = QVBoxLayout()

        self.active_tasks_group = QGroupBox("Active Tasks")
        self.active_tasks_group.setStyleSheet(f"color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
        self.active_tasks_layout = QVBoxLayout()
        self.active_tasks_layout.setAlignment(Qt.AlignTop)
        self.active_tasks_group.setLayout(self.active_tasks_layout)
        self.task_sections.addWidget(self.active_tasks_group)

        self.completed_tasks_group = QGroupBox("Completed Tasks")
        self.completed_tasks_group.setStyleSheet(f"color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
        self.completed_tasks_layout = QVBoxLayout()
        self.completed_tasks_layout.setAlignment(Qt.AlignTop)
        self.completed_tasks_group.setLayout(self.completed_tasks_layout)
        self.task_sections.addWidget(self.completed_tasks_group)

        
        layout.addLayout(self.task_sections)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{ 
                background-color: {CARD_COLOR}; 
                color: {TEXT_COLOR}; 
                border-radius: 5px; 
            }}
            QProgressBar::chunk {{ 
                background-color: {PRIMARY_COLOR}; 
                border-radius: 5px; 
            }}
        """)
        layout.addWidget(self.progress_bar)

        button_layout = QHBoxLayout()
        self.clear_completed_button = QPushButton("🗑️ Clear Completed")
        self.clear_completed_button.setStyleSheet(DELETE_BUTTON_STYLE)
        self.clear_completed_button.clicked.connect(self.clear_completed_tasks)
        button_layout.addWidget(self.clear_completed_button)

        self.file_manager_button = QPushButton("📂 File Manager")
        self.file_manager_button.setStyleSheet(SECONDARY_BUTTON_STYLE)
        self.file_manager_button.clicked.connect(self.open_file_manager)
        button_layout.addWidget(self.file_manager_button)

        layout.addLayout(button_layout)

        self.load_tasks()

        self.setLayout(layout)

    def add_task(self):
        try:
            task_text = self.task_input.text().strip()
            if task_text:
                details_dialog = TaskDetailsDialog()
                if details_dialog.exec_() == QDialog.Accepted:
                    details = details_dialog.get_details()
                    self.create_task_item(task_text, details)
                    self.task_input.clear()
                    self.save_tasks()
            else:
                QMessageBox.warning(self, "Warning", "Please enter a task!")
        except Exception as e:
            print(f"Error in add_task: {e}")
            QMessageBox.critical(self, "Error", f"Failed to add task: {e}")

    def create_task_item(self, task_text, details):
        try:
            task_widget = QWidget()
            task_layout = QHBoxLayout()

            checkbox = QCheckBox()
            checkbox.setStyleSheet(f"color: {TEXT_COLOR};")
            checkbox.stateChanged.connect(lambda: self.mark_task_completed(task_widget, checkbox))
            task_layout.addWidget(checkbox)

            task_label = QLineEdit(task_text)
            task_label.setReadOnly(True)
            task_label.setStyleSheet(f"background-color: transparent; border: none; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
            task_layout.addWidget(task_label)

            priority_label = QLabel(details["priority"])
            priority_label.setStyleSheet(
                f"color: {PRIMARY_COLOR if details['priority'] == 'High' else SECONDARY_COLOR if details['priority'] == 'Medium' else TEXT_COLOR}; font-size: 12px;"
            )
            task_layout.addWidget(priority_label)

            due_date_label = QLabel(details["due_date"])
            due_date_label.setStyleSheet(f"color: {SECONDARY_COLOR}; font-size: 12px;")
            task_layout.addWidget(due_date_label)

            tags_label = QLabel(details["tags"])
            tags_label.setStyleSheet(f"color: {TEXT_COLOR}; font-size: 12px;")
            task_layout.addWidget(tags_label)

            delete_button = QPushButton("🗑️")
            delete_button.setStyleSheet(f"background-color: transparent; border: none; color: {DANGER_COLOR}; font-size: 14px;")
            delete_button.clicked.connect(lambda: self.delete_task(task_widget))
            task_layout.addWidget(delete_button)

            task_widget.setLayout(task_layout)

            self.active_tasks_layout.addWidget(task_widget)
        except Exception as e:
            print(f"Error in create_task_item: {e}")
            QMessageBox.critical(self, "Error", f"Failed to create task: {e}")

    def mark_task_completed(self, task_widget, checkbox):
        try:
            if checkbox.isChecked():
                self.active_tasks_layout.removeWidget(task_widget)
                self.completed_tasks_layout.addWidget(task_widget)
                task_widget.setStyleSheet(f"background-color: {CARD_COLOR}; color: {TEXT_COLOR}; border-radius: 10px; padding: 8px;")
            self.save_tasks()
            self.update_progress()
        except Exception as e:
            print(f"Error in mark_task_completed: {e}")
            QMessageBox.critical(self, "Error", f"Failed to mark task as completed: {e}")

    def delete_task(self, task_widget):
        try:
            self.active_tasks_layout.removeWidget(task_widget)
            self.completed_tasks_layout.removeWidget(task_widget)
            task_widget.deleteLater()
            self.save_tasks()
            self.update_progress()
        except Exception as e:
            print(f"Error in delete_task: {e}")
            QMessageBox.critical(self, "Error", f"Failed to delete task: {e}")

    def clear_completed_tasks(self):
        try:
            for i in reversed(range(self.completed_tasks_layout.count())):
                widget = self.completed_tasks_layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()
            self.save_tasks()
            self.update_progress()
        except Exception as e:
            print(f"Error in clear_completed_tasks: {e}")
            QMessageBox.critical(self, "Error", f"Failed to clear completed tasks: {e}")

    def open_file_manager(self):
        try:
            self.file_manager = FileManager()
            self.file_manager.show()
        except Exception as e:
            print(f"Error in open_file_manager: {e}")
            QMessageBox.critical(self, "Error", f"Failed to open file manager: {e}")

    def update_progress(self):
        try:
            total_tasks = self.active_tasks_layout.count() + self.completed_tasks_layout.count()
            completed_tasks = self.completed_tasks_layout.count()
            self.progress_bar.setValue(int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0)
        except Exception as e:
            print(f"Error in update_progress: {e}")
            QMessageBox.critical(self, "Error", f"Failed to update progress: {e}")

    def save_tasks(self):
        try:
            tasks = []
            for i in range(self.active_tasks_layout.count()):
                widget = self.active_tasks_layout.itemAt(i).widget()
                if widget:
                    task_text = widget.findChild(QLineEdit).text()
                    checkbox = widget.findChild(QCheckBox)
                    priority_label = widget.findChild(QLabel)
                    due_date_label = widget.findChildren(QLabel)[1]
                    tags_label = widget.findChildren(QLabel)[2]
                    tasks.append(
                        f"{task_text},{checkbox.isChecked()},{priority_label.text()},{due_date_label.text()},{tags_label.text()}")
            for i in range(self.completed_tasks_layout.count()):
                widget = self.completed_tasks_layout.itemAt(i).widget()
                if widget:
                    task_text = widget.findChild(QLineEdit).text()
                    checkbox = widget.findChild(QCheckBox)
                    priority_label = widget.findChild(QLabel)
                    due_date_label = widget.findChildren(QLabel)[1]
                    tags_label = widget.findChildren(QLabel)[2]
                    tasks.append(
                        f"{task_text},{checkbox.isChecked()},{priority_label.text()},{due_date_label.text()},{tags_label.text()}")
            with open("todo_qt_advanced.txt", "w") as file:
                file.write("\n".join(tasks))
            print("Tasks saved successfully.") 
        except Exception as e:
            print(f"Error in save_tasks: {e}") 
            QMessageBox.critical(self, "Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
        try:
            with open("todo_qt_advanced.txt", "r") as file:
                tasks = file.read().splitlines()
                for task in tasks:
                    if task:
                        parts = task.split(",")
                        if len(parts) < 5:
                            print(f"Skipping invalid task: {task}") 
                            continue
                        task_text = parts[0]
                        completed = parts[1]
                        priority = parts[2]
                        due_date = parts[3]
                        tags = parts[4]
                        details = {"priority": priority, "due_date": due_date, "tags": tags}
                        self.create_task_item(task_text, details)
                        if completed == "True":
                            task_widget = self.active_tasks_layout.itemAt(self.active_tasks_layout.count() - 1).widget()
                            checkbox = task_widget.findChild(QCheckBox)
                            checkbox.setChecked(True)
                            self.mark_task_completed(task_widget, checkbox)
        except FileNotFoundError:
            print("No saved tasks found.") 
        except Exception as e:
            print(f"Error in load_tasks: {e}") 
            QMessageBox.critical(self, "Error", f"Failed to load tasks: {e}")

