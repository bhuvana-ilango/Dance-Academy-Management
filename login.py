from tkinter import *
from tkinter import messagebox
from tkinter import font
import admin
import instructor
from database import Database

# creating a database object 
db = Database("mainDatabase.db")

class Login:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        # Background Color
        self.root.config(bg="#222222")

        # Call the tkinter frame to the window
        self.loginControlFrame()

    """CTA Methods"""

    # login method to redirect to the next frames
    def loginFunc(self):
        if self.txtUsername.get() == 'bhuvana' and self.txtPassword.get() == 'bhuvana':
            self.loginFrame.destroy()
            self.topFrame.destroy()
            admin.AdminControls(self.root)
        elif db.instructorLogin(self.txtUsername.get(), self.txtPassword.get()):
            self.loginFrame.destroy()
            self.topFrame.destroy()
            instructor.InstructorControls(self.root)
        else:
            messagebox.showerror("Error!", "Check your credentials or Please Contact System Admin!")
            self.username.set("")
            self.password.set("")

        
    """Login Frame"""

    def loginControlFrame(self):
        # top Frame as Welcome Message
        self.topFrame = Frame(self.root, bg="#222222")
        self.topFrame.pack(side=TOP)

        self.labelCompanyName = Label(self.topFrame, text="Dance Academy", font=("Times New Roman", 55),bg="#222222",fg="#22a39f")
        self.labelCompanyName.grid(row=0, column=0, columnspan=2, padx=0,pady=10)
        self.labelDesc = Label(self.topFrame, text="Dance your soul away!", font=("Times New Roman", 25, "italic"),bg="#222222",fg="#22a39f")
        self.labelDesc.grid(row =1, column=0, columnspan=4, padx=40, pady=5)

        # Login Frame Configurations
        self.loginFrame = Frame(self.root, bg="#22a39f")
        self.loginFrame.pack(anchor=CENTER, fill=X, padx=400, pady=20)
        self.login_frame_title = Label(self.loginFrame, text="  LOGIN HERE!", font=("Rubik Vinyl", 25), bg="#22a39f",fg="#434242")
        self.login_frame_title.grid(row=0,column=10, columnspan=1, padx=20, pady=20, sticky="w")

        # Username
        self.labelUsername = Label(self.loginFrame, text="Username", font=("Times New Roman", 16, "bold"), bg="#22a39f",fg="#434242")
        self.labelUsername.grid(row=1, column=8, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.loginFrame, textvariable=self.username, font=("Times New Roman", 15), width=30,bd=5)
        self.txtUsername.grid(row=1, column=10, padx=10, pady=5, sticky="w")

        # Password
    
        self.labelPassword = Label(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"), bg="#22a39f",fg="#434242")
        self.labelPassword.grid(row=2, column=8, padx=10, pady=5, sticky="w")
        self.txtPassword = Entry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=30,bd=5, show="*")
        self.txtPassword.grid(row=2, column=10, padx=10, pady=5, sticky="w")

        # Login Button
        self.btnLogin = Button(self.loginFrame, command=self.loginFunc, text="Login", bd=0, cursor="hand2",
                               fg="white", bg="#434242", width=10, font=("Impact", 15))
        self.btnLogin.grid(row=3, column=10,padx=10,pady=10, sticky="e")

        # empty label for spacing in grid
        self.emptyLabel = Label(self.loginFrame, font=("Times New Roman", 16, "bold"), bg="#22a39f",fg="#22a39f")
        self.emptyLabel.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        
