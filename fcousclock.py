import tkinter as tk
from tkinter import messagebox
import time

class FocusTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("300x200")

        self.time_remaining = 25 * 60  # 初始时间设置为25分钟，以秒为单位

        self.label = tk.Label(self.master, text=self.format_time(self.time_remaining))
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="开始专注", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="停止专注", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        while self.time_remaining > 0:
            self.label.config(text=self.format_time(self.time_remaining))
            self.master.update()
            time.sleep(1)
            self.time_remaining -= 1
        messagebox.showinfo("提醒", "专注时间结束！")
        self.reset_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_timer()

    def reset_timer(self):
        self.time_remaining = 25 * 60
        self.label.config(text=self.format_time(self.time_remaining))

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()
