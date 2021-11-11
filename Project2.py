class Contact:
    def __init__(self,name,address,number,birthdate):
        self.name = name
        self.address = address
        self.number = number
        self.birthdate = birthdate

    def displayinfo(self):
        return f"{self.name}:" \
               f" address={self.address}, phone number={self.number}, birthdate={self.birthdate}"


def get_contact_details():
    f = open("Contacts.txt","r")
    contacts = f.readlines()
    f.close()
    return contacts


def create_contact(contacts,i):
    contact = contacts[i].split(", ")
    c = Contact(contact[0],contact[1],contact[2],contact[3])
    return c



contactslist = get_contact_details()
contacts_dic = {"c"+str(x):create_contact(contactslist,x) for x in range(len(contactslist))}
print(contacts_dic["c1"].displayinfo())

