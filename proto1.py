import tkinter as tk
from tkinter import font
import pywhatkit as kit


def send_message():
    recipient_name = name.get()
    recipient_phone_number = phone_number.get()
    message_subject = subject.get()

    message = f"Hello {recipient_name}! This is a reminder about the {message_subject} SAC coming up. We wish you best of luck and we believe you'll pass."

    kit.sendwhatmsg_instantly(recipient_phone_number, message)

    print("Message sent!")


def on_entry_click(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.config(fg="black")  # Change text color to black


def on_focus_out(event, entry, placeholder_text):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg="grey")  # Change text color back to grey


window = tk.Tk()
window.title('TMMRSRST')
label_font = font.Font(weight="bold")
button_font = font.Font(size=18)

label1 = tk.Label(text='The Motivational Messenger and Reminder Sender in Relation to School Tests', font=label_font,
                  bg='#D5F0FF', width=13, height=7, wraplength=150)
label1.grid(row=0, column=0, rowspan=3, padx=(10, 0), pady=(10, 0))

name = tk.Entry(fg="grey")
name.insert(0, "name")
name.bind("<FocusIn>", lambda event: on_entry_click(event, name, "name"))
name.bind("<FocusOut>", lambda event: on_focus_out(event, name, "name"))
name.grid(row=0, column=1, padx=(10, 10))

phone_number = tk.Entry(fg="grey")
phone_number.insert(0, "phone number")
phone_number.bind("<FocusIn>", lambda event: on_entry_click(event, phone_number, "phone number"))
phone_number.bind("<FocusOut>", lambda event: on_focus_out(event, phone_number, "phone number"))
phone_number.grid(row=1, column=1, padx=(10, 10))

subject = tk.Entry(fg="grey")
subject.insert(0, "subject")
subject.bind("<FocusIn>", lambda event: on_entry_click(event, subject, "subject"))
subject.bind("<FocusOut>", lambda event: on_focus_out(event, subject, "subject"))
subject.grid(row=2, column=1, padx=(10, 10))

button = tk.Button(text='SEND :)', bg='red', command=send_message, width=10, height=1, font=button_font)
button.grid(row=3, column=0, columnspan=3, pady=(10, 10))

window.mainloop()
