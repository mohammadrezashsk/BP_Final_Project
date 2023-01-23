import json
import Model
import pandas as pd
import os
def key(user):
    item=user.UserName[0]
    return ord(item)
def get_all(filename ='first'):
    try:
        with open(filename,'r') as file:
            data=json.load(file)
    except:
        with open(filename,'w') as file:
            data={'0':{'FirstName':'admin','LastName':'admin','UserName':'admin','Password':'admin','PhoneNumber':'admin','Contacts':[ {'ContactID':'0','UserName':'admin','PhoneNumber':'admin'} ],'IsAdmin':'1'} }
            json.dump(data,file)
    users=[]
    for Id in data:
        Di=data[Id]
        contacts=Di['Contacts']
        c=[]
        for contact in contacts:
            c.append(Model.CONTACT(contact['ContactID'],contact['UserName'],contact['PhoneNumber']) )
        user=Model.USER(Id,Di['FirstName'],Di['LastName'],Di['Password'],Di['PhoneNumber'],c,Di['UserName'],Di['IsAdmin'])
        users.append(user)
    return users
            
def get_by_username(username,filename='first'):
    users=get_all(filename)
    for user in users:
        if user.UserName == username:
            return user
    return False

def get_by_ID(Id,filename='first'):
    users=get_all(filename)
    for user in users:
        if user.UserID == Id:
            return user
    return False
def write(users,filename):
    data={}
    for i in range(len(users)):
        user=users[i]
        contacts=[]
        d={}
        for u in user.Contacts:
            d['ContactID']=u.ContactID
            d['UserName']=u.UserName
            d['PhoneNumber']=u.PhoneNumber
            contacts.append(d)
            d={}
            
        data[str(i)]={'FirstName':user.FirstName,'LastName':user.LastName,'UserName':user.UserName,'Password':user.Password,'PhoneNumber':user.PhoneNumber,'Contacts':contacts,'IsAdmin':user.IsAdmin}
        with open(filename,'w') as file:
            json.dump(data,file)
            
def refresh(filename):
    data=get_all(filename)
    for i in range(len(data)):
        data[i].UserID=str(i)
    write(data,filename)
def add(user,filename):
    users=get_all(filename)
    users.append(user)
    write(users,filename)
    refresh(filename)

def update(user0,user1,filename):
    users=get_all(filename)
    for i in range(len(users)):
        if users[i].UserName == user0.UserName:
            users[i]=user1
            break
    write(users,filename)
def delete(username,filename):
    users=get_all(filename)
    for i in range(len(users)):
        if users[i].UserName == username:
            del users[i]
            break
    write(users,filename)
    refresh(filename)
def addcontacct(user,contact,filename):
    users=get_all(filename)
    for u in range(len(users)):
        if user.UserName == users[u].UserName:
            users[u].Contacts+=[contact]
            break
    write(users,filename)
def removecontact (user,cun,filename):
    users=get_all(filename)
    contacts=[]
    for i in range(len(users)):
        if users[i].UserName == user.UserName:
            for contact in users[i].Contacts:
                #print(contact.UserName)
                if contact.UserName !=cun:
                    contacts.append(contact)
        users[i].Contacts=contacts
        contacts=[]
    write(users,filename)
def search(username,text,filename):
    user=get_by_username(username,filename)
    results=[]
    for contact in user.Contacts:
        if (text in contact.UserName) or (text in contact.PhoneNumber):
            results.append({'UserName':contact.UserName,'PhoneNumber':contact.PhoneNumber})
    df=pd.DataFrame(results)
    df.sort_values(by=['UserName'])
    print('_________________________________________________________________________________________________')
    print(df)
    print('_________________________________________________________________________________________________')
def editcontact(user,cun,newconect,filename):
    users=get_all(filename)
    for i in range(len(users)):
        for j in range(len(users[i].Contacts)):
            if users[i].Contacts[j].UserName ==cun:
                users[i].Contacts[j]=newconect
                break
    write(users,filename)
def delete_db(filename):
    name=filename
    os.remove(name)
    