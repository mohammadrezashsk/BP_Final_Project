import Model
import DB
import Tools
import tkinter as tk
from tkinter import filedialog as fd
root = tk.Tk()
root.withdraw()
filename=fd.askopenfilename(filetypes=[('Json files','.json')])

while True:
    IsLogin=False
    action=input('[1:Login, 2:Exit]\n')
    if action =='2':
        exit()
    if action =='1':
        username=input('Please enter your username: ')
        user=DB.get_by_username(username,filename)
        if user != False:
            for i in range(3):
                password=input('Please enter your password: ')
                if password == user.Password:
                    IsLogin=True
                    break
            if IsLogin:
                if user.IsAdmin == '1':
                    while IsLogin:
                        admin_action=input('[1:Manage Users, 2:Setting, 3:Logout]\n')
                        if admin_action =='3':
                            break
                        if admin_action == '1':
                            while  IsLogin:
                                Tools.print_all(filename)
                                manage_User=input('[1:Add user, 2: Remove User, 3:Edit User, 4:Exit]\n')
                                if manage_User =='4':
                                    break
                                if manage_User =='1':
                                    firstname=input('Please enter a firstname: ')
                                    lastname=input('Please enter a lastname: ')
                                    username=firstname+'_'+lastname
                                    user=DB.get_by_username(username,filename)
                                    if user == False:
                                        password=input('Please enter a password: ')
                                        phonenumber=input('Please enter a phonenumber: ')
                                        contacts=[Model.CONTACT('0',username,phonenumber)]
                                        user=Model.USER('1',firstname,lastname,password,phonenumber,contacts,username)
                                        DB.add(user,filename)
                                        
                                if manage_User == '2':
                                    username=input('Please enter a username: ')
                                    user=DB.get_by_username(username,filename)
                                    if user != False:
                                        DB.delete(username,filename)
                                if manage_User =='3':
                                    un=input('Enter your username: ')
                                    user0=DB.get_by_username(un,filename)
                                    
                                    firstname=input('Enter new first name (or press enter to skip): ')
                                    if firstname =='':
                                        firstname =user0.FirstName
                                    lastname=input('Enter new last name (or press enter to skip): ')
                                    if lastname =='':
                                        lastname =user0.LastName                                
                                    username=input('Enter new username (or press enter to skip): ')
                                    if username =='':
                                        username =firstname+'_'+lastname                             
                                    phonenumber=input('Enter new  phone number (or press enter to skip): ')
                                    if phonenumber =='':
                                        phonenumber =user0.PhoneNumber                                
                                    password=input('Enter new password (or press enter to skip): ')
                                    if password =='':
                                        password =user0.Password 
                                    contact=Model.CONTACT('0',username,phonenumber)
                                    contacts=user0.Contacts
                                    contacts[0]=contact
                                    user1=Model.USER('0',firstname,lastname,password,phonenumber,contacts,username)   
                                    DB.update(user0,user1,filename)                       
                        if admin_action == '2':
                           while  IsLogin:
                                settiing_action=input('[1:Delete acount, 2:Suport, 3:Exit]\n')            
                                if settiing_action =='3':
                                    break
                                if settiing_action =='1':
                                    sure=input('Are you sure? (y/n ): ')
                                    if sure.lower() =='y':
                                        DB.delete_db(filename)
                                        IsLogin=False
                                        exit()      
                                if settiing_action =='2':
                                    username=input('Please enter the username: ')
                                    user_suport=DB.get_by_username(username,filename) 
                                    while IsLogin:   
                                        manage_contact=input('[1:Add contact, 2:Remove contact, 3:Edit contact,4:Search, 5:Exit]\n')
                                        if manage_contact =='5':
                                            break
                                        if manage_contact =='1':
                                            firstname=input('Please enter the your contact firstname: ')
                                            lastname=input('Please enter the your contact lastname: ')
                                            username=firstname+'_'+lastname
                                            phonenumber=input('Please enter the your contact phone number: ')  
                                            last=int(user_suport.Contacts[-1].ContactID  ) 
                                            last=str(last+1)
                                            contact=Model.CONTACT(last,username,phonenumber)
                                            DB.addcontacct(user_suport,contact,filename)   
                                        if manage_contact =='2':
                                            cun=input('Please enter the your contact username: ')

                                            if cun != user_suport.UserName:
                                                DB.removecontact(user_suport,cun,filename)
                                                                            
                                                                        
                                        if manage_contact =='3':
                                            cun=input('Please enter the your contact username: ') 
                                            for c in user_suport.Contacts:
                                                if c.UserName == cun:
                                                    contact=c
                                                    break
                                            username=contact.UserName.split('_')
                                            fname=input('Please enter the new firstname of your contact (or press enter to skip): ')
                                            if fname =='':
                                                fname=username[0]
                                            lname=input('Please enter the new lastname of your contact (or press enter to skip): ')
                                            if lname =='':
                                                lname=username[1]
                                            pnumber=input('Please enter the new phonenumber of your contact (or press enter to skip): ')
                                            if pnumber =='':
                                                pnumber=user_suport.PhoneNumber
                                                last=int(user_suport.Contacts[-1].ContactID  ) 
                                                last=str(last+1)
                                                uname=fname+'_'+lname
                                                ncontact=Model.CONTACT(last,uname,pnumber)
                                                DB.editcontact(user_suport,cun,ncontact,filename)                                            
                                        if manage_contact == '4':
                                            text=input('Search: ')
                                            DB.search(user_suport.UserName,text,filename)                                       
                else:
                    while IsLogin:
                        user_action=input('[1:Manage Contacts, 2:Setting, 3:Logout]\n')
                        if user_action =='3':
                            break
                        if user_action =='1':
                            while IsLogin:
                                user=DB.get_by_username(user.UserName,filename)
                                manage_contact=input('[1:Add contact, 2:Remove contact, 3:Edit contact,4:Search, 5:Exit]\n')
                                if manage_contact =='5':
                                    break
                                if manage_contact =='1':
                                    firstname=input('Please enter the your contact firstname: ')
                                    lastname=input('Please enter the your contact lastname: ')
                                    username=firstname+'_'+lastname
                                    phonenumber=input('Please enter the your contact phone number: ')  
                                    last=int(user.Contacts[-1].ContactID  ) 
                                    last=str(last+1)
                                    contact=Model.CONTACT(last,username,phonenumber)
                                    DB.addcontacct(user,contact,filename)
                                
                                if manage_contact =='2':
                                    cun=input('Please enter the your contact username: ')

                                    if cun != user.UserName:
                                        DB.removecontact(user,cun,filename)
                                    
                                
                                if manage_contact =='3':
                                    cun=input('Please enter the your contact username: ') 
                                    for c in user.Contacts:
                                        if c.UserName == cun:
                                            contact=c
                                            break
                                    username=contact.UserName.split('_')
                                    fname=input('Please enter the new firstname of your contact (or press enter to skip): ')
                                    if fname =='':
                                        fname=username[0]
                                    lname=input('Please enter the new lastname of your contact (or press enter to skip): ')
                                    if lname =='':
                                        lname=username[1]
                                    pnumber=input('Please enter the new phonenumber of your contact (or press enter to skip): ')
                                    if pnumber =='':
                                        pnumber=user.PhoneNumber
                                    last=int(user.Contacts[-1].ContactID  ) 
                                    last=str(last+1)
                                    uname=fname+'_'+lname
                                    ncontact=Model.CONTACT(last,uname,pnumber)
                                    DB.editcontact(user,cun,ncontact,filename)                                            
                                if manage_contact == '4':
                                    text=input('Search: ')
                                    DB.search(user.UserName,text,filename)       
                        if user_action =='2':
                            while IsLogin:
                                settiing_action=input('[1:Edit information, 2:Delete acount, 3:Exit]\n')            
                                if settiing_action =='3':
                                    break
                                if settiing_action =='1':
                                    print()
                                    print(f"""First name: {user.FirstName}
LastName: {user.LastName}
UserName: {user.UserName}
PhoneNumber: {user.PhoneNumber}
Password: {user.Password} """)
                                    print()
                                    user0=DB.get_by_username(user.UserName,filename)
                                    
                                    firstname=input('Enter new first name (or press enter to skip): ')
                                    if firstname =='':
                                        firstname =user0.FirstName
                                    lastname=input('Enter new last name (or press enter to skip): ')
                                    if lastname =='':
                                        lastname =user0.LastName                                
                                    username =firstname+'_'+lastname                             
                                    phonenumber=input('Enter new  phone number (or press enter to skip): ')
                                    if phonenumber =='':
                                        phonenumber =user0.PhoneNumber                                
                                    password=input('Enter new password (or press enter to skip): ')
                                    if password =='':
                                        password =user0.Password 
                                    contact=Model.CONTACT('0',username,phonenumber)
                                    contacts=user0.Contacts
                                    contacts[0]=contact
                                    user1=Model.USER('0',firstname,lastname,password,phonenumber,contacts,username)   
                                    DB.update(user0,user1,filename)
                                    user=user1   
                                if settiing_action =='2':
                                    sure=input('Are you sure? (y/n ): ')
                                    if sure.lower() =='y':
                                        DB.delete(user.UserName,filename)
                                        IsLogin=False