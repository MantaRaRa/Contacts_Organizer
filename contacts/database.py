# connecting to the dataBase

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase


def createConnection(databaseName):
    # creating or opening a dataBase connection
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    return True
