# -*- coding: utf-8 -*-
"""
Created on wed Aug 07, 06:11:34 2019

@author: Hemraj
"""

                
from tkinter import * 
from PIL import ImageTk, Image
import os
from tkinter import messagebox
import time
import random
import re




creds='tempfile.temp'
login='login.temp'


def about():
    msg=messagebox.showinfo( "About Canteen", "A canteen is a refreshment\
 center for the students. It is necessary\
 to have a canteen in the college premises.\
 The food and snacks supplied by outside\
 restaurants are usually sub standard and\
 injurious to health. So, students can get\
 hygienic food in the college canteen. \n\
 '''Anand Engineering College''' canteen is situated in the middle\
 of the college. Students of all departments can\
 go there whenever they need. The canteen is clean\
 and there are a few students who remain in charge\
 of keeping it clean. Some instructive posters are\
 hung on the wall. Snacks of all types are sold here.\
 Even tea, soft drinks are available here. The canteen\
 is favorite to me because I like its clean environment\
 and systematic service. It plays an important role\
 in our college life. Students often discuss topics\
 of their texts over a cup of tea in the college canteen.\
 They thus utilize their leisure time in the canteen in a\
 productive way.") 



def FileSignup():
    if nameE.get()=='' or passwordE=='' or emailidE.get()=='' or phoneE.get()=='':
        
        msg=messagebox.showinfo('Invalid Signup ', 'Sorry you have \
 not entred  either Username or Password.\n\
                                Please Fill Them')

    else:
        with open(creds,'a') as f:
            f.write(nameE.get())
            f.write(' , ')
            f.write(passwordE.get())
            f.write(' , ')
            f.write(emailidE.get())
            f.write(' , ')
            f.write(phoneE.get())
            f.write('\n')            
        sucess=Label(root,text=' signup  sucesss\
     now go to login',fg='white',font=('calibri',13),bg='green')
        sucess.pack()
        sucess.place(x=230,y=360)
            
        

    
    
def CheckLogin():
    with open(creds,'r') as f:
        data=f.readlines()
        print(data)
        print(e1.get())

        
    with open(login,'a') as s:
        s.write(e1.get())
        print(e1.get())
        s.write('\n')
        s.write(e2.get())
        print(e2.get())
        s.write('\n')
        
                
                
    with open(login,'r') as s:
        data=s.readlines()
        lname=data[0]
        print(lname)
        lpassword=data[1]
        print(lpassword)

        
                
    if (lname=="de" and lpassword=="dehah") or (e1.get()=='HEMRAJ' and e2.get()=='ACER'):
        
        
        items = ('sandwitch','samosa','paneer pakora','veg aloo petty','veg spring roll',
                         'veg pasta','omlet 2 eggs','chilli potatos','burger','sandwitch (non veg)','Total amount')
            
        def total(entries):
            sand = (float(entries['sandwitch'].get()))
            samo =(float(entries['samosa'].get()))
            paneer=(float(entries['paneer pakora'].get()))
            veg_aloo=(float(entries['veg aloo petty'].get()))
            veg_spring=(float(entries['veg spring roll'].get()))
            veg_p=(float(entries['veg pasta'].get())) 
            omlet=(float(entries['omlet 2 eggs'].get()))
            chilli=(float(entries['chilli potatos'].get()))
            bur=(float(entries['burger'].get()))
            sand2=(float(entries['sandwitch (non veg)'].get()))
                    
                    
            sum = ( sand*15.0 + samo*7.0 +paneer*20.0  + veg_aloo*20.0 +
                   veg_spring*20.0 +veg_p*35.0 + omlet*20.0 +chilli*30.0 +bur*20.0
                   + sand2*25.0)
            print(sum)
            if sum ==0:
                messagebox.showwarning('required','please fill  the quantity of foody items in \
                                       the entrybox')
        
                        
            else:
                
                entries['Total amount'].delete(0, END)
                entries['Total amount'].insert(0, sum )
                    
        def reset(entries):
            entries['sandwitch'].delete(0, END)
            entries['samosa'].delete(0, END)
            entries['paneer pakora'].delete(0, END)
            entries['veg aloo petty'].delete(0, END)
            entries['veg pasta'].delete(0, END)
            entries['veg spring roll'].delete(0, END)
            entries['omlet 2 eggs'].delete(0, END)
            entries['chilli potatos'].delete(0, END)
            entries['burger'].delete(0, END)
            entries['sandwitch (non veg)'].delete(0, END)
            entries['Total amount'].delete(0, END)
                    
        
                    
                    
                
        def labels_and_entry(r1, items):
            entries= {}
            for item in items:
                print(item)
                row = Frame(r1)
                lab = Label(row, width=22, text=item+": ", anchor='w',bg='blue',fg='white')
                ent = Entry(row ,bg='yellow')
                ent.insert(0, "0")
                ent.focus()
                row.pack(side=TOP, 
                         fill=X, 
                         padx=5, 
                         pady=5)
                lab.pack(side=LEFT)
                ent.pack(side=LEFT, 
                         expand=NO, 
                         fill=X)
                entries[item] = ent
            return entries
                
                
                
                 
                
                
                
        if __name__=='__main__':
            r1=Tk()
            r1.geometry('1600x800+-9+0')    
            
            path1= ("C:\\Users\\Hemraj\\Desktop\\icon11.ico")
            r1.iconbitmap(path1)
            
            canteenposter= Label(r1, text='Choose And Fill Menu Items', font=('arial', 30, 'bold'), bg='STEEL BLUE',fg='black')
            canteenposter.pack(side=TOP)
                
            r1.title(' fill Quantities')
            ents=labels_and_entry(r1, items)
            b1 = Button(r1, text="TOTAL",bg='green',fg='white',command =(lambda e=ents: total(e)))
            b1.pack(side=LEFT, padx=5, pady=5)
            b2 = Button(r1, text="RESET",bg='green',fg='white',command =(lambda e=ents: reset(e)))
            b2.pack(side=LEFT, padx=5, pady=5)
                    
            b3 = Button(r1, text="EXIT",bg='green',fg='white',command=r1.destroy)
            b3.pack(side=LEFT, padx=5, pady=5)
                    
            r1.mainloop()
                


        
        
        
        
        
       
        else:
            msg=messagebox.showinfo('invalid login', 'Sorry you have \
entred wrong either Username or Password.\n\
                                Please Try Again')
          
  
#def DelUser():
#    os.remove(creds)
#    rootA.destroy()
#    Signup()
#if os.path.isfile(creds):
#    Login()
#else:
#    Signup()
# 

    


   #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WINDOW 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#  

  
  
   
root = Tk()

#root.attributes('-fullscreen',True)
root.geometry('1600x800+-10+0')
root.title('CANTEEN GUI APP')

path1= ("C:\\Users\\Hemraj\\Desktop\\icon11.ico")
root.iconbitmap(path1)

localtime = time.asctime(time.localtime(time.time()))
lbl=Label(root,text=localtime,font=('arial',20,'bold'),bg='green',fg='white')
lbl.pack()
lbl.place(x=870,y=0)



intruction=Label(root,text='please enter new Credidentials\n',fg='white',bg='green')
intruction.pack()
intruction.place(x=240,y=5)
    
nameL=Label(root,text='New Username*:')
passwordL=Label(root,text='New Password*:')
emailidl=Label(root,text='Email id*:')
phonel=Label(root,text='phone no*:')
nameL.pack()
emailidl.pack()
phonel.pack()
nameL.place(x=240,y=50)
passwordL.place(x=240,y=88)
emailidl.place(x=240,y=126)
phonel.place(x=240,y=164)


        
nameE=Entry(root,bd=5)
passwordE=Entry(root,bd=5,show='*')
emailidE=Entry(root,bd=5)
phoneE=Entry(root,bd=5)
nameE.pack()
nameE.place(x=350,y=50)
passwordE.pack()
passwordE.place(x=350,y=88)
emailidE.pack()
emailidE.place(x=350,y=126)
phoneE.pack()
phoneE.place(x=350,y=164)
    
signupbutton=Button(root,text='Signup',command=FileSignup)
signupbutton.pack()
signupbutton.place(x=242,y=202) 
    

 

canvas = Canvas(root,bg= "red", height=250, width=350,)



# Load the image file
im = Image.open('C:\\Users\\Hemraj\\Desktop\\GIF_Image1564397938995.gif')
# Put the image into a canvas compatible class, and stick in an
# arbitrary variable to the garbage collector doesn't destroy it
canvas.image = ImageTk.PhotoImage(im)
# Add the image to the canvas, and set the anchor to the top left / north west corner
canvas.create_image(0,0, image=canvas.image, anchor='nw')
canvas.pack() 
#root.geometry('500x500+359+150')


msg=Label(root,text=' Welcome To Anand Engineering College Canteen ',background='green',fg='white')       
msg.config(font=('callibri',17,'italic bold underline '))
msg1=Label(root,text=' WE WILL TRYING TO FULL SATISFYING YOU HERE ',background='green',fg='white')
msg.pack()
msg1.pack() 

l1=Label(root,text='user name*:')
L2=Label(root,text='password*:')
e1=Entry(root,bd=5)
e1.focus()
e2=Entry(root,bd=5,show='*')
l1.place(x=510,y=330)
L2.place(x=510,y=370)
e1.place(x=600,y=330)
e2.place(x=600,y=370)

    
    


#c.grid(columnspan=2)
#greenbutton.pack()
#redbutton.pack() 

menu_bar=Menu(root)
file_menu=Menu(menu_bar,tearoff=0,bg='yellow')
file_menu.add_command(label=' >>for veg student')
file_menu.add_separator()

file_menu.add_command(label='1.Sandwich (veg)___> 15/-')
file_menu.add_command(label='2.Samosa___________> 7/-')
file_menu.add_command(label='3.Paneer pakora____> 20/-')
file_menu.add_command(label='4.Veg Aloo Patty____> 20/-')
file_menu.add_command(label='5.Veg spring roll____> 20/-')
file_menu.add_command(label='6.Grilled sandwich__> 25/-')
file_menu.add_command(label='7.Aloo tikki_________> 10/-')
file_menu.add_command(label='8.Veg paneer Patty_> 35/-')
file_menu.add_command(label='9.cake______________> 200/-')
file_menu.add_command(label='10.veg pasta_______> 180/-')
file_menu.add_command(label='11.Omlet 2 eggs____> 20/-')
file_menu.add_command(label='12.Chilli Potato_____> 30/-')
file_menu.add_command(label='13.Burger___________> 20/-')
file_menu.add_command(label='14.Sandwich ( non veg)__> 25/-')
menu_bar.add_cascade(label='MENU',menu=file_menu)
root.config(menu=menu_bar)





filemenu=Menu(menu_bar,tearoff=0,bg='yellow')
filemenu.add_command(label='click to read me',command=about)

menu_bar.add_cascade(label='About Canteen',menu=filemenu)
root.config(menu=menu_bar)


filemenu=Menu(menu_bar,tearoff=0,bg='yellow')
filemenu.add_command(label='EXIT',command=root.destroy)
menu_bar.add_cascade(label='click to exit',menu=filemenu)
root.config(menu=menu_bar)


loginbutton = Button(root, text="Login", fg="green",command=CheckLogin) 
loginbutton.pack()
forgetbutton = Button(root ,text='forget password',fg='red')
forgetbutton.pack()
loginbutton.place(x=535,y=400)
forgetbutton.place(x=660,y=400)








 
root.mainloop() 
