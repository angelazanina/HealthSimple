#Judith, Arthur, Geeneth, Angela
#HealthSimple v1.0

#imports
from plyer import notification
import time
import threading

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
    get_ctgry = category.get()
    get_msg = msg.get()
    get_time = var.get()
    
    #input validation
    if get_ctgry =="" or get_msg == "" or get_time =="":
        messagebox.showerror("Oops!", "Looks like we're missing some info.")
    else:
        time_sec = get_time*60
        messagebox.showinfo("Notification set", "Confirm notification?")
        
        #time.sleep can be problematic in a while loop
        time.sleep(time_sec)
        
        #adding to history file
        history_fo.write(get_ctgry+","+get_msg+","+str(get_time)+"\n")

        
        #we can add logo too!!
        notification.notify(title=get_ctgry,
                            message=get_msg,
                            app_name="HealthSimple",
                            timeout=20)
        
        history_fo.close()

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
category = Entry(widget, width="25", font=("poppins",10))
category.place(x=123, y=25)

#label2
msg_label = Label(widget, text="Display Message", font=("poppins", 10, 'bold'))
msg_label.place(x=20, y=80)

#entry2
msg = Entry(widget, width="25", font=("poppins", 10))
msg.place(x=170, y=77, height=30)

#label3
time_label = Label(widget, text="Set Time", font=("poppins", 10, 'bold'))
time_label.place(x=20, y=135)

#entry3
def change(var):
    time1 = int(var)
var = DoubleVar()
time1_slider = Scale(widget, from_=0, to=120, orient = HORIZONTAL, command=change, variable=var) 
time1_slider.place(x=90, y=120)


#label4
time_min_label = Label(widget, text="mins", font=("poppins", 10))
time_min_label.place(x=200, y=135)

#creating the notif button
#fg - color to render text
#bd - size of the border around inicator
#width - width of button
#relief - how the button stands out from the background

#creating a new thread for the notification function
#notif_thread = threading.Thread(target=get_info, args=[])

notif_button = Button(widget, width=20, text="SET NOTIFICATION", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#528DFF", relief="raised",
                command=get_info)


notif_button.place(x=30, y=200)

#creating the manage button
manage_button = Button(widget, width=20, text="MANAGE", font=("poppins", 10, 'bold'), fg="#ffffff", bg="#ffc052", relief="raised")
manage_button.place(x=30, y=250)

#makes the widget window resizable
widget.resizable(0,0)
#infinite loop - runs as long as the window is not closed
widget.mainloop()

