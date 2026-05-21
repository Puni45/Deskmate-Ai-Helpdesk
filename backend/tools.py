from mock_db import users, tickets
import random

def check_software_access(user, software):

    access_list = users[user]["software_access"]

    return software in access_list


def create_ticket(user, issue, priority):

    ticket_id = f"INC-{random.randint(1000,9999)}"

    tickets[ticket_id] = {
        "status": "Open",
        "issue": issue,
        "priority": priority
    }

    return ticket_id


def reset_password(user):

    return "Password reset link sent successfully."


def check_ticket_status(ticket_id):

    if ticket_id in tickets:
        return tickets[ticket_id]

    return None


def check_vpn(user):

    return users[user]["vpn_enabled"]