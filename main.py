from customtkinter import *
import tkinter
import method
window = CTk()
window.title("Курсовая")
window.geometry("1280x720+120+120")
window.resizable(True, True)
font = CTkFont(size=24)

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
    return matrix


def work():
    result, sum = method.heuristic_algorithm(get_mat())
    textbox_result.insert("0.0", f"Результат работы алгоритма:\nПостроенное КСД: {result}\nСуммарная длина ребер равна: {sum}")


def click_button_clear():
    textbox_result.delete("1.0", tkinter.END)


CTkLabel(window, text="Введите кол-во вершин :").place(x=20, y=30)

e = CTkEntry(window)
e.place(x=180, y=30)
e.bind("<Return>", get_x)

button2 = CTkButton(window, text="Подтвердить", width=40, command=work)

textbox_result = CTkTextbox(window, width=600, height=600, font=font)
textbox_result.place(x=600, y=25)

button_3 = CTkButton(window, text="Очистить", command=click_button_clear)
button_3.place(x=840, y=650)

window.mainloop()