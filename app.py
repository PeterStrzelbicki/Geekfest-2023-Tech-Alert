"""
This file will contain the code for the Chat UI.
Currently also handles the receiving of messages
from the user and handling the response returned
by the Chat Logic    
"""
from tkinter import *

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
        self.window.configure(width=500, height=300, bg=BG_COLOUR)
        
        # head label
        head_label = Label(self.window, bg=LABEL_COLOUR, fg=LABEL_TEXT_COLOUR,
                           text="I'm Here to Help!", font=FONT_BOLD, pady=5)
        head_label.place(relwidth=1)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOUR, fg=TEXT_COLOUR,
                                font=FONT)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        self._insert_message("Suspicious software has been detected. \nA trusted contact has been notified.", "Bot")

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
