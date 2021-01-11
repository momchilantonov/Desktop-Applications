from tkinter import *
from tkinter import messagebox
import sqlite3

# Create LogIn Screen
tk = Tk()  # Create Parent
tk.title("Log In")  # Create Title for the Screen
tk.geometry("400x150")  # Set the Size for the Screen
tk.resizable(False, False)  # Set the Screen NOT Resizable
tk.iconbitmap("images\\ArtVisionIcon.ico")  # Create ICON for the Screen

# Take File for Background and Set it
bg = PhotoImage(file="images\\bg.png")  # Set Image for Background
log_canvas = Canvas(tk, width=400, height=150)  # Create Canvas
log_canvas.pack(fill="both", expand=True)  # Pack Canvas
log_canvas.create_image(0, 0, image=bg, anchor=NW)  # Set Image in Canvas for Background

# Create LogIn Label
log_canvas.create_text(200, 25, text="ArtVision Studio", font=("Courier", 24, "bold", "italic"), fill="#000000")


def check_user():
    # User Validation
    conn = sqlite3.connect("ArtVision.db")  # Create DB or Connect to existing
    cur = conn.cursor()  # Create a Cursor
    cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")  # Create DB Table if NOT Exists
    # TODO: # Create Admin User and Admin Pass - only with installation
    # cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")
    cur.execute("SELECT * FROM users")  # Search the Values from DB Table
    record = cur.fetchall()  # Create a VAR to collect all records from the  DB Table

    # Loop Thru Records
    for rec in record:
        if rec[0] == user_entry.get() and rec[1] == pass_entry.get():  # Check the username and password
            entry()  # If the Input is OK, go to Entry Screen
        else:
            # Show a Message Box with Incorrect Input
            messagebox.showwarning("LogIn ERROR!", "Incorrect username or password!\nPlease try again.", )

    conn.commit()  # Commit changes
    conn.close()  # Close connection


def users_data():
    # Create LogIn Screen
    user = Toplevel()  # Create Slave
    user.title("Users")  # Create Title for the Screen
    user.geometry("500x500")  # Set the Size for the Screen
    user.resizable(False, False)  # Set the Screen NOT Resizable
    user.iconbitmap("images\\ArtVisionIcon.ico")  # Create ICON for the Screen

    # Take File for Background and Set it
    user_bg = PhotoImage(file="images\\bg.png")  # Set Image for Background
    user_canvas = Canvas(user, width=500, height=500)  # Create Canvas
    user_canvas.pack(fill="both", expand=True)  # Pack Canvas
    user_canvas.create_image(0, 0, image=user_bg, anchor=NW)  # Set Image in Canvas for Background

    # Create LogIn Label
    user_canvas.create_text(250, 25, text="ArtVision Studio", font=("Courier", 24, "bold", "italic"), fill="#000000")

    def query():
        # Create Screen
        show = Toplevel()  # Create Slave
        show.title("User List")  # Create Title for the Screen
        show.geometry("300x300")  # Set the Size for the Screen
        show.configure(bg="#FB8CE2")  # Set Background color
        show.resizable(False, False)  # Set the Screen NOT Resizable
        show.iconbitmap("images\\ArtVisionIcon.ico")  # Create ICON for the Screen

        # Create Connection with DB and take data
        conn = sqlite3.connect("ArtVision.db")  # Create DB or Connect to existing
        cur = conn.cursor()  # Create a Cursor
        cur.execute("SELECT *, OID FROM users")  # Search the Values from DB Table
        record = cur.fetchall()  # Create a VAR to collect all records from the  DB Table

        # Loop Thru Records and Create a Table with data
        rows = len(record)
        cols = len(record[0])
        for r in range(rows):
            for c in range(cols):
                table = Entry(show, width=10, bg="#F652D0", font=("Courier", 12, "bold", "italic"))
                table.grid(row=r, column=c)
                table.insert(END, record[r][c])

    def add():
        return

    def change():
        return

    def delete():
        return

    # # Create Labels
    # Create Labels for add and delete users
    user_canvas.create_text(80, 112, text="Username", font=("Courier", 12, "bold", "italic"), fill="#000000")
    user_canvas.create_text(80, 142, text="Password", font=("Courier", 12, "bold", "italic"), fill="#000000")
    user_canvas.create_text(80, 242, text="Username", font=("Courier", 12, "bold", "italic"), fill="#000000")
    user_canvas.create_text(85, 342, text="User's ID", font=("Courier", 12, "bold", "italic"), fill="#000000")
    user_canvas.create_text(72, 60, text="Add User", font=("Courier", 16, "bold", "italic"), fill="#000000")
    user_canvas.create_text(90, 200, text="Change User", font=("Courier", 16, "bold", "italic"), fill="#000000")
    user_canvas.create_text(92, 300, text="Delete User", font=("Courier", 16, "bold", "italic"), fill="#000000")
    user_canvas.create_text(106, 400, text="Show All Users", font=("Courier", 16, "bold", "italic"), fill="#000000")

    # # Create Entry Boxes
    # Create Entry Boxes for add and delete user
    add_user = Entry(user, width=25, borderwidth=3, font=("Times", 10, "bold", "italic"))
    add_pass = Entry(user, width=25, borderwidth=3, font=("Times", 10, "bold", "italic"))
    change_user = Entry(user, width=25, borderwidth=3, font=("Times", 10, "bold", "italic"))
    delete_user = Entry(user, width=25, borderwidth=3, font=("Times", 10, "bold", "italic"))
    user_canvas.create_window(145, 100, anchor=NW, window=add_user)
    user_canvas.create_window(145, 130, anchor=NW, window=add_pass)
    user_canvas.create_window(145, 230, anchor=NW, window=change_user)
    user_canvas.create_window(145, 330, anchor=NW, window=delete_user)

    # # Create Buttons
    # Creat Button for Query
    button_query = Button(user, text="Show All Users in DataBase", borderwidth=3,
                          font=("Courier", 12, "bold", "italic"), command=query)
    button_query.bind('<Return>', lambda event=None: button_query.invoke())
    user_canvas.create_window(196, 430, height=40, width=275, anchor=NW, window=button_query)

    # Creat Button for Add Users
    button_add = Button(user, text="Add", borderwidth=3,
                        font=("Courier", 12, "bold", "italic"), command=add)
    button_add.bind('<Return>', lambda event=None: button_add.invoke())
    user_canvas.create_window(360, 100, height=55, width=120, anchor=NW, window=button_add)

    # Creat Button for Change Users
    button_change = Button(user, text="Change", borderwidth=3,
                           font=("Courier", 12, "bold", "italic"), command=change)
    button_change.bind('<Return>', lambda event=None: button_change.invoke())
    user_canvas.create_window(360, 230, height=25, width=120, anchor=NW, window=button_change)

    # Creat Button for Delete Users
    button_delete = Button(user, text="Delete", borderwidth=3,
                           font=("Courier", 12, "bold", "italic"), command=delete)
    button_delete.bind('<Return>', lambda event=None: button_delete.invoke())
    user_canvas.create_window(360, 330, height=25, width=120, anchor=NW, window=button_delete)

    # Create Lines
    user_canvas.create_line(120, 70, 477, 70)
    user_canvas.create_line(158, 210, 477, 210)
    user_canvas.create_line(158, 310, 477, 310)
    user_canvas.create_line(192, 410, 477, 410)

    user.mainloop()


def graphics_data():
    return


def contacts_data():
    return


def procedures():
    return


def applications():
    return


def entry():
    tk.destroy()  # Close the LogIn Screen

    # Create Screen
    enter = Tk()  # Create Parent
    enter.title("Welcome")  # Create Title for the Screen
    enter.geometry("500x500")  # Set the Size for the Screen
    enter.resizable(False, False)  # Set the Screen NOT Resizable
    enter.iconbitmap("images\\ArtVisionIcon.ico")  # Create ICON for the Screen

    # Take File for Background and Set it
    enter_bg = PhotoImage(file="images\\bg.png")  # Set Image for Background
    enter_canvas = Canvas(enter, width=500, height=500)  # Create Canvas
    enter_canvas.pack(fill="both", expand=True)  # Pack Canvas
    enter_canvas.create_image(0, 0, image=enter_bg, anchor=NW)  # Set Image in Canvas for Background

    # Create LogIn Label
    enter_canvas.create_text(250, 25, text="ArtVision Studio", font=("Courier", 24, "bold", "italic"), fill="#000000")

    # # Create Buttons
    # Creat Button Graphics
    button_graphics = Button(enter, text="Graphics", borderwidth=3,
                             font=("Courier", 14, "bold", "italic"), command=graphics_data)
    button_graphics.bind('<Return>', lambda event=None: button_graphics.invoke())
    enter_canvas.create_window(150, 110, height=50, width=200, anchor=NW, window=button_graphics)

    # Creat Button Contacts
    button_contacts = Button(enter, text="Contacts", borderwidth=3,
                             font=("Courier", 14, "bold", "italic"), command=contacts_data)
    button_contacts.bind('<Return>', lambda event=None: button_contacts.invoke())
    enter_canvas.create_window(150, 230, height=50, width=200, anchor=NW, window=button_contacts)

    # Creat Button Users
    button_users = Button(enter, text="Users", borderwidth=3,
                          font=("Courier", 14, "bold", "italic"), command=users_data)
    button_users.bind('<Return>', lambda event=None: button_users.invoke())
    enter_canvas.create_window(150, 290, height=50, width=200, anchor=NW, window=button_users)

    # Creat Button Procedures
    button_procedures = Button(enter, text="Procedures", borderwidth=3,
                               font=("Courier", 14, "bold", "italic"), command=procedures)
    button_procedures.bind('<Return>', lambda event=None: button_procedures.invoke())
    enter_canvas.create_window(150, 170, height=50, width=200, anchor=NW, window=button_procedures)

    # Creat Button Applications
    button_applications = Button(enter, text="Applications", borderwidth=3,
                                 font=("Courier", 14, "bold", "italic"), command=applications)
    button_applications.bind('<Return>', lambda event=None: button_applications.invoke())
    enter_canvas.create_window(150, 350, height=50, width=200, anchor=NW, window=button_applications)

    enter.mainloop()


# # Create Labels
# Create Labels for user and pass
log_canvas.create_text(105, 60, text="Username", font=("Courier", 12, "bold", "italic"), fill="#000000")
log_canvas.create_text(105, 90, text="Password", font=("Courier", 12, "bold", "italic"), fill="#000000")

# # Create Entry Boxes
# Create Entry Boxes for LogIn
user_entry = Entry(tk, width=25, borderwidth=3, show="*", font=("Times", 10, "bold", "italic"))
pass_entry = Entry(tk, width=25, borderwidth=3, show="*", font=("Times", 10, "bold", "italic"))
log_canvas.create_window(160, 50, anchor=NW, window=user_entry)
log_canvas.create_window(160, 80, anchor=NW, window=pass_entry)

# # Create Buttons
# Creat Button for Entry
button_entry = Button(tk, text="Enter", borderwidth=3,
                      font=("Courier", 12, "bold", "italic"), command=check_user)
button_entry.bind('<Return>', lambda event=None: button_entry.invoke())
log_canvas.create_window(160, 115, height=25, width=185, anchor=NW, window=button_entry)

tk.mainloop()
