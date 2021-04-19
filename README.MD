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
```


