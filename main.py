from customtkinter import *
import method
window = CTk()
window.title("Курсовая")
window.geometry("650x500+120+120")
window.resizable(True, True)


text_var = []
entries = []
def get_x(e):
    global entries
    for i in entries:
        for j in i:
            j.destroy()
    entries = []
    x2 = 0
    y2 = 0
    x_save = 0
    global rc
    rc = int(e.widget.get())
    print(e.widget.get())
    rows, cols = (rc, rc)
    for i in range(rows):
        text_var.append([])
        entries.append([])
        for j in range(cols):
            text_var[i].append(StringVar())
            entries[i].append(CTkEntry(window, textvariable=text_var[i][j], width=30))
            entries[i][j].place(x=30 + x2, y=60 + y2)
            x2 += 32
            x_save += 32
        y2 += 30
        x2 = 0
    button2.place(x=x_save / 18, y=60 + y2)

def get_mat():
    rows, cols = (rc, rc)
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(int(text_var[i][j].get()))
            print(type(matrix[i][j]))
    print(matrix)


e = CTkEntry(window)
e.place(x=180, y=30)
e.bind("<Return>", get_x)

CTkLabel(window, text="Введите кол-во вершин :").place(x=20, y=30)

button2 = CTkButton(window, text="Подтвердить", width=40, command=get_mat)

window.mainloop()