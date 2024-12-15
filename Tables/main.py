import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QWidget, QLineEdit, QHBoxLayout, QFileDialog, QTableWidgetItem
)
from PyQt5.QtCore import Qt

class TableWindow(QMainWindow):
    def __init__(self, rows, cols, width, height):
        super().__init__()

        self.setWindowTitle("Table Editor")
        self.setGeometry(100, 100, width, height)


        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)


        self.table = QTableWidget()
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)
        self.layout.addWidget(self.table)

        # Цикл
        for row in range(rows):
            for col in range(cols):
                line_edit = QLineEdit()
                self.table.setCellWidget(row, col, line_edit)


        self.button_layout = QHBoxLayout()

        # Кнопки
        self.add_row_btn = QPushButton("Add row")
        self.add_row_btn.clicked.connect(self.add_row)
        self.button_layout.addWidget(self.add_row_btn)

        self.delete_row_btn = QPushButton("Delete row")
        self.delete_row_btn.clicked.connect(self.delete_row)
        self.button_layout.addWidget(self.delete_row_btn)

        self.save_btn = QPushButton("Save to file")
        self.save_btn.clicked.connect(self.save_to_file)
        self.button_layout.addWidget(self.save_btn)

        self.layout.addLayout(self.button_layout)
        self.setCentralWidget(self.central_widget)

    def add_row(self):
        # Добавление строки ниже
        current_rows = self.table.rowCount()
        self.table.insertRow(current_rows)
        cols = self.table.columnCount()
        for col in range(cols):
            line_edit = QLineEdit()
            self.table.setCellWidget(current_rows, col, line_edit)



    def delete_row(self):
        # Удаление строки
        selected = self.table.currentRow()
        if selected >= 0:
            self.table.removeRow(selected)

    def save_to_file(self):
        # Сохранение
        path, _ = QFileDialog.getSaveFileName(self, "Save to file", "", "CSV Files (*.csv);;All Files (*)")
        if path:
            with open(path, "w", encoding="utf-8") as file:
                for row in range(self.table.rowCount()):
                    row_data = []
                    for col in range(self.table.columnCount()):
                        widget = self.table.cellWidget(row, col)
                        if widget and isinstance(widget, QLineEdit):
                            row_data.append(widget.text())
                        else:
                            row_data.append("")
                    file.write(",".join(row_data) + "\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Параметры
    width = int(input("Window width: "))
    height = int(input("Window height: "))
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    window = TableWindow(rows, cols, width, height)
    window.show()

    sys.exit(app.exec_())

