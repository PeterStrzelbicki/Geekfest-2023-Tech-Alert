"""
This file will contain the code for the Chat UI.
Currently also handles the receiving of messages
from the user and handling the response returned
by the Chat Logic    
"""
from tkinter import *
import os

# set constants for background and text colors
LABEL_COLOUR = "#264794"
BG_COLOUR = "#FFFFFF"
TEXT_COLOUR = "#000000"
LABEL_TEXT_COLOUR = "#FFFFFF"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self.msg_entry = None  # Initialize msg_entry here
        self._setup_window()
    
    def run(self):
        self.window.mainloop()  
    
    def _setup_window(self):
        self.window.title("Chat Window")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=450, height=550, bg=BG_COLOUR)
        
        # head label
        head_label = Label(self.window, bg=LABEL_COLOUR, fg=LABEL_TEXT_COLOUR,
                           text="I'm Here to Help!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # divider
        line = Label(self.window, width=450, bg=LABEL_COLOUR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOUR, fg=TEXT_COLOUR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=LABEL_COLOUR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # Check if a termination message exists in the file
        if os.path.exists("log.txt"):
            with open("log.txt", "r") as file:
                termination_message = file.read()
            self._insert_message(termination_message, "Bot")
            os.remove("log.txt")
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#FFFFFF", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=LABEL_COLOUR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
    
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        if self.msg_entry:
            self.msg_entry.delete(0, END)
        
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
