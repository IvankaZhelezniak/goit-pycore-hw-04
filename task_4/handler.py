def add_contact(args, contacts: dict) -> str:
    if len(args) != 2:
        return "Invalid arguments. Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts: dict) -> str:
    if len(args) != 2:
        return "Invalid arguments. Usage: change <name> <new_phone>"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."
    
def show_phone(args, contacts: dict) -> str:
    if len(args) != 1:
        return "Invalid arguments. Usage: phone <name>"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])