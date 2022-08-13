import tkinter as tk
from tkinter import IntVar, PhotoImage, messagebox
from  tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
import time
from datetime import datetime
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import random
import yagmail

def blog_page():
        bg = Image.open('bgbgbg.png')
        bg = ImageTk.PhotoImage(bg)
        bg_label = tk.Label(image = bg)
        bg_label.image = bg
        bg_label.place(relwidth = 1, relheight = 1)

        frame = tk.Frame(root, bg = '#d9d9d9')
        frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.08)

        blog_button = tk.Button(frame, text = "Blogging", command = Home_page)
        blog_button.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

        def activity_page():
            frame4 = tk.Frame(root, bg = '#d9d9d9')
            frame4.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.08)

            blog_button = tk.Button(frame4, text = "Blogging", command = blog_page)
            blog_button.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

            activity_button = tk.Button(frame4, text = 'Activity', command = activity_page)
            activity_button.place(relx = 0.3, rely = 0, relwidth = 0.4, relheight = 1)

            profile_button = tk.Button(frame4, text = "Profile")
            profile_button.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)

            frame5 = tk.Frame(root, bg = '#bee7a5')
            frame5.place(relx = 0.1, rely = 0.2, relwidth = 0.6, relheight = 0.75)

            add_activity = tk.Button(frame2, text = "+", bg = '#bee7a5')
            add_activity.place(relx = 0.85, rely = 0.05, relwidth = 0.1, relheight = 0.1)

            frame6 = tk.Frame(root, bg = '#bee7a5')
            frame6.place(relx = 0.72, rely = 0.2, relwidth = 0.17, relheight = 0.75)

        activity_button = tk.Button(frame, text = 'Activity', command = activity_page)
        activity_button.place(relx = 0.3, rely = 0, relwidth = 0.4, relheight = 1)

        profile_button = tk.Button(frame, text = "Profile")
        profile_button.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)

        frame2 = tk.Frame(root, bg = '#bee7a5')
        frame2.place(relx = 0.1, rely = 0.2, relwidth = 0.6, relheight = 0.75)

        def show_blog():
            user1 = random.choice(username_list)
            user2 = random.choice(username_list)
            user3 = random.choice(username_list) 

            temp_frame1 = tk.Frame(frame2, bg = '#d9d9d9')
            temp_frame1.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.25)
            
            with open("logininfo.txt" , "r") as f:
                for x in f.read().splitlines():
                    user_list = x.split()
                    if user_list[0] == user1:
                        file = user1 + '_blogging.txt'

                blog_object = open(file, "r")
                blog_info = blog_object.read()
        
                username_label = tk.Label(temp_frame1, text = "@" + f"{user1}", bg = '#d9d9d9')
                username_label.place(relx = 0.1, rely = 0.1, relwidth = 0.2, relheight = 0.15)

                blog_label = tk.Label(temp_frame1, text = f"{blog_info}", bg = '#d9d9d9')
                blog_label.place(relx = 0.1, rely = 0.3, relwidth = 0.9, relheight = 0.3)

                date_label = tk.Label(temp_frame1, text = f"{today}", bg = '#d9d9d9')
                date_label.place(relx = 0.1, rely = 0.6, relwidth = 0.2, relheight = 0.15)

            temp_frame2 = tk.Frame(frame2, bg = '#d9d9d9')
            temp_frame2.place(relx = 0.1, rely = 0.5, relwidth = 0.8, relheight = 0.25)
            
            with open("logininfo.txt" , "r") as f:
                for x in f.read().splitlines():
                    user_list = x.split()
                    if user_list[0] == user2:
                        file = user2 + '_blogging.txt'

                blog_object2 = open(file, "r")
                blog_info2 = blog_object2.read()

                username_label2 = tk.Label(temp_frame2, text = "@" + f"{user2}", bg = '#d9d9d9')
                username_label2.place(relx = 0.1, rely = 0.1, relwidth = 0.2, relheight = 0.15)

                blog_label2 = tk.Label(temp_frame2, text = f"{blog_info2}", bg = '#d9d9d9')
                blog_label2.place(relx = 0.1, rely = 0.3, relwidth = 0.9, relheight = 0.3)

                date_label2 = tk.Label(temp_frame2, text = f"{today}", bg = '#d9d9d9')
                date_label2.place(relx = 0.1, rely = 0.6, relwidth = 0.2, relheight = 0.15)

            temp_frame3 = tk.Frame(frame2, bg = '#d9d9d9')
            temp_frame3.place(relx = 0.1, rely = 0.8, relwidth = 0.8, relheight = 0.25)
            
            with open("logininfo.txt" , "r") as f:
                for x in f.read().splitlines():
                    user_list = x.split()
                    if user_list[0] == user3:
                        file = user3 + '_blogging.txt'

                blog_object3 = open(file, "r")
                blog_info3 = blog_object3.read()

                username_label3 = tk.Label(temp_frame3, text = "@" + f"{user3}", bg = '#d9d9d9')
                username_label3.place(relx = 0.1, rely = 0.1, relwidth = 0.2, relheight = 0.15)

                blog_label3 = tk.Label(temp_frame3, text = f"{blog_info3}", bg = '#d9d9d9')
                blog_label3.place(relx = 0.1, rely = 0.3, relwidth = 0.9, relheight = 0.3)

                date_label3 = tk.Label(temp_frame3, text = f"{today}", bg = '#d9d9d9')
                date_label3.place(relx = 0.1, rely = 0.6, relwidth = 0.2, relheight = 0.15)
                
        refresh_button = tk.Button(frame2, text = "refresh", command = show_blog)
        refresh_button.place(relx = 0.1, rely = 0.1, relwidth = 0.3, relheight = 0.05)

        def add_blog_page():
            add_blog_frame = tk.Frame(root, bg = '#bee7a5')
            add_blog_frame.place(relx = 0.1, rely = 0.2, relwidth = 0.6, relheight = 0.75)

            name_field = tk.StringVar()
            username_field = tk.StringVar()
            title_field = tk.StringVar()
            post_field = tk.StringVar()

            name_label = tk.Label(add_blog_frame, text = "Enter Name", bg = '#bee7a5')
            name_label.place(relx = 0.05, rely = 0.2, relwidth = 0.2, relheight = 0.05)

            name = tk.Entry(add_blog_frame, textvariable = name_field)
            name.place(relx = 0.3, rely = 0.2, relwidth = 0.5, relheight= 0.05)

            username_label = tk.Label(add_blog_frame, text = "Enter username", bg = '#bee7a5')
            username_label.place(relx = 0.05, rely = 0.3, relwidth = 0.2, relheight = 0.05)

            username = tk.Entry(add_blog_frame, textvariable = username_field)
            username.place(relx = 0.3, rely = 0.3, relwidth = 0.5, relheight= 0.05)

            title_label = tk.Label(add_blog_frame, text = "Enter title", bg = '#bee7a5')
            title_label.place(relx = 0.05, rely = 0.4, relwidth = 0.2, relheight = 0.05)

            title = tk.Entry(add_blog_frame, textvariable = title_field)
            title.place(relx = 0.3, rely = 0.4, relwidth = 0.5, relheight= 0.05)

            post_label = tk.Label(add_blog_frame, text = "Enter post", bg = '#bee7a5')
            post_label.place(relx = 0.05, rely = 0.5, relwidth = 0.2, relheight = 0.05)

            post = tk.Entry(add_blog_frame, textvariable = post_field)
            post.place(relx = 0.3, rely = 0.5, relwidth = 0.5, relheight= 0.15)

            def add_blogs():
                #Adding it to txt
                '''TO BE DELETED'''
                uns_file = username_field.get() + '_blogging.txt'
                blog_content = post_field.get()+"\n"
                fileobj = open(uns_file,'a')
                fileobj.write(blog_content)


            submit_button = tk.Button(add_blog_frame, text = "Post", command = add_blogs)
            submit_button.place(relx = 0.3, rely = 0.7, relwidth = 0.2, relheight = 0.1)

        add_blog = tk.Button(frame2, text = "+", bg = '#bee7a5', command = add_blog_page)
        add_blog.place(relx = 0.85, rely = 0.05, relwidth = 0.1, relheight = 0.1)

        frame3 = tk.Frame(root, bg = '#bee7a5')
        frame3.place(relx = 0.72, rely = 0.2, relwidth = 0.17, relheight = 0.75)
        searchfield_Var=tk.StringVar()
        search_field=tk.Entry(frame3, textvariable=searchfield_Var)
        search_field.place(relx=0.17, rely=0.06, relwidth=0.6, relheight=0.078)

def Login(username, password):
    with open('logininfo.txt', "r") as f:
        for line in f.read().splitlines():
            if line.split()[0] == username:
                if line.split()[1] == password:
                    return True
                else:
                    return False
            else:
                continue
    return None

username_list = []
with open("logininfo.txt", "r") as f:
    for x in f.read().splitlines():
        line = x.split()
        if line[4] != '0': 
            username_list.append(line[0])
        else:
            continue

today = datetime.today().strftime("%d/%m/%Y")
root=tk.Tk()

def Home_page():
    HEIGHT=500
    WIDTH=800

    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
    canvas.pack()

    bg = Image.open('bgbgbg.png')
    bg = ImageTk.PhotoImage(bg)
    bg_label = tk.Label(image = bg)
    bg_label.image = bg
    bg_label.place(relwidth = 1, relheight = 1)

    frame = tk.Frame(root, bg = '#d9d9d9')
    frame.place(relx = 0.2, rely = 0.2, relwidth = 0.6, relheight = 0.6)
    root.title('ReEarth')

    welcome = tk.Label(frame, text = "LOGIN")
    welcome.place(relx = 0.1, rely = 0.05, relwidth = 0.8, relheight = 0.1)

    username_field = tk.StringVar()
    password_field = tk.StringVar()

    username_info = tk.Label(frame, text = "Enter username", bg = '#d9d9d9')
    username_info.place(relx = 0.2, rely = 0.3, relwidth = 0.2, relheight = 0.1)

    mem_username = tk.Entry(frame, text = "Enter username", textvariable = username_field)
    mem_username.place(relx = 0.4, rely = 0.3, relwidth = 0.4, relheight = 0.1)

    password_info = tk.Label(frame, text = "Enter password", bg = '#d9d9d9')
    password_info.place(relx = 0.2, rely = 0.5, relwidth = 0.2, relheight = 0.1)

    mem_password = tk.Entry(frame, text = "Enter password", show="*", textvariable = password_field)
    mem_password.place(relx = 0.4, rely = 0.5, relwidth = 0.4, relheight = 0.1)

    def home_submit():
        global memberun,memberpass
        memberun=username_field.get()
        memberpass=password_field.get()
        logged_in = Login(memberun, memberpass)
        print("logged in")
        if logged_in:
            print("hello")
            blog_page()
        elif logged_in is None: 
            username_field.set("") 
            password_field.set("")
            error_msg = tk.Label(frame, text = "You have entered an invalid username. Please try again.", fg="red", bg = '#d9d9d9')
            error_msg.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.1)
        elif not logged_in: 
            password_field.set("") 
            error_msg = tk.Label(frame, text = "You have entered the incorrect password. Please try again.", fg="red", bg = '#d9d9d9')
            error_msg.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.1)
    mem_login_button = tk.Button(frame, text = "Login", command=home_submit)
    mem_login_button.place(relx = 0.5, rely = 0.7, relwidth = 0.3, relheight = 0.1)

    def sign_up():
        signup_frame=tk.Frame(root, bg= '#d9d9d9')
        signup_frame.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.6)

        signup_info = tk.Label(signup_frame, text = "Sign Up", bg = '#d9d9d9')
        signup_info.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.1)

        signupname=tk.Label(signup_frame, text="Enter Name: ",bg = '#d9d9d9')
        signupname.place(relx = 0.25, rely = 0.2, relwidth = 0.2, relheight = 0.05)
        
        name_var=tk.StringVar()
        
        signupname_field = tk.Entry(signup_frame, textvariable = name_var)
        signupname_field.place(relx = 0.45, rely = 0.2, relwidth = 0.3, relheight= 0.05)

        signup_un=tk.Label(signup_frame, text="Enter Username: ",bg = '#d9d9d9')
        signup_un.place(relx = 0.25, rely = 0.3, relwidth = 0.2, relheight = 0.05)
        
        un_var=tk.StringVar()
        
        signupun_field = tk.Entry(signup_frame, textvariable = un_var)
        signupun_field.place(relx = 0.45, rely = 0.3, relwidth = 0.3, relheight= 0.05)

        signup_pass=tk.Label(signup_frame, text="Enter Password: ",bg = '#d9d9d9')
        signup_pass.place(relx = 0.25, rely = 0.4, relwidth = 0.2, relheight = 0.05)
        
        pass_var=tk.StringVar()

        signuppass_field = tk.Entry(signup_frame, textvariable = pass_var)
        signuppass_field.place(relx = 0.45, rely = 0.4, relwidth = 0.3, relheight= 0.05)

        signup_email=tk.Label(signup_frame, text="Enter Email: ",bg = '#d9d9d9')
        signup_email.place(relx = 0.25, rely = 0.5, relwidth = 0.2, relheight = 0.05)
        
        email_var=tk.StringVar()
        
        signupemail_field = tk.Entry(signup_frame, textvariable = email_var)
        signupemail_field.place(relx = 0.45, rely = 0.5, relwidth = 0.3, relheight= 0.05)

        def signupsubmit():
            newpassget=pass_var.get()
            if len(newpassget)<6:
                messagebox.showerror('Try Again','Password should be more than 6 characters!')
                pass_var.set('')
            else:
                try:
                    OTPSent = random.randint(100000,1000000)
                    print(OTPSent)
                    contents="Greetings!\nYour verification number is: "+str(OTPSent)+"\nThank you,\nRe-Earth"
                    yagmail.SMTP('re.earth44@gmail.com','mzolbbyaxmmbueaj').send('Nikshitha.ram@gmail.com','ACCOUNT VERIFICATION', contents)
                    OTP=tk.Tk()
                    HEIGHT=50
                    WIDTH=70
                    canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
                    canvas.pack()
                    otp_label = tk.Label(OTP, text = "Enter OTP")
                    otp_label.place(relx = 0.3, rely = 0.1, relwidth = 0.4, relheight = 0.1) 
                    OTP_var=tk.StringVar()
                    #bee7a5
                    otp_entry = tk.Entry(OTP, textvariable=OTP_var)
                    otp_entry.place(relx = 0.1, rely = 0.2, relwidth = 0.8, relheight = 0.1)

                    global OTPEntered
                    OTPEntered=OTP_var.get()
                    def otpverif():
                        print(OTPEntered,OTPSent)
                        if OTP_var.get().lstrip()==OTPSent:
                            #appendvalues
                            addvalue=un_var.get()+' '+pass_var+' '+email_var+' '+name_var+'\n'
                            loginfile=open('logininfo','a')
                            loginfile.write(addvalue)
                            #create blog files
                            filecreatename=un_var.get()+'_blogging.txt'
                            createfile=open(filecreatename,'w')
                            createfile.close()
                    
                    otp_submitbutton=tk.Button(OTP, text="Submit", command=otpverif)
                    otp_submitbutton.place(relx=0.3,rely=0.35,relwidth=0.4,relheight=0.1)

                except:
                    messagebox.showerror('Try Again','Enter valid Email id!!')

        
        signup_submit = tk.Button(signup_frame, text = "Confirm", command=signupsubmit)
        signup_submit.place(relx = 0.35, rely = 0.6, relwidth = 0.3, relheight = 0.1)

    signup_button = tk.Button(frame, text = "Sign Up",command=sign_up)
    signup_button.place(relx = 0.15, rely = 0.7, relwidth = 0.3, relheight = 0.1)

    
Home_page()
