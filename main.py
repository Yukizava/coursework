from customtkinter import *
from tkinter import messagebox
import tkinter
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import method


window = CTk()
window.title("Эвристический алгоритм построения КСД")
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
    if e.widget.get() == '':
        messagebox.showerror("Ошибка", "Пустое поле")
        pass
    else:
        global rc
        rc = int(e.widget.get())
        rows, cols = (rc, rc)
        if rc <= 0:
            messagebox.showerror("Ошибка", "Количество вершин меньше или равно нулю")
        else:
            for i in range(rows):
                text_var.append([])
                entries.append([])
                for j in range(cols):
                    text_var[i].append(StringVar())
                    entries[i].append(CTkEntry(window, textvariable=text_var[i][j], width=30))
                    entries[i][j].place(x=120 + x2, y=80 + y2)
                    x2 += 32
                    x_save += 32
                y2 += 30
                x2 = 0
            button2.place(x=120, y=82 + y2)


def get_mat():
    rows, cols = (rc, rc)
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            if str(text_var[i][j].get()) == '':
                messagebox.showerror("Ошибка", "Пустая ячейка")
                break
            else:
                if int(text_var[i][j].get()) < 0:
                    messagebox.showerror("Ошибка", "Значение не может быть отрицательной")
                else:
                    matrix[i].append(int(text_var[i][j].get()))
    return matrix


def work():
    result, sum = method.heuristic_algorithm(get_mat())
    textbox_result.insert("0.0", f"Результат работы алгоритма:\nПостроенное КСД: {result}\nСуммарная длина ребер равна: {sum}\n")
    fig, ax = plt.subplots()
    G = nx.Graph()
    G.add_edges_from(result)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color="#1f6aa5", font_color="white", edge_color="white")
    ax.set_facecolor("#1d1e1e")
    fig.set_facecolor("#242424")
    plt.show()


def click_button_clear():
    textbox_result.delete("1.0", tkinter.END)


CTkLabel(window, text="Введите кол-во вершин:").place(x=20, y=30)

entry = CTkEntry(window)
entry.place(x=180, y=30)
entry.bind("<Return>", get_x)

button2 = CTkButton(window, text="Подтвердить", width=40, command=work)

textbox_result = CTkTextbox(window, width=600, height=600, font=font)
textbox_result.place(x=600, y=25)

button3 = CTkButton(window, text="Очистить", command=click_button_clear)
button3.place(x=840, y=650)

window.mainloop()