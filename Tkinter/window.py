import tkinter as tk


saluti = tk.Label(
    text="Sono una label",
    fg="white",
    bg="black",
    width=10,
    height=10
)

button = tk.Button(
    text="Sono un pulsante cliccami!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

saluti.pack()
button.pack()
window = tk.Tk()
window.mainloop()