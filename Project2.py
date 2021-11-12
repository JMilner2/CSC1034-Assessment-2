class Contact:
    def __init__(self, name, address, number, birthdate):
        self.name = name
        self.address = address
        self.number = number
        self.birthdate = birthdate

    def displayinfo(self):
        return f"{self.name}:" \
               f" address={self.address}, phone number={self.number}, birthdate={self.birthdate}"


def get_contact_details():
    f = open("Contacts.txt", "r")
    contacts = f.readlines()
    f.close()
    return contacts


def create_contact(contacts, i):
    contact = contacts[i].split(", ")
    c = Contact(contact[0], contact[1], contact[2], contact[3])
    return c


def search_contact(contacts):
    pass


contactslist = get_contact_details()
contacts_dic = {"c" + str(x): create_contact(contactslist, x) for x in range(len(contactslist))}
print(contacts_dic["c1"].displayinfo())

while True:
    user_choice = 0
    user_input = False
    while not user_input:
        try:
            user_choice = input("ENTER WHAT YOU WANT YOU DO: \n"
                                "1 = search for contact \n"
                                "2 = print the whole list of contacts \n"
                                "3 = edit a contacts details \n"
                                "4 = add a new contact \n"
                                "5 = save and exit contacts \n"
                                "CHOICE = ")
            float(user_choice)
            user_input = True
        except ValueError:
            print("ONLY ENTER THE NUMBER FOR WHAT YOU WANT TO DO")

    if user_choice == 1:
        search_contact(contacts_dic)
