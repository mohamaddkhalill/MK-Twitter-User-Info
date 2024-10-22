# Software Name: MK Twitter User Info
# Version: 1.0
# Author: Mohamad Khalil
# Year: 2024

import tkinter as tk
from tkinter import ttk
from twikit.guest import GuestClient
from threading import Thread
import asyncio

async def get_user_info(screen_name):
    """
    Retrieves the user information for the given screen name.
    """
    guest_client = GuestClient()
    await guest_client.activate()

    try:
        user = await guest_client.get_user_by_screen_name(screen_name)
        user_info = f"User ID: {user.id}\nName: {user.name}\nScreen Name: {user.screen_name}\n"
        user_info += f"Location: {user.location if user.location else 'Not available'}\n"
        user_info += f"Description: {user.description}\nFollowers Count: {user.followers_count}\n"
        user_info += f"Following Count: {getattr(user, 'friends_count', 'Not available')}\n"
        user_info += f"Account Creation Date: {getattr(user, 'created_at', 'Not available')}\n"

        return user_info

    except Exception as e:
        return f"Error: {str(e)}. Please check the username."

def run_in_thread(func, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(func(*args))

def start_process(screen_name, progress_label, progress_bar, memo_box):
    progress_label.config(text="Starting the process...")
    progress_bar['value'] = 10
    progress_bar.update()

    user_info = run_in_thread(get_user_info, screen_name)
    
    progress_label.config(text="Fetching user info completed.")
    progress_bar['value'] = 100
    progress_bar.update()

    memo_box.delete(1.0, tk.END)
    memo_box.insert(tk.END, user_info)

root = tk.Tk()
root.title("MK Twitter User Info")

font_family = ("Arial", 12) 

label_screen_name = tk.Label(root, text="User Name:", font=font_family)
label_screen_name.grid(row=0, column=0, padx=10, pady=5)
entry_screen_name = tk.Entry(root, width=30, font=font_family)
entry_screen_name.grid(row=0, column=1, padx=10, pady=5)

progress_label = tk.Label(root, text="Welcome", font=font_family)
progress_label.grid(row=1, column=0, columnspan=2, pady=10)
progress_bar = ttk.Progressbar(root, length=300, mode='determinate')
progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

memo_box = tk.Text(root, height=10, width=50, font=font_family, wrap=tk.WORD)
memo_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

memo_box.tag_configure("right", justify="right")

start_button = tk.Button(root, text="Start", font=font_family, command=lambda: Thread(target=start_process, args=(entry_screen_name.get(), progress_label, progress_bar, memo_box)).start())
start_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
