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
        and adds a new contact to the end of the list"""
        file = open("Contacts.txt", "a")
        contact_details = (self.name + ", " + self.address + ", " + self.number + ", " + self.birthdate + "\n")
        file.write(contact_details)
        file.close()


def check_blank(uinput):
    """Checks for a blank input and keep asking until an valid input is given
    """
    while True:
        if uinput == "" or uinput == " ":
            uinput = input("INPUT CANT BE BLANK\n"
                           "ENTER: ")
        else:
            break
    return uinput


def get_contact_details():
    """Opens contacts txt and saves contents.
     Removes any blank lines"""
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


def update_contacts_list(contacts_list):
    """Re-writes contacts.txt adding any edited contacts details"""
    file = open("Contacts.txt", "w")
    file.write("")
    file.close()
    for i in contacts_list:
        contacts_list[i].save_contact()


while True:  # Main loop, creates contacts and adds them to the contacts dic
    contactslist = get_contact_details()
    contacts_dic = {"c" + str(x): create_contact(contactslist, x) for x in range(len(contactslist))}
    user_choice = 0
    user_input = False
    while not user_input:  # Error handling, only letting users enter an int
        try:
            user_choice = input("\nENTER WHAT YOU WANT YOU DO: \n"
                                "1 = search for contact \n"
                                "2 = print the whole list of contacts \n"
                                "3 = edit a contacts details \n"
                                "4 = add a new contact \n"
                                "5 = save and exit contacts \n"
                                "\nCHOICE = ")
            float(user_choice)
            user_input = True
        except ValueError:
            print("ONLY ENTER THE NUMBER FOR WHAT YOU WANT TO DO")

    if user_choice == "1":  # takes a choice of name, ect... and then takes an input of what is being searched for
        choice = ""
        while True:
            validchoice = ["1", "2", "3", "4"]
            if choice not in validchoice:  # Wont allow an input other than 1-4
                print("\nCHOOSE FROM THE LIST FROM BELOW")
                choice = input("WHAT DO YOU WANT TO SEARCH BY?:\n"
                               "1 = NAME\n"
                               "2= ADDRESS\n"
                               "3= PHONE NUMBER\n"
                               "4 = DOB\n"
                               "\nCHOICE = ")
            else:
                break
        userinfo = check_blank(input("ENTER : "))  # checks for blank inputs
        for i in contacts_dic:
            contacts_dic[i].search_contact(userinfo, choice)
        print("\nALL CONTACTS HAVE BEEN SEARCHED FOR MATCHING DETAILS\n")  # Conformation that the search had been done

    elif user_choice == "2":  # Displays all contacts
        for i in contacts_dic:
            print(contacts_dic[i].displayinfo())

    elif user_choice == "3":  # Calls edit contact function
        edit_contact(contacts_dic)

    elif user_choice == "4":  # Adds a new contact and saves new contact to the contacts dictionary
        add_new_contact()
        contactslist = get_contact_details()
        contacts_dic = {"c" + str(x): create_contact(contactslist, x) for x in range(len(contactslist))}

    elif user_choice == "5":  # Saves contacts to contacts.txt and exits main loop
        update_contacts_list(contacts_dic)
        break

    else:
        print("INVALID CHOICE")  # Exception handling
    update_contacts_list(contacts_dic)  # Keeps contacts.txt updated for when a contact has been edited
