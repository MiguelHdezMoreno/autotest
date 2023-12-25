import psutil
import threading
import tkinter as tk
import time

# Function to monitor CPU usage
def monitor_cpu():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_label.config(text=f"CPU Usage: {cpu_percent}%")
        cpu_label.update()
        time.sleep(0.5)

# Function to monitor memory usage
def monitor_memory():
    while True:
        memory = psutil.virtual_memory()
        memory_label.config(text=f"Memory Usage: {memory.percent}%")
        memory_label.update()
        time.sleep(0.5)

# Function to monitor disk usage
def monitor_disk():
    while True:
        disk = psutil.disk_usage('/')
        disk_label.config(text=f"Disk Usage: {disk.percent}%")
        disk_label.update()
        time.sleep(0.5)
def monitor_disk():
    while True:
        disk = psutil.disk_usage('/')
        disk_label.config(text=f"Disk Usage: {disk.percent}%")
        disk_label.update()

# Create the GUI window
window = tk.Tk()
window.title("System Monitor")

# Set the window size
window.geometry("400x300")

# Create labels to display usage information
cpu_label = tk.Label(window, text="CPU Usage: ")
memory_label = tk.Label(window, text="Memory Usage: ")
disk_label = tk.Label(window, text="Disk Usage: ")

# Use grid layout manager to center the labels
cpu_label.grid(row=0, column=0, pady=10, sticky="nsew")
memory_label.grid(row=1, column=0, pady=10, sticky="nsew")
disk_label.grid(row=2, column=0, pady=10, sticky="nsew")

# Create and start the monitoring threads
cpu_thread = threading.Thread(target=monitor_cpu)
memory_thread = threading.Thread(target=monitor_memory)
disk_thread = threading.Thread(target=monitor_disk)

cpu_thread.start()
memory_thread.start()
disk_thread.start()

# Start the GUI event loop
window.mainloop()