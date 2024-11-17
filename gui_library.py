import tkinter as tk
from tkinter import ttk, messagebox
from flow1 import lend_book
from flow2 import send_return_alert
from flow3 import mark_book_returned

# Function to handle the submit button (First section)
def submit():
    name = name_entry.get()
    usn = usn_entry.get()
    book_id = book_id_entry.get()
    email = email_entry.get()

    if not name or not usn or not book_id or not email:
        messagebox.showwarning("Input Error", "Please fill all fields!")
    else:
        lend_book(name, usn, book_id, email)


# Function to handle the cancel button (First section)
def cancel():
    name_entry.delete(0, tk.END)
    usn_entry.delete(0, tk.END)
    book_id_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


# Function to handle the send alert button (Second section)
def send_alert():
    send_return_alert()


# Function to handle the returned button (Third section)
def returned():
    usn = returned_usn_entry.get()
    if not usn:
        messagebox.showwarning("Input Error", "Please enter a USN!")
    else:
        mark_book_returned(usn)


# Function to display only the selected section
def show_section():
    selected = section_var.get()
    section1_frame.pack_forget()
    section2_frame.pack_forget()
    section3_frame.pack_forget()

    if selected == 1:
        section1_frame.pack(pady=20)
    elif selected == 2:
        section2_frame.pack(pady=20)
    elif selected == 3:
        section3_frame.pack(pady=20)


# Create the main window
root = tk.Tk()
root.title("Library Management System")

# Create radio buttons to select sections
section_var = tk.IntVar(value=1)  # Set default section to 1

radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

radio1 = tk.Radiobutton(radio_frame, text="Section 1", variable=section_var, value=1, command=show_section)
radio1.grid(row=0, column=0, padx=10)
radio2 = tk.Radiobutton(radio_frame, text="Section 2", variable=section_var, value=2, command=show_section)
radio2.grid(row=0, column=1, padx=10)
radio3 = tk.Radiobutton(radio_frame, text="Section 3", variable=section_var, value=3, command=show_section)
radio3.grid(row=0, column=2, padx=10)

# Section 1: Accept Name, USN, Book ID, Email
section1_frame = tk.Frame(root)

name_label = tk.Label(section1_frame, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(section1_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

usn_label = tk.Label(section1_frame, text="USN")
usn_label.grid(row=1, column=0, padx=10, pady=5)
usn_entry = tk.Entry(section1_frame)
usn_entry.grid(row=1, column=1, padx=10, pady=5)

book_id_label = tk.Label(section1_frame, text="Book ID")
book_id_label.grid(row=2, column=0, padx=10, pady=5)
book_id_entry = tk.Entry(section1_frame)
book_id_entry.grid(row=2, column=1, padx=10, pady=5)

email_label = tk.Label(section1_frame, text="Email")
email_label.grid(row=3, column=0, padx=10, pady=5)
email_entry = tk.Entry(section1_frame)
email_entry.grid(row=3, column=1, padx=10, pady=5)

submit_button = tk.Button(section1_frame, text="Submit", command=submit)
submit_button.grid(row=4, column=0, padx=10, pady=5)

cancel_button = tk.Button(section1_frame, text="Cancel", command=cancel)
cancel_button.grid(row=4, column=1, padx=10, pady=5)

# Section 2: Send Alert
section2_frame = tk.Frame(root)

send_alert_button = tk.Button(section2_frame, text="Send Alert", command=send_alert)
send_alert_button.pack(pady=10)

# Section 3: Accept USN and Returned Book
section3_frame = tk.Frame(root)

returned_usn_label = tk.Label(section3_frame, text="Enter USN")
returned_usn_label.pack(padx=10, pady=5)

returned_usn_entry = tk.Entry(section3_frame)
returned_usn_entry.pack(padx=10, pady=5)

returned_button = tk.Button(section3_frame, text="Returned", command=returned)
returned_button.pack(pady=10)

# Initially display the first section
show_section()

# Start the Tkinter event loop
root.mainloop()
