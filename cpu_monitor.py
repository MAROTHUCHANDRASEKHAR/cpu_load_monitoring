import tkinter as tk
from tkinter import ttk
import psutil

def update_cpu_usage():
    usage = psutil.cpu_percent(interval=0.1)
    progress['value'] = usage
    label.config(text=f"CPU Usage: {usage}%")
    root.after(1000, update_cpu_usage)

root = tk.Tk()
root.title("CPU Load Monitor")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="CPU Usage: 0%", font=("Helvetica", 14))
label.pack(pady=10)

progress = ttk.Progressbar(root, orient='horizontal', length=250, mode='determinate')
progress.pack(pady=10)

update_cpu_usage()
root.mainloop()
