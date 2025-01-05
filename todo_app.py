# todo_app.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QCheckBox,
    QMessageBox, QLabel, QProgressBar, QGroupBox, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt
from task_details_dialog import TaskDetailsDialog
from styles import *

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR}; border-radius: 15px;")

        # Main layout
        layout = QVBoxLayout()

        # Header
        header = QLabel("My To-Do List")
        header.setStyleSheet(f"font-size: {HEADER_FONT_SIZE}px; font-weight: bold; color: #81A1C1;")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)

        # Input field and add button
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

        # Task sections
        self.task_sections = QVBoxLayout()

        # Active Tasks
        self.active_tasks_group = QGroupBox("Active Tasks")
        self.active_tasks_group.setStyleSheet(f"color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
        self.active_tasks_layout = QVBoxLayout()
        self.active_tasks_layout.setAlignment(Qt.AlignTop)  # Align items to the top
        self.active_tasks_group.setLayout(self.active_tasks_layout)
        self.task_sections.addWidget(self.active_tasks_group)

        # Timed Tasks
        self.timed_tasks_group = QGroupBox("Timed Tasks")
        self.timed_tasks_group.setStyleSheet(f"color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
        self.timed_tasks_layout = QVBoxLayout()
        self.timed_tasks_layout.setAlignment(Qt.AlignTop)  # Align items to the top
        self.timed_tasks_group.setLayout(self.timed_tasks_layout)
        self.task_sections.addWidget(self.timed_tasks_group)

        # Completed Tasks
        self.completed_tasks_group = QGroupBox("Completed Tasks")
        self.completed_tasks_group.setStyleSheet(f"color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
        self.completed_tasks_layout = QVBoxLayout()
        self.completed_tasks_layout.setAlignment(Qt.AlignTop)  # Align items to the top
        self.completed_tasks_group.setLayout(self.completed_tasks_layout)
        self.task_sections.addWidget(self.completed_tasks_group)

        layout.addLayout(self.task_sections)

        # Progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet(PROGRESS_BAR_STYLE)
        layout.addWidget(self.progress_bar)

        # Buttons for additional functionality
        button_layout = QHBoxLayout()
        self.clear_completed_button = QPushButton("🗑️ Clear Completed")
        self.clear_completed_button.setStyleSheet(DELETE_BUTTON_STYLE)
        self.clear_completed_button.clicked.connect(self.clear_completed_tasks)
        button_layout.addWidget(self.clear_completed_button)

        self.sort_button = QPushButton("🔽 Sort by Priority")
        self.sort_button.setStyleSheet(BUTTON_STYLE)
        self.sort_button.clicked.connect(self.sort_tasks)
        button_layout.addWidget(self.sort_button)

        layout.addLayout(button_layout)

        # Load saved tasks
        self.load_tasks()

        # Set layout
        self.setLayout(layout)

    def add_task(self):
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

    def create_task_item(self, task_text, details):
        try:
            # Create a custom widget for the task item
            task_widget = QWidget()
            task_layout = QHBoxLayout()

            # Checkbox for completing the task
            checkbox = QCheckBox()
            checkbox.setStyleSheet(f"color: {TEXT_COLOR};")
            checkbox.stateChanged.connect(lambda: self.mark_task_completed(task_widget, checkbox))
            task_layout.addWidget(checkbox)

            # Task label
            task_label = QLineEdit(task_text)
            task_label.setReadOnly(True)
            task_label.setStyleSheet(
                f"background-color: transparent; border: none; color: {TEXT_COLOR}; font-size: {FONT_SIZE}px;")
            task_layout.addWidget(task_label)

            # Priority label
            priority_label = QLabel(details["priority"])
            priority_label.setStyleSheet(
                f"color: {PRIORITY_HIGH_COLOR if details['priority'] == 'High' else PRIORITY_MEDIUM_COLOR if details['priority'] == 'Medium' else PRIORITY_LOW_COLOR}; font-size: 12px;"
            )
            task_layout.addWidget(priority_label)

            # Due date label
            due_date_label = QLabel(details["due_date"])
            due_date_label.setStyleSheet(f"color: {DUE_DATE_COLOR}; font-size: 12px;")
            task_layout.addWidget(due_date_label)

            # Tags label
            tags_label = QLabel(details["tags"])
            tags_label.setStyleSheet(f"color: {TAGS_COLOR}; font-size: 12px;")
            task_layout.addWidget(tags_label)

            # Timer label
            timer_label = QLabel(details["timer"])
            timer_label.setStyleSheet(f"color: {TIMER_COLOR}; font-size: 12px;")
            task_layout.addWidget(timer_label)

            # Delete button
            delete_button = QPushButton("🗑️")
            delete_button.setStyleSheet(
                f"background-color: transparent; border: none; color: {DELETE_BUTTON_COLOR}; font-size: 14px;")
            delete_button.clicked.connect(lambda: self.delete_task(task_widget))
            task_layout.addWidget(delete_button)

            # Set layout to the widget
            task_widget.setLayout(task_layout)

            # Add to the appropriate section
            if details["timer"] != "00:00":
                print(f"Adding to timed tasks: {task_text}")  # Debugging
                self.timed_tasks_layout.addWidget(task_widget)
            else:
                print(f"Adding to active tasks: {task_text}")  # Debugging
                self.active_tasks_layout.addWidget(task_widget)
        except Exception as e:
            print(f"Error in create_task_item: {e}")  # Debugging
            QMessageBox.critical(self, "Error", f"Failed to create task: {e}")

    def mark_task_completed(self, task_widget, checkbox):
        if checkbox.isChecked():
            # Move the task to the completed section
            self.active_tasks_layout.removeWidget(task_widget)
            self.timed_tasks_layout.removeWidget(task_widget)
            self.completed_tasks_layout.addWidget(task_widget)
            task_widget.setStyleSheet(COMPLETED_TASK_STYLE)
        self.save_tasks()

    def delete_task(self, task_widget):
        self.active_tasks_layout.removeWidget(task_widget)
        self.timed_tasks_layout.removeWidget(task_widget)
        self.completed_tasks_layout.removeWidget(task_widget)
        task_widget.deleteLater()
        self.save_tasks()

    def clear_completed_tasks(self):
        for i in reversed(range(self.completed_tasks_layout.count())):
            widget = self.completed_tasks_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.save_tasks()

    def sort_tasks(self):
        # Sort tasks by priority (High > Medium > Low)
        pass  # Implement sorting logic here

    def update_progress(self):
        total_tasks = (
            self.active_tasks_layout.count() +
            self.timed_tasks_layout.count() +
            self.completed_tasks_layout.count()
        )
        completed_tasks = self.completed_tasks_layout.count()
        self.progress_bar.setValue(int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0)

    def save_tasks(self):
        try:
            tasks = []
            # Save active tasks
            for i in range(self.active_tasks_layout.count()):
                widget = self.active_tasks_layout.itemAt(i).widget()
                if widget:
                    task_text = widget.findChild(QLineEdit).text()
                    checkbox = widget.findChild(QCheckBox)
                    priority_label = widget.findChild(QLabel)
                    due_date_label = widget.findChildren(QLabel)[1]
                    tags_label = widget.findChildren(QLabel)[2]
                    timer_label = widget.findChildren(QLabel)[3]
                    tasks.append(
                        f"{task_text},{checkbox.isChecked()},{priority_label.text()},{due_date_label.text()},{tags_label.text()},{timer_label.text()}")
            # Save timed tasks
            for i in range(self.timed_tasks_layout.count()):
                widget = self.timed_tasks_layout.itemAt(i).widget()
                if widget:
                    task_text = widget.findChild(QLineEdit).text()
                    checkbox = widget.findChild(QCheckBox)
                    priority_label = widget.findChild(QLabel)
                    due_date_label = widget.findChildren(QLabel)[1]
                    tags_label = widget.findChildren(QLabel)[2]
                    timer_label = widget.findChildren(QLabel)[3]
                    tasks.append(
                        f"{task_text},{checkbox.isChecked()},{priority_label.text()},{due_date_label.text()},{tags_label.text()},{timer_label.text()}")
            # Save completed tasks
            for i in range(self.completed_tasks_layout.count()):
                widget = self.completed_tasks_layout.itemAt(i).widget()
                if widget:
                    task_text = widget.findChild(QLineEdit).text()
                    checkbox = widget.findChild(QCheckBox)
                    priority_label = widget.findChild(QLabel)
                    due_date_label = widget.findChildren(QLabel)[1]
                    tags_label = widget.findChildren(QLabel)[2]
                    timer_label = widget.findChildren(QLabel)[3]
                    tasks.append(
                        f"{task_text},{checkbox.isChecked()},{priority_label.text()},{due_date_label.text()},{tags_label.text()},{timer_label.text()}")
            with open("todo_qt_advanced.txt", "w") as file:
                file.write("\n".join(tasks))
            print("Tasks saved successfully.")  # Debugging
        except Exception as e:
            print(f"Error in save_tasks: {e}")  # Debugging
            QMessageBox.critical(self, "Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
        try:
            with open("todo_qt_advanced.txt", "r") as file:
                tasks = file.read().splitlines()
                for task in tasks:
                    if task:
                        # Split the task into parts
                        parts = task.split(",")
                        if len(parts) < 6:
                            print(f"Skipping invalid task: {task}")  # Debugging
                            continue
                        task_text = parts[0]
                        completed = parts[1]
                        priority = parts[2]
                        due_date = parts[3]
                        tags = parts[4]
                        timer = parts[5]
                        details = {"priority": priority, "due_date": due_date, "tags": tags, "timer": timer}
                        self.create_task_item(task_text, details)
                        # Mark task as completed if needed
                        if completed == "True":
                            task_widget = self.active_tasks_layout.itemAt(self.active_tasks_layout.count() - 1).widget()
                            checkbox = task_widget.findChild(QCheckBox)
                            checkbox.setChecked(True)
                            self.mark_task_completed(task_widget, checkbox)
        except FileNotFoundError:
            print("No saved tasks found.")  # Debugging
        except Exception as e:
            print(f"Error in load_tasks: {e}")  # Debugging
            QMessageBox.critical(self, "Error", f"Failed to load tasks: {e}")

