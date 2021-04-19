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