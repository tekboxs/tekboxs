import pickle
import tkinter as tk
from tkinter import ttk
import keyboard as key
import time




x, y, k, j, cont = 0, 0, 0, 0, 0
xd, yd = 0, 0
l = True
vezes = 1
btnum, colorv, btentry = [], [], []
fundo = ['green', 'yellow', 'red']

off = []
trans = []
on = []
obs = []


def color(identfy):
    identfy = int(identfy) - 1
    curcolor = btnum[identfy]["bg"]

    if curcolor == 'green':
        btnum[identfy]['bg'] = fundo[1]
        identfy += 1
        on.remove(identfy)
        off.append(identfy)

    elif curcolor == 'yellow':
        btnum[identfy]['bg'] = fundo[2]
        identfy += 1
        off.remove(identfy)
        trans.append(identfy)

    elif curcolor == 'red':
        btnum[identfy]['bg'] = fundo[0]
        identfy += 1
        trans.remove(identfy)
        on.append(identfy)


def use(state):
    on.sort(), off.sort(), trans.sort()
    global vezes
    if state == 1:
        lbstate['text'] = "Modo NÃO lançado"
        window.update()
        time.sleep(1.5)
        window.lower()
    elif state == 2:
        lbstate['text'] = "Modo JÁ lançado"
        window.update()
        time.sleep(1.5)
        window.lower()

    key.wait('f2')
    if state == 1:
        for online in range(0, 2):
            key.press_and_release('tab')
    elif state == 2:
        key.press_and_release('tab')
    while l:
        if key.is_pressed('shift'):
            break
        if vezes in off:
            key.press_and_release('tab')  # entrou na bolinha

            key.press_and_release('right')

            key.press_and_release('tab')  # entrou na obs

            if btentry[vezes - 1].get() != '':
                time.sleep(0.5)
                key.press_and_release('enter')
                time.sleep(0.5)
                key.write(btentry[vezes - 1].get())
                time.sleep(0.5)
            key.press_and_release('tab')
            if state == 2:
                key.press_and_release('tab')

            vezes += 1

        elif vezes in on:
            key.press_and_release('tab')  # entrou na bolinha

            key.press_and_release('right')

            key.press_and_release('right')

            key.press_and_release('tab')

            if btentry[vezes - 1].get() != '':
                time.sleep(0.5)
                key.press_and_release('enter')
                time.sleep(0.5)
                key.write(btentry[vezes - 1].get())
                time.sleep(0.5)

            key.press_and_release('tab')
            if state == 2:
                key.press_and_release('tab')
            vezes += 1

        elif vezes in trans:
            if state == 2:
                key.press_and_release('tab')
                key.press_and_release('tab')
                if btentry[vezes - 1].get() != '':
                    time.sleep(0.5)
                    key.press_and_release('enter')
                    time.sleep(0.5)
                    key.write(btentry[vezes - 1].get())
                    time.sleep(0.5)
                key.press_and_release('tab')
                key.press_and_release('tab')
            vezes += 1
        if vezes == alunos + 1:
            vezes = 1
            window.update()
            window.deiconify()
            window.attributes("-topmost")
            break


def load(state):
    global off, on, eva, trans, obs, btnum, btentry
    del off[:], on[:], trans[:], obs[:]
    idsala = combo_turmas.get()
    try:
        file = open(f'data{idsala}.pkl', 'rb')
        on = pickle.load(file)
        off = pickle.load(file)
        trans = pickle.load(file)
        obs = pickle.load(file)
        file.close()
    except FileNotFoundError:
        save(True)

    if state:
        Editwin(True)
    else:
        Editwin(False)

    for cor_bt in range(1, alunos + 1):
        if btnum[cor_bt - 1]["text"] in on:
            btnum[cor_bt - 1]["bg"] = fundo[0]
        elif btnum[cor_bt - 1]["text"] in off:
            btnum[cor_bt - 1]["bg"] = fundo[1]
        elif btnum[cor_bt - 1]["text"] in trans:
            btnum[cor_bt - 1]["bg"] = fundo[2]

    for entry_bt in range(0, alunos):
        try:
            btentry[entry_bt].insert(string=f'{obs[entry_bt]}', index=2)
        except IndexError:
            pass


def save(new):
    global obs
    if not new:
        del obs[:]
        idsala = combo_turmas.get()
        infoVet = open(f'data{idsala}.pkl', 'wb')
        pickle.dump(on, infoVet)
        pickle.dump(off, infoVet)
        pickle.dump(trans, infoVet)

        for ver in range(0, alunos):
            obs.append(btentry[ver].get())

        pickle.dump(obs, infoVet)
        infoVet.close()
    else:
        idsala = combo_turmas.get()
        infoVet = open(f'data{idsala}.pkl', 'wb')
        infoVet.close()
        del off[:], trans[:], obs[:], on[:]
        for reset in range(1, alunos + 1):
            on.append(reset)


def Editwin(visible):
    global btnum, btentry
    window2 = tk.Toplevel(window)
    window2.title('Editar estado')
    master = window2
    frame = tk.Frame(master)

    if not visible:
        window2.withdraw()

    ka, ja = 0, 0
    del btnum[:], btentry[:]  # tratamento para erro de invalid creating

    for xal in range(1, alunos + 1):
        btnum.append(tk.Button(master, text=xal, width=9, height=1, font='arialblack', bg='green'))
        btnum[xal - 1]['command'] = lambda arg=f"{xal}": color(arg)
        btnum[xal - 1].grid(row=ja, column=ka, padx=5, pady=5)
        ja += 2
        btentry.append(tk.Entry(master, width=14))
        btentry[xal - 1].grid(row=ja - 1, column=ka)
        btentry[xal - 1].insert(string='', index=2)

        if ja % 9 == 0:
            ka += 1
            ja = 0

    save_bt = tk.Button(master, text='Salvar', bg='orange', width=13)
    save_bt['command'] = lambda arg=False: save(arg)
    save_bt.grid(row=ja, column=ka)
    frame.grid()


window = tk.Tk()
window.attributes('-topmost', True)  # overlay
window.title('Lojotron3.0')
turmas = ['1-a', '1-b', '1-c', '1-d', '1-e', '2-a', '2-b', '2-c',
          '2-d', '2-e', '3-a', '3-b', '3-c', '3-d', '3-e']
ct = tk.StringVar()
combo_turmas = ttk.Combobox(window, width=10, textvariable=ct, font=('arialblack', 12))
combo_turmas['values'] = turmas
combo_turmas.current(0)
combo_turmas.grid(row=0, column=1)
ct_label = tk.Label(window, text='Escolha a Turma:').grid(row=0, column=0)

bt0 = tk.Button(window, text='LANÇAR F.', bg='red', fg='white', width=15)

bt0["command"] = lambda arg=1: use(arg)
bt1 = tk.Button(window, text='ALTERAR F.', bg='green', fg='white', width=15)

bt1["command"] = lambda arg=2: use(arg)
bt2 = tk.Button(window, text='Editar', bg='blue', fg='white', width=15)
bt2["command"] = lambda arg=True: load(arg)
bt2.grid(row=7, column=0)
bt3 = tk.Button(window, text='Carregar', bg='yellow', width=15)
bt3["command"] = lambda arg=False: load(arg)
bt3.grid(row=7, column=1)

lbstate = tk.Label(window, fg='red', font='arialblack')
lbstate.place(x=10, y=450)
alunos = 36

for i in range(1, alunos + 1):
    on.append(i)

window.mainloop()
