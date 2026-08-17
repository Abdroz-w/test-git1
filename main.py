import tkinter as tk
from tkinter import font as tkfont

# Палитра: тёмная «космическая» тема с тёплыми акцентами
COLORS = {
    "bg": "#0f0e17",
    "surface": "#1a1929",
    "surface_light": "#252438",
    "accent": "#ff8906",
    "accent_hover": "#ff9f2e",
    "accent_pressed": "#e07a05",
    "text": "#fffffe",
    "text_muted": "#a7a9be",
    "success_bg": "#1b4332",
    "success_surface": "#2d6a4f",
    "success_text": "#95d5b2",
    "progress_track": "#252438",
    "progress_fill": "#ff8906",
    "border": "#3d3a5c",
}

GOAL = 10
clicks = 0


def update_progress():
    progress = min(clicks / GOAL, 1.0)
    fill_width = int(progress_bar_width * progress)
    progress_fill.place(x=0, y=0, width=fill_width, height=8)
    progress_label.config(text=f"{min(clicks, GOAL)} / {GOAL}")


def set_success_theme():
    root.config(bg=COLORS["success_bg"])
    main_frame.config(bg=COLORS["success_surface"], highlightbackground=COLORS["success_text"])
    title_label.config(bg=COLORS["success_surface"], fg=COLORS["success_text"])
    label_count.config(bg=COLORS["success_surface"], fg=COLORS["text"])
    subtitle_label.config(bg=COLORS["success_surface"], fg=COLORS["success_text"])
    progress_track.config(bg=COLORS["success_bg"])
    progress_fill.config(bg=COLORS["success_text"])
    progress_label.config(bg=COLORS["success_surface"], fg=COLORS["success_text"])
    btn_click.config(
        bg=COLORS["success_text"],
        activebackground="#74c69d",
        fg=COLORS["success_bg"],
        activeforeground=COLORS["success_bg"],
    )


def count_clicks():
    global clicks
    clicks += 1
    label_count.config(text=str(clicks))
    update_progress()

    # Лёгкая анимация «пульса» при клике
    label_count.config(fg=COLORS["accent"])
    root.after(120, lambda: label_count.config(fg=COLORS["text"]))

    if clicks >= GOAL and clicks == GOAL:
        set_success_theme()
        subtitle_label.config(text="Цель достигнута! Продолжай кликать 🎉")
    elif clicks > GOAL:
        subtitle_label.config(text=f"Ты уже на {clicks} кликах — молодец!")


def on_enter(_):
    if clicks < GOAL:
        btn_click.config(bg=COLORS["accent_hover"])


def on_leave(_):
    if clicks < GOAL:
        btn_click.config(bg=COLORS["accent"])


root = tk.Tk()
root.title("Кликер")
root.geometry("400x420")
root.resizable(False, False)
root.config(bg=COLORS["bg"])

title_font = tkfont.Font(family="Segoe UI", size=22, weight="bold")
count_font = tkfont.Font(family="Segoe UI", size=48, weight="bold")
body_font = tkfont.Font(family="Segoe UI", size=11)
button_font = tkfont.Font(family="Segoe UI", size=14, weight="bold")

main_frame = tk.Frame(
    root,
    bg=COLORS["surface"],
    highlightbackground=COLORS["border"],
    highlightthickness=1,
    padx=32,
    pady=28,
)
main_frame.pack(expand=True, fill="both", padx=24, pady=24)

title_label = tk.Label(
    main_frame,
    text="Кликер",
    font=title_font,
    bg=COLORS["surface"],
    fg=COLORS["accent"],
)
title_label.pack(pady=(0, 4))

subtitle_label = tk.Label(
    main_frame,
    text=f"Набери {GOAL} кликов, чтобы победить",
    font=body_font,
    bg=COLORS["surface"],
    fg=COLORS["text_muted"],
)
subtitle_label.pack(pady=(0, 24))

label_count = tk.Label(
    main_frame,
    text="0",
    font=count_font,
    bg=COLORS["surface"],
    fg=COLORS["text"],
)
label_count.pack(pady=(0, 8))

progress_label = tk.Label(
    main_frame,
    text=f"0 / {GOAL}",
    font=body_font,
    bg=COLORS["surface"],
    fg=COLORS["text_muted"],
)
progress_label.pack(pady=(0, 6))

progress_bar_width = 280
progress_track = tk.Frame(main_frame, bg=COLORS["progress_track"], width=progress_bar_width, height=8)
progress_track.pack(pady=(0, 28))
progress_track.pack_propagate(False)

progress_fill = tk.Frame(progress_track, bg=COLORS["progress_fill"], height=8)

btn_click = tk.Button(
    main_frame,
    text="Кликни меня!",
    font=button_font,
    command=count_clicks,
    bg=COLORS["accent"],
    fg=COLORS["bg"],
    activebackground=COLORS["accent_pressed"],
    activeforeground=COLORS["bg"],
    relief="flat",
    cursor="hand2",
    padx=28,
    pady=12,
    borderwidth=0,
)
btn_click.pack()
btn_click.bind("<Enter>", on_enter)
btn_click.bind("<Leave>", on_leave)

update_progress()
root.mainloop()