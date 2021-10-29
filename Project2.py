class Contact:
    def __init__(self,name,address,number,birthdate):
        self.name = name
        self.address = address
        self.number = number
        self.birthdate = birthdate

    def displayinfo(self):
        return f"{self.name} address:{self.address}, phone number:{self.number}, birthdate:{self.birthdate}"
    