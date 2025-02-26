import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Minimal Selection Test")

chat_display = scrolledtext.ScrolledText(root, wrap="word", bg="#1e1e1e", fg="#e0e0e0", font=("Arial", 12))
chat_display.pack(fill="both", expand=True, padx=10, pady=10)

chat_display.config(
    insertbackground="#e0e0e0",
    selectbackground="red",      # Extreme color for testing
    selectforeground="white",
    inactiveselectbackground="red"
)

chat_display.insert("end", "This is some sample text.\nSelect text by dragging your mouse.\nYou should see a red highlight as you select.\nMore text here to test longer selections.")

root.mainloop()