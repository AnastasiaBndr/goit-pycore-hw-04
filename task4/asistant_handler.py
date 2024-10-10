def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact exists!"
    else:
        contacts[name] = phone
        return "Contact added."


def change_contact(args, contacts):
    if (len(args) <= 1):
        return "Not enough values!"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact changed."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(args, contacts):
    if not contacts:
        return "No contacts available."
    return contacts
