import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QDialog, QFormLayout, QLineEdit, QLabel, QHeaderView


class Employee:
    def __init__(self, name, email, phone, title):
        self.name = name
        self.email = email
        self.phone = phone
        self.title = title


class EmployeeDirectory(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Read employees from file
        self.employees = []
        try:
            with open('employees.csv', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    fields = line.strip().split(',')
                    employee = Employee(fields[0], fields[1], fields[2], fields[3])
                    self.employees.append(employee)
        except FileNotFoundError:
            pass

        # Create table widget
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Name', 'Email', 'Phone', 'Title'])
        self.table.setRowCount(len(self.employees))
        for i, employee in enumerate(self.employees):
            name_item = QTableWidgetItem(employee.name)
            email_item = QTableWidgetItem(employee.email)
            phone_item = QTableWidgetItem(employee.phone)
            title_item = QTableWidgetItem(employee.title)
            self.table.setItem(i, 0, name_item)
            self.table.setItem(i, 1, email_item)
            self.table.setItem(i, 2, phone_item)
            self.table.setItem(i, 3, title_item)

        # Set sorting behavior
        self.table.setSortingEnabled(True)

        # Create add button
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.showAddDialog)

        # Create delete button
        delete_button = QPushButton('Delete')
        delete_button.clicked.connect(self.deleteSelectedRows)

        # Create search box and button
        search_label = QLabel('Search:')
        self.search_box = QLineEdit()
        search_button = QPushButton('Search')
        search_button.clicked.connect(self.searchEmployees)

        # Create layout for search box and button
        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_box)
        search_layout.addWidget(search_button)

        # Create layout for add and delete buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(delete_button)

        # Create main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.table)
        main_layout.addLayout(button_layout)

        # Set main layout
        self.setLayout(main_layout)

        # Set window properties
        self.setWindowTitle('Employee Directory')
        self.show()

    def showAddDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Add Employee')

        # Create form layout for dialog
        form_layout = QFormLayout()

        # Create line edits for each field
        name_edit = QLineEdit()
        email_edit = QLineEdit()
        phone_edit = QLineEdit()
        title_edit = QLineEdit()

        # Add labels and line edits to form layout
        form_layout.addRow('Name:', name_edit)
        form_layout.addRow('Email:', email_edit)
        form_layout.addRow('Phone:', phone_edit)
        form_layout.addRow('Title:', title_edit)

        # Create buttons
        ok_button = QPushButton('OK')
        ok_button.clicked.connect(lambda: self.addEmployee(name_edit.text(), email_edit.text(), phone_edit.text(), title_edit.text()))
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(dialog.reject)

        # Add buttons to form layout
        button_layout = QHBoxLayout()
