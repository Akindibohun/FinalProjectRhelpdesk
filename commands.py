"""
This module utilizes the command pattern  to 
specify and implement the business logic layer
"""
from datetime import datetime
import sys

import requests

from database import DatabaseManager

# module scope
db = DatabaseManager("helpdesk.db")


class CreateTicketTableCommand:
    """
    uses the DatabaseManager to create the ticket table
    """

    def execute(self):
        db.create_table(
            "helpdesk",
            {
                "helpdeskID": "integer primary key autoincrement",
                "description": "string",
                "tickettype": "string",
                "ticketID": "int",
                "ticketDate": "date",
            },
            

        )


class SLACommand:
    """
    This class will:

    1. Expect a dictionary containing the ticketID, ticketdescription,tickettype,ticketID and ticketDate for a  ticket created.
    2. Add the current datetime to the dictionary as ticketDate.
    3. Insert the data into the ticket table using the DatabaseManager.add method.
    4. Return a success message that will eventually be displayed by the presentation layer.
    """

    def execute(self, data, timestamp=None):
        data["ticketDate"] = datetime.utcnow().isoformat()
        db.add("ticket", data)
        return "ticket added!"

class IssueCommand:
    """
    This class will:
    1. Expect a dictionary containing the IssueID, IssueType,tickettype,IssueTitle, Assignee and IssueDescription for Issue created.
    2. contain details information for Issues submitted by end users
    """
    
    def execute(self):
        db.create_class(
            "Issue",
            {
                "IssueID": "integer primary key autoincrement",
                "IssueType": "string",
                "IssueTitle": "string",
                "Assignee": "string",
                "IssueDescription": "string",
            },


    class ServiceDeskCommand:
    """
        This class will:
    1. Expect a dictionary containing the ID, ServiceDeskName,ServiceDeskType, and ServiceDeskDescription for ServicDesk.
    2. contain ServiceDesk attributes in the database.
    """
    def execute(self):
        db.create_class(
            "ServiceDesk",
            {
                "ID": "integer primary key autoincrement",
                "ServiceDeskName": "string",
                "ServiceDeskType": "string",
                "ServiceDeskDescription": "string",
            },


    class UserCommand:
        """
        This class will:
    1. Expect a dictionary containing the UserID, UserRole,ServiceDeskType,UserName, and UserAddress for class User.
    2. contain end users information
    """
    def execute(self):
        db.create_class(
            "User",
            {
                "UserID": "integer primary key autoincrement",
                "UserRole": "integer",
                "UserName": "string",
                "UserAddress": "string",
            },

        class RoleCommand:
    """
        This class will:
    1. Expect a dictionary containing the UserID, RoleTitle,and RoleDescription for class Role.
    2. shows roles information
    """
    def execute(self):
        db.create_class(
            "Role",
            {
                "UserID": "integer primary key autoincrement",
                "RoleTitle": "string",
                "RoleDescription": "string",
            },
            
        class PermissionCommand:
             """
        This class will:
    1. Expect a dictionary containing the PermissionID, PermissionRole,and PermissionDescription for class Role.
    2. shows user and ServiceDesk permission information
    """
    def execute(self):
        db.create_class(
            "Permission",
            {
                "PermissionID": "integer primary key autoincrement",
                "PermissionRole": "string",
                "PermissionDescription": "string",
            },
    class SLACommand:
                 """
        This class will:
    1. Expect a dictionary containing the SLATitle, Status, Priority,and RequestAssignee for class Role.
    2. shows SLA information for ticket submitted
    """
    def execute(self):
        db.create_class(
            "SLA",
            {
                "SLATitle": "integer primary key autoincrement",
                "Status": "text",
                "Priority": "text"
                "RequestAssignee": "text",
            },



    def __init__(self, order_by="ticketDate"):
        self.order_by = order_by

    def execute(self):
        return db.select("ticket", order_by=self.order_by).fetchall()


    def execute(self, data):
        db.edit("ticket", {"ticketID": data})
        return "ticket edited!"

        def execute(self, data):
            db.pause("ticket", {"ticketID": data})
        return "ticket paused!"





class EdithelpdeskCommand:
    def execute(self, data):
        db.update(
            "helpdesk",
            {"id": data["id"]},
            data["update"],
        )
        return "helpdesk updated!"


class QuitCommand:
    def execute(self):
        sys.exit()
