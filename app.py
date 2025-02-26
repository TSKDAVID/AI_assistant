import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from assistant import chat_with_ai

# Colors
BG_COLOR = "#2c3e50"
TEXT_COLOR = "#ecf0f1"
HEADER_COLOR = "#34495e"
BTN_COLOR = "#1abc9c"
CHAT_LIST_COLOR = "#22313f"
USER_MSG_COLOR = "#465366"
AI_MSG_COLOR = "#12396e"

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

# Left panel - chat list
chat_list_frame = tk.Frame(root, bg=CHAT_LIST_COLOR, width=150)
chat_list_frame.pack(side="left", fill="y")

# Add a label inside chat list
chat_list_label = tk.Label(chat_list_frame, text="Chats", fg=TEXT_COLOR, bg=CHAT_LIST_COLOR, font=("Arial", 12, "bold"))
chat_list_label.pack(pady=10)

# Right panel - chat display and input field
chat_area_frame = tk.Frame(root, bg=BG_COLOR)
chat_area_frame.pack(side="right", fill="both", expand=True)

# Scrollable chat display
chat_display = scrolledtext.ScrolledText(chat_area_frame, wrap="word", bg=BG_COLOR, fg=TEXT_COLOR, font=("Arial", 12))
chat_display.pack(fill="both", expand=True, padx=10, pady=10)
chat_display.config(state="disabled")

# Input field and send button
input_frame = tk.Frame(chat_area_frame, bg=BG_COLOR)
input_frame.pack(side="bottom", fill="x", padx=10, pady=10)

user_input = tk.Entry(input_frame, bg="#ffffff", font=("Arial", 12))
user_input.pack(side="left", fill="x", expand=True, padx=5)
user_input.bind("<Return>", lambda event: send_message())

ai_message_started = False

def display_user_message(message):
    chat_display.config(state="normal")
    chat_display.insert("end", f"You: {message}\n", "user")
    chat_display.config(state="disabled")
    chat_display.yview("end")

def display_ai_message(chunk):
    global ai_message_started
    chat_display.config(state="normal")
    if not ai_message_started:
        chat_display.insert("end", "AI: ", "ai")  # Newline BEFORE "AI:"
        ai_message_started = True
    chat_display.insert("end", chunk, "ai")
    chat_display.config(state="disabled")
    chat_display.yview("end")

def update_ui(chunk, is_final_chunk=False):  # Add is_final_chunk flag
    root.after(0, lambda: display_ai_message(chunk))
    if is_final_chunk:  # Add newline only if it's the final chunk
        root.after(0, lambda: chat_display.config(state="normal"))
        root.after(0, lambda: chat_display.insert("end", "\n", "ai"))  # Newline after AI message
        root.after(0, lambda: chat_display.config(state="disabled"))
        root.after(0, lambda: chat_display.yview("end"))
        ai_message_started = False  # Reset for the next AI message

def send_message():
    message = user_input.get().strip()
    if message:
        chat_display.config(state="normal")
        chat_display.config(state="disabled")
        chat_display.yview("end")
        display_user_message(message)
        user_input.delete(0, tk.END)

        def process_thread():
            process_ai_response(message)

        Thread(target=process_thread).start()

def process_ai_response(user_message):
    global ai_message_started
    ai_message_started = False
    chat_with_ai(user_message, update_ui)  # Pass the modified update_ui

send_button = tk.Button(input_frame, text="Send", bg=BTN_COLOR, fg="white", font=("Arial", 12), command=send_message)
send_button.pack(side="right")

# Add text styles
chat_display.tag_configure("user", foreground="white", background=USER_MSG_COLOR, font=("Arial", 12, "bold"))
chat_display.tag_configure("ai", foreground="black", background=AI_MSG_COLOR, font=("Arial", 12, "bold"))

# Run the application
root.mainloop()