from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #



def generate_password():
    letter =['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    number =['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Choose the password!")

    nr_letter =random.randint(8,10)
    nr_number = random.randint(2,4)
    nr_symbols=random.randint(2,4)

    # password = []

    password_letters = [random.choice(letter) for _ in range(nr_letter)]

    password_numbers = [random.choice(number) for _ in range(nr_number)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols +password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # Insert password into the password entry field
    password_entry.insert(0,password)
    pyperclip.paste(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()

    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:{
         "email":email,
         "password":password,
    }
                
                }
# Check if any fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have't left any fields empty.")

    else:

        try:
            with open("data.json","r") as data_file:
                 #reading old data
                 data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)
        else:
                 #updating old data with new data
            data.update(new_data)

            with open("data.json" , "w") as data_file:
                json.dump(data,data_file,indent=4)
                 # Clear website and password entries after saving

        finally:
                # data_file.write(f"{website} | {email} | {password}")
                website_entry.delete(0, END) # to clear website entry
                password_entry.delete(0, END) # to clear password entry

    
# --------------------------FIND PASSWORD --------------------------- #
def find_password():
    # Get the website name from the entry field
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
             # If file or data not found, show error message
    except json.JSONDecodeError:
            messagebox.showinfo(title="Error",message="No data File Found. ")
             # Check if website exists in data
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email : {email}\nPassword: {password}")
        else:
             messagebox.showinfo(title="Error",message=f"No details for {website} exists. ")

     

# ---------------------------- UI SETUP ------------------------------- #
# Initialize main window

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)
# Set up canvas for logo
canvas = Canvas(width=200, height =200 )

logo_img = PhotoImage(file="/Users/aamirsaifi965479gmail.com/Downloads/password-manager-start/logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column=1,row=0)

#labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1,sticky="w")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2,sticky="w")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3,sticky="w")

#button layout

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=37,command = save)
add_button.grid(column=1, row=4,columnspan=2)

#search button
search_button = Button(text="Search",width=13, command=find_password )
search_button.grid(column=2,row=1)

#entry

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus() # courser blink on website entry

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0, "aamir@gmail.com") # insert text at given index

password_entry= Entry(width=21)
password_entry.grid(column=1, row=3)



# Run the main application loop

window.mainloop()

