import DB
import Model
import pandas as pd
def key(user):
    item=user.UserName[0]
    return ord(item)
def print_all(filename='first'):
    users=DB.get_all(filename)
    index=['FirstName','LastName','UserName','Phone Number','Password']
    d=[]
    for user in users:
        di={'First Name':user.FirstName,'LastName':user.LastName,'UserName':user.UserName,'PhoneNumber':user.PhoneNumber,'Password':user.Password}
        d.append(di)
    print('_________________________________________________________________________________________________')
    df=pd.DataFrame(data=d)
    df.sort_values(by=['UserName'])
    print(df) 
    print('_________________________________________________________________________________________________')
    print()
    
def print_contacts(user):
    contacts=user.Contacts
    L=[]
    for contact in contacts:
        d={'UserName':contact.UserName,'PhoneNumber':contact.PhoneNumber}
        L.append(d)
    df=pd.DataFrame(L)
    df.sort_values(by=['UserName'])
    print('______________________________________________')
    print(df) 
    print('______________________________________________')
    print()


