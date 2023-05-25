"""
Lucas Dinh
May 2023

Lucas Dinh
May 2023

During my project, I gained valuable experience in using multiple modules of 
Tkinter, including Label(), Button(), and Frame(). One particular challenge I 
encountered was implementing the reset button, which required detecting a 
specific label, "loss," and destroying it. To overcome this, I used a variable 
called "loss" and checked its type using an if-else statement. If the variable 
was a Label object, it would be destroyed; otherwise, nothing would be done.

Another challenge I faced was properly placing the buttons. I utilized a for 
loop, but determining the exact button positions proved challenging.

This project was instrumental in my learning of Tkinter and building 
interactive GUIs. I feel more confident in using these modules and creating 
engaging user interfaces.



Another challenge was placing the buttons. To place the buttons i used a for loop,
the main part that was challenging was trying to figure out where the buttons 
would end up as it was difficult to determine the output.


Overall this project helped me learn Tkinter and howw 
"""
from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.geometry("400x425")
root.title("Q4 final project")
root.resizable(width=False, height=False)
#dictionary to hold login informations
login_data={'amontanus':'python2023','lucas':'2008'}
#---------------------------------------------------------------------------------------------------------------------------
#function wipes all widgets in root
def wipe():
    """Clears all widgets in the root window."""
    for widget in root.winfo_children():
        widget.destroy()
#---------------------------------------------------------------------------------------------------------------------------
def login():
    """
    Validates the login credentials entered by the user.
    If the login is successful, it creates the main menu frame.
    Otherwise, it displays an error message.
    """
    username = username_entry.get().lower()
    password = password_entry.get().lower()
    
    if username in login_data and login_data[username] == password:
        wipe()
        create_main_menu()
    else:
        error_label.config(text="Incorrect username or password")

def create_main_menu():
    """
    Creates the main menu frame and buttons for different game options.
    """
    wipe()
    global main_menu
    main_menu = Frame(root)
    main_menu.pack()

    y_button = Button(main_menu, text="YuGiOh", command=Yugi_Menu)
    m_button = Button(main_menu, text="MagicTheGathering", command=MTG_Menu)
    
    y_button.grid(row=0, column=0, sticky=W, pady=2, padx=50)
    m_button.grid(row=1, column=0, sticky=W, pady=2, padx=35)

# Setup login GUI
login_screen = Frame(root, width=200, height=200)
login_screen.config(width=200, height=200)
login_screen.pack()

username_label = Label(login_screen, text='Enter username: ')
username_label.pack()
username_entry = Entry(login_screen)
username_entry.pack()
password_label = Label(login_screen, text='Enter password: ')
password_label.pack()
password_entry = Entry(login_screen, show="*")
password_entry.pack()
login_button = Button(login_screen, text="Login", command=login)
login_button.pack()
error_label = Label(login_screen, fg="red")
error_label.pack()
#---------------------------------------------------------------------------------------------------------------------------
#diceroll function
def diceroll(Label):
    """
    Simulates rolling a 20-sided dice and displays the result in the given 
    Label widget.
    """
    Label["text"] = "Rolling..."
    d20 = list(range(1, 21))
    Label.after(500, lambda: Label.config(text=str(random.choice(d20))))
#---------------------------------------------------------------------------------------------------------------------------
#coinflip function
def coinflip(Label):
    """
    Simulates flipping a coin and displays the result (Heads or Tails) in the 
    given Label widget.
    """
    Label['text'] = "Flipping..."       
    Label.after(500, lambda: 
                Label.config(text=random.choice(["Heads", "Tails"])))
#---------------------------------------------------------------------------------------------------------------------------
# makes a new frame for the YuGiOh lifepoint counter menu
def Yugi_Menu():
    """
    Creates a new frame for the YuGiOh lifepoint counter menu.
    """
    wipe()
    
    # Add a button to go back to the main menu
    back_button = Button(root, text="Back", command=create_main_menu)
    back_button.pack()

    #player1 frame
    p1=Frame(root, width=400, height=200, borderwidth=5, relief=GROOVE)
    p1.pack()
    p1_label=Label(p1, text='player1')
    p1_label.place(x=0, y=0)
    #player2 frame
    p2=Frame(root, width=400, height=200, borderwidth=5, relief=GROOVE)
    p2.pack()
    p2_label=Label(p2, text='player2')
    p2_label.place(x=0, y=0)
    #add the player frames to the YuGiOh menu
    lifepoint_counterYuGi(p1)
    lifepoint_counterYuGi(p2)
#---------------------------------------------------------------------------------------------------------------------------
# Makes a new frame for MagicTheGathering lifepoint counter menu
def MTG_Menu():
    """
    Creates a new frame for the MagicTheGathering lifepoint counter menu.
    """
    wipe()
    
    # Add a button to go back to the main menu
    back_button = Button(root, text="Back", command=create_main_menu)
    back_button.pack()

    #player1 frame
    p1=Frame(root, width=400, height=200, borderwidth=5, relief=GROOVE)
    p1.pack()
    p1_label=Label(p1, text='player1')
    p1_label.place(x=0, y=0)
    #player2 frame
    p2=Frame(root, width=400, height=200, borderwidth=5, relief=GROOVE)
    p2.pack()
    p2_label=Label(p2, text='player2')
    p2_label.place(x=0, y=0)
    #add the player frames to the MTG menu
    lifepoint_counterMTG(p1)
    lifepoint_counterMTG(p2)
#---------------------------------------------------------------------------------------------------------------------------
#YuGiOh

# function to make widgets for the lifepoint menu 
def lifepoint_counterYuGi(frame):
    """
    Creates the lifepoint counter menu for YuGiOh.

    Args:
        frame: The frame where the lifepoint counter menu will be displayed.
    """
    frame.counter = 8000
    buttons = []
    loss = None
    
    #reset funtion
    def reset():
        """
        Resets the lifepoint counter and clears the loss label if displayed.
        """
        nonlocal loss
        if isinstance(loss,Label)==True:
            loss.destroy()
            loss = None
        totalpoints['text'] = '8000'
        frame.counter = 8000
        for button in buttons:
            button.configure(state=NORMAL)
        for child in frame.winfo_children():
            if child not in [reset_button, totalpoints, add, sub, flipresult, 
                             rollresult]:
                child.configure(state=NORMAL)
        
    #reset button     
    reset_button = Button(frame, text="reset here", command=reset)
    reset_button.pack()
    reset_button.place(x=150 , y=160)
    
    #sets the counter for total lifepoints
    def pointscounter(n):
        """
        Updates the lifepoint counter by adding or subtracting the given value.
        Displays a loss label if the lifepoint counter reaches zero.

        Args:
            n: The value to be added or subtracted from the lifepoint counter.
        """
        nonlocal loss
        frame.counter += n
        totalpoints['text'] = str(frame.counter)
        #if lifepoint reaches zero displays "You Loss!" label
        if frame.counter <= 0:
            totalpoints.pack_forget()
            loss = Label(frame, text="You Loss!", font=('Arial',50))
            loss.pack()
            loss.place(x=50, y=50)
            for button in buttons:
                button.configure(state=DISABLED)
            for child in frame.winfo_children():
                if child not in [reset_button, totalpoints, add, sub, 
                                 flipresult, rollresult]:
                    child.configure(state=DISABLED)
               
    # Total points label
    totalpoints = Label(frame, text=frame.counter, font=('Arial',25))
    totalpoints.place(x=155, y=0)

    # Addition buttons
    add = Label(frame, text="add", borderwidth=5, relief=GROOVE)
    add.pack()
    add.place(x=50, y=125)
    button_values = [100, 500, 1000]
    x_pos = 0
    for value in button_values:
        a = Button(frame, text=value, command=lambda n=value: pointscounter(n))
        a.place(x=x_pos, y=160)
        x_pos += 50
        buttons.append(a)

    # Subtraction buttons
    sub = Label(frame, text="subtract", borderwidth=5, relief=GROOVE)
    sub.pack()
    sub.place(x=285, y=125)
    button_values2 = [-100, -500, -1000]
    num_buttons2 = len(button_values2)
    button_width2 = 50
    total_width2 = num_buttons2 * button_width2
    x2_start = 400 - total_width2 - 10
    for i, value in enumerate(button_values2):
        s =Button(frame, text=value, command=lambda n=value: pointscounter(n))
        s.place(x=x2_start + i*button_width2, y=160)
        buttons.append(s)
        

    #coinflip button
    flipresult=Label(frame,text=" ")
    flipresult.pack()
    flipresult.place(x=10,y=95)
    coinflip_button = Button(frame, text="Flip the Coin", command=lambda 
                             Label=flipresult: coinflip(Label))
    coinflip_button.pack()
    coinflip_button.place(x=10,y=60)
    
    #diceroll button
    rollresult=Label(frame,text=" ")
    rollresult.pack()
    rollresult.place(x=300,y=95)
    diceroll_button = Button(frame, text="Roll the Dice(20d)", command=lambda
                             Label=rollresult: diceroll(Label))
    diceroll_button.pack()
    diceroll_button.place(x=275,y=60)
#---------------------------------------------------------------------------------------------------------------------------
#MTG

# function to make widgets for the lifepoint menu 
def lifepoint_counterMTG(frame):
    """
    Creates the lifepoint counter menu for Magic: The Gathering.

    Args:
        frame: The frame where the lifepoint counter menu will be displayed.
    """
    frame.counter = 20
    buttons = []
    loss = None
    
    #reset funtion
    def reset():
        """
       Resets the lifepoint counter and clears the loss label if displayed.
       """
        nonlocal loss
        if isinstance(loss,Label)==True:
            loss.destroy()
            loss = None
        totalpoints['text'] = '20'
        frame.counter = 20
        for button in buttons:
            button.configure(state=NORMAL)
        for child in frame.winfo_children():
            if child not in [reset_button, totalpoints, add, sub, flipresult, 
                             rollresult]:
                child.configure(state=NORMAL)
        
    #reset button     
    reset_button = Button(frame, text="reset here", command=reset)
    reset_button.pack()
    reset_button.place(x=150 , y=160)
    
    #sets the counter for total lifepoints
    def pointscounter(n):
        """
        Updates the lifepoint counter by adding or subtracting the given value.
        Displays a loss label if the lifepoint counter reaches zero.

        Args:
            n: The value to be added or subtracted from the lifepoint counter.
        """
        nonlocal loss
        frame.counter += n
        totalpoints['text'] = str(frame.counter)
        #if lifepoint reaches zero displays "You Loss!" label
        if frame.counter <= 0:
            totalpoints.pack_forget()
            loss = Label(frame, text="You Loss!", font=('Arial',50))
            loss.pack()
            loss.place(x=50, y=50)
            for button in buttons:
                button.configure(state=DISABLED)
            for child in frame.winfo_children():
                if child not in [reset_button, totalpoints, add, sub, 
                                 flipresult, rollresult]:
                    child.configure(state=DISABLED)
               
    # Total points label
    totalpoints = Label(frame, text=frame.counter, font=('Arial',25))
    totalpoints.place(x=155, y=0)

    # Addition buttons
    add = Label(frame, text="add", borderwidth=5, relief=GROOVE)
    add.pack()
    add.place(x=50, y=125)
    button_values = [1, 5, 10]
    x_pos = 0
    for value in button_values:
        a = Button(frame, text=value, command=lambda n=value: pointscounter(n))
        a.place(x=x_pos, y=160)
        x_pos += 50
        buttons.append(a)

    # Subtraction buttons
    sub = Label(frame, text="subtract", borderwidth=5, relief=GROOVE)
    sub.pack()
    sub.place(x=285, y=125)
    button_values2 = [-1, -5, -10]
    num_buttons2 = len(button_values2)
    button_width2 = 50
    total_width2 = num_buttons2 * button_width2
    x2_start = 400 - total_width2 - 10
    for i, value in enumerate(button_values2):
        s =Button(frame, text=value, command=lambda n=value: pointscounter(n))
        s.place(x=x2_start + i*button_width2, y=160)
        buttons.append(s)
        

    #coinflip button
    flipresult=Label(frame,text=" ")
    flipresult.pack()
    flipresult.place(x=10,y=95)
    coinflip_button = Button(frame, text="Flip the Coin", command=lambda 
                             Label=flipresult: coinflip(Label))
    coinflip_button.pack()
    coinflip_button.place(x=10,y=60)
    
    #diceroll button
    rollresult=Label(frame,text=" ")
    rollresult.pack()
    rollresult.place(x=300,y=95)
    diceroll_button = Button(frame, text="Roll the Dice(20d)", command=lambda 
                             Label=rollresult: diceroll(Label))
    diceroll_button.pack()
    diceroll_button.place(x=275,y=60)
 #---------------------------------------------------------------------------------------------------------------------------
    
    
#run
root.mainloop()
