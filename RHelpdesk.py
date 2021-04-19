"""
This module provides the presentation layer and can be consdired "the program."

This module facilitates an infinite loop, it is design to 
create ticket,search ticket by date, pause SLA, update ticket
    
"""
import os

import commands


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)

    def __str__(self):
        return self.name


def clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def print_options(options):
    """
    1. Print the keyboard key for the user to enter to choose the option.
    2. Print the option text.
    3. Check if the user’s input matches an option and, if so, choose it.
    """
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    """
    1. Prompt the user to enter a choice, using Python’s built-in input function.
    2. If the user’s choice matches one of those listed, call that option’s choose method.
    3. Otherwise, repeat.
    """
    choice = input("Choose an option: ")
    while not option_choice_is_valid(choice, options):
        print("Invalid choice")
        choice = input("Choose an option: ")
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_new_helpdesk_data():
    return {
        "helpdeskID": get_user_input("helpdeskID"),
        "ticketDate": get_user_input("ticketDate"),
        "ticketID": get_user_input("ticketID", required=True),
    }


def get_helpdeskID_for_deletion():
    return get_user_input("Enter a helpdesk ID to delete")




def get_new_helpdesk_info():
    heldpesk_id = get_user_input("Enter a heldpesk ID to edit")
    field = get_user_input("Choose a value to edit (helpdeskID, tickettype,ticketDate,ticketID)")
    new_value = get_user_input(f"Enter the new value for {field}")
    return {
        "id": helpdeskID,
        "update": {field: new_value},
    }


def loop():

    clear_screen()
    # All steps for showing and selecting options
    
    options = {
        "A": Option(
            "create heldpesk",
            commands.helpdeskTableCommand(),
            prep_call=get_new_heldpesk_data,
        ),
        "B": Option("SLA by ticketDate", commands.createSLACommand()),
        "T": Option(
            "create Issue by ID", commands.createIssueCommand(order_by="IssueID")
        ),
        "E": Option(
            "ServiceDesk Command",
            commands.createServiceDeskCommand(),
            prep_call=get_new_helpdesk_info,
        ),
        "D": Option(
            "Delete a helpdesk",
            commands.DeletehelpdeskCommand(),
            prep_call=get_heldesk_id_for_deletion,
        ),
       
       
        "Q": Option("Quit", commands.QuitCommand()),
    }
    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()
    _ = input("Press ENTER to return to menu")


# this ensures that this module runs first
if __name__ == "__main__":
    commands.CreatehelpdeskTableCommand().execute()

    # endless program loop
    while True:
        loop()
