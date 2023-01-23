class CONTACT:
    def __init__(self,ContactID,UserName,PhoneNumber):
        self.ContactID=ContactID
        self.UserName=UserName
        self.PhoneNumber=PhoneNumber
class USER:
    def __init__(self,UserID,FirstName,LastName,Password,PhoneNumber,Contacts,UserName,IsAdmin=False):
        self.UserID=UserID
        self.FirstName=FirstName
        self.LastName=LastName
        self.Password=Password
        self.PhoneNumber=PhoneNumber
        self.UserName=UserName
        self.IsAdmin=IsAdmin
        self.Contacts=[]
        for i in range(len(Contacts)):
            Ci=Contacts[i]
            contact=CONTACT(Ci.ContactID, Ci.UserName, Ci.PhoneNumber)
            self.Contacts.append(contact)


        
