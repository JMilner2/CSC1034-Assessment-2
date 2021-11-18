class Contact:
    def __init__(self, name, address, number, birthdate):
        """Constructor for Contact class
        """

        self.name = name
        self.address = address
        self.number = number
        self.birthdate = birthdate

    def displayinfo(self):
        """Returns a formatted version of the client class
        """

        return f"{self.name}:" \
               f" address={self.address}, phone number={self.number}, birthdate={self.birthdate}"

    def search_contact(self, contact_detail, number):
        """Searches contact for completely matching details
        Displays contact info if there is a match
        """

        if number == "1":
            if self.name == contact_detail:
                print(self.displayinfo())
        elif number == "2":
            if self.address == contact_detail:
                print(self.displayinfo())
        elif number == "3":
            if self.number == contact_detail:
                print(self.displayinfo())
        elif number == "4":
            if self.birthdate == (contact_detail + "\n"):
                print(self.displayinfo())
        else:
            print("INVALID CHOICE MADE")  # Captures any incorrect user inputs and returns an error message

    def change_contact_details(self):
        """Changes contact details while stopping any blank inputs
        """

        self.name = check_blank(input("ENTER A NAME FOR CONTACT: "))
        self.address = check_blank(input("ENTER AN ADDRESS FOR CONTACT: "))
        self.number = check_blank(input("ENTER A PHONE NUMBER FOR CONTACT: "))
        self.birthdate = check_blank(input("ENTER A DATE OF BIRTH FOR CONTACT(XX/XX/XXXX): "))

    def save_contact(self):
        """Opens text file containing contacts list
        and adds a new contact to the end of the list
        """

        file = open("Contacts.txt", "a")
        contact_details = (self.name + ", " + self.address + ", " + self.number + ", " + self.birthdate + "\n")
        file.write(contact_details)
        file.close()


def check_blank(uinput):
    """Checks for a blank input and keep asking until an valid input is given
    """

    while True:
        if len(uinput.strip()) == 0:
            uinput = input("INPUT CANT BE BLANK\n"
                           "ENTER: ")
        else:
            break
    return uinput


def get_contact_details():
    """Opens contacts txt and saves contents.
     Removes any blank lines
     """

    f = open("Contacts.txt", "r")
    contacts = f.readlines()
    for contact in contacts:
        if contact == "\n":
            contacts.remove(contact)
    f.close()
    return contacts


def create_contact(contacts, num):
    """Takes contacts list splits each contact up and creates a contact.
    Returns c so it can be added to a contacts dictionary
    """

    contact = contacts[num].split(", ")
    c = Contact(contact[0], contact[1], contact[2], contact[3])
    return c


def edit_contact(contacts_list):
    """Displays contacts and takes a user input of which to edit
    """

    print("WHICH CONTACT WOULD YOU LIKE TO EDIT:")
    for i in contacts_list:
        print(i + " = " + contacts_list[i].displayinfo())
    contact_to_edit = input("PLEASE CHOOSE A CONTACT TO EDIT(E.G. c1,c2)\n"
                            "CHOICE: ")
    try:
        contacts_list[contact_to_edit].change_contact_details()  # Uses change_contact_details to edit contact

    except KeyError:  # Throws a KeyError if the user input is invalid
        print("INVALID CHOICE MADE")


def add_new_contact():
    """Creates a new contact, and stops blank entry's
    Saves new contact to contacts.txt
    """

    name = check_blank(input("New contacts name: "))
    address = check_blank(input("New contacts address: "))
    number = check_blank(input("New contacts number: "))
    dob = check_blank(input("New contacts date of birth(xx/xx/xxxx): "))
    new_contact = Contact(name, address, number, dob)
    new_contact.save_contact()
    return  new_contact


def update_contacts_list(contacts_list):
    """Re-writes contacts.txt adding any edited contacts details
    """

    file = open("Contacts.txt", "w")
    file.write("")
    file.close()
    for i in contacts_list:
        contacts_list[i].save_contact()


# TESTS START HERE(Testing all the functions that don't read/write to contacts.txt)

eg_contact = Contact("bob", "far far away", "999", "00/00/0000")
print(eg_contact.displayinfo())  # Testing the Display info function - Should display all contact info
print("\n")
eg_contact.search_contact("bob", "1")  # Testing the search contact function - Should display all contact info
print("\n")
eg_contact.change_contact_details()  # Testing the change contact details function
print(eg_contact.displayinfo())  # Should display change contact details, with no blank inputs
print("\n")
check_blank("")  # Testing check blank - should print INPUT CANT BE BLANK and ask for input until valid input is given
print("\n")
new_contact = add_new_contact()  # Testing add contact
print(new_contact.displayinfo())  # Should print new contact details
print("\n")
