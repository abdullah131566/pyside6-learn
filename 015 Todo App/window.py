from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from mainwindow_ui import Ui_TodoWindow

from models.TodoModel import TodoModel
import os
import json

class MyWindow(QWidget, Ui_TodoWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.todoFilePath = os.path.join(os.path.dirname(__file__), "todos.json")
        self.todoModel = TodoModel()
        self.load()
        self.todoView.setModel(self.todoModel)

        self.todoEdit.setFocus()
        self.todoEdit.setValidator(QRegularExpressionValidator("^[a-zA-Z][a-zA-Z ]+"))
        self.todoEdit.textChanged.connect(self.validateAndEnableAddButton)

        self.addTodoButton.clicked.connect(self.addTodo)
        self.deleteTodoButton.clicked.connect(self.deleteTodo)
        self.markDoneTodoButton.clicked.connect(self.toggleMarkTodo)


    def validateAndEnableAddButton(self):
        if self.todoEdit.hasAcceptableInput():
            self.addTodoButton.setEnabled(True)
        else:
            self.addTodoButton.setEnabled(False)


    def addTodo(self):
        if not self.todoEdit.hasAcceptableInput():
            return
        
        self.todoModel.todos.append((False, self.todoEdit.text()))
        self.todoModel.layoutChanged.emit()

        self.save()

        self.todoEdit.clear()
        self.todoEdit.setFocus()


    def deleteTodo(self):
        try:
            index = self.todoView.selectedIndexes()[0]
            del self.todoModel.todos[index.row()]
            self.todoModel.layoutChanged.emit()
            self.save()

        except IndexError as e:
            QMessageBox.warning(self, "No Selection",
                                "You have not highlighted any todo!",
                                QMessageBox.Ok)
        
    
    def toggleMarkTodo(self):
        try:
            index = self.todoView.selectedIndexes()[0].row()
            status, text = self.todoModel.todos[index]
            self.todoModel.todos[index] = (~status, text)
            self.todoModel.dataChanged.emit(index, index)
            self.save()

        except IndexError as e:
            QMessageBox.warning(self, "No Selection",
                                "You have not highlighted any todo!",
                                QMessageBox.Ok)


    def load(self):
        try:
            with open(self.todoFilePath, "r") as f:
                self.todoModel.todos = json.load(f)
        except FileNotFoundError as e:
            pass


    def save(self):
        try:
            with open(self.todoFilePath, "w") as f:
                json.dump(self.todoModel.todos, f)
        except FileNotFoundError as e:
            pass