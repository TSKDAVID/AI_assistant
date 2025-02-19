import tkinter as tk
from tkinter import scrolledtext
from assistant import chat_with_ai
# Colors
chat = chat_with_ai
BG_COLOR = "#2c3e50"  # Background color (dark blue-gray)
TEXT_COLOR = "#ecf0f1"  # Light text
HEADER_COLOR = "#34495e"  # Header background
BTN_COLOR = "#1abc9c"  # Button color
CHAT_LIST_COLOR = "#22313f"  # Left panel color
USER_MSG_COLOR = "#2980b9"  # User message background
AI_MSG_COLOR = "#27ae60"  # AI message background

# Create main window
root = tk.Tk()
root.title("Assistant")
root.geometry("600x600")
root.configure(bg=BG_COLOR)

# Create a header frame
header = tk.Frame(root, bg=HEADER_COLOR, height=50)
header.pack(fill="x")

# Title label
title_label = tk.Label(header, text="Assistant", fg=TEXT_COLOR, bg=HEADER_COLOR, font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# **LEFT PANEL - CHAT LIST**
chat_list_frame = tk.Frame(root, bg=CHAT_LIST_COLOR, width=150)
chat_list_frame.pack(side="left", fill="y")

# Add a label inside chat list
chat_list_label = tk.Label(chat_list_frame, text="Chats", fg=TEXT_COLOR, bg=CHAT_LIST_COLOR, font=("Arial", 12, "bold"))
chat_list_label.pack(pady=10)

# **RIGHT PANEL - CHAT DISPLAY + INPUT FIELD**
chat_area_frame = tk.Frame(root, bg=BG_COLOR)
chat_area_frame.pack(side="right", fill="both", expand=True)

# **SCROLLABLE CHAT DISPLAY**
chat_display = scrolledtext.ScrolledText(chat_area_frame, wrap="word", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
chat_display.pack(fill="both", expand=True, padx=10, pady=10)
chat_display.config(state="disabled")  # Disable editing

# **INPUT FIELD + SEND BUTTON**
input_frame = tk.Frame(chat_area_frame, bg=BG_COLOR)
input_frame.pack(side="bottom", fill="x", padx=10, pady=10)

user_input = tk.Entry(input_frame, bg="#ffffff", font=("Arial", 12))
user_input.pack(side="left", fill="x", expand=True, padx=5)
user_input.bind("<Return>", lambda event: send_message())  # Press Enter to send

send_button = tk.Button(input_frame, text="Send", bg=BTN_COLOR, fg="white", font=("Arial", 12), command=lambda: send_message())
send_button.pack(side="right")


# **Function to Display User Messages**
def send_message():
    message = user_input.get().strip()
    if message:
        # Display user message
        display_user_message(message)
         # Extracts the actual string text
        # Clear input field
        user_input.delete(0, tk.END)
        ai_response = chat_with_ai(message)
       



        display_ai_message(ai_response)

        # Scroll to the bottom
        chat_display.yview("end")


# **Function to Display AI Messages**
def display_ai_message(message):
    chat_display.config(state="normal")  # Enable editing
    chat_display.insert("end", f"AI: {message}\n", "ai")  # AI message
    chat_display.config(state="disabled")  # Disable editing


# **Function to Display User Messages with Styling**
def display_user_message(message):
    chat_display.config(state="normal")  # Enable editing
    chat_display.insert("end", f"You: {message}\n", "user")  # User message
    chat_display.config(state="disabled")  # Disable editing


# Add Text Styles
chat_display.tag_configure("user", foreground="white", background=USER_MSG_COLOR, font=("Arial", 12, "bold"))
chat_display.tag_configure("ai", foreground="black", background=AI_MSG_COLOR, font=("Arial", 12, "bold"))  # AI message styling

# Run the application
root.mainloop()
