# RHelpdesk

I will be using Barky architecure design here. I am not good in coding but I hope my representation  give ideal of what I am trying to achieve with new RHelpdsek System.


# Layered Architecture

At a basic level, the architecture is designed with a layered strategy to include the following common/typical elements:

* **Presentation Layer** In R-Helpdesk design,presentation layer would be responsible for handling all user interface and browser communication logic, and it display that information on a screen in particular format.  This is the R-Helpdesk module.

* **Business Logic Layer** (will be a module called commands.py here) - it as All classes, attaributes and their data types defined. In R-Helpdesk design, business layer would be responsible for executing specific business rules associated with the request and this is where I have commands.py module. The business layer doesn’t need to be concerned about how to format customer data for display on a screen or even where the customer data is coming from; it gets the data from the persistence layer, perform business logic against the data, and pass that information up to the presentation layer.  

* **Presistence Layer** (will be a module called database.py here) The persistence layer contains the code to access the database. The database layer is the underlying database technology (SQL Server, ). The persistence layer is the set of code to manipulate the database. It contains SQL statements and Connection details.



The initial database wil consist of a table called `helpdesk`:

``` sql
CREATE TABLE IF NOT EXISTS helpdesk
(
    helpdeskID INTEGER PRIMARY KEY AUTOINCREMENT,
                description STRING NOT NULL,
                tickettype STRING NOT NULL,
                ticketID INTEGER NOT NULL
                ticketDate DATE NOT NULL
);
(
SELECT Tickets.*, date_format (ClosedTickets.EntryDate, '%c/%e/%y %l: %i %p')
FROM Tickets
LEFT JOIN ServiceDesk ON Tickets.ID = ServiceDesk.ID
LEFT JOIN RequestAssignee ON Tickets. ticketDate = RequestAssignee.ticketDate
LEFT JOIN Status ON SLA.ID = Status.ID
WHERE (Tickets. UserID LIKE '%John%')
ORDER BY ticketDate Desc, RequestAssignee.ticketDate, ServiceDesk.ID
);

All Classes are stored here
My test was done using the database.py and command.py

test_database.py
# I will be using database.py to test

import os
from datetime import datetime
import sqlite3

import pytest


from database import DatabaseManager

@pytest.fixture
def database_manager() -> DatabaseManager:
    
    filename = "helpdesk.db"
    dbm = DatabaseManager(filename)
    yield dbm
    dbm.__del__()           # explicitly release the database manager
    os.remove(filename)


def test_database_manager_create_table(database_manager):
    # arrange and act
    database_manager.create_table(
        "helpdesk",
        {
           "helpdeskID": "integer primary key autoincrement",
                "description": "string",
                "tickettype": "string",
                "ticketID": "int",
                "ticketDate": "date",
        },
    )

    #assert
    conn = database_manager.connection
    cursor = conn.cursor()

    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='helpdesk' ''')

    assert cursor.fetchone()[0] == 1

    #cleanup
    # this is probably not really needed
    database_manager.drop_table("helpdesk")


def test_database_manager_add_helpdesk(database_manager):

    # arrange
    database_manager.create_table(
        "helpdesk",
        {
           "helpdeskID": "integer primary key autoincrement",
                "description": "string",
                "tickettype": "string",
                "ticketID": "int",
                "ticketDate": "date",
        },
    )

    data = {
        "helpdeskID": "integer primary key autoincrement",
                "description": "string",
                "tickettype": "string",
                "ticketID": "int",
                "ticketDate": "date",       
    }

    # act
    database_manager.add("helpdesk", data)

    # assert
    conn = database_manager.connection
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM helpdesk WHERE helpdeskID='5' ''')    
    assert cursor.fetchone()[0] == 1    
    
During Unit Testing
It is important to test that end users are able to submit ticket successfully.
Tickets can be searched and updated
SLAs is puased during non-work hours
New System Design works as proposed.






```


