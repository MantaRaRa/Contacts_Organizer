# connecting to the dataBase

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def createConnection(databaseName):
    # creating a database if none is found, otherwise the app opens the dataBase
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


def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF IT DOESNT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            MENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )


def createConnection(databaseName):

    _createContactsTable()
    return True
