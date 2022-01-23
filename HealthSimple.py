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
from tkinter.messagebox import askokcancel, showinfo, WARNING

#imaging library
#ImageTk module is like a support between PIL and Tkinter
from PIL import Image, ImageTk

#file to save all the history
history_fo = open("notif_history.txt", "w")
history_fo.write("Category,Message,Time\n")
history_fo.close()

#global variable to determind state
global end
end = FALSE

def stop():
    answer = askokcancel(
        title='Confirmation',
        message='Do you want to stop your notifications?',
        icon=WARNING)

    if answer:
        showinfo(
            title='Stopping',
            message='Your notifications have been stopped!',
            )
        global end
        end = True

#functions
#function to get info

#---------------------------------------------------------------------
class notificationClass:

    def get_info(self):
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
        if (ctgrs_l == []) or (get_time ==0 and Motivation.get()==TRUE):
            messagebox.showerror("Oops!", "Looks like we're missing some info.")
        else:
            #time_sec = get_time*60
            time_sec = 10

            joined_ctgrs = ",".join(ctgrs_l)
            history_fo.write(joined_ctgrs+","+str(get_time)+"\n")

            MotivationTimeInterval = time_sec
            ActivityTimeInterval = 1800
            HydrationTimeInterval = 1200

            TimeReset = time.time()
            
            
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

    def __init__(self):
        notifications_thread = threading.Thread(target=self.get_info)
        notifications_thread.start()

def run_thread():
    global end
    end = False
    notificationClass()

def confirm():
    answer = askokcancel(
        title='Confirmation',
        message='Do you want to start your notifications?',
        icon=WARNING)

    if answer:
        showinfo(
            title='Confirming',
            message='Your notifications have been enabled!',
            )
        run_thread()
            
#---------------------------------------------------------------------
#def open_history():
    

#creating the tk object which allows us to create/manipulate widget
widget = Tk()
widget.title("HealthSimple")
widget.geometry("550x350")

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
    if (l==[]):
        msg['text'] = 'Please Choose a Category'
        msg.config(fg = 'red')
    else:
        joined_l = ", ".join(l)
        msg['text'] = joined_l
        msg.config(fg = 'black')

mb=  Menubutton ( widget, text="Categories", relief=RAISED, activebackground = 'pink')
mb.place(x=123, y=25)
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

Motivation = IntVar()
Water = IntVar()
Activity = IntVar()

def hide():
    if Motivation.get() == TRUE:
        time1_slider.place(x=90, y=120)
        time_label.place(x=20, y=135)
        time_min_label.place(x=250, y=135)
    elif Motivation.get() == FALSE:
        time1_slider.place_forget()
        time_label.place_forget()
        time_min_label.place_forget()

mb.menu.add_checkbutton ( label="Motivation", variable=Motivation, command=lambda:[hide(), change_text()])
mb.menu.add_checkbutton ( label="Water", variable=Water, command = change_text)
mb.menu.add_checkbutton ( label="Activity", variable=Activity, command = change_text)


#label2
msg_label = Label(widget, text="Categories Chosen", font=("poppins", 10, 'bold'))
msg_label.place(x=20, y=80)

#entry2
msg = Label(widget, font=("poppins", 10), text = 'Please Choose a Category', fg = 'red')
msg.place(x=170, y=77, height=30)

#label3
time_label = Label(widget, text="Set Time", font=("poppins", 10, 'bold'))
time_label.place(x=20, y=135)
time_label.place_forget()

#entry3
def change(var):
    time1 = int(var)
var = DoubleVar()
time1_slider = Scale(widget, from_=0, to=120, orient = HORIZONTAL, length = 150, command=change, variable=var, activebackground = 'pink') 
time1_slider.place(x=90, y=120)
time1_slider.place_forget()

#label4
time_min_label = Label(widget, text="mins", font=("poppins", 10))
time_min_label.place(x=250, y=135)
time_min_label.place_forget()

#creating the notif button
#fg - color to render text
#bd - size of the border around inicator
#width - width of button
#relief - how the button stands out from the background

#creating a new thread for the notification function
#notif_thread = threading.Thread(target=get_info, args=[])

notif_button = Button(widget, width=20, text="SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF", relief="raised", activeforeground = 'white', 
                command=confirm, activebackground = 'medium blue')


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
