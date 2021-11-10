import tkinter as tk
import ttkbootstrap as ttk


DARK = 'superhero'
LIGHT = 'flatly'


def create_entry_test(bootstyle, style):
    frame = ttk.Frame(padding=10)

    # title
    title = ttk.Label(frame, text='Entry', anchor=tk.CENTER)
    title.pack(padx=5, pady=2, fill=tk.BOTH)
    ttk.Separator(frame).pack(padx=5, pady=5, fill=tk.X)

    # default
    entry = ttk.Entry(frame, bootstyle=bootstyle)
    entry.pack(padx=5, pady=5, fill=tk.BOTH)
    entry.insert(tk.END, 'default')

    # color
    for color in style.theme.colors:
        entry = ttk.Entry(frame, bootstyle=color)
        entry.pack(padx=5, pady=5, fill=tk.BOTH)
        entry.insert(tk.END, color)

    # disabled
    entry = ttk.Entry(frame, bootstyle=bootstyle)
    entry.insert(tk.END, bootstyle)
    entry.configure(state=tk.DISABLED)
    entry.pack(padx=5, pady=5, fill=tk.BOTH)

    return frame


if __name__ == '__main__':
    # create visual widget style tests
    root = tk.Tk()
    style = ttk.Style(theme=LIGHT)

    test1 = create_entry_test('TEntry', style)
    test1.pack(side=tk.LEFT, fill=tk.BOTH)

    root.mainloop()
