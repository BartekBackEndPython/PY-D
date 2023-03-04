from tkinter import *
import subprocess
from os import environ
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mgbox
from colors import *

file = ""
interpreter = ""


def open_file(text_widget):
    opened_file = filedialog.askopenfile(initialdir="C:\\", title="Open Python File", filetypes=(("Python files", "*.py"),
                                                                                               ('PythonW files', "*.pyw")))

    global file
    file = opened_file.name
    text_widget.delete(1.0, END)
    text_widget.insert(1.0, opened_file.read())


def frame_widget_build(frame, widget, win):
    save_entry = Entry(frame, background="#404040", insertbackground="#000000", font=("Bebas", 25))
    save_entry.place(relx=0.5, rely=0.15, anchor=CENTER)

    def save():
        global file
        file = save_entry.get()
        save_file(text_widget=widget, window=win)

    save_button = Button(frame, text="SAVE", font=("Bebas", 20), background=TEXT_EDITOR_COLOR, foreground="#FFFFFF", command=save)
    save_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def destroy_frame():
        frame.destroy()

    exit_frame_button = Button(frame, text="X", font=("Bebas", 20), background="#FF0000", foreground="#FFFFFF", command=destroy_frame)
    exit_frame_button.place(relx=1, rely=0, anchor=NE)


def save_file(text_widget, window):
    if bool(file):
        with open(file, "w") as save_file_:
            save_file_.write(text_widget.get(1.0, END))
    else:
        frame = Frame(window, background=SAVE_FRAME_COLOR, height=300, width=600)
        frame.place(relx=0.5, rely=0.45, anchor=CENTER)
        frame_widget_build(frame, widget=text_widget, win=window)



def configure_interpreter():
    username = environ['USERPROFILE'].split("\\")
    username = username[len(username) - 1]
    print(username)
    interpreter_file = filedialog.askopenfile(initialdir=f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Python", title="Configure Python Interpreter", filetypes=(("Choose Interpreter", "*.exe"), ))

    global interpreter
    interpreter = interpreter_file.name


def run_python_file():
    if not bool(file):
        mgbox.showerror(title="File not configured", message="Please configure a file")
        return
    if not bool(interpreter):
        mgbox.showerror(title="Interpreter not configured", message="Please configure an Interpreter")
        return

    cmd_command = f"""\"\"{interpreter}\" \"{file}\"\""""

    # subprocess.Popen(f'cmd.exe /K {cmd_command}')
    # system(f"{cmd_command})
    subprocess.run(f"start cmd.exe /K {cmd_command}", shell=True)
    print(f"""running: \"\"{interpreter}\" \"{file}\"\"""")
