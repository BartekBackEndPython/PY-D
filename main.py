from tkinter import *
import menu_bar_options
from highlight import highlight
from colors import *

window = Tk()
window.geometry("1200x800")
window.title("BarPek IDE")
window.configure(background=BG_COLOR)
window.resizable(False, False)

IDE_text = Text(window, background=TEXT_EDITOR_COLOR, foreground="#AAAAAA", height=45, width=140, insertbackground=CURSOR_COLOR, tabs=16)
IDE_text.place(relx=0.5, rely=0.01, anchor=N)

highlight(IDE_text=IDE_text)


def init_menu_bar():
    menu_bar = Menu(window, background=MENU_BAR_COLOR)
    window.config(menu=menu_bar)
    file_menu = Menu(menu_bar, tearoff=False)

    menu_bar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Open Python file", command=lambda: menu_bar_options.open_file(IDE_text))
    file_menu.add_command(label="Save Python file", command=lambda: menu_bar_options.save_file(IDE_text, window=window))
    file_menu.add_command(label="Configure Python interpreter", command=menu_bar_options.configure_interpreter)
    file_menu.add_command(label="Run Python File", command=menu_bar_options.run_python_file)


init_menu_bar()


window.mainloop()
