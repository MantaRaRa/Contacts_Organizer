"""This module provides Contacts application."""
import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window


def main():
    """Contacts main function."""
    # Creating the application
    app = QApplication(sys.argv)
    # Connecting to the database, if it doesn't it will close the application with an error message
    if not createConnection("contacts.sqlite"):
        sys.exit(1)
    # Creating the main window after connecting to the database
    win = Window()
    win.show()
    # Running the loop
    sys.exit(app.exec_())
