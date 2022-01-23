#Judith, Arthur, Geeneth, Angela
#HealthSimple v1.0

#imports
from plyer import notification
import time
import threading
import multiprocessing

#to help make GUI
from tkinter import *
from tkinter import messagebox

#imaging library
#ImageTk module is like a support between PIL and Tkinter
from PIL import Image, ImageTk

#file to save all the history
history_fo = open("notif_history.txt", "w")
history_fo.write("Category,Message,Time\n")
history_fo.close()

#functions
#function to get info
def get_info():
    history_fo = open("notif_history.txt", "a")
    
    #getting the user input
    ctgrs_l = []
    if (Motivation.get() == True):
        ctgrs_l.append("Motivation")
    if (Water.get() ==True):
        ctgrs_l.append("Water")
    if (Activity.get() ==True):
        ctgrs_l.append("Activity")
    get_ctgry = ctgrs_l
    get_time = var.get()
    
    #input validation
    if ctgrs_l == [] or get_time ==0:
        messagebox.showerror("Oops!", "Looks like we're missing some info.")
    else:
        #time_sec = get_time*60
        time_sec = 10
        messagebox.showinfo("Notification set", "Confirm notification?")

        joined_ctgrs = ",".join(ctgrs_l)
        history_fo.write(joined_ctgrs+","+str(get_time)+"\n")

        MotivationTimeInterval = time_sec
        ActivityTimeInterval = 1800
        HydrationTimeInterval = 1200

        TimeReset = time.time()
        end = FALSE
        
        MotivationTimeEnd = MotivationTimeInterval + TimeReset
        ActivityTimeEnd = ActivityTimeInterval + TimeReset
        HydrationTimeEnd = HydrationTimeInterval + TimeReset
        while (end==FALSE):
            if time.time() > MotivationTimeEnd :
                notification.notify(
                    title = 'Motivation',
                    message = 'You Got This!',
                    timeout = 20
                    )
                MotivationTimeEnd = MotivationTimeInterval + time.time()

            if time.time() > ActivityTimeEnd :
                notification.notify(
                    title = 'Activity',
                    message = 'Get Up and Walk/Stretch',
                    timeout = 20
                    )
                ActivityTimeEnd = ActivityTimeInterval + time.time()

            if time.time() > HydrationTimeEnd :
                notification.notify(
                    title = 'Hydration',
                    message = 'Drink Some Water',
                    timeout = 20,
                    app_icon = 'water.ico'
                    )
                HydrationTimeEnd = HydrationTimeEnd + time.time()        

#def open_history():
    

#creating the tk object which allows us to create/manipulate widget
widget = Tk()
widget.title("HealthSimple")
widget.geometry("550x350")

#root = Tk()

logo = Image.open("Panda.png")
tkLogo = ImageTk.PhotoImage(logo)  #making tkinter compatible photo

#implementinga display box with our image
#the grid() method organizes widget in table like structure
logo_label = Label(widget, image=tkLogo).grid(row=1, column=1)

#label1
ctgry_label = Label(widget, text="Category", font=("poppins", 10, 'bold'))
ctgry_label.place(x=20, y=25)

#entry1 - **instead of Entry object, make drop down menu?**
#Entry widget accepts single line text strings from user
#category = Entry(widget, width="25", font=("poppins",10))
def change_text():
    l = []
    if (Motivation.get() == True):
        l.append("Motivation")
    if (Activity.get() == True):
        l.append("Activity")
    if (Water.get() == True):
        l.append("Water")
    joined_l = ", ".join(l)
    msg['text'] = joined_l
mb=  Menubutton ( widget, text="Categories", relief=RAISED, activebackground = 'pink')
mb.place(x=123, y=25)
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

Motivation = IntVar()
Water = IntVar()
Activity = IntVar()

mb.menu.add_checkbutton ( label="Motivation", variable=Motivation, command = change_text)
mb.menu.add_checkbutton ( label="Water", variable=Water, command = change_text)
mb.menu.add_checkbutton ( label="Activity", variable=Activity, command = change_text)


#label2
msg_label = Label(widget, text="Categories Chosen", font=("poppins", 10, 'bold'))
msg_label.place(x=20, y=80)

#entry2
msg = Label(widget, font=("poppins", 10), text = '')
msg.place(x=170, y=77, height=30)

#label3
time_label = Label(widget, text="Set Time", font=("poppins", 10, 'bold'))
time_label.place(x=20, y=135)

#entry3
def change(var):
    time1 = int(var)
var = DoubleVar()
time1_slider = Scale(widget, from_=0, to=120, orient = HORIZONTAL, length = 150, command=change, variable=var, activebackground = 'pink') 
time1_slider.place(x=90, y=120)

#label4
time_min_label = Label(widget, text="mins", font=("poppins", 10))
time_min_label.place(x=250, y=135)

#creating the notif button
#fg - color to render text
#bd - size of the border around inicator
#width - width of button
#relief - how the button stands out from the background

#creating a new thread for the notification function
#notif_thread = threading.Thread(target=get_info, args=[])

notif_button = Button(widget, width=20, text="SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF", relief="raised", activeforeground = 'white', 
                command=get_info, activebackground = 'medium blue')


notif_button.place(x=30, y=200)

#creating the manage button
manage_button = Button(widget, width=20, text="MANAGE", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#ffc052", relief="raised", activebackground = 'dark orange', activeforeground = 'white')
manage_button.place(x=30, y=250)

#creating the stop button
stop_button = Button(widget, width=20, text='STOP', font = ("poppins", 10, 'bold'), fg = 'white', bg = 'red' , relief = 'raised', activebackground = 'dark red', activeforeground = 'white', command = stop)
stop_button.place (x=30, y=300)

#makes the widget window resizable
widget.resizable(0,0)
#infinite loop - runs as long as the window is not closed
widget.mainloop()
