import tkinter as tk

clicks = 0
def count_clicks():
    global clicks
    clicks += 1
    label_count.config(text=f"Нажатий:{clicks}")
    if clicks > 10:
        root.config(bg="#d4edda")
        label_count.config(bg="#d4edda", fg="#155724")
root = tk.Tk()
root.title('Кликер')
root.geometry("350x250")

label_count = tk.Label(root, text="Нажатий: 0", font=("Arial", 16))
label_count.pack(pady=30)

btn_click = tk.Button(root, text="Кликни меня!", font=("Arial", 14), command=count_clicks, bg="#007bff", fg="white")
btn_click.pack(pady=20)


root.mainloop()