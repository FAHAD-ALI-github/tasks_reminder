import pandas as pd
from datetime import datetime
import time
import threading
import webbrowser
from plyer import notification
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Load Excel once
EXCEL_FILE = "weekend_plan.xlsx"
df = pd.read_excel(EXCEL_FILE)

running = False  # control flag for reminder loop

def check_tasks():
    global running
    while running:
        now = datetime.now()
        current_day = now.strftime("%A")    
        current_time = now.strftime("%H:%M")  

        today_tasks = df[df["Day"].str.lower() == current_day.lower()]

        for _, task in today_tasks.iterrows():
            task_time = str(task["Time Slot"]).strip()
            if task_time == current_time:
                title = f"📚 {task['Subject / Task']}"
                message = f"{task['Duration']} | {task['Type']}"
                
                # Send notification
                notification.notify(
                    title=title,
                    message=message + f"\n🔗 {task['Resource']}",
                    timeout=15
                )

                # Auto-open link if available
                if isinstance(task["Resource"], str) and task["Resource"].startswith("http"):
                    webbrowser.open(task["Resource"])

        time.sleep(60)  # check every 1 minute


def start_reminders():
    global running
    if not running:
        running = True
        threading.Thread(target=check_tasks, daemon=True).start()
        messagebox.showinfo("Reminder", "✅ Task reminders started!")
    else:
        messagebox.showinfo("Reminder", "Already running!")


def stop_reminders():
    global running
    running = False
    messagebox.showinfo("Reminder", "⏸ Task reminders stopped.")


def show_today_tasks():
    now = datetime.now()
    current_day = now.strftime("%A")
    today_tasks = df[df["Day"].str.lower() == current_day.lower()]

    if today_tasks.empty:
        messagebox.showinfo("Today’s Tasks", "🎉 No tasks scheduled for today!")
        return

    tasks_text = ""
    for _, task in today_tasks.iterrows():
        tasks_text += f"⏰ {task['Time Slot']} – {task['Subject / Task']} ({task['Duration']})\n"
        tasks_text += f"   🔗 {task['Resource']}\n\n"

    # Scrollable popup
    task_win = tk.Toplevel(root)
    task_win.title(f"Tasks for {current_day}")
    task_win.geometry("500x400")

    text_area = scrolledtext.ScrolledText(task_win, wrap=tk.WORD, font=("Segoe UI", 10))
    text_area.pack(expand=True, fill='both')
    text_area.insert(tk.END, tasks_text)
    text_area.config(state=tk.DISABLED)


# GUI Setup
root = tk.Tk()
root.title("📌 Study Reminder App")
root.geometry("300x200")

lbl = tk.Label(root, text="Weekend Study Reminder", font=("Segoe UI", 12, "bold"))
lbl.pack(pady=10)

btn_start = tk.Button(root, text="▶ Start Reminders", command=start_reminders, bg="green", fg="white")
btn_start.pack(pady=5)

btn_stop = tk.Button(root, text="⏸ Stop Reminders", command=stop_reminders, bg="red", fg="white")
btn_stop.pack(pady=5)

btn_show = tk.Button(root, text="📅 Show Today’s Tasks", command=show_today_tasks, bg="blue", fg="white")
btn_show.pack(pady=5)

btn_exit = tk.Button(root, text="❌ Exit", command=root.quit, bg="gray", fg="white")
btn_exit.pack(pady=5)

root.mainloop()
