"""Python Day 16 — list mastery/revision | 02 Nov 2026.

Reproduces successful practice examples. Additional independent challenges
are in Day_16_Notes.md and were not completed in this session.
"""


def inventory_example():
    devices = ["Laptop", "Printer", "Router", "Monitor"]
    devices.append("Firewall")
    devices.insert(2, "Switch")
    devices.remove("Printer")
    removed_device = devices.pop()
    print("Final inventory:", devices)
    print("Removed device:", removed_device)


def ticket_example():
    tickets = [101, 102, 103, 104]
    tickets.append(105)
    tickets.insert(0, 999)
    tickets.remove(102)
    closed_ticket = tickets.pop()
    print("Remaining:", tickets)
    print("Closed ticket Number:", closed_ticket)


def pop_at_index_example():
    tickets = [101, 102, 103]
    closed_ticket = tickets.pop(1)
    print("Removed with pop(1):", closed_ticket)
    print("Remaining:", tickets)


if __name__ == "__main__":
    inventory_example()
    ticket_example()
    pop_at_index_example()
