# Contacts_Organizer

This App is a digital Ro-Lo-Dex, a place where I can store Important data and Contact info.

This Python App is created in PyCharm 2022.2.1 (Community Edition) and  leverages PyQt to create the GUI and SQLite to store the data.

### Special instructions required for the Reviewer:

Please Install and Import Dependencies listed below in the Terminal:

```pip install --upgrade pip```

```pip install pyqt5```

Run ```contacts.py``` from the command line or ```SHIFT + F10```

### Feature 1: (Database)
Connecting to the Database With PyQt and SQLite

### Feature 2: (Manipulate and clean data)
Manage contact data using PyQt’s Model-View architecture. 
To update the name of a contact, you can double-click the cell containing the name, update the name, and then press Enter to automatically save the changes to the database. 

### Feature 3: (Analyze your data)
In a COMMAND Line or Terminal using SQLite to confirm the Database.

Open up CMD  
Type:

```pyton``` to enter the Python environment

```import os```

```print("Current working directory: {0}".format(os.getcwd()))```
to see your current directory

```os.chdir('/.../.../.../Contacts_Organizer')``` Change your directory to the Contacts_Organizer folder you downloaded



```
>>>from contacts.database import createConnection

>>> # Create a connection
>>> createConnection("contacts.sqlite")
> 
True

>>> # Confirm that contacts table exists
>>> from PyQt5.QtSql import QSqlDatabase
>>> db = QSqlDatabase.database()
>>> db.tables()
> 
['contacts', 'sqlite_sequence']
```

### Feature 4: (Visualize your data)
using PyQt to create the GUI

### Special Thanks to Leodanis Pozo Ramos and CodeKY Mentors for their Contributions.
